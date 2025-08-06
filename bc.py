import sqlite3
import hashlib
import json
from datetime import datetime

class Blockchain:
    """
    Implémentation d'une blockchain sécurisée et persistante utilisant SQLite.
    Inclut un algorithme de preuve de travail avec une difficulté dynamique.
    """
    def __init__(self, db_file="blockchain.db"):
        """
        Initialise la blockchain en se connectant à la base de données.
        Crée les tables nécessaires et un bloc de genèse si la chaîne est vide.
        """
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        self.create_tables()

        # Crée un bloc de genèse si la blockchain est vide
        if not self.get_last_block_index():
            # Le premier bloc n'a pas de bloc précédent, '1' est une convention
            # La preuve de travail est par défaut de 100
            self.new_block(proof=100, previous_hash='1')

    def create_tables(self):
        """
        Crée les tables `blocks` et `transactions` dans la base de données SQLite.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS blocks (
                id INTEGER PRIMARY KEY,
                index_block INTEGER UNIQUE,
                timestamp TEXT,
                proof INTEGER,
                previous_hash TEXT,
                hash TEXT UNIQUE
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                sender TEXT,
                recipient TEXT,
                amount REAL,
                block_index INTEGER,
                FOREIGN KEY (block_index) REFERENCES blocks (index_block)
            )
        ''')
        self.conn.commit()

    def new_block(self, proof, previous_hash=None):
        """
        Crée et ajoute un nouveau bloc à la blockchain.
        Ce bloc inclut les transactions en attente.
        
        :param proof: La preuve de travail (le résultat du minage).
        :param previous_hash: Le hachage du bloc précédent.
        :return: Le nouveau bloc sous forme de dictionnaire.
        """
        last_block_index = self.get_last_block_index() or 0
        block = {
            'index_block': last_block_index + 1,
            'timestamp': str(datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.get_last_block()),
            'transactions': self.get_pending_transactions()
        }
        
        # Insère le bloc dans la table `blocks`
        block_hash = self.hash(block)
        self.cursor.execute('''
            INSERT INTO blocks (index_block, timestamp, proof, previous_hash, hash)
            VALUES (?, ?, ?, ?, ?)
        ''', (block['index_block'], block['timestamp'], block['proof'], block['previous_hash'], block_hash))
        
        # Associe les transactions en attente au nouveau bloc
        self.cursor.execute('''
            UPDATE transactions
            SET block_index = ?
            WHERE block_index IS NULL
        ''', (block['index_block'],))
        
        self.conn.commit()
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Crée une nouvelle transaction et l'ajoute à la liste des transactions en attente.
        
        :param sender: Adresse de l'expéditeur.
        :param recipient: Adresse du destinataire.
        :param amount: Le montant de la transaction.
        :return: L'index du bloc qui contiendra cette transaction.
        """
        self.cursor.execute('''
            INSERT INTO transactions (sender, recipient, amount, block_index)
            VALUES (?, ?, ?, ?)
        ''', (sender, recipient, amount, None))
        self.conn.commit()
        
        return (self.get_last_block_index() or 0) + 1

    def get_pending_transactions(self):
        """
        Récupère toutes les transactions qui ne sont pas encore dans un bloc.
        
        :return: Une liste de transactions en attente.
        """
        self.cursor.execute('SELECT sender, recipient, amount FROM transactions WHERE block_index IS NULL')
        return [{'sender': row[0], 'recipient': row[1], 'amount': row[2]} for row in self.cursor.fetchall()]

    def get_last_block_index(self):
        """
        Récupère l'index du dernier bloc miné.
        
        :return: L'index du dernier bloc, ou `None` si la chaîne est vide.
        """
        self.cursor.execute('SELECT MAX(index_block) FROM blocks')
        result = self.cursor.fetchone()[0]
        return result

    def get_last_block(self):
        """
        Récupère le dernier bloc complet (y compris ses transactions).
        
        :return: Le dernier bloc sous forme de dictionnaire, ou `None`.
        """
        last_block_index = self.get_last_block_index()
        if not last_block_index:
            return None
        
        self.cursor.execute('SELECT * FROM blocks WHERE index_block = ?', (last_block_index,))
        block_row = self.cursor.fetchone()
        
        # Construit le dictionnaire du bloc
        block = {
            'index_block': block_row[1],
            'timestamp': block_row[2],
            'proof': block_row[3],
            'previous_hash': block_row[4],
            'hash': block_row[5],
        }
        
        # Récupère et ajoute les transactions du bloc
        self.cursor.execute('SELECT sender, recipient, amount FROM transactions WHERE block_index = ?', (last_block_index,))
        block['transactions'] = [{'sender': row[0], 'recipient': row[1], 'amount': row[2]} for row in self.cursor.fetchall()]
        
        return block

    @staticmethod
    def hash(block):
        """
        Calcule le hachage SHA-256 d'un bloc.
        
        :param block: Le bloc à hacher.
        :return: Le hachage hexadécimal du bloc.
        """
        # On s'assure que le dictionnaire est ordonné pour avoir un hachage constant
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def calculate_difficulty(self):
        """
        Calcule la difficulté de minage en fonction du temps écoulé depuis
        le dernier bloc.
        La difficulté est augmentée si les blocs sont minés trop rapidement,
        et diminuée si c'est trop lent.
        """
        last_block = self.get_last_block()
        if not last_block or last_block['index_block'] == 1:
            return 4  # Difficulté par défaut pour le bloc de genèse
        
        self.cursor.execute('SELECT timestamp FROM blocks WHERE index_block = ?', (last_block['index_block'] - 1,))
        previous_block_timestamp_str = self.cursor.fetchone()[0]
        
        last_timestamp = datetime.strptime(last_block['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        previous_timestamp = datetime.strptime(previous_block_timestamp_str, '%Y-%m-%d %H:%M:%S.%f')
        
        time_elapsed = (last_timestamp - previous_timestamp).seconds
        
        # Si le temps est inférieur à 15 secondes, on augmente la difficulté
        if time_elapsed < 15:
            return 5
        # Si le temps est supérieur à 45 secondes, on diminue la difficulté
        elif time_elapsed > 45:
            return 3
        else:
            return 4  # La difficulté reste à 4 zéros par défaut

    def proof_of_work(self):
        """
        Algorithme de preuve de travail avec difficulté dynamique.
        Le mineur doit trouver un nombre (proof) qui donne un hachage
        conforme à la difficulté actuelle de la chaîne.
        """
        last_block = self.get_last_block()
        last_proof = last_block['proof']
        difficulty = self.calculate_difficulty()
        
        print(f"Difficulté de minage actuelle : {difficulty} zéros")
        
        proof = 0
        while not self.valid_proof(last_proof, proof, difficulty):
            proof += 1
            
        return proof

    @staticmethod
    def valid_proof(last_proof, proof, difficulty):
        """
        Valide la preuve de travail en utilisant une difficulté variable.
        La difficulté est représentée par le nombre de zéros au début du hachage.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        
        # Le hachage doit commencer par un nombre de zéros correspondant à la difficulté.
        return guess_hash[:difficulty] == "0" * difficulty
        
    def close(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()

# --- Section d'exécution ---
if __name__ == '__main__':
    # Crée une instance de la blockchain, ce qui initialise la base de données
    # Supprimez le fichier blockchain.db pour recommencer à zéro
    blockchain = Blockchain()

    print("--- Ajout de transactions en attente ---")
    blockchain.new_transaction("alice", "bob", 1)
    blockchain.new_transaction("bob", "charlie", 0.5)

    print("\n--- Minage d'un nouveau bloc ---")
    last_block = blockchain.get_last_block()
    
    proof = blockchain.proof_of_work()
    
    # On récompense le mineur pour son travail
    blockchain.new_transaction(sender="0", recipient="miner_address", amount=1)
    
    blockchain.new_block(proof, previous_hash=last_block['hash'])

    print("\nBlockchain complète (extraite de la base de données) :")
    blockchain.cursor.execute('SELECT * FROM blocks ORDER BY index_block')
    for block_row in blockchain.cursor.fetchall():
        block_index = block_row[1]
        print(f"Index : {block_index}")
        print(f"Timestamp : {block_row[2]}")
        print(f"Proof : {block_row[3]}")
        print(f"Previous Hash : {block_row[4]}")
        
        blockchain.cursor.execute('SELECT sender, recipient, amount FROM transactions WHERE block_index = ?', (block_index,))
        transactions = [{'sender': row[0], 'recipient': row[1], 'amount': row[2]} for row in blockchain.cursor.fetchall()]
        print(f"Transactions : {transactions}")
        print("-" * 20)

    blockchain.close()