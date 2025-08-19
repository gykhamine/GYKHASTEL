import customtkinter as ctk
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

class CryptographyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Documentation Complète : Cryptography")
        self.geometry("1200x900")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Création du cadre de navigation latéral
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side="left", fill="y", padx=(10, 0), pady=10)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Menu de navigation",
                                                   compound="left", font=ctk.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.pack(padx=20, pady=(20, 10))

        # Création des boutons de navigation par section
        self.crypto_label = ctk.CTkLabel(self.navigation_frame, text="Cryptography", font=ctk.CTkFont(size=16, weight="bold"))
        self.crypto_label.pack(fill="x", padx=10, pady=(10, 0))
        self.crypto_buttons = self.create_buttons(self.navigation_frame, [
            ("Introduction", self.show_intro),
            ("Chiffrement de Fichiers (Symétrique)", self.show_file_encryption_symmetric),
            ("Chiffrement de Fichiers (Asymétrique)", self.show_file_encryption_asymmetric),
            ("Chiffrement Symétrique (Fernet)", self.show_symmetric_encryption),
            ("Chiffrement Asymétrique (RSA)", self.show_asymmetric_encryption),
            ("Fonctions de Hachage", self.show_hashing),
            ("Signatures Numériques", self.show_digital_signatures),
        ])

        # Création du cadre principal pour le contenu
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        
        self.content_textbox = ctk.CTkTextbox(self.content_frame, wrap="word", font=ctk.CTkFont(size=14))
        self.content_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.content_textbox.configure(state="disabled")
        
        # Démarrage sur le premier onglet
        self.show_intro()

    def create_buttons(self, parent, button_list):
        buttons = []
        for text, command in button_list:
            button = ctk.CTkButton(parent, corner_radius=0, height=40, border_spacing=10, text=text,
                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                   anchor="w", command=command)
            button.pack(fill="x", padx=10, pady=2)
            buttons.append(button)
        return buttons

    def set_content(self, title, text, code=None, explanation=None):
        self.content_textbox.configure(state="normal")
        self.content_textbox.delete("1.0", "end")
        
        self.content_textbox.insert("1.0", f"**{title}**\n\n{text}")
        if explanation:
            self.content_textbox.insert("end", f"\n\n**Explication du code :**\n{explanation}")
        if code:
            self.content_textbox.insert("end", f"\n\n```python\n{code}\n```")
        
        self.content_textbox.configure(state="disabled")

    def show_intro(self):
        content = (
            "**Introduction à Cryptography.io** 🔒\n\n"
            "La bibliothèque **Cryptography** est un outil de pointe en Python pour la sécurité. Elle fournit des primitives cryptographiques, des algorithmes standards et des implémentations sécurisées pour des tâches telles que le chiffrement de données, la signature numérique et le hachage. Son API est divisée en deux couches : une API de haut niveau (comme **`Fernet`**), simple d'utilisation, et une API de bas niveau pour des besoins plus complexes et sur mesure."
        )
        self.set_content("Introduction", content)
    
    def show_file_encryption_symmetric(self):
        code_example = (
            "from cryptography.fernet import Fernet\n"
            "\n"
            "# --- Fonctions de chiffrement/déchiffrement de fichier ---\n"
            "def encrypt_file(filename, fernet):\n"
            "    # Ouvre le fichier en mode binaire 'rb' (read binary)\n"
            "    with open(filename, 'rb') as file:\n"
            "        # Lit tout le contenu du fichier dans la mémoire\n"
            "        file_data = file.read()\n"
            "    # Chiffre les données lues en utilisant la clé Fernet\n"
            "    encrypted_data = fernet.encrypt(file_data)\n"
            "    # Ouvre un nouveau fichier pour l'écriture binaire ('wb')\n"
            "    with open(filename + '.enc', 'wb') as file:\n"
            "        # Écrit les données chiffrées dans le nouveau fichier\n"
            "        file.write(encrypted_data)\n"
            "    print(f'Fichier chiffré : {filename}.enc')\n"
            "\n"
            "def decrypt_file(filename, fernet):\n"
            "    # Ouvre le fichier chiffré en mode binaire\n"
            "    with open(filename, 'rb') as file:\n"
            "        encrypted_data = file.read()\n"
            "    # Déchiffre les données en utilisant la même clé Fernet\n"
            "    decrypted_data = fernet.decrypt(encrypted_data)\n"
            "    # Ouvre un nouveau fichier pour écrire les données déchiffrées\n"
            "    with open(filename.replace('.enc', '.dec'), 'wb') as file:\n"
            "        file.write(decrypted_data)\n"
            "    print(f'Fichier déchiffré : {filename.replace('.enc', '.dec')}')\n"
            "\n"
            "# --- Utilisation --- (le fichier 'test.txt' doit exister)\n"
            "# Crée une clé de chiffrement symétrique sécurisée\n"
            "# key = Fernet.generate_key()\n"
            "# Initialise l'objet Fernet avec la clé\n"
            "# f = Fernet(key)\n"
            "# Appelle les fonctions (commenté pour éviter l'exécution automatique)\n"
            "# encrypt_file('test.txt', f)\n"
            "# decrypt_file('test.txt.enc', f)\n"
        )
        explanation = (
            "Cette section montre comment utiliser l'API de haut niveau **`Fernet`** pour chiffrer et déchiffrer des fichiers. Cette méthode est recommandée pour sa simplicité et sa sécurité par défaut.\n\n"
            "- **`Fernet.generate_key()` :** Génère une clé de 32 octets aléatoires, sécurisée et encodée en base64 URL-safe. **Il est crucial de stocker cette clé de manière sécurisée.**\n"
            "- **`Fernet(key)` :** Crée une instance de Fernet. Cet objet gère le chiffrement et le déchiffrement.\n"
            "- **`with open(filename, 'rb') as file:` :** Ouvre le fichier en mode binaire de lecture. C'est essentiel car les données chiffrées ne sont pas du texte.\n"
            "- **`file.read()` :** Lit tout le contenu binaire du fichier en une seule fois. Attention aux très grands fichiers, car cela peut consommer beaucoup de mémoire.\n"
            "- **`fernet.encrypt(file_data)` :** Prend les données binaires et les chiffre. Le résultat est un 'token' qui inclut les données chiffrées, mais aussi des informations de sécurité comme un horodatage et une signature HMAC pour vérifier l'intégrité.\n"
            "- **`file.write(encrypted_data)` :** Écrit les données chiffrées dans un nouveau fichier (`.enc`).\n"
            "- **`fernet.decrypt(encrypted_data)` :** Déchiffre les données. Le processus vérifie l'intégrité et l'horodatage. Si les données ont été altérées, cette fonction lèvera une exception, assurant que vous ne travaillez qu'avec des données authentiques."
        )
        self.set_content("Chiffrement de Fichiers (Symétrique)", explanation, code_example)

    def show_file_encryption_asymmetric(self):
        code_example = (
            "import os\n"
            "from cryptography.fernet import Fernet\n"
            "from cryptography.hazmat.primitives.asymmetric import rsa, padding\n"
            "from cryptography.hazmat.primitives import hashes\n"
            "from cryptography.hazmat.backends import default_backend\n\n"
            "# --- Fonctions de chiffrement/déchiffrement hybride ---\n"
            "# 1. Chiffrer la clé symétrique avec la clé publique RSA\n"
            "def encrypt_symmetric_key(public_key):\n"
            "    # Génère une clé Fernet (symétrique) pour le chiffrement du fichier\n"
            "    sym_key = Fernet.generate_key()\n"
            "    # Chiffre cette petite clé symétrique avec la clé publique RSA (rapide)\n"
            "    encrypted_sym_key = public_key.encrypt(\n"
            "        sym_key,\n"
            "        padding.OAEP(\n"
            "            mgf=padding.MGF1(algorithm=hashes.SHA256()),\n"
            "            algorithm=hashes.SHA256(),\n"
            "            label=None\n"
            "        )\n"
            "    )\n"
            "    # Retourne la clé symétrique originale et sa version chiffrée\n"
            "    return sym_key, encrypted_sym_key\n"
            "\n"
            "# 2. Déchiffrer la clé symétrique avec la clé privée RSA\n"
            "def decrypt_symmetric_key(private_key, encrypted_sym_key):\n"
            "    # Déchiffre la clé symétrique en utilisant la clé privée RSA\n"
            "    decrypted_sym_key = private_key.decrypt(\n"
            "        encrypted_sym_key,\n"
            "        padding.OAEP(\n"
            "            mgf=padding.MGF1(algorithm=hashes.SHA256()),\n"
            "            algorithm=hashes.SHA256(),\n"
            "            label=None\n"
            "        )\n"
            "    )\n"
            "    return decrypted_sym_key\n"
            "\n"
            "# --- Utilisation --- (commenté pour éviter l'exécution)\n"
            "# private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())\n"
            "# public_key = private_key.public_key()\n"
            "# sym_key, encrypted_sym_key = encrypt_symmetric_key(public_key)\n"
            "# decrypted_sym_key = decrypt_symmetric_key(private_key, encrypted_sym_key)\n"
            "# assert sym_key == decrypted_sym_key\n"
            "# print('La clé symétrique déchiffrée peut maintenant être utilisée pour un fichier !')\n"
        )
        explanation = (
            "L'approche hybride est la solution standard pour chiffrer de grands fichiers avec la cryptographie asymétrique.\n\n"
            "- **`rsa.generate_private_key(...)` :** Génère une paire de clés RSA. L'exécution est lente, mais n'est faite qu'une seule fois.\n"
            "- **`Fernet.generate_key()` :** Génère la clé symétrique qui va effectivement chiffrer le fichier. Cette clé est rapide à créer et à utiliser.\n"
            "- **`public_key.encrypt(...)` :** C'est le cœur de l'approche hybride. On chiffre la **petite clé symétrique** avec la clé publique RSA. C'est rapide et permet de la partager de manière sécurisée.\n"
            "- **`padding.OAEP(...)` :** Le remplissage (padding) est une étape de sécurité indispensable. **OAEP** est le standard recommandé pour le chiffrement RSA. `hashes.SHA256()` est l'algorithme de hachage utilisé dans ce schéma.\n"
            "- **`private_key.decrypt(...)` :** Seule la clé privée peut déchiffrer la clé symétrique chiffrée. Une fois que c'est fait, on peut utiliser cette clé symétrique pour le chiffrement et le déchiffrement du gros fichier (comme vu dans la section précédente)."
        )
        self.set_content("Chiffrement de Fichiers (Asymétrique)", explanation, code_example)
    
    def show_symmetric_encryption(self):
        code_example = (
            "from cryptography.fernet import Fernet\n\n"
            "# Génère une clé secrète\n"
            "key = Fernet.generate_key()\n"
            "# Crée l'objet de chiffrement\n"
            "f = Fernet(key)\n"
            "# Message à chiffrer (doit être en octets)\n"
            "message = b'Un message secret a chiffrer'\n"
            "# Chiffre le message\n"
            "token = f.encrypt(message)\n"
            "# Déchiffre le message\n"
            "decrypted_message = f.decrypt(token)\n"
            "print(f'Original : {message.decode()}')\n"
            "print(f'Déchiffré : {decrypted_message.decode()}')\n"
        )
        explanation = (
            "Cette section est une introduction à l'API de haut niveau **`Fernet`**, expliquant les principes de base du chiffrement symétrique.\n\n"
            "- **`Fernet.generate_key()` :** Crée une clé aléatoire. C'est la seule information secrète nécessaire.\n"
            "- **`Fernet(key)` :** Initialise l'objet Fernet. Il utilise la clé pour configurer l'algorithme de chiffrement.\n"
            "- **`b'...'` :** Indique que la chaîne de caractères est de type **bytes**. La cryptographie fonctionne sur les octets, pas sur les chaînes de texte.\n"
            "- **`f.encrypt(message)` :** Chiffre les octets du message. Le résultat est un jeton (`token`) qui contient les données chiffrées, un horodatage et une signature HMAC pour la sécurité.\n"
            "- **`f.decrypt(token)` :** Déchiffre le jeton et récupère le message d'origine, après avoir validé son intégrité et sa fraîcheur (via l'horodatage)."
        )
        self.set_content("Chiffrement Symétrique (Fernet)", explanation, code_example)
    
    def show_asymmetric_encryption(self):
        code_example = (
            "from cryptography.hazmat.primitives import serialization\n"
            "from cryptography.hazmat.primitives.asymmetric import rsa, padding\n"
            "from cryptography.hazmat.backends import default_backend\n"
            "from cryptography.hazmat.primitives import hashes\n\n"
            "# Génère une clé privée RSA\n"
            "private_key = rsa.generate_private_key(\n"
            "    public_exponent=65537, key_size=2048, backend=default_backend()\n"
            ")\n"
            "# Extrait la clé publique de la clé privée\n"
            "public_key = private_key.public_key()\n"
            "# Message à chiffrer (petite quantité)\n"
            "message = b'Un petit message secret'\n"
            "# Chiffrement avec la clé publique\n"
            "ciphertext = public_key.encrypt(\n"
            "    message,\n"
            "    padding.OAEP(\n"
            "        mgf=padding.MGF1(algorithm=hashes.SHA256()),\n"
            "        algorithm=hashes.SHA256(),\n"
            "        label=None\n"
            "    )\n"
            ")\n"
            "# Déchiffrement avec la clé privée\n"
            "decrypted_message = private_key.decrypt(\n"
            "    ciphertext,\n"
            "    padding.OAEP(\n"
            "        mgf=padding.MGF1(algorithm=hashes.SHA256()),\n"
            "        algorithm=hashes.SHA256(),\n"
            "        label=None\n"
            "    )\n"
            ")\n"
            "print(f'Original : {message.decode()}')\n"
            "print(f'Déchiffré : {decrypted_message.decode()}')\n"
        )
        explanation = (
            "Cette section explique le chiffrement asymétrique avec RSA, un algorithme fondamental pour l'échange de clés et les signatures numériques.\n\n"
            "- **`rsa.generate_private_key(...)` :** Génère la **paire de clés** (privée et publique). `key_size=2048` est une taille standard et sécurisée pour les clés RSA.\n"
            "- **`private_key.public_key()` :** La clé publique peut être dérivée de la clé privée. Elle est destinée à être partagée publiquement.\n"
            "- **`public_key.encrypt(...)` :** Utilise la clé publique pour chiffrer les données. Seule la clé privée correspondante peut déchiffrer ce message.\n"
            "- **`padding.OAEP(...)` :** Le remplissage (`padding`) est une technique indispensable pour la sécurité du chiffrement RSA. Sans un bon padding, une attaque peut récupérer les données chiffrées. OAEP est le standard recommandé.\n"
            "- **`private_key.decrypt(...)` :** Utilise la clé privée pour déchiffrer les données chiffrées par la clé publique correspondante. C'est l'opération inverse du chiffrement."
        )
        self.set_content("Chiffrement Asymétrique (RSA)", explanation, code_example)

    def show_hashing(self):
        code_example = (
            "from cryptography.hazmat.primitives import hashes\n\n"
            "# Crée un objet de hachage SHA256\n"
            "digest = hashes.Hash(hashes.SHA256())\n"
            "# Ajoute les données à hacher\n"
            "digest.update(b'un message a hacher')\n"
            "# Finalise le calcul pour obtenir le hachage\n"
            "hashed_data = digest.finalize()\n"
            "\n"
            "print(f'Données hachées (SHA256) : {hashed_data.hex()}')\n"
        )
        explanation = (
            "Le hachage est un processus à sens unique qui produit une empreinte numérique unique pour un ensemble de données. Il est utilisé pour vérifier l'intégrité, mais pas la confidentialité des données.\n\n"
            "- **`hashes.Hash(hashes.SHA256())` :** Crée un objet qui gérera le calcul du hachage. On spécifie l'algorithme à utiliser, ici **SHA256**.\n"
            "- **`digest.update(b'...')` :** Ajoute des données à l'objet de hachage. On peut appeler cette méthode plusieurs fois pour hacher un flux de données (streaming).\n"
            "- **`digest.finalize()` :** Calcule le hachage final. Après cette étape, l'objet ne peut plus être modifié et renvoie l'empreinte numérique."
        )
        self.set_content("Fonctions de Hachage (SHA256)", explanation, code_example)

    def show_digital_signatures(self):
        code_example = (
            "from cryptography.hazmat.primitives import hashes\n"
            "from cryptography.hazmat.primitives.asymmetric import rsa, padding\n"
            "from cryptography.hazmat.backends import default_backend\n\n"
            "# Génère les clés (privée et publique)\n"
            "private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())\n"
            "public_key = private_key.public_key()\n"
            "# Données à signer\n"
            "data = b'Des donnees a signer'\n"
            "# Crée la signature avec la clé privée\n"
            "signature = private_key.sign(\n"
            "    data,\n"
            "    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),\n"
            "    hashes.SHA256()\n"
            ")\n"
            "# Vérifie la signature avec la clé publique\n"
            "try:\n"
            "    public_key.verify(\n"
            "        signature, data,\n"
            "        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),\n"
            "        hashes.SHA256()\n"
            "    )\n"
            "    print('La signature est valide.')\n"
            "except Exception:\n"
            "    print('La signature est invalide.')\n"
        )
        explanation = (
            "Une signature numérique garantit l'authenticité et l'intégrité d'un message. Elle prouve que le message a été créé par le détenteur de la clé privée et qu'il n'a pas été altéré.\n\n"
            "- **`private_key.sign(...)` :** La signature est créée en utilisant la **clé privée** de l'expéditeur. Le message est haché, puis ce hachage est chiffré avec la clé privée. Le `padding.PSS` est le schéma de remplissage recommandé pour les signatures RSA.\n"
            "- **`public_key.verify(...)` :** Le destinataire utilise la **clé publique** de l'expéditeur pour vérifier la signature. Cette fonction recalcule le hachage du message, le compare avec celui déchiffré depuis la signature. Si les deux correspondent, la signature est valide."
        )
        self.set_content("Signatures Numériques", explanation, code_example)

if __name__ == "__main__":
    app = CryptographyApp()
    app.mainloop()