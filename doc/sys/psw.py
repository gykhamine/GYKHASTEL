import customtkinter as ctk

class PasswordManagementApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des Mots de Passe Linux")
        self.geometry("1100x750")

        # Configure grid layout for the main window (1 row, 2 columns)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Vertical Navigation Frame (Navbar) ---
        self.navigation_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame,
                                                    text="Mots de Passe Linux",
                                                    compound="left",
                                                    font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # --- Content Frame (where tab content will be displayed) ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Dictionary to hold tab content as CTkTextbox widgets
        self.tab_content_widgets = {}

        # --- Navigation Buttons ---
        self.create_navigation_buttons()

        # Set initial content
        self.select_frame_by_name("1. Introduction")

    def create_navigation_buttons(self):
        button_info = [
            ("1. Introduction", 1),
            ("2. Fichiers Clés", 2),
            ("3. Gestion des Utilisateurs", 3),
            ("4. Gestion des Groupes", 4),
            ("5. Politiques de Mots de Passe", 5),
            ("6. Outils de Gestion", 6),
            ("7. Hachage des Mots de Passe", 7),
            ("8. Attributs de Mots de Passe", 8),
            ("9. Bonnes Pratiques", 9)
        ]

        for i, (text, row) in enumerate(button_info):
            button = ctk.CTkButton(self.navigation_frame,
                                   text=text,
                                   command=lambda name=text: self.select_frame_by_name(name),
                                   corner_radius=0,
                                   height=40,
                                   fg_color="transparent",
                                   hover_color=("gray70", "gray30"),
                                   text_color=("gray10", "gray90"),
                                   anchor="w")
            button.grid(row=row, column=0, sticky="ew", padx=0, pady=0)
            setattr(self, f"nav_button_{row}", button)

        self.create_tab_content()

    def select_frame_by_name(self, name):
        # Update button colors
        buttons = [getattr(self, f"nav_button_{i}") for i in range(1, 10)]
        for btn in buttons:
            if btn.cget("text") == name:
                btn.configure(fg_color=("gray75", "gray25"))
            else:
                btn.configure(fg_color="transparent")

        # Hide all content frames and show the selected one
        for frame_name, widget in self.tab_content_widgets.items():
            if frame_name == name:
                widget.grid(row=0, column=0, sticky="nsew")
            else:
                widget.grid_forget()

    def create_tab_content(self):
        def add_scrollable_text_to_content_frame(name, text_content):
            frame = ctk.CTkFrame(self.content_frame, corner_radius=0)
            text_widget = ctk.CTkTextbox(frame, wrap="word", width=800, height=600)
            text_widget.insert("0.0", text_content)
            text_widget.configure(state="disabled")
            text_widget.pack(padx=10, pady=10, fill="both", expand=True)
            self.tab_content_widgets[name] = frame

        # --- Tab 1: Introduction ---
        intro_text = """
        ### Introduction à la Gestion des Mots de Passe Linux

        La gestion des utilisateurs et de leurs mots de passe est une pierre angulaire de la sécurité et de l'administration sur les systèmes Linux. Elle détermine qui peut accéder au système et aux ressources, et comment cette authentification est protégée.

        **Objectifs Clés :**
        -   **Sécurité :** Protéger l'accès non autorisé aux systèmes et aux données.
        -   **Authentification :** Vérifier l'identité des utilisateurs.
        -   **Autorisation :** Permettre l'accès aux ressources appropriées après authentification.
        -   **Conformité :** Respecter les politiques de sécurité (ex: complexité des mots de passe, expiration).

        Les mots de passe sur Linux ne sont jamais stockés en clair. Ils sont toujours **hachés** (transformés par une fonction cryptographique unidirectionnelle) et stockés. Cela signifie que même un administrateur système ne peut pas "voir" votre mot de passe, seulement sa version hachée. Lors de la connexion, le mot de passe entré est haché et comparé au hachage stocké.

        Cette application vous guidera à travers les concepts, les fichiers, les outils et les bonnes pratiques pour une gestion robuste des mots de passe sur Linux.
        """
        add_scrollable_text_to_content_frame("1. Introduction", intro_text)

        # --- Tab 2: Fichiers Clés ---
        key_files_text = """
        ### Fichiers Clés pour la Gestion des Utilisateurs et Mots de Passe

        Plusieurs fichiers système essentiels contiennent les informations sur les utilisateurs, les groupes et les mots de passe hachés.

        #### 1. `/etc/passwd`
        -   Contient des informations de base sur chaque compte utilisateur.
        -   **Format :** `nom_utilisateur:x:UID:GID:Commentaire:Répertoire_personnel:Shell`
        -   `x` : Indique que le mot de passe haché est stocké dans `/etc/shadow`.
        -   **Accessible en lecture par tout le monde.** C'est pourquoi les mots de passe ne sont pas stockés ici.

        **Exemple :**
        `john:x:1001:1001:John Doe:/home/john:/bin/bash`

        #### 2. `/etc/shadow`
        -   Contient les mots de passe hachés des utilisateurs et des informations sur l'expiration des mots de passe.
        -   **Accessible en lecture uniquement par l'utilisateur `root` (et les membres du groupe `shadow` si présent).**
        -   **Format :** `nom_utilisateur:mot_de_passe_haché:dernière_mod_mdp:âge_min_mdp:âge_max_mdp:jours_avant_expiration:jours_après_expiration:date_expiration_compte:réservé`

        **Exemple :**
        `john:$6$rounds=40000$....../......:19760:0:99999:7::: `
        (Le `$6$` indique un hachage SHA-512)

        #### 3. `/etc/group`
        -   Contient des informations sur les groupes d'utilisateurs.
        -   **Accessible en lecture par tout le monde.**
        -   **Format :** `nom_groupe:x:GID:membres`
        -   `x` : Indique que les mots de passe hachés pour les groupes (rarement utilisés) sont dans `/etc/gshadow`.

        **Exemple :**
        `admin:x:1000:` (groupe `admin` avec GID 1000, aucun membre listé ici)
        `developers:x:1002:john,jane` (groupe `developers` avec membres `john` et `jane`)

        #### 4. `/etc/gshadow`
        -   Contient les mots de passe hachés pour les groupes et les administrateurs de groupes (rarement utilisé).
        -   **Accessible en lecture uniquement par l'utilisateur `root`.**
        -   **Format :** `nom_groupe:mot_de_passe_haché:administrateurs:membres`

        #### 5. `/etc/login.defs`
        -   Contient des paramètres par défaut pour la création de nouveaux utilisateurs et des politiques de mots de passe globales.
        -   **Exemples de paramètres :**
            -   `PASS_MAX_DAYS`: Nombre maximum de jours pendant lesquels un mot de passe peut être utilisé.
            -   `PASS_MIN_DAYS`: Nombre minimum de jours avant qu'un mot de passe puisse être changé.
            -   `PASS_WARN_AGE`: Nombre de jours avant l'expiration pour avertir l'utilisateur.
            -   `UID_MIN`, `GID_MIN`: UIDs/GIDs minimum pour les utilisateurs et groupes normaux.
        -   Ces paramètres agissent comme des valeurs par défaut lors de la création d'utilisateurs, mais les paramètres spécifiques dans `/etc/shadow` ont la priorité.

        #### 6. `/etc/default/useradd`
        -   Contient les valeurs par défaut pour la commande `useradd`, comme le répertoire de squelette (`SKEL`), le shell par défaut (`SHELL`), et le groupe principal (`GROUP`).
        """
        add_scrollable_text_to_content_frame("2. Fichiers Clés", key_files_text)

        # --- Tab 3: Gestion des Utilisateurs ---
        user_management_text = """
        ### Gestion des Utilisateurs

        Les commandes suivantes sont utilisées pour créer, modifier et supprimer des comptes utilisateurs. Seul l'utilisateur `root` peut exécuter ces commandes.

        #### 1. Créer un Utilisateur : `useradd`
        Permet de créer un nouveau compte utilisateur avec des options spécifiques.

        **Syntaxe de base :**
        `sudo useradd [options] nom_utilisateur`

        **Options Courantes :**
        -   `-m` : Crée le répertoire personnel de l'utilisateur (`/home/nom_utilisateur`). **Recommandé.**
        -   `-s /chemin/vers/shell` : Spécifie le shell de connexion (ex: `/bin/bash`, `/bin/sh`, `/sbin/nologin`).
        -   `-c "Commentaire"` : Ajoute une description (souvent le nom complet).
        -   `-G groupe1,groupe2` : Ajoute l'utilisateur à des groupes supplémentaires.
        -   `-g groupe_principal` : Définit le groupe principal de l'utilisateur.
        -   `-u UID` : Définit l'UID (User ID) spécifique.
        -   `-d /chemin/home` : Définit un répertoire personnel personnalisé.
        -   `-e YYYY-MM-DD` : Définit une date d'expiration pour le compte.
        -   `-f jours` : Définit le nombre de jours après expiration du mot de passe avant que le compte ne soit désactivé.

        **Exemple :**
        `sudo useradd -m -s /bin/bash -c "Alice Dupont" -G sudo,developers alice`
        (Crée 'alice', son répertoire personnel, avec bash comme shell, l'ajoute aux groupes `sudo` et `developers`.)

        #### 2. Définir/Modifier le Mot de Passe : `passwd`
        Permet de définir ou de changer le mot de passe d'un utilisateur.

        **Syntaxe de base :**
        `sudo passwd nom_utilisateur` (pour root, qui sera invité à entrer le nouveau mot de passe deux fois)
        `passwd` (pour l'utilisateur lui-même, qui sera invité à entrer l'ancien puis le nouveau mot de passe)

        #### 3. Modifier les Attributs d'un Utilisateur : `usermod`
        Permet de modifier les propriétés d'un compte utilisateur existant.

        **Syntaxe de base :**
        `sudo usermod [options] nom_utilisateur`

        **Options Courantes (similaires à `useradd`) :**
        -   `-l nouveau_nom` : Change le nom d'utilisateur (ne change pas le répertoire personnel).
        -   `-d /nouveau/home -m` : Déplace le répertoire personnel vers un nouveau chemin.
        -   `-s /bin/bash` : Change le shell.
        -   `-G groupe1,groupe2` : Ajoute l'utilisateur à de NOUVEAUX groupes.
        -   `-aG groupe` : Ajoute l'utilisateur à un groupe sans supprimer les autres.
        -   `-U` : Déverrouille un compte.
        -   `-L` : Verrouille un compte (empêche la connexion).
        -   `-e YYYY-MM-DD` : Change la date d'expiration du compte.

        **Exemple :**
        `sudo usermod -aG sales bob` (Ajoute 'bob' au groupe 'sales' sans retirer les autres groupes.)
        `sudo usermod -L charlie` (Verrouille le compte de 'charlie'.)

        #### 4. Supprimer un Utilisateur : `userdel`
        Permet de supprimer un compte utilisateur.

        **Syntaxe de base :**
        `sudo userdel [options] nom_utilisateur`

        **Option Courante :**
        -   `-r` : Supprime également le répertoire personnel et la file de spoule de l'utilisateur. **Recommandé.**

        **Exemple :**
        `sudo userdel -r david` (Supprime 'david' et son répertoire personnel.)

        #### 5. Afficher les Infos Utilisateur : `id`
        Affiche l'UID, le GID et les groupes auxquels un utilisateur appartient.

        **Exemple :**
        `id john`
        `uid=1001(john) gid=1001(john) groupes=1001(john),10(wheel),1002(developers)`
        """
        add_scrollable_text_to_content_frame("3. Gestion des Utilisateurs", user_management_text)

        # --- Tab 4: Gestion des Groupes ---
        group_management_text = """
        ### Gestion des Groupes

        Les groupes sont essentiels pour gérer les permissions d'accès aux fichiers et aux ressources de manière collective.

        #### 1. Créer un Groupe : `groupadd`
        Permet de créer un nouveau groupe d'utilisateurs.

        **Syntaxe de base :**
        `sudo groupadd [options] nom_groupe`

        **Options Courantes :**
        -   `-g GID` : Spécifie un GID (Group ID) pour le nouveau groupe.
        -   `-r` : Crée un groupe système (avec un GID bas, généralement 0-999).

        **Exemple :**
        `sudo groupadd sales` (Crée un groupe nommé 'sales'.)

        #### 2. Modifier un Groupe : `groupmod`
        Permet de modifier les propriétés d'un groupe existant.

        **Syntaxe de base :**
        `sudo groupmod [options] nom_groupe`

        **Options Courantes :**
        -   `-n nouveau_nom` : Change le nom du groupe.
        -   `-g nouveau_GID` : Change le GID du groupe.

        **Exemple :**
        `sudo groupmod -n managers teamlead` (Renomme le groupe 'managers' en 'teamlead'.)

        #### 3. Supprimer un Groupe : `groupdel`
        Permet de supprimer un groupe. Un groupe ne peut pas être supprimé s'il est le groupe principal d'un utilisateur existant.

        **Syntaxe de base :**
        `sudo groupdel nom_groupe`

        **Exemple :**
        `sudo groupdel old_group` (Supprime le groupe 'old_group'.)

        #### 4. Gérer les Membres d'un Groupe : `gpasswd`
        `gpasswd` est un outil flexible pour ajouter ou supprimer des membres d'un groupe, ou définir un administrateur de groupe.

        **Syntaxe de base :**
        `sudo gpasswd [options] groupe`

        **Options Courantes :**
        -   `-a utilisateur` : Ajoute un utilisateur au groupe.
        -   `-d utilisateur` : Supprime un utilisateur du groupe.
        -   `-A utilisateur1,utilisateur2` : Définit les utilisateurs administrateurs du groupe.
        -   `-M utilisateur1,utilisateur2` : Définit les membres du groupe (remplace les membres existants).

        **Exemples :**
        `sudo gpasswd -a sara developers` (Ajoute 'sara' au groupe 'developers'.)
        `sudo gpasswd -d bob developers` (Supprime 'bob' du groupe 'developers'.)
        `sudo gpasswd -M alice,bob sales` (Définit 'alice' et 'bob' comme les seuls membres du groupe 'sales'.)

        #### 5. Afficher les Membres d'un Groupe : `getent group` ou `grep`
        Pour afficher tous les membres d'un groupe, vous pouvez inspecter `/etc/group` ou utiliser `getent`.

        **Exemple :**
        `getent group developers`
        `developers:x:1002:john,jane,sara`

        `grep ^developers /etc/group`
        `developers:x:1002:john,jane,sara`

        #### 6. Nouvelle Groupe Par Défaut pour `useradd`
        Le fichier `/etc/default/useradd` peut spécifier un groupe par défaut pour les nouveaux utilisateurs via la directive `GROUP=`.
        """
        add_scrollable_text_to_content_frame("4. Gestion des Groupes", group_management_text)

        # --- Tab 5: Politiques de Mots de Passe ---
        password_policy_text = """
        ### Politiques de Mots de Passe

        Les politiques de mots de passe définissent les règles que les mots de passe doivent suivre. Elles sont cruciales pour la sécurité.

        #### 1. Expiration des Mots de Passe (`/etc/shadow`)
        Les champs dans `/etc/shadow` contrôlent l'expiration et les avertissements :
        -   **`dernière_mod_mdp` :** Date (en jours depuis 1970-01-01) de la dernière modification du mot de passe.
        -   **`âge_min_mdp` :** Nombre minimum de jours avant qu'un utilisateur puisse changer son mot de passe. `0` signifie "peut changer à tout moment".
        -   **`âge_max_mdp` :** Nombre maximum de jours après lequel le mot de passe doit être changé. `99999` signifie "jamais expiré".
        -   **`jours_avant_expiration` :** Nombre de jours avant l'expiration pour avertir l'utilisateur.

        **Modification via `chage` :**
        L'outil `chage` (change age) permet de gérer ces attributs.
        `sudo chage -M 90 john` (Mot de passe de John expire après 90 jours.)
        `sudo chage -m 7 john` (John doit attendre au moins 7 jours avant de pouvoir changer son mot de passe.)
        `sudo chage -W 14 john` (Avertir John 14 jours avant l'expiration.)
        `sudo chage -E 2025-12-31 john` (Le compte de John expire le 31 décembre 2025.)
        `sudo chage -l john` (Lister les informations d'expiration pour John.)

        #### 2. Complexité des Mots de Passe (PAM et `pam_cracklib`/`pam_pwquality`)

        Linux utilise le module **PAM (Pluggable Authentication Modules)** pour l'authentification. Les règles de complexité sont généralement définies dans les fichiers de configuration PAM.

        **Fichiers pertinents :**
        -   `/etc/pam.d/passwd` : Règle l'authentification de `passwd`.
        -   `/etc/pam.d/system-auth` : Règle l'authentification générale du système.
        -   `/etc/pam.d/sshd` : Règle l'authentification SSH.

        **Modules PAM couramment utilisés pour la complexité :**

        -   **`pam_pwquality.so` (recommandé, moderne) :**
            Ce module fournit des règles de qualité de mot de passe plus robustes.
            **Exemple de configuration dans `/etc/pam.d/system-auth` (section `password` requise) :**
            ```
            password    requisite     pam_pwquality.so try_first_pass local_users_only \
                                        retry=3 authtok_type= minlen=12 minclass=3 dcredit=-1 ucredit=-1 \
                                        ocredit=-1 lcredit=-1 dictcheck=1 reject_upper reject_lower reject_digit reject_other \
                                        enforce_for_root
            ```
            -   `minlen=12` : Longueur minimale de 12 caractères.
            -   `minclass=3` : Au moins 3 classes de caractères (majuscules, minuscules, chiffres, symboles).
            -   `dcredit=-1`, `ucredit=-1`, `ocredit=-1`, `lcredit=-1` : Exige au moins un chiffre, une majuscule, un symbole, une minuscule.
            -   `dictcheck=1` : Vérifie contre les mots de dictionnaire.
            -   `reject_upper`, etc. : Empêche la réutilisation de caractères spécifiques (par exemple, si le mot de passe contient des chiffres, un nouveau mot de passe doit aussi contenir des chiffres).
            -   `enforce_for_root`: Applique ces règles au mot de passe de root.

        -   **`pam_cracklib.so` (ancien, moins flexible) :**
            Utilisé sur les systèmes plus anciens.
            **Exemple :**
            ```
            password    requisite     pam_cracklib.so try_first_pass retry=3 minlen=8 difok=3 \
                                        ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
            ```
            -   `minlen=8` : Longueur minimale de 8.
            -   `difok=3` : Au moins 3 caractères différents de l'ancien mot de passe.
            -   `ucredit`, `lcredit`, `dcredit`, `ocredit` : Exigences de caractères (majuscules, minuscules, chiffres, autres).

        Après modification des fichiers PAM, les changements sont immédiatement appliqués pour les futures tentatives de changement de mot de passe.
        """
        add_scrollable_text_to_content_frame("5. Politiques de Mots de Passe", password_policy_text)

        # --- Tab 6: Outils de Gestion ---
        management_tools_text = """
        ### Outils de Gestion des Mots de Passe et Utilisateurs

        En plus des commandes vues précédemment (`useradd`, `usermod`, `userdel`, `groupadd`, `groupmod`, `groupdel`, `passwd`, `chage`, `gpasswd`), voici d'autres outils utiles.

        #### 1. `pwck` (Password Check)
        -   Vérifie l'intégrité et la syntaxe des fichiers `/etc/passwd` et `/etc/shadow`.
        -   Alerte sur les incohérences ou les erreurs.
        -   `sudo pwck`

        #### 2. `grpck` (Group Check)
        -   Vérifie l'intégrité et la syntaxe des fichiers `/etc/group` et `/etc/gshadow`.
        -   `sudo grpck`

        #### 3. `newusers`
        -   Permet de créer plusieurs utilisateurs à partir d'un fichier texte formaté.
        -   **Très utile pour l'automatisation.**
        -   Le fichier doit être au format de `/etc/passwd`.
        -   `sudo newusers fichier_utilisateurs.txt`
        -   Les mots de passe peuvent être définis après avec `chpasswd`.

        #### 4. `chpasswd`
        -   Permet de mettre à jour les mots de passe de plusieurs utilisateurs à partir d'un fichier ou de l'entrée standard.
        -   **Format du fichier :** `utilisateur:mot_de_passe_en_clair`
        -   `sudo chpasswd < users_passwords.txt`
        -   `echo "john:N0uv3auM0tDePasse" | sudo chpasswd` (À éviter pour des raisons de sécurité !)

        #### 5. `su` (Substitute User)
        -   Permet de changer d'utilisateur (souvent vers `root`).
        -   `su -` (se connecter en tant que root avec l'environnement de root)
        -   `su nom_utilisateur` (se connecter en tant que cet utilisateur, en gardant l'environnement de l'utilisateur d'origine)

        #### 6. `sudo` (SuperUser DO)
        -   Permet à un utilisateur autorisé d'exécuter des commandes avec les privilèges d'un autre utilisateur (par défaut `root`), sans connaître le mot de passe de l'utilisateur cible.
        -   Configuration via `visudo` (voir la section dédiée à visudo).

        #### 7. `logname`
        -   Affiche le nom de connexion de l'utilisateur actuel.
        -   `logname`

        #### 8. `finger` (souvent non installé par défaut)
        -   Affiche des informations sur les utilisateurs du système.
        -   Peut être considéré comme une faille de sécurité s'il est utilisé en externe.
        -   `finger nom_utilisateur`

        #### 9. `last` / `lastlog`
        -   `last` : Affiche l'historique des dernières connexions des utilisateurs.
        -   `lastlog` : Affiche les informations de la dernière connexion de chaque utilisateur.
        """
        add_scrollable_text_to_content_frame("6. Outils de Gestion", management_tools_text)

        # --- Tab 7: Hachage des Mots de Passe ---
        hashing_text = """
        ### Hachage des Mots de Passe

        Les mots de passe ne sont jamais stockés en clair sur Linux pour des raisons de sécurité fondamentales. Ils sont transformés par une **fonction de hachage cryptographique unidirectionnelle**.

        #### Pourquoi le Hachage ?
        -   **Protection :** Si le fichier `/etc/shadow` est compromis, les attaquants n'obtiennent pas les mots de passe en clair, mais seulement leurs hachages.
        -   **Vérification :** Le système peut vérifier un mot de passe sans jamais le connaître en clair. Quand un utilisateur se connecte, son mot de passe est haché et comparé au hachage stocké.

        #### Fonctions de Hachage Courantes sur Linux :
        Le type de hachage est indiqué par un préfixe dans le champ du mot de passe dans `/etc/shadow`.

        -   **`$1$` : MD5**
            -   Ancien et **déconseillé** car vulnérable aux attaques par collision et à la force brute (faible coût de calcul).
            -   Ex: `$1$salt$hashed_password`

        -   **`$2a$`, `$2y$`, `$2b$` : Blowfish (bcrypt)**
            -   Plus moderne et résistant à la force brute grâce à un facteur de coût (itérations) configurable.
            -   `$2y$` est la version la plus courante.
            -   Ex: `$2y$10$salt_and_hashed_password` (le '10' est le facteur de coût)

        -   **`$5$` : SHA-256**
            -   Plus sécurisé que MD5. Utilise un sel et un nombre d'itérations.
            -   Ex: `$5$rounds=5000$salt$hashed_password` (le '5000' est le nombre d'itérations)

        -   **`$6$` : SHA-512**
            -   Actuellement le standard et **le plus recommandé** pour les systèmes Linux modernes.
            -   Offre une meilleure résistance aux attaques par force brute que SHA-256 et MD5.
            -   Utilise un sel et un nombre d'itérations.
            -   Ex: `$6$rounds=5000$salt$hashed_password`

        #### Le "Sel" (Salt) :
        -   Une chaîne de caractères aléatoire ajoutée au mot de passe avant le hachage.
        -   **Pourquoi un sel ?** Empêche les attaques par "rainbow table" (tables pré-calculées de hachages de mots de passe courants) et garantit que deux utilisateurs avec le même mot de passe auront des hachages différents. Chaque hachage de mot de passe dans `/etc/shadow` a son propre sel unique.

        #### Facteur de Coût (Rounds) :
        -   Le nombre d'itérations qu'une fonction de hachage effectue.
        -   Un facteur de coût plus élevé rend le hachage plus lent, ce qui est une bonne chose ! Cela rend les attaques par force brute beaucoup plus coûteuses en temps et en ressources.
        -   Le nombre de tours par défaut pour SHA-512 est souvent de 5000. Vous pouvez le voir dans le hachage (par exemple, `rounds=5000`).
        -   Le facteur de coût est géré par les configurations PAM, notamment dans `/etc/login.defs` pour les valeurs par défaut de `ENCRYPT_METHOD` et `SHA_CRYPT_ALGORITHM_ROUNDS`.

        #### Changer l'Algorithme de Hachage par Défaut :
        Vous pouvez définir l'algorithme de hachage par défaut pour les nouveaux mots de passe dans `/etc/login.defs` :
        `ENCRYPT_METHOD SHA512` (ou `BLOWFISH`, `MD5`)

        Pour les mots de passe existants, ils conserveront leur méthode de hachage jusqu'à ce qu'ils soient modifiés. Lors de la modification, ils seront hachés avec la nouvelle méthode par défaut.
        """
        add_scrollable_text_to_content_frame("7. Hachage des Mots de Passe", hashing_text)

        # --- Tab 8: Attributs de Mots de Passe ---
        password_attributes_text = """
        ### Attributs Avancés des Mots de Passe et des Comptes

        Au-delà de l'expiration simple, les systèmes Linux offrent des options granulaires pour gérer l'état et le comportement des comptes utilisateurs. Ces attributs sont principalement gérés via la commande `chage`.

        #### 1. Verrouiller / Déverrouiller un Compte :

        -   **Verrouiller un compte (`-L` ou `--lock`) :** Empêche un utilisateur de se connecter sans supprimer son compte. Le mot de passe haché dans `/etc/shadow` est préfixé d'un `!`.
            `sudo usermod -L nom_utilisateur`
            Le mot de passe haché de `john` passe de :
            `john:$6$rounds=...`
            à :
            `john:!$6$rounds=...`

        -   **Déverrouiller un compte (`-U` ou `--unlock`) :** Supprime le `!` et permet à l'utilisateur de se connecter à nouveau.
            `sudo usermod -U nom_utilisateur`

        #### 2. Expiration du Compte Entier :

        -   **Définir une date d'expiration (`-E` ou `--expiredate`) :** Le compte sera désactivé après cette date.
            `sudo chage -E "YYYY-MM-DD" nom_utilisateur`
            **Exemple :** `sudo chage -E "2025-12-31" alice` (Alice ne pourra plus se connecter après le 31 décembre 2025.)

        -   **Effacer la date d'expiration :**
            `sudo chage -E -1 nom_utilisateur`

        #### 3. Période d'Inactivité après l'Expiration du Mot de Passe :

        -   **Définir la période d'inactivité (`-I` ou `--inactive`) :** Nombre de jours après l'expiration du mot de passe (si `PASS_MAX_DAYS` est défini) où le compte sera désactivé si l'utilisateur ne se connecte pas ou ne change pas son mot de passe.
            `sudo chage -I jours nom_utilisateur`
            **Exemple :** `sudo chage -I 30 bob` (Si le mot de passe de Bob expire, il a 30 jours pour le changer avant que son compte ne soit verrouillé.)

        -   **Désactiver la période d'inactivité :**
            `sudo chage -I -1 nom_utilisateur`

        #### 4. Afficher les Attributs :

        -   **Lister tous les attributs (`-l` ou `--list`) :**
            `sudo chage -l nom_utilisateur`
            Ceci affichera toutes les informations d'expiration, d'inactivité, etc., pour l'utilisateur spécifié.

        **Exemple de sortie `chage -l john` :**
        ```
        Last password change                                : Jul 20, 2025
        Password expires                                  : Aug 18, 2025
        Password inactive                                 : never
        Account expires                                   : never
        Minimum number of days between password change    : 0
        Maximum number of days between password change    : 30
        Number of days of warning before password expires : 7
        ```

        Ces attributs offrent un contrôle précis sur la durée de vie et le comportement des comptes, permettant aux administrateurs de renforcer la sécurité en gérant les risques liés aux comptes obsolètes ou aux mots de passe non mis à jour.
        """
        add_scrollable_text_to_content_frame("8. Attributs de Mots de Passe", password_attributes_text)

        # --- Tab 9: Bonnes Pratiques ---
        best_practices_text = """
        ### Bonnes Pratiques pour la Gestion des Mots de Passe Linux

        Une gestion rigoureuse des mots de passe est cruciale pour la sécurité de tout système Linux.

        1.  **Politique de Mots de Passe Forte :**
            -   **Longueur :** Exigez une longueur minimale d'au moins 12-16 caractères.
            -   **Complexité :** Forcez l'utilisation de majuscules, minuscules, chiffres et symboles.
            -   **Unicité :** Empêchez la réutilisation des anciens mots de passe (PAM peut gérer cela).
            -   **Expiration :** Définissez une durée de vie maximale pour les mots de passe (ex: 90 jours).

        2.  **Utilisez des Outils Fiables :**
            -   **`passwd` :** Toujours pour changer les mots de passe.
            -   **`chage` :** Pour gérer les politiques d'expiration des mots de passe et des comptes.
            -   **`usermod` / `useradd` / `userdel` :** Pour la gestion des utilisateurs et leurs attributs.

        3.  **Renforcez PAM :**
            -   Configurez **`pam_pwquality`** (ou `pam_cracklib`) dans `/etc/pam.d/system-auth` (et potentiellement `passwd` et `sshd`) pour imposer la complexité.
            -   Assurez-vous que les modules de `cracklib`/`pwquality` sont configurés pour vérifier les mots de passe courants (dictionnaires).

        4.  **Verrouillez les Comptes Inutilisés :**
            -   Si un utilisateur est temporairement inactif, **verrouillez son compte** avec `usermod -L` plutôt que de le supprimer.
            -   Désactivez ou supprimez les comptes qui ne sont plus nécessaires.

        5.  **Audit Régulier :**
            -   Vérifiez régulièrement les fichiers `/etc/passwd`, `/etc/shadow`, et `/etc/group` pour détecter toute anomalie ou compte non autorisé.
            -   Utilisez `pwck` et `grpck` pour vérifier l'intégrité de ces fichiers.
            -   Vérifiez la date de dernière connexion des utilisateurs avec `lastlog` pour identifier les comptes dormants.

        6.  **Sécurité du Fichier `shadow` :**
            -   Assurez-vous que les permissions de `/etc/shadow` sont strictes (généralement `0640` ou `0400`) et que seul `root` peut le lire.
            -   Ne partagez jamais le contenu de ce fichier.

        7.  **Utilisez `sudo` (avec `visudo`) au lieu de `su` vers `root` :**
            -   Minimisez l'utilisation du compte `root` direct. Accordez les privilèges via `sudo` pour des tâches spécifiques.
            -   Chaque action `sudo` est loguée, offrant une meilleure traçabilité.

        8.  **Informez les Utilisateurs :**
            -   Éduquez les utilisateurs sur l'importance des mots de passe forts et sur les politiques de l'entreprise.
            -   Fournissez des directives claires sur la création de mots de passe (phrases de passe).

        9.  **Gestion Centralisée (pour de grands environnements) :**
            -   Pour un grand nombre d'utilisateurs, envisagez des solutions centralisées comme **LDAP (OpenLDAP)**, **FreeIPA**, ou **Active Directory** pour la gestion des identités et des mots de passe.

        10. **Surveillance des Logs :**
            -   Surveillez les logs d'authentification (`/var/log/auth.log` ou `/var/log/secure`) pour détecter les tentatives de connexion échouées ou les activités suspectes.
        """
        add_scrollable_text_to_content_frame("9. Bonnes Pratiques", best_practices_text)

if __name__ == "__main__":
    app = PasswordManagementApp()
    app.mainloop()