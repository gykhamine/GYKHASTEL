import customtkinter

# --- Contenu complet du cours ---
cryptography_course = {
    "intro_course": {
        "titre": "Cours Complet : Les Fondamentaux de la Cryptographie",
        "contenu": "Félicitations ! Vous êtes sur le point de terminer ce cours. Il couvre les principes fondamentaux de la cryptographie, de la théorie à l'application pratique. Nous avons exploré les algorithmes clés, leurs mathématiques et la manière dont ils sont utilisés ensemble dans le monde réel.\n\n"
                   "**Sommaire du cours :**\n"
                   "- **Partie 1 : RSA** - Chiffrement asymétrique et ses mathématiques.\n"
                   "- **Partie 2 : AES** - Chiffrement symétrique et son fonctionnement interne.\n"
                   "- **Partie 3 : Concepts Clés & Applications** - Fonctions de hachage, signatures numériques et cryptographie hybride.\n\n"
                   "Veuillez sélectionner une section dans le menu de gauche pour revoir les concepts."
    },
    "rsa_details_long": {
        "titre": "Partie 1.1: RSA - Explication détaillée",
        "contenu": "Le chiffrement RSA (Rivest-Shamir-Adleman) est un algorithme de cryptographie asymétrique, ce qui signifie qu'il utilise une paire de clés : une **clé publique** pour le chiffrement et une **clé privée** pour le déchiffrement. Cette approche a révolutionné la sécurité des communications, car elle permet à n'importe qui de chiffrer un message pour un destinataire sans avoir besoin d'échanger une clé secrète au préalable. La sécurité de RSA repose entièrement sur une propriété mathématique unique et très difficile à inverser : la **factorisation des grands nombres premiers**.\n\n"
                   "Pour comprendre RSA, il faut d'abord maîtriser trois concepts mathématiques fondamentaux. Le premier est celui des **nombres premiers**. Les nombres premiers, comme 7, 13 ou 101, sont des nombres qui ne sont divisibles que par 1 et par eux-mêmes. Le principe de base de RSA est qu'il est facile de multiplier deux grands nombres premiers pour obtenir un produit, mais il est extraordinairement difficile de retrouver les deux nombres premiers initiaux à partir de ce produit. Ce problème est connu sous le nom de **problème de la factorisation**. Le deuxième concept est l'**arithmétique modulaire**, que l'on peut comparer au fonctionnement d'une horloge. L'opération $a \pmod n$ renvoie le reste de la division de $a$ par $n$. Cette opération est utilisée de manière intensive dans RSA pour garantir que les calculs restent dans une fourchette de valeurs gérable, même avec de très grandes puissances. Enfin, la **fonction indicatrice d'Euler** ($\phi(n)$) est cruciale. Pour deux nombres premiers $p$ et $q$, cette fonction se calcule simplement par $\phi(n) = (p-1) \times (q-1)$, où $n = p \times q$. Cette valeur est le secret qui permet de générer la clé privée et ne peut être calculée facilement que si l'on connaît les nombres premiers $p$ et $q$."
    },
    "rsa_chiffrement_process": {
        "titre": "Partie 1.2: RSA - Processus de Chiffrement",
        "contenu": "Le chiffrement avec RSA est l'opération que tout le monde peut effectuer en utilisant la clé publique du destinataire. C'est l'étape où le message est transformé en un texte illisible.\n\n"
                   "**Étapes du chiffrement :**\n"
                   "1. **Le message $M$** : Le message doit être converti en un nombre. Pour un texte, on utilise généralement une table de caractères comme ASCII pour convertir chaque lettre en un nombre. Ce nombre doit être inférieur à $n$.\n"
                   "2. **La clé publique** : L'expéditeur a besoin de la clé publique du destinataire, soit la paire $(e, n)$.\n"
                   "3. **La formule de chiffrement** : On applique la formule de puissance modulaire :\n"
                   "   - **$C = M^e \pmod{n}$**\n"
                   "4. **Le résultat** : Le résultat $C$ est le message chiffré, qui est envoyé au destinataire. Sans la clé privée $d$, il est impossible de retrouver $M$ à partir de $C$ et de la clé publique $(e, n)$, car il faudrait calculer $d$ en factorisant $n$, ce qui est un problème mathématiquement insoluble pour de grands nombres."
    },
    "rsa_dechiffrement_process": {
        "titre": "Partie 1.3: RSA - Processus de Déchiffrement",
        "contenu": "Le déchiffrement est l'opération qui permet de retrouver le message original. Seul le destinataire, qui possède la clé privée, peut effectuer cette opération.\n\n"
                   "**Étapes du déchiffrement :**\n"
                   "1. **Le message chiffré $C$** : Le destinataire reçoit le message chiffré $C$.\n"
                   "2. **La clé privée** : Le destinataire utilise sa clé privée, la paire $(d, n)$.\n"
                   "3. **La formule de déchiffrement** : On applique la formule de puissance modulaire inverse :\n"
                   "   - **$M = C^d \pmod{n}$**\n"
                   "4. **Le résultat** : Le résultat $M$ est le nombre du message original. Le destinataire peut le reconvertir en texte pour le lire. Le fait que l'opération de déchiffrement \"annule\" parfaitement l'opération de chiffrement est garanti par le théorème d'Euler en mathématiques."
    },
    "rsa_math_details_enc": {
        "titre": "Partie 1.4: RSA - Maths du Chiffrement",
        "contenu": "L'opération de chiffrement est une **puissance modulaire** qui transforme le message en nombre en un autre nombre chiffré. Le calcul est rapide et direct.\n\n"
                   "**La formule :**\n"
                   "   - $C = M^e \pmod{n}$\n\n"
                   "**Exemple simple et commenté :**\n"
                   "   - Clé publique : $(e, n) = (7, 33)$.\n"
                   "   - Message clair $M = 4$. Nous voulons calculer $4^7 \pmod{33}$.\n"
                   "   - **Étape 1** : On commence par les petites puissances pour éviter les grands nombres.\n"
                   "     - $4^1 = 4$\n"
                   "     - $4^2 = 16$\n"
                   "   - **Étape 2** : On continue et on prend le modulo à chaque fois.\n"
                   "     - $4^3 = 4^2 \times 4 = 16 \times 4 = 64$\n"
                   "     - $64 \pmod{33} = 31$\n"
                   "   - **Étape 3** : On continue de la même manière.\n"
                   "     - $4^4 = 4^3 \times 4 \equiv 31 \times 4 = 124$\n"
                   "     - $124 \pmod{33} = 25$\n"
                   "   - **Étape 4** : On cherche à atteindre la puissance 7.\n"
                   "     - $4^7 = 4^4 \times 4^3 \equiv 25 \times 31 = 775 \pmod{33}$\n"
                   "     - $775 \div 33 = 23$ reste $16$. Donc $775 \equiv 16 \pmod{33}$.\n"
                   "   - Le message chiffré $C$ est donc **16**."
    },
    "rsa_math_details_dec": {
        "titre": "Partie 1.5: RSA - Maths du Déchiffrement",
        "contenu": "Le déchiffrement utilise la clé privée pour inverser l'opération de chiffrement. Il s'agit également d'une **puissance modulaire**.\n\n"
                   "**La formule :**\n"
                   "   - $M = C^d \pmod{n}$\n\n"
                   "**Exemple simple et commenté (suite) :**\n"
                   "   - Clé privée : $(d, n) = (3, 33)$.\n"
                   "   - Message chiffré $C = 16$. Nous voulons calculer $16^3 \pmod{33}$.\n"
                   "   - **Étape 1** : On calcule les puissances du message chiffré.\n"
                   "     - $16^1 = 16$\n"
                   "   - **Étape 2** : On continue et on prend le modulo à chaque fois.\n"
                   "     - $16^2 = 256$\n"
                   "     - $256 \pmod{33} = 25$\n"
                   "   - **Étape 3** : On calcule la dernière puissance en utilisant le résultat précédent.\n"
                   "     - $16^3 = 16^2 \times 16 \equiv 25 \times 16 = 400 \pmod{33}$\n"
                   "     - $400 \pmod{33} = 4$\n"
                   "   - Le message déchiffré $M$ est donc **4**, ce qui correspond bien au message original."
    },
    "aes_details_long": {
        "titre": "Partie 2.1: AES - Explication détaillée",
        "contenu": "L'AES (Advanced Encryption Standard) est un algorithme de cryptographie symétrique, largement considéré comme le standard mondial pour le chiffrement des données. Contrairement à RSA, AES utilise la **même clé** pour le chiffrement et le déchiffrement. Il s'agit d'un **chiffrement par blocs**, ce qui signifie qu'il ne traite pas les données bit par bit, mais par blocs de 128 bits (16 octets). La clé peut avoir une taille de 128, 192 ou 256 bits, ce qui influence le nombre de \"tours\" de transformation qu'il effectue sur chaque bloc.\n\n"
                   "La sécurité d'AES ne repose pas sur la théorie des nombres, mais sur un mélange complexe de substitutions et de permutations qui manipulent les données dans un **corps fini** (appelé $GF(2^8)$). Le chiffrement se déroule en plusieurs tours, et chaque tour est une combinaison de quatre transformations distinctes appliquées à une matrice de 4x4 octets, que l'on appelle l'**état**.\n\n"
                   "Les quatre transformations d'un tour AES sont les suivantes :\n\n"
                   "1. **SubBytes (Substitution d'octets)** : Chaque octet de la matrice d'état est remplacé par un autre octet en utilisant une table de substitution fixe appelée **S-box**. Cette transformation est la seule qui est non linéaire, et elle est conçue pour introduire une confusion dans le chiffrement.\n\n"
                   "2. **ShiftRows (Décalage de lignes)** : Cette étape est une simple permutation cyclique des octets dans les lignes de la matrice d'état. Le but de cette opération est de diffuser les octets horizontalement, ce qui garantit qu'un octet chiffré ne dépend pas uniquement de sa colonne d'origine.\n\n"
                   "3. **MixColumns (Mélange de colonnes)** : C'est l'étape la plus complexe mathématiquement. Chaque colonne de la matrice d'état est transformée par une multiplication matricielle dans le corps fini $GF(2^8)$. Cette opération a pour effet de mélanger les quatre octets de chaque colonne, ce qui assure une diffusion verticale et complète.\n\n"
                   "4. **AddRoundKey (Ajout de la sous-clé)** : C'est l'étape finale de chaque tour. Une sous-clé (ou \"round key\") est combinée avec la matrice d'état via une opération **OU Exclusif (XOR)** bit par bit. Cette sous-clé est dérivée de la clé originale de l'algorithme grâce à un processus complexe appelé le **key schedule**.\n\n"
                   "Le processus de chiffrement AES consiste à répéter ces quatre transformations plusieurs fois : 10 tours pour une clé de 128 bits, 12 pour 192 bits et 14 pour 256 bits. Seul le dernier tour omet l'étape `MixColumns`. Pour le déchiffrement, le processus est simplement inversé : chaque étape est appliquée dans l'ordre inverse en utilisant les transformations inverses de chaque opération.\n\n"
                   "La vitesse et l'efficacité d'AES sont ses plus grands atouts. Contrairement à RSA, qui est lent et gourmand en calcul, AES est optimisé pour les processeurs modernes, ce qui le rend idéal pour chiffrer de grandes quantités de données. Sa sécurité, alliée à sa performance, en a fait le standard de facto pour les communications sécurisées, les VPN, les protocoles TLS/SSL (HTTPS) et le chiffrement de fichiers sur les disques durs."
    },
    "aes_chiffrement_process": {
        "titre": "Partie 2.2: AES - Processus de Chiffrement",
        "contenu": "Le processus de chiffrement AES est une séquence répétée des transformations. Voici la séquence pour un bloc de 128 bits :\n\n"
                   "1. **Initialisation** : Le bloc de données initial est combiné avec la clé principale via un XOR (AddRoundKey).\n\n"
                   "2. **Tours de chiffrement (9 tours)** : Chaque tour se compose des 4 étapes :\n"
                   "   - SubBytes\n"
                   "   - ShiftRows\n"
                   "   - MixColumns\n"
                   "   - AddRoundKey\n\n"
                   "3. **Dernier tour (10ème)** : Le dernier tour est légèrement différent, il ne contient pas l'étape MixColumns :\n"
                   "   - SubBytes\n"
                   "   - ShiftRows\n"
                   "   - AddRoundKey\n\n"
                   "Cette succession de transformations garantit que chaque bit du texte chiffré dépend de manière complexe de chaque bit du texte clair et de la clé, ce qui le rend résistant aux attaques."
    },
    "aes_dechiffrement_process": {
        "titre": "Partie 2.3: AES - Processus de Déchiffrement",
        "contenu": "Le déchiffrement AES est l'inverse exact du chiffrement. Le processus est inversé à la fois dans l'ordre des tours et dans les transformations utilisées.\n\n"
                   "1. **Initialisation (inverse)** : Le bloc chiffré est combiné avec la dernière sous-clé via un XOR (AddRoundKey).\n\n"
                   "2. **Dernier tour du déchiffrement (1er tour du chiffrement)** : Ce tour inverse les transformations du dernier tour de chiffrement, mais dans l'ordre inverse et avec les fonctions inverses :\n"
                   "   - Inverse ShiftRows\n"
                   "   - Inverse SubBytes\n"
                   "   - AddRoundKey (avec la sous-clé correspondante)\n\n"
                   "3. **Tours de déchiffrement (9 tours)** : Les tours restants inversent la séquence normale :\n"
                   "   - Inverse MixColumns\n"
                   "   - Inverse ShiftRows\n"
                   "   - Inverse SubBytes\n"
                   "   - AddRoundKey (avec la sous-clé correspondante)\n\n"
                   "Le processus se termine une fois que toutes les transformations inverses ont été appliquées, restaurant le texte original."
    },
    "aes_math_details_enc": {
        "titre": "Partie 2.4: AES - Maths du Chiffrement",
        "contenu": "Les opérations d'AES sont des opérations sur des octets représentés comme des polynômes dans un **corps fini $GF(2^8)$**. Voici les mathématiques appliquées pour le chiffrement :\n\n"
                   "**1. SubBytes** :\n"
                   "   - L'octet d'entrée est remplacé par un autre octet en utilisant une table de substitution fixe (la S-Box). L'opération mathématique derrière cela est de trouver l'**inverse multiplicatif** de l'octet dans le corps fini, puis de lui appliquer une transformation linéaire. Pour nous, c'est comme regarder une table : l'octet '53' est remplacé par l'octet 'ca'.\n\n"
                   "**2. ShiftRows** :\n"
                   "   - C'est une simple permutation des octets. Aucune opération mathématique complexe ici, juste des décalages bit à bit et de lignes.\n\n"
                   "**3. MixColumns** :\n"
                   "   - C'est l'étape la plus complexe. Chaque colonne de la matrice est vue comme un vecteur de 4 octets. Ce vecteur est multiplié par une matrice fixe $M$ pour créer une nouvelle colonne. Toutes les multiplications et additions sont effectuées selon les règles de l'algèbre dans un corps fini $GF(2^8)$. L'effet est de s'assurer que chaque octet d'une colonne est un mélange de tous les octets de la colonne d'origine.\n\n"
                   "**4. AddRoundKey** :\n"
                   "   - Une opération mathématique très simple : le **OU Exclusif (XOR)** bit par bit. C'est une addition sans retenue. On prend les 128 bits de la matrice d'état et les 128 bits de la sous-clé du tour, et on les combine avec un XOR pour créer le nouvel état."
    },
    "aes_math_details_dec": {
        "titre": "Partie 2.5: AES - Maths du Déchiffrement",
        "contenu": "Le déchiffrement AES utilise des fonctions mathématiques inverses pour annuler les opérations de chiffrement.\n\n"
                   "**1. Inverse AddRoundKey** :\n"
                   "   - L'opération XOR est sa propre inverse. On applique le même XOR avec la même sous-clé du tour pour annuler l'effet de l'étape de chiffrement.\n\n"
                   "**2. Inverse ShiftRows** :\n"
                   "   - Les décalages de lignes sont inversés. Par exemple, si une ligne a été décalée de 2 positions à gauche, elle est maintenant décalée de 2 positions à droite pour revenir à son état initial.\n\n"
                   "**3. Inverse SubBytes** :\n"
                   "   - On utilise une table de substitution inverse (l'inverse S-box). Au lieu de trouver l'inverse multiplicatif, on applique la transformation inverse de `SubBytes` pour retrouver l'octet d'origine.\n\n"
                   "**4. Inverse MixColumns** :\n"
                   "   - La multiplication matricielle est inversée. On multiplie chaque colonne de la matrice d'état par la matrice inverse de la matrice $M$ utilisée pendant le chiffrement. Les calculs sont les mêmes, mais la matrice est différente. L'effet est d'annuler le mélange de colonnes, restaurant les colonnes à leur état précédent."
    },
    "concepts_avances": {
        "titre": "Partie 3: Concepts Clés & Applications",
        "contenu": "**1. Fonctions de Hachage :**\n"
                   "   - Une fonction de hachage (comme SHA-256) prend une donnée de taille variable et génère une empreinte unique de taille fixe.\n"
                   "   - Propriétés clés : **Unidirectionnelle** (impossible de remonter au message) et **résistante aux collisions** (difficile de trouver deux messages avec le même hash).\n"
                   "   - Rôle : Elles garantissent l'**intégrité** d'un message. Si le hash d'un message change, c'est que le message a été altéré.\n\n"
                   "**2. La Signature Numérique (avec RSA) :**\n"
                   "   - Objectif : Prouver l'**authenticité** et la **non-répudiation** d'un message.\n"
                   "   - Le principe est inversé par rapport au chiffrement : L'expéditeur génère le hash du message et le chiffre avec sa **clé privée RSA**. Le destinataire utilise la **clé publique** de l'expéditeur pour déchiffrer la signature et obtient le hash. Il le compare ensuite au hash qu'il a lui-même calculé à partir du message reçu. Si les deux hashs correspondent, la signature est valide.\n\n"
                   "**3. Cryptographie Hybride (TLS/SSL) :**\n"
                   "   - Problème : RSA est lent, AES est rapide. Comment combiner leurs forces ?\n"
                   "   - Solution : On utilise la cryptographie hybride. L'algorithme **RSA** (lent mais sécurisé) est utilisé au début de la connexion pour échanger en toute sécurité une **clé AES** (symétrique). Une fois la clé AES partagée, toute la communication est chiffrée et déchiffrée par **AES**, qui est extrêmement rapide. C'est le fonctionnement des connexions sécurisées (HTTPS) sur le web."
    }
}

