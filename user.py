import customtkinter as ctk

class UserGroupPermissionsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des Utilisateurs, Groupes et Permissions Linux")
        self.geometry("1100x750")

        # Configure grid layout for the main window (1 row, 2 columns)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Vertical Navigation Frame (Navbar) ---
        self.navigation_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame,
                                                    text="Guide Linux",
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
            ("2. Gestion des Utilisateurs", 2),
            ("3. Gestion des Groupes", 3),
            ("4. Permissions de Fichiers et Répertoires", 4),
            ("5. Permissions Spéciales (SUID, SGID, Sticky)", 5),
            ("6. ACLs (Listes de Contrôle d'Accès)", 6),
            ("7. Umask", 7),
            ("8. Propriété des Fichiers", 8),
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
        ### Introduction à la Gestion des Utilisateurs, Groupes et Permissions Linux

        La sécurité et l'administration des systèmes Linux reposent fondamentalement sur un modèle d'accès strict basé sur les **utilisateurs**, les **groupes** et les **permissions** sur les fichiers et répertoires. Comprendre et maîtriser ces concepts est essentiel pour tout administrateur système ou utilisateur avancé.

        **Objectifs de ce Guide :**
        -   Apprendre à **créer et gérer des utilisateurs** individuels.
        -   Comprendre le rôle des **groupes** pour organiser les utilisateurs et simplifier les permissions.
        -   Maîtriser les **permissions de base** (lecture, écriture, exécution) pour les fichiers et répertoires.
        -   Découvrir les **permissions spéciales** (SUID, SGID, Sticky Bit) et leur impact sur la sécurité.
        -   Explorer les **ACLs (Listes de Contrôle d'Accès)** pour une gestion des permissions plus granulaire.
        -   Comprendre le rôle de l'**umask** dans la définition des permissions par défaut.
        -   Apprendre à gérer la **propriété** des fichiers et répertoires.

        Ce système permet de définir précisément qui peut faire quoi sur le système, garantissant ainsi l'intégrité des données et la stabilité des opérations.
        """
        add_scrollable_text_to_content_frame("1. Introduction", intro_text)

        # --- Tab 2: Gestion des Utilisateurs ---
        users_text = """
        ### Gestion des Utilisateurs

        Un **utilisateur** est une entité qui peut se connecter au système et interagir avec lui. Chaque utilisateur est identifié par un **UID (User ID)** unique.

        #### 1. Fichiers Clés pour les Utilisateurs :
        -   `/etc/passwd` : Informations de base sur les utilisateurs (nom, UID, GID principal, répertoire personnel, shell).
        -   `/etc/shadow` : Mots de passe hachés et politiques d'expiration des mots de passe (accessible uniquement par `root`).

        #### 2. Créer un Utilisateur : `useradd`
        Permet d'ajouter un nouveau compte utilisateur.

        **Syntaxe :** `sudo useradd [options] nom_utilisateur`

        **Options courantes :**
        -   `-m` : Crée le **répertoire personnel** de l'utilisateur (`/home/nom_utilisateur`). **Fortement recommandé.**
        -   `-s /chemin/shell` : Spécifie le **shell de connexion** (ex: `/bin/bash`, `/sbin/nologin`).
        -   `-c "Commentaire"` : Ajoute un commentaire ou une description (souvent le nom complet de l'utilisateur).
        -   `-G groupe1,groupe2` : Ajoute l'utilisateur à des **groupes secondaires** spécifiques.
        -   `-g groupe_principal` : Définit le **groupe principal** de l'utilisateur. Si non spécifié, un groupe du même nom que l'utilisateur est souvent créé par défaut (`useradd user -m` crée un groupe `user`).
        -   `-u UID` : Spécifie un **UID** personnalisé.
        -   `-e YYYY-MM-DD` : Définit une **date d'expiration** pour le compte.

        **Exemple :**
        `sudo useradd -m -s /bin/bash -c "Alice Martin" -G admin,dev alice`
        *Crée l'utilisateur 'alice', son répertoire personnel, utilise /bin/bash comme shell et l'ajoute aux groupes 'admin' et 'dev'.*

        #### 3. Définir/Modifier le Mot de Passe : `passwd`
        Après avoir créé un utilisateur, vous devez lui assigner un mot de passe.

        **Syntaxe :** `sudo passwd nom_utilisateur`

        **Exemple :**
        `sudo passwd alice`
        *Le système vous invitera à entrer et confirmer le nouveau mot de passe pour 'alice'.*

        #### 4. Modifier un Utilisateur : `usermod`
        Permet de modifier les attributs d'un compte utilisateur existant.

        **Syntaxe :** `sudo usermod [options] nom_utilisateur`

        **Options courantes (similaires à `useradd`) :**
        -   `-l nouveau_nom` : Change le **nom d'utilisateur** (le répertoire personnel n'est pas renommé automatiquement).
        -   `-d /nouveau/chemin -m` : Déplace le répertoire personnel vers un nouveau chemin.
        -   `-s /bin/sh` : Change le shell.
        -   `-aG groupe` : **Ajoute** l'utilisateur à un groupe **sans retirer les groupes existants**.
        -   `-G groupe1,groupe2` : **Remplace** les groupes secondaires existants par ceux spécifiés.
        -   `-L` : **Verrouille** le compte (empêche la connexion). Le mot de passe haché dans `/etc/shadow` est préfixé d'un `!`.
        -   `-U` : **Déverrouille** le compte.

        **Exemple :**
        `sudo usermod -aG sales bob`
        *Ajoute l'utilisateur 'bob' au groupe 'sales' tout en conservant ses autres appartenances de groupe.*
        `sudo usermod -L charlie`
        *Verrouille le compte de 'charlie' pour empêcher la connexion.*

        #### 5. Supprimer un Utilisateur : `userdel`
        Supprime un compte utilisateur.

        **Syntaxe :** `sudo userdel [options] nom_utilisateur`

        **Option courante :**
        -   `-r` : Supprime également le **répertoire personnel** de l'utilisateur et sa file de spoule. **Fortement recommandé.**

        **Exemple :**
        `sudo userdel -r david`
        *Supprime l'utilisateur 'david' et son répertoire personnel.*

        #### 6. Informations sur l'Utilisateur : `id`
        Affiche l'UID, le GID principal et tous les groupes secondaires auxquels un utilisateur appartient.

        **Exemple :**
        `id alice`
        `uid=1001(alice) gid=1001(alice) groupes=1001(alice),27(sudo),1002(dev)`
        """
        add_scrollable_text_to_content_frame("2. Gestion des Utilisateurs", users_text)

        # --- Tab 3: Gestion des Groupes ---
        groups_text = """
        ### Gestion des Groupes

        Un **groupe** est une collection d'utilisateurs. Les groupes simplifient la gestion des permissions en permettant d'accorder ou de refuser l'accès à des ressources pour un ensemble d'utilisateurs plutôt que pour chaque utilisateur individuellement. Chaque groupe est identifié par un **GID (Group ID)** unique.

        #### 1. Fichiers Clés pour les Groupes :
        -   `/etc/group` : Informations sur les groupes (nom, GID, liste des membres secondaires).
        -   `/etc/gshadow` : Mots de passe hachés pour les groupes et administrateurs de groupes (rarement utilisés, accessible uniquement par `root`).

        #### 2. Créer un Groupe : `groupadd`
        Permet d'ajouter un nouveau groupe.

        **Syntaxe :** `sudo groupadd [options] nom_groupe`

        **Options courantes :**
        -   `-g GID` : Spécifie un **GID** personnalisé pour le nouveau groupe.
        -   `-r` : Crée un **groupe système** (avec un GID bas, généralement 0-999).

        **Exemple :**
        `sudo groupadd sales`
        *Crée un groupe nommé 'sales'.*

        #### 3. Modifier un Groupe : `groupmod`
        Permet de modifier les attributs d'un groupe existant.

        **Syntaxe :** `sudo groupmod [options] nom_groupe`

        **Options courantes :**
        -   `-n nouveau_nom` : Change le **nom** du groupe.
        -   `-g nouveau_GID` : Change le **GID** du groupe.

        **Exemple :**
        `sudo groupmod -n support_team helpdesk`
        *Renomme le groupe 'support_team' en 'helpdesk'.*

        #### 4. Supprimer un Groupe : `groupdel`
        Supprime un groupe. Un groupe ne peut pas être supprimé s'il est le groupe principal d'un utilisateur existant.

        **Syntaxe :** `sudo groupdel nom_groupe`

        **Exemple :**
        `sudo groupdel old_project`
        *Supprime le groupe 'old_project'.*

        #### 5. Gérer les Membres d'un Groupe : `gpasswd`
        `gpasswd` est un outil flexible pour ajouter ou supprimer des membres d'un groupe, ou définir un administrateur de groupe.

        **Syntaxe :** `sudo gpasswd [options] groupe`

        **Options courantes :**
        -   `-a utilisateur` : **Ajoute** un utilisateur au groupe.
        -   `-d utilisateur` : **Supprime** un utilisateur du groupe.
        -   `-A utilisateur1,utilisateur2` : Définit les **administrateurs** du groupe (ces utilisateurs peuvent ajouter/supprimer des membres du groupe).
        -   `-M utilisateur1,utilisateur2` : Définit les **membres** du groupe (remplace les membres existants).

        **Exemples :**
        `sudo gpasswd -a sara sales`
        *Ajoute 'sara' au groupe 'sales'.*
        `sudo gpasswd -d john sales`
        *Supprime 'john' du groupe 'sales'.*
        `sudo gpasswd -M alice,bob dev`
        *Définit 'alice' et 'bob' comme les seuls membres du groupe 'dev'.*

        #### 6. Lister les Groupes et leurs Membres : `getent group` ou `grep`
        Pour afficher tous les membres d'un groupe, vous pouvez inspecter `/etc/group` ou utiliser `getent`.

        **Exemple :**
        `getent group sales`
        `sales:x:1003:sara,claire`

        `grep ^dev /etc/group`
        `dev:x:1002:alice,bob`
        """
        add_scrollable_text_to_content_frame("3. Gestion des Groupes", groups_text)

        # --- Tab 4: Permissions de Fichiers et Répertoires ---
        permissions_text = """
        ### Permissions de Fichiers et Répertoires

        Les permissions Linux sont au cœur du modèle de sécurité et déterminent qui peut lire, écrire ou exécuter un fichier ou un répertoire. Elles sont divisées en trois catégories d'utilisateurs et trois types de permissions.

        #### 1. Catégories d'Utilisateurs :
        -   **U**ser (Propriétaire) : Les permissions pour le propriétaire du fichier.
        -   **G**roup (Groupe) : Les permissions pour les membres du groupe propriétaire du fichier.
        -   **O**thers (Autres) : Les permissions pour tous les autres utilisateurs du système.

        #### 2. Types de Permissions :
        -   **r** (read - lecture) :
            -   **Fichier :** Peut lire le contenu du fichier.
            -   **Répertoire :** Peut lister le contenu du répertoire.
        -   **w** (write - écriture) :
            -   **Fichier :** Peut modifier ou supprimer le fichier.
            -   **Répertoire :** Peut créer, supprimer ou renommer des fichiers *dans* le répertoire (même si le fichier appartient à un autre utilisateur).
        -   **x** (execute - exécution) :
            -   **Fichier :** Peut exécuter le fichier (s'il s'agit d'un script ou d'un programme binaire).
            -   **Répertoire :** Peut "entrer" ou traverser le répertoire (nécessaire pour accéder aux fichiers à l'intérieur).

        #### 3. Affichage des Permissions (`ls -l`) :
        Les permissions sont affichées dans un format de 10 caractères au début de la sortie de `ls -l`.

        `drwxr-xr--`
        -   **1er caractère :** Type de fichier (`-` pour fichier régulier, `d` pour répertoire, `l` pour lien symbolique, `b` pour périphérique bloc, `c` pour périphérique caractère, `p` pour pipe nommé, `s` pour socket).
        -   **Caractères 2-4 :** Permissions du **propriétaire** (User). (rwx)
        -   **Caractères 5-7 :** Permissions du **groupe** (Group). (r-x)
        -   **Caractères 8-10 :** Permissions des **autres** (Others). (r--)

        **Exemple :** `drwxr-xr-- 2 john dev 4096 Jul 20 10:30 project_docs`
        -   `d` : C'est un répertoire.
        -   `rwx` (propriétaire John) : John peut lire, écrire et exécuter (entrer) dans le répertoire.
        -   `r-x` (groupe dev) : Les membres du groupe 'dev' peuvent lire et exécuter (entrer) dans le répertoire, mais pas modifier son contenu.
        -   `r--` (autres) : Tous les autres utilisateurs peuvent lire le contenu du répertoire, mais pas y entrer, ni le modifier.

        #### 4. Modifier les Permissions : `chmod`
        `chmod` (change mode) permet de modifier les permissions d'un fichier ou d'un répertoire.

        **Méthodes :**

        **a) Symbolique (UGO) :**
        -   `u` (user), `g` (group), `o` (others), `a` (all).
        -   `+` (ajouter), `-` (retirer), `=` (définir exactement).
        -   `r`, `w`, `x`.

        **Exemples :**
        -   `chmod u+x script.sh` : Ajoute la permission d'exécution pour le propriétaire.
        -   `chmod g-w data.txt` : Retire la permission d'écriture pour le groupe.
        -   `chmod o=r index.html` : Définit la permission de lecture (seulement) pour les autres.
        -   `chmod ug+rw,o-rwx file.txt` : Ajoute lecture/écriture pour user/group, retire tout pour les autres.
        -   `chmod a+rwx myfile` : Rend le fichier lisible, modifiable, exécutable par tout le monde (DANGEREUX !).

        **b) Numérique (Octal) :**
        Chaque permission a une valeur numérique : `r=4`, `w=2`, `x=1`. La somme des valeurs donne le nombre pour chaque catégorie.
        -   `rwx = 4+2+1 = 7`
        -   `rw- = 4+2+0 = 6`
        -   `r-x = 4+0+1 = 5`
        -   `--- = 0+0+0 = 0`

        Les permissions sont spécifiées par un nombre à trois chiffres : `user_perm group_perm other_perm`.

        **Exemples :**
        -   `chmod 755 mon_script.sh` : `rwxr-xr-x` (propriétaire: tout, groupe: lecture+exécution, autres: lecture+exécution). C'est la permission standard pour un script exécutable.
        -   `chmod 644 mon_fichier.txt` : `rw-r--r--` (propriétaire: lecture+écriture, groupe: lecture seule, autres: lecture seule). C'est la permission standard pour un fichier texte.
        -   `chmod 777 mon_dossier/` : `rwxrwxrwx` (tout le monde peut tout faire). **À éviter absolument pour des raisons de sécurité !**

        #### 5. Modifier le Propriétaire et le Groupe Propriétaire : `chown` et `chgrp`

        -   **`chown` (change owner) :** Modifie le propriétaire (utilisateur) et/ou le groupe propriétaire d'un fichier/répertoire.
            -   `sudo chown nouvel_utilisateur fichier`
            -   `sudo chown :nouveau_groupe fichier` (change seulement le groupe)
            -   `sudo chown nouvel_utilisateur:nouveau_groupe fichier` (change user et group)
            -   `sudo chown -R user:group repertoire/` (récursif)

        -   **`chgrp` (change group) :** Modifie uniquement le groupe propriétaire d'un fichier/répertoire.
            -   `sudo chgrp nouveau_groupe fichier`
            -   `sudo chgrp -R nouveau_groupe repertoire/` (récursif)

        Ces commandes sont fondamentales pour la mise en place d'un système de fichiers sécurisé et organisé.
        """
        add_scrollable_text_to_content_frame("4. Permissions de Fichiers et Répertoires", permissions_text)

        # --- Tab 5: Permissions Spéciales (SUID, SGID, Sticky) ---
        special_permissions_text = """
        ### Permissions Spéciales : SUID, SGID et Sticky Bit

        En plus des permissions classiques (rwx), Linux propose des permissions spéciales qui affectent le comportement des exécutables et des répertoires.

        #### 1. SUID (Set User ID) Bit :
        -   **Appliqué à :** Fichiers exécutables.
        -   **Effet :** Lorsqu'un fichier exécutable avec le bit SUID est exécuté, il s'exécute avec les permissions du **propriétaire du fichier**, et non de l'utilisateur qui l'exécute.
        -   **Indication :** Un `s` à la place du `x` pour la catégorie du propriétaire dans `ls -l`. (Ex: `rwsr-xr-x`)
        -   **Utilisation typique :** Permettre à des programmes non-root d'effectuer des tâches privilégiées (ex: `passwd` est SUID root pour pouvoir modifier `/etc/shadow`).
        -   **Risque de sécurité :** Un programme malveillant avec SUID pourrait être exploité pour obtenir des privilèges élevés. Il faut être très prudent avec les SUID.

        **Exemple :**
        `ls -l /usr/bin/passwd`
        `-rwsr-xr-x. 1 root root 27832 Jul 20  2025 /usr/bin/passwd`
        *Notez le `s` à la place du `x` pour le propriétaire `root`.*

        **Définir le SUID :**
        -   Symbolique : `chmod u+s fichier_exec`
        -   Numérique : Préfixe `4` aux permissions octales (ex: `chmod 4755 fichier_exec`)

        #### 2. SGID (Set Group ID) Bit :
        -   **Appliqué à :**
            -   **Fichiers exécutables :** S'exécute avec les permissions du **groupe propriétaire du fichier**, et non du groupe de l'utilisateur. Indiqué par un `s` à la place du `x` pour la catégorie du groupe. (Ex: `rwxr-sr-x`)
            -   **Répertoires :** Tout nouveau fichier ou sous-répertoire créé dans ce répertoire héritera du **groupe propriétaire du répertoire parent**, et non du groupe principal de l'utilisateur qui crée le fichier. Très utile pour les répertoires partagés.
                Indiqué par un `s` à la place du `x` pour la catégorie du groupe. (Ex: `drwxrwsr-x`)

        **Exemple SGID sur répertoire :**
        `drwxrwsr-x. 2 root project_dev 4096 Jul 20 10:30 shared_proj`
        *Tous les fichiers créés dans `shared_proj` appartiendront automatiquement au groupe `project_dev`.*

        **Définir le SGID :**
        -   Symbolique : `chmod g+s fichier_ou_repertoire`
        -   Numérique : Préfixe `2` aux permissions octales (ex: `chmod 2775 repertoire/`)

        #### 3. Sticky Bit :
        -   **Appliqué à :** Répertoires uniquement.
        -   **Effet :** Les utilisateurs peuvent créer des fichiers et des sous-répertoires dans le répertoire, mais ne peuvent **supprimer ou renommer** que leurs propres fichiers/sous-répertoires. Les fichiers d'autres utilisateurs sont protégés.
        -   **Indication :** Un `t` à la place du `x` pour la catégorie des autres dans `ls -l`. (Ex: `drwxrwxrwt`)
        -   **Utilisation typique :** Répertoires de partage public comme `/tmp` et `/var/tmp`.

        **Exemple :**
        `ls -ld /tmp`
        `drwxrwxrwt. 12 root root 4096 Jul 20 10:30 /tmp`
        *Notez le `t` à la place du `x` pour les 'autres'.*

        **Définir le Sticky Bit :**
        -   Symbolique : `chmod o+t repertoire`
        -   Numérique : Préfixe `1` aux permissions octales (ex: `chmod 1777 repertoire_public/`)

        #### Résumé des Préfixes Numériques :
        -   `4` : SUID
        -   `2` : SGID
        -   `1` : Sticky Bit

        Ces valeurs sont ajoutées au premier chiffre des permissions octales.
        Ex: `chmod 777` (rwxrwxrwx) + Sticky Bit = `chmod 1777` (rwxrwxrwt)
        Ex: `chmod 755` (rwxr-xr-x) + SUID = `chmod 4755` (rwsr-xr-x)
        Ex: `chmod 770` (rwxrwx---) + SGID = `chmod 2770` (rwxrws---)
        """
        add_scrollable_text_to_content_frame("5. Permissions Spéciales (SUID, SGID, Sticky)", special_permissions_text)

        # --- Tab 6: ACLs (Listes de Contrôle d'Accès) ---
        acls_text = """
        ### ACLs (Listes de Contrôle d'Accès)

        Les permissions traditionnelles de Linux (propriétaire, groupe, autres) peuvent être limitantes si vous avez besoin d'un contrôle d'accès plus granulaire. Les **ACLs (Access Control Lists)** permettent de définir des permissions pour des utilisateurs ou des groupes spécifiques qui ne sont ni le propriétaire, ni le groupe propriétaire.

        #### 1. Pourquoi les ACLs ?
        -   **Granularité :** Permet d'accorder des permissions à des utilisateurs ou groupes individuels en plus des trois catégories standard.
        -   **Flexibilité :** Permet de gérer des scénarios d'accès complexes qui ne seraient pas possibles avec les permissions Unix classiques.

        #### 2. Prérequis :
        -   Le système de fichiers doit supporter les ACLs (la plupart des systèmes de fichiers modernes comme ext2/3/4, XFS, Btrfs le font).
        -   Les paquets `acl` (qui incluent `getfacl` et `setfacl`) doivent être installés.
            `sudo dnf install acl` ou `sudo apt install acl`

        #### 3. Afficher les ACLs : `getfacl`
        Permet de voir les ACLs définies pour un fichier ou un répertoire.
        Si une ACL est définie, `ls -l` affichera un `+` à la fin des permissions standard.

        **Exemple :**
        `ls -l mon_fichier.txt`
        `-rw-rw-r--+ 1 user1 dev_team 0 Jul 20 10:00 mon_fichier.txt`
        *Le `+` indique qu'une ACL est définie.*

        `getfacl mon_fichier.txt`
        ```
        # file: mon_fichier.txt
        # owner: user1
        # group: dev_team
        user::rw-
        user:user2:r--   # ACL: user2 a la permission de lecture
        group::rw-
        mask::rw-
        other::r--
        ```
        *Ici, `user2` a des permissions de lecture, même s'il n'est ni le propriétaire ni dans le groupe `dev_team`.*

        #### 4. Définir les ACLs : `setfacl`

        `setfacl` permet de modifier les ACLs.

        **Options courantes :**
        -   `-m` (modify) : Modifie les ACLs existantes ou en ajoute de nouvelles.
        -   `-x` (remove) : Supprime des ACLs spécifiques.
        -   `-b` (remove all) : Supprime toutes les ACLs (revient aux permissions standard).
        -   `-R` (recursive) : Applique récursivement aux sous-répertoires et fichiers.
        -   `-d` (default) : Définit les ACLs par défaut pour un répertoire (les nouveaux fichiers/dossiers héritent de ces ACLs).

        **Syntaxe de base :** `sudo setfacl -m u:utilisateur:perms fichier_ou_repertoire`
        `sudo setfacl -m g:groupe:perms fichier_ou_repertoire`

        **Exemples :**
        -   **Donner à `user3` la lecture/écriture sur `mon_fichier.txt` :**
            `sudo setfacl -m u:user3:rw mon_fichier.txt`

        -   **Donner au groupe `qa` la lecture seule sur `data_dir/` :**
            `sudo setfacl -m g:qa:r-x data_dir/`

        -   **Définir des ACLs par défaut pour un répertoire (les nouveaux fichiers hériteront) :**
            `sudo setfacl -m d:u:user4:rwx project_folder/`
            `sudo setfacl -m d:g:dev_group:r-x project_folder/`

        -   **Supprimer une ACL spécifique :**
            `sudo setfacl -x u:user3 mon_fichier.txt`

        -   **Supprimer toutes les ACLs :**
            `sudo setfacl -b mon_fichier.txt`

        #### 5. Le Champ `mask` :
        -   Le `mask` est une permission maximale pour toutes les entrées ACL autres que le propriétaire et les autres.
        -   Les permissions effectives d'une ACL sont le résultat d'un `AND` logique entre les permissions de l'ACL et le `mask`.
        -   Lorsque vous ajoutez une ACL, `setfacl` met à jour automatiquement le `mask` à moins que vous ne le spécifiiez explicitement.
        -   **Exemple :** Si une ACL donne `rwx` mais que le `mask` est `r-x`, l'accès effectif sera `r-x`.
        -   Vous pouvez définir le `mask` manuellement : `sudo setfacl -m m::rw- mon_fichier.txt`

        Les ACLs sont un outil puissant pour les administrateurs qui nécessitent une flexibilité d'autorisation au-delà du modèle Unix traditionnel.
        """
        add_scrollable_text_to_content_frame("6. ACLs (Listes de Contrôle d'Accès)", acls_text)

        # --- Tab 7: Umask ---
        umask_text = """
        ### Umask

        Le **umask** est un paramètre important qui détermine les permissions par défaut des nouveaux fichiers et répertoires créés sur un système Linux. Il ne définit pas les permissions qui *seront* accordées, mais plutôt celles qui *seront retirées* des permissions maximales par défaut.

        #### 1. Comment Ça Marche :
        -   Les permissions maximales par défaut sont :
            -   **Fichiers :** `666` (rw-rw-rw-) - Lecture et écriture pour tout le monde.
            -   **Répertoires :** `777` (rwxrwxrwx) - Lecture, écriture et exécution pour tout le monde.
        -   Le umask est une valeur octale à 3 ou 4 chiffres. Chaque chiffre représente les permissions à **masquer** (retirer) pour le propriétaire, le groupe, et les autres.
        -   La permission finale est obtenue en soustrayant le umask des permissions maximales.

        **Formule :** `Permissions_Finales = Permissions_Maximales_Par_Défaut - Umask`

        **Exemple : Umask `022`**
        -   **Pour un fichier :**
            `666 (rw-rw-rw-) - 022 = 644 (rw-r--r--)`
            *Le propriétaire a lecture/écriture, le groupe et les autres ont lecture seule.*
        -   **Pour un répertoire :**
            `777 (rwxrwxrwx) - 022 = 755 (rwxr-xr-x)`
            *Le propriétaire a tout, le groupe et les autres ont lecture/exécution.*

        **Exemple : Umask `002`** (commun dans les environnements multi-utilisateurs où le groupe doit avoir l'écriture)
        -   **Pour un fichier :**
            `666 - 002 = 664 (rw-rw-r--)`
            *Le propriétaire et le groupe ont lecture/écriture, les autres ont lecture seule.*
        -   **Pour un répertoire :**
            `777 - 002 = 775 (rwxrwxr-x)`
            *Le propriétaire et le groupe ont tout, les autres ont lecture/exécution.*

        #### 2. Afficher l'Umask : `umask`
        Pour voir le umask actuel de votre session shell :
        `umask`
        *Sortie typique : `0022` (le premier '0' indique l'absence de permissions spéciales pour le umask).*

        #### 3. Définir l'Umask : `umask`
        Vous pouvez définir le umask temporairement pour votre session shell :
        `umask 007` (pour restreindre l'accès aux autres)

        #### 4. Umask Persistant :
        Pour que le umask soit défini à chaque connexion, il est généralement configuré dans :
        -   `/etc/profile` (pour tous les utilisateurs)
        -   `/etc/bashrc` ou `/etc/zshrc` (pour tous les utilisateurs utilisant ces shells)
        -   `~/.bashrc`, `~/.profile`, `~/.zshrc` (pour un utilisateur spécifique)

        De nombreux systèmes utilisent un umask par défaut de `0022` (pour les utilisateurs normaux) ou `0002` (pour les utilisateurs qui doivent partager des fichiers dans un environnement de groupe), ou `0027` (pour des restrictions plus strictes, où les autres n'ont aucune permission et le groupe a des restrictions).

        #### 5. Importance du Umask :
        Le umask est une mesure de sécurité préventive. En le configurant correctement, vous vous assurez que les nouveaux fichiers ne sont pas accidentellement créés avec des permissions trop permissives, réduisant ainsi les risques d'exposition de données.
        """
        add_scrollable_text_to_content_frame("7. Umask", umask_text)

        # --- Tab 8: Propriété des Fichiers ---
        ownership_text = """
        ### Propriété des Fichiers et Répertoires

        Chaque fichier et répertoire sur un système Linux possède un **propriétaire (utilisateur)** et un **groupe propriétaire**. Ces attributs sont essentiels pour le modèle de permissions Unix.

        #### 1. Afficher la Propriété : `ls -l`
        La commande `ls -l` affiche le propriétaire et le groupe propriétaire juste après les permissions et le nombre de liens.

        **Exemple :**
        `ls -l /etc/passwd`
        `-rw-r--r--. 1 root root 2341 Oct 26  2024 /etc/passwd`
        *Ici, le propriétaire est `root` et le groupe propriétaire est `root`.*

        `ls -l /home/john/data.txt`
        `-rw-r--r--. 1 john users 1234 Jul 20 10:00 /home/john/data.txt`
        *Le propriétaire est `john` et le groupe propriétaire est `users`.*

        #### 2. Changer le Propriétaire : `chown` (Change Owner)
        La commande `chown` est utilisée pour modifier l'utilisateur propriétaire et/ou le groupe propriétaire d'un fichier ou d'un répertoire. Seul l'utilisateur `root` (ou un utilisateur avec `sudo` privileges) peut changer le propriétaire d'un fichier.

        **Syntaxe de base :**
        `sudo chown [options] NOUVEL_UTILISATEUR[:NOUVEAU_GROUPE] FICHIER_OU_REPERTOIRE`

        **Exemples :**
        -   **Changer l'utilisateur propriétaire :**
            `sudo chown bob /home/alice/rapport.txt`
            *Le fichier `rapport.txt` appartient maintenant à `bob`.*

        -   **Changer le groupe propriétaire (sans changer l'utilisateur) :**
            `sudo chown :developers /var/www/html/index.html`
            *Le groupe propriétaire de `index.html` est maintenant `developers`.*

        -   **Changer l'utilisateur et le groupe propriétaire :**
            `sudo chown alice:web_users /var/www/html/images/`
            *Le répertoire `images/` appartient maintenant à `alice` et au groupe `web_users`.*

        -   **Changer récursivement (pour les répertoires) :**
            `sudo chown -R user:group /chemin/vers/dossier/`
            *Modifie récursivement la propriété de tous les fichiers et sous-répertoires.*

        #### 3. Changer le Groupe Propriétaire : `chgrp` (Change Group)
        La commande `chgrp` est une version simplifiée de `chown` qui ne permet de modifier que le groupe propriétaire d'un fichier ou d'un répertoire. Elle est moins couramment utilisée que `chown` car `chown` peut faire les deux.

        **Syntaxe de base :**
        `sudo chgrp [options] NOUVEAU_GROUPE FICHIER_OU_REPERTOIRE`

        **Exemples :**
        -   `sudo chgrp admin /etc/myapp/config.conf`
            *Le groupe propriétaire de `config.conf` est maintenant `admin`.*

        -   `sudo chgrp -R project_team /srv/data/projectX/`
            *Modifie récursivement le groupe propriétaire de tous les éléments dans `projectX/`.*

        #### 4. Importance de la Propriété :
        -   La propriété est le premier niveau de contrôle d'accès dans le modèle de permissions Unix. Le propriétaire a généralement le contrôle le plus étendu sur le fichier.
        -   La bonne définition de la propriété est cruciale pour la sécurité, car elle détermine qui peut modifier les permissions du fichier, son contenu, ou le supprimer.
        -   Dans les environnements multi-utilisateurs, il est courant que les fichiers créés par un utilisateur appartiennent à cet utilisateur, mais soient dans un groupe qui facilite la collaboration avec d'autres.
        """
        add_scrollable_text_to_content_frame("8. Propriété des Fichiers", ownership_text)

        # --- Tab 9: Bonnes Pratiques ---
        best_practices_text = """
        ### Bonnes Pratiques pour la Gestion des Utilisateurs, Groupes et Permissions

        Une gestion rigoureuse des utilisateurs, des groupes et des permissions est fondamentale pour la sécurité et la stabilité d'un système Linux.

        1.  **Principe du Moindre Privilège :**
            -   Accordez toujours le minimum de permissions nécessaires pour qu'un utilisateur ou un service puisse fonctionner. N'accordez pas `root` ou des permissions `rwx` (777) à moins que ce ne soit absolument indispensable et justifié.
            -   Pour les services, créez des utilisateurs dédiés non-interactifs (`-s /sbin/nologin`).

        2.  **Utilisez les Groupes Intelligemment :**
            -   Organisez les utilisateurs en groupes logiques (ex: `dev`, `ops`, `sales`, `webusers`).
            -   Accorder des permissions aux groupes plutôt qu'aux utilisateurs individuels simplifie grandement la gestion, surtout dans les grands environnements.
            -   La plupart des fichiers créés par un utilisateur devraient appartenir à son groupe principal ou à un groupe de travail partagé.

        3.  **Permissions de Répertoires vs. Fichiers :**
            -   Pour les répertoires : `rwx` (7) signifie traverser, lister, modifier. `r-x` (5) signifie traverser et lister mais pas modifier.
            -   Pour les fichiers : `r` (4) lecture, `w` (2) écriture, `x` (1) exécution.
            -   Un répertoire doit souvent avoir la permission `x` pour être traversable.

        4.  **Umask Approprié :**
            -   Configurez un umask par défaut restrictif (ex: `0022` ou `0027`) pour garantir que les nouveaux fichiers et répertoires ne sont pas créés avec des permissions trop larges.

        5.  **Utilisez les Permissions Spéciales avec Prudence :**
            -   **SUID :** À utiliser avec une extrême précaution. Ne donnez le SUID qu'aux exécutables dont vous comprenez parfaitement le fonctionnement et l'impact sur la sécurité.
            -   **SGID sur répertoires :** Très utile pour les répertoires de collaboration où tous les fichiers doivent appartenir au même groupe.
            -   **Sticky Bit :** Indispensable pour les répertoires partagés où les utilisateurs peuvent créer des fichiers mais ne doivent pas les supprimer (ex: `/tmp`).

        6.  **ACLs pour la Granularité :**
            -   Si les permissions traditionnelles ne suffisent pas, utilisez les ACLs pour des contrôles d'accès plus précis à des utilisateurs ou groupes spécifiques.
            -   Soyez attentif au `mask` lors de l'utilisation des ACLs.

        7.  **Audit Régulier :**
            -   Vérifiez régulièrement les utilisateurs, les groupes et les permissions critiques (ex: permissions sur `/etc`, `/var`, `/usr/local/bin`).
            -   Recherchez les fichiers SUID/SGID inhabituels sur votre système (`find / -perm /4000 -o -perm /2000 -ls 2>/dev/null`).
            -   Utilisez `pwck` et `grpck` pour vérifier l'intégrité des fichiers de configuration.

        8.  **Automatisation :**
            -   Pour les environnements à grande échelle, utilisez des outils de gestion de configuration (Ansible, Puppet, Chef) pour garantir la cohérence des utilisateurs, groupes et permissions sur plusieurs machines.

        9.  **Gestion des Mots de Passe :**
            -   Associez toujours des politiques de mots de passe robustes (longueur, complexité, expiration) à la gestion des utilisateurs. (Voir notre guide sur la gestion des mots de passe).

        10. **Documentation :**
            -   Documentez toutes les configurations d'utilisateurs, de groupes et de permissions non standards, en particulier pour les applications ou services spécifiques.
        """
        add_scrollable_text_to_content_frame("9. Bonnes Pratiques", best_practices_text)

if __name__ == "__main__":
    app = UserGroupPermissionsApp()
    app.mainloop()