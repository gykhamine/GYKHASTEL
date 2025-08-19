import customtkinter as ctk
import sqlite3
from tkinter import messagebox

class SQLiteApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre principale ---
        self.title("Guide Ultime : Introduction à SQLite")
        self.geometry("1200x900")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        # --- Création du cadre de navigation latéral ---
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side="left", fill="y", padx=(10, 0), pady=10)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Menu de navigation",
                                                   compound="left", font=ctk.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.pack(padx=20, pady=(20, 10))

        # --- Création des boutons de navigation ---
        self.intro_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Introduction à SQLite",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_intro)
        self.intro_button.pack(fill="x", padx=10, pady=5)
        
        self.connection_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Connexion et Création",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_connection)
        self.connection_button.pack(fill="x", padx=10, pady=5)
        
        self.crud_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Opérations CRUD",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_crud)
        self.crud_button.pack(fill="x", padx=10, pady=5)

        self.transaction_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Transactions et Erreurs",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_transaction)
        self.transaction_button.pack(fill="x", padx=10, pady=5)
        
        self.memory_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Gestion de la RAM",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_memory_management)
        self.memory_button.pack(fill="x", padx=10, pady=5)

        self.advanced_query_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Requêtes avancées",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_advanced_query)
        self.advanced_query_button.pack(fill="x", padx=10, pady=5)

        self.close_db_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Fermer la BDD",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.close_database)
        self.close_db_button.pack(fill="x", padx=10, pady=5)

        # --- Création du cadre principal pour le contenu ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        
        self.content_textbox = ctk.CTkTextbox(self.content_frame, wrap="word", font=ctk.CTkFont(size=14))
        self.content_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.content_textbox.configure(state="disabled")
        
        # --- Connexion à la base de données au démarrage ---
        self.db_path = "mon_application.db"
        self.conn = None
        self.cursor = None
        self.show_intro()

    def set_content(self, title, text, code=None):
        self.content_textbox.configure(state="normal")
        self.content_textbox.delete("1.0", "end")
        
        self.content_textbox.insert("1.0", f"**{title}**\n\n{text}")
        if code:
            self.content_textbox.insert("end", f"\n\n```python\n{code}\n```")
        
        self.content_textbox.configure(state="disabled")

    def show_intro(self):
        content = (
            "**Introduction à SQLite** 🗃️\n\n"
            "**SQLite** est une bibliothèque logicielle qui implémente un système de gestion de base de données relationnelle (`SGBDR`) léger, autonome, sans serveur et sans configuration. Il est très populaire pour les applications mobiles, les navigateurs web (Firefox, Chrome), et les systèmes embarqués, mais aussi pour les prototypes ou les petites applications de bureau en Python.\n\n"
            "**Avantages de SQLite :**\n"
            "- **Sans serveur :** Contrairement à MySQL ou PostgreSQL, SQLite ne nécessite pas de serveur distinct. La base de données est stockée dans un simple fichier sur le disque.\n"
            "- **Intégration facile :** La bibliothèque est incluse par défaut dans la plupart des installations Python, vous n'avez donc rien à installer de plus.\n"
            "- **Léger et rapide :** C'est une solution idéale pour les applications qui ne gèrent pas un trafic important d'utilisateurs en simultané."
        )
        self.set_content("Introduction à SQLite", content)
    
    def show_connection(self):
        code_example = (
            "import sqlite3\n\n"
            "# 1. Se connecter à une base de données. Si elle n'existe pas, elle sera créée.\n"
            "conn = sqlite3.connect('mon_application.db')\n\n"
            "# 2. Créer un objet curseur pour exécuter des requêtes SQL.\n"
            "cursor = conn.cursor()\n\n"
            "# 3. Exécuter une requête pour créer une table 'utilisateurs'.\n"
            "cursor.execute('''\n"
            "    CREATE TABLE IF NOT EXISTS utilisateurs (\n"
            "        id INTEGER PRIMARY KEY,\n"
            "        nom TEXT NOT NULL,\n"
            "        age INTEGER\n"
            "    )\n"
            "''')\n\n"
            "# 4. Valider les changements (sinon la table ne sera pas enregistrée).\n"
            "conn.commit()\n\n"
            "# 5. Fermer la connexion.\n"
            "conn.close()"
        )
        content = (
            "**Connexion, création de tables et fermeture** 🏗️\n\n"
            "Pour interagir avec une base de données SQLite, vous devez suivre un processus simple et standard.\n\n"
            "**1. La connexion (`sqlite3.connect()`) :**\n"
            "   - Cette fonction établit une connexion à un fichier de base de données. Si le fichier n'existe pas, SQLite le crée automatiquement. Si vous passez `:memory:` comme nom de fichier, la base de données est créée en mémoire vive et sera effacée à la fermeture.\n\n"
            "**2. L'objet curseur (`conn.cursor()`) :**\n"
            "   - Le curseur est un objet qui vous permet d'exécuter des requêtes SQL et de naviguer dans les résultats.\n\n"
            "**3. Exécution d'une requête (`cursor.execute()`) :**\n"
            "   - C'est la fonction principale pour envoyer n'importe quelle commande SQL. L'exemple montre la création d'une table avec trois colonnes : `id`, `nom` et `age`.\n\n"
            "**4. Validation (`conn.commit()`) et fermeture (`conn.close()`) :**\n"
            "   - `conn.commit()` est essentiel ! Il enregistre de manière permanente toutes les modifications effectuées depuis le dernier commit. Ne pas l'appeler signifie que vos modifications seront perdues. Une fois le travail terminé, `conn.close()` libère la connexion à la base de données."
        )
        self.set_content("Connexion et Création", content, code_example)
        
    def show_crud(self):
        code_example = (
            "import sqlite3\n\n"
            "conn = sqlite3.connect('mon_application.db')\n"
            "cursor = conn.cursor()\n\n"
            "# --- 1. CREATE (Insertion de données) ---\n"
            "# Utilisation d'un paramètre (évite l'injection SQL)\n"
            "cursor.execute(\"INSERT INTO utilisateurs (nom, age) VALUES (?, ?)\", ('Alice', 30))\n"
            "conn.commit()\n"
            "print('Alice a été insérée.')\n\n"
            "# --- 2. READ (Lecture de données) ---\n"
            "cursor.execute(\"SELECT * FROM utilisateurs\")\n"
            "utilisateurs = cursor.fetchall()\n"
            "for user in utilisateurs:\n"
            "    print(user)\n\n"
            "# --- 3. UPDATE (Mise à jour) ---\n"
            "cursor.execute(\"UPDATE utilisateurs SET age = ? WHERE nom = ?\", (31, 'Alice'))\n"
            "conn.commit()\n"
            "print('L\\'âge d\\'Alice a été mis à jour.')\n\n"
            "# --- 4. DELETE (Suppression) ---\n"
            "cursor.execute(\"DELETE FROM utilisateurs WHERE nom = ?\", ('Alice',))\n"
            "conn.commit()\n"
            "print('Alice a été supprimée.')\n\n"
            "conn.close()"
        )
        content = (
            "**Les opérations CRUD (Create, Read, Update, Delete)** ⚙️\n\n"
            "Les opérations CRUD sont les quatre fonctions de base et essentielles de toute base de données. SQLite facilite grandement leur implémentation.\n\n"
            "**1. Création (`INSERT`) :**\n"
            "   - Pour insérer de nouvelles données, on utilise la commande SQL `INSERT`. Il est fortement recommandé d'utiliser des **paramètres** (`?`) à la place de la concaténation de chaînes, pour prévenir les attaques par **injection SQL**.\n\n"
            "**2. Lecture (`SELECT`) :**\n"
            "   - `SELECT` est utilisée pour récupérer des données. Les méthodes du curseur comme `fetchone()`, `fetchall()` ou `fetchmany()` permettent de récupérer les résultats de la requête. `fetchall()` renvoie une liste de tuples, où chaque tuple est une ligne de la table.\n\n"
            "**3. Mise à jour (`UPDATE`) :**\n"
            "   - La commande `UPDATE` permet de modifier des données existantes. La clause `WHERE` est cruciale pour spécifier quelles lignes doivent être modifiées.\n\n"
            "**4. Suppression (`DELETE`) :**\n"
            "   - La commande `DELETE` supprime des lignes. Sans la clause `WHERE`, elle effacerait *toutes* les données de la table."
        )
        self.set_content("Opérations CRUD", content, code_example)

    def show_transaction(self):
        code_example = (
            "import sqlite3\n\n"
            "conn = sqlite3.connect('mon_application.db')\n"
            "cursor = conn.cursor()\n\n"
            "# --- Transaction avec commit ---\n"
            "try:\n"
            "    cursor.execute(\"INSERT INTO utilisateurs (nom, age) VALUES (?, ?)\", ('Bob', 25))\n"
            "    conn.commit()  # Sauvegarde la modification\n"
            "    print('Bob a été ajouté avec succès.')\n"
            "except sqlite3.Error as e:\n"
            "    print(f'Erreur: {e}')\n"
            "    conn.rollback() # Annule la modification si elle échoue\n\n"
            "# --- Transaction qui échoue avec rollback ---\n"
            "try:\n"
            "    # Cette requête va échouer (age doit être un nombre)\n"
            "    cursor.execute(\"INSERT INTO utilisateurs (nom, age) VALUES (?, ?)\", ('Charlie', 'invalide'))\n"
            "    conn.commit() \n"
            "except sqlite3.Error as e:\n"
            "    print(f\"Erreur: {e}\")\n"
            "    print(\"La transaction a été annulée (rollback).\")\n"
            "    conn.rollback() # Annule la tentative d'insertion\n\n"
            "conn.close()"
        )
        content = (
            "**Transactions et gestion des erreurs** 🛡️\n\n"
            "En base de données, une **transaction** est une série d'opérations exécutées comme une seule unité logique de travail. Soit toutes les opérations réussissent (`commit`), soit aucune ne se produit (`rollback`). Cela garantit l'intégrité des données.\n\n"
            "**1. Le `commit()` :**\n"
            "   - `conn.commit()` valide une transaction. Toutes les requêtes `INSERT`, `UPDATE` ou `DELETE` effectuées avant le `commit` sont enregistrées de manière permanente.\n\n"
            "**2. Le `rollback()` :**\n"
            "   - Si une erreur se produit pendant une transaction, `conn.rollback()` est appelé pour annuler toutes les opérations en attente. La base de données revient à l'état où elle se trouvait avant le début de la transaction.\n\n"
            "**3. Gestion des erreurs (`try...except`) :**\n"
            "   - Il est vivement recommandé d'utiliser un bloc `try...except` pour encadrer vos transactions. En cas d'exception `sqlite3.Error`, vous pouvez appeler `conn.rollback()` pour annuler la transaction et éviter de corrompre la base de données. C'est une pratique essentielle pour construire des applications robustes."
        )
        self.set_content("Transactions et Erreurs", content, code_example)
    
    def show_memory_management(self):
        code_example = (
            "import sqlite3\n\n"
            "# Créer une base de données en mémoire vive\n"
            "print('Création d\\'une base de données en mémoire vive : :memory:')\n"
            "conn_ram = sqlite3.connect(':memory:')\n"
            "cursor_ram = conn_ram.cursor()\n\n"
            "cursor_ram.execute(\"CREATE TABLE utilisateurs_temp (id INTEGER, nom TEXT)\")\n"
            "cursor_ram.execute(\"INSERT INTO utilisateurs_temp VALUES (1, 'Data-RAM')\")\n"
            "conn_ram.commit()\n\n"
            "cursor_ram.execute(\"SELECT * FROM utilisateurs_temp\")\n"
            "print('Résultat de la BDD en RAM:', cursor_ram.fetchall())\n\n"
            "# Fermer la connexion : toutes les données sont perdues !\n"
            "conn_ram.close()\n"
            "print('La connexion a été fermée. Les données en RAM sont maintenant effacées.')\n\n"
            "# --- Optimisation de la performance (mémoire) --- \n"
            "conn = sqlite3.connect('mon_application.db')\n"
            "cursor = conn.cursor()\n"
            "print('\\n--- Optimisation du cache de pages ---')\n"
            "# Définir la taille du cache en kilooctets (ici 32 Mo)\n"
            "cursor.execute('PRAGMA cache_size = 32768')\n"
            "print('Taille du cache de pages définie sur 32 Mo.')\n"
            "conn.close()\n"
        )
        content = (
            "**Gestion de la mémoire RAM et des performances** 🚀\n\n"
            "Même si SQLite stocke les données sur le disque, il utilise la mémoire vive (RAM) pour des raisons de performance. Comprendre comment il gère cette mémoire est crucial pour l'optimisation.\n\n"
            "**1. Base de données en mémoire vive (`:memory:`) :**\n"
            "   - En passant le nom de fichier `:memory:` à `sqlite3.connect()`, vous créez une base de données qui réside entièrement en RAM. C'est extrêmement rapide car il n'y a pas d'accès disque, mais toutes les données sont **perdues dès que la connexion est fermée**. C'est parfait pour des tests, des calculs temporaires ou des applications où la persistance n'est pas nécessaire.\n\n"
            "**2. Le cache de pages (Page Cache) :**\n"
            "   - SQLite ne lit ou n'écrit pas les données octet par octet sur le disque, mais par blocs appelés **pages**. Il stocke ces pages dans un **cache de pages** en mémoire pour accélérer les opérations. Plus la taille du cache est grande, moins il y a d'accès au disque, ce qui améliore la performance.\n"
            "   - La commande `PRAGMA cache_size = -N` (où N est le nombre de pages) ou `PRAGMA cache_size = taille_en_ko` est utilisée pour ajuster cette taille. La valeur par défaut est généralement de 2000 pages (environ 1.5 Mo), mais vous pouvez l'augmenter pour les applications à forte intensité de lecture.\n\n"
            "**3. Autres PRAGMA :**\n"
            "   - **`PRAGMA synchronous` :** Contrôle la synchronisation du fichier de la base de données avec le disque. Une valeur de `OFF` est plus rapide mais moins sûre en cas de panne de courant. `FULL` est plus sûr mais plus lent.\n"
            "   - **`PRAGMA journal_mode` :** Gère la manière dont les transactions sont enregistrées. Le mode `WAL` (`Write-Ahead Logging`) est souvent plus performant que le mode par défaut (`DELETE`) pour les applications avec de nombreuses lectures et écritures concurrentes."
        )
        self.set_content("Gestion de la RAM", content, code_example)

    def show_advanced_query(self):
        code_example = (
            "import sqlite3\n\n"
            "conn = sqlite3.connect('mon_application.db')\n"
            "cursor = conn.cursor()\n\n"
            "# Insertion de données d'exemple pour les agrégats\n"
            "cursor.executemany(\"INSERT INTO utilisateurs (nom, age) VALUES (?, ?)\", \n"
            "                   [('David', 22), ('Emma', 28), ('Franck', 31), ('Olivia', 22)])\n"
            "conn.commit()\n\n"
            "print('--- Fonctions d\\'agrégation ---')\n"
            "# Nombre total d'utilisateurs\n"
            "cursor.execute(\"SELECT COUNT(*) FROM utilisateurs\")\n"
            "count = cursor.fetchone()[0]\n"
            "print(f\"Nombre total d'utilisateurs: {count}\")\n\n"
            "# Âge moyen des utilisateurs\n"
            "cursor.execute(\"SELECT AVG(age) FROM utilisateurs\")\n"
            "avg_age = cursor.fetchone()[0]\n"
            "print(f\"Âge moyen: {avg_age:.2f}\")\n\n"
            "# Âge maximum\n"
            "cursor.execute(\"SELECT MAX(age) FROM utilisateurs\")\n"
            "max_age = cursor.fetchone()[0]\n"
            "print(f\"Âge maximum: {max_age}\")\n\n"
            "print('\\n--- Clauses WHERE et ORDER BY ---')\n"
            "# Sélectionner les noms et âges des personnes triées par âge décroissant\n"
            "cursor.execute(\"SELECT nom, age FROM utilisateurs ORDER BY age DESC\")\n"
            "print('Utilisateurs (par âge décroissant):', cursor.fetchall())\n\n"
            "conn.close()"
        )
        content = (
            "**Requêtes avancées et Fonctions d'agrégation** 📊\n\n"
            "Au-delà des opérations de base, SQLite supporte un large éventail de requêtes SQL pour filtrer, trier et agréger vos données. En voici quelques exemples pratiques.\n\n"
            "**1. Fonctions d'agrégation (`COUNT`, `AVG`, `MAX`, etc.) :**\n"
            "   - Les fonctions d'agrégation calculent une valeur unique à partir d'un ensemble de valeurs. `COUNT(*)` est utilisé pour compter le nombre de lignes, `AVG(colonne)` pour la moyenne, `MAX(colonne)` pour la valeur maximale, et `SUM(colonne)` pour la somme.\n\n"
            "**2. Tri (`ORDER BY`) :**\n"
            "   - La clause `ORDER BY` trie les résultats d'une requête en fonction d'une ou plusieurs colonnes. C'est essentiel pour présenter les données de manière structurée.\n"
            "   - `ORDER BY age DESC` trie par âge du plus grand au plus petit (décroissant), tandis que `ASC` (par défaut) trie dans l'ordre croissant.\n\n"
            "**3. Utilisation de `executemany()` pour l'insertion en masse :**\n"
            "   - La méthode `cursor.executemany()` est très utile pour insérer plusieurs lignes à la fois, ce qui est beaucoup plus performant qu'une série d'appels `execute()` individuels."
        )
        self.set_content("Requêtes avancées", content, code_example)
        
    def close_database(self):
        if self.conn:
            self.conn.close()
            messagebox.showinfo("Fermeture de la BDD", "La connexion à la base de données a été fermée.")
            self.conn = None
            self.cursor = None
        else:
            messagebox.showinfo("Fermeture de la BDD", "Aucune connexion n'est active.")

if __name__ == "__main__":
    app = SQLiteApp()
    app.mainloop()