# --- Fonction pour afficher les détails du sujet sélectionné ---
def afficher_details(section_key):
    """Met à jour le panneau de détails avec les informations de la section choisie."""
    
    details = cryptography_course.get(section_key, {"titre": "Section introuvable", "contenu": "Détails non disponibles."})
    
    titre = details["titre"]
    contenu = details["contenu"]
    
    details_label.configure(text=titre)
    details_textbox.configure(state="normal")
    details_textbox.delete("1.0", "end")
    details_textbox.insert("1.0", contenu)
    details_textbox.configure(state="disabled")

# --- Configuration de la fenêtre principale ---
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("Cours Complet sur la Cryptographie")

# --- Créer les deux cadres principaux ---
frame_liste = customtkinter.CTkFrame(master=app, width=250)
frame_liste.pack(pady=20, padx=20, fill="y", side="left")

frame_details = customtkinter.CTkFrame(master=app)
frame_details.pack(pady=20, padx=20, fill="both", expand=True, side="right")

# --- Contenu du cadre de la liste (gauche) ---
liste_label = customtkinter.CTkLabel(master=frame_liste, text="Sujets du cours", font=("Helvetica", 18, "bold"))
liste_label.pack(pady=10, padx=10)

liste_frame = customtkinter.CTkScrollableFrame(master=frame_liste, width=200)
liste_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Ajouter un bouton pour chaque sujet
sujets = [
    ("Introduction", "intro_course"),
    ("--- Partie 1: RSA ---", ""),
    ("1.1 Explication détaillée", "rsa_details_long"),
    ("1.2 Processus de Chiffrement", "rsa_chiffrement_process"),
    ("1.3 Processus de Déchiffrement", "rsa_dechiffrement_process"),
    ("1.4 Maths du Chiffrement", "rsa_math_details_enc"),
    ("1.5 Maths du Déchiffrement", "rsa_math_details_dec"),
    ("--- Partie 2: AES ---", ""),
    ("2.1 Explication détaillée", "aes_details_long"),
    ("2.2 Processus de Chiffrement", "aes_chiffrement_process"),
    ("2.3 Processus de Déchiffrement", "aes_dechiffrement_process"),
    ("2.4 Maths du Chiffrement", "aes_math_details_enc"),
    ("2.5 Maths du Déchiffrement", "aes_math_details_dec"),
    ("--- Partie 3: Applications ---", ""),
    ("3.1 Concepts clés & Hybride", "concepts_avances"),
]

for nom, cle in sujets:
    if cle:
        button = customtkinter.CTkButton(master=liste_frame, text=nom, command=lambda c=cle: afficher_details(c))
        button.pack(pady=5, padx=5, fill="x")
    else:
        # Créer un label pour les titres de section
        label = customtkinter.CTkLabel(master=liste_frame, text=nom, font=("Helvetica", 14, "bold"), anchor="w")
        label.pack(pady=(15, 5), padx=5, fill="x")

# --- Contenu du cadre des détails (droite) ---
details_label = customtkinter.CTkLabel(master=frame_details, text="Sélectionnez un sujet", font=("Helvetica", 18, "bold"))
details_label.pack(pady=10, padx=10)

details_textbox = customtkinter.CTkTextbox(master=frame_details, corner_radius=10, font=("Courier", 14), wrap="word")
details_textbox.pack(pady=10, padx=10, fill="both", expand=True)
details_textbox.configure(state="disabled")

# Afficher la page d'introduction au démarrage
afficher_details("intro_course")

# --- Lancer l'application ---
if __name__ == "__main__":
    app.mainloop()