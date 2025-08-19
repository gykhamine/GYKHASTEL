import customtkinter as ctk

class VisudoConfigApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Configuration de visudo")
        self.geometry("1100x750") # Increased width and height for better layout

        # Configure grid layout for the main window (1 row, 2 columns)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Vertical Navigation Frame (Navbar) ---
        self.navigation_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1) # Allows content to push to top

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame,
                                                    text="visudo Guide",
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

        # --- Navigation Buttons (instead of CTkTabview for vertical) ---
        self.create_navigation_buttons()

        # Set initial content
        self.select_frame_by_name("1. Introduction")

    def create_navigation_buttons(self):
        # Create buttons for each section
        button_info = [
            ("1. Introduction", 1),
            ("2. Format de Base", 2),
            ("3. Alias Utilisateurs/Groupes", 3),
            ("4. Alias Hôtes", 4),
            ("5. Alias Commandes", 5),
            ("6. NOPASSWD & Options", 6),
            ("7. Permissions & Refus", 7),
            ("8. Commandes Groupées/Options", 8), # New tab
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
            setattr(self, f"nav_button_{row}", button) # Store button reference

        self.create_tab_content() # Create all content initially

    def select_frame_by_name(self, name):
        # Update button colors
        buttons = [getattr(self, f"nav_button_{i}") for i in range(1, 10)] # Adjust range if more tabs
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
                widget.grid_forget() # Hide other frames

    def create_tab_content(self):
        # Helper function to add scrollable text content
        def add_scrollable_text_to_content_frame(name, text_content):
            frame = ctk.CTkFrame(self.content_frame, corner_radius=0)
            text_widget = ctk.CTkTextbox(frame, wrap="word", width=800, height=600) # Adjust width/height
            text_widget.insert("0.0", text_content)
            text_widget.configure(state="disabled") # Make it read-only
            text_widget.pack(padx=10, pady=10, fill="both", expand=True)
            self.tab_content_widgets[name] = frame # Store the frame

        # --- Tab 1: Introduction ---
        intro_text = """
        Bienvenue dans l'application de configuration de **visudo**.

        ### Qu'est-ce que 'visudo' ?
        **visudo** est un outil essentiel utilisé pour modifier le fichier `/etc/sudoers`. Il est le SEUL moyen sûr de modifier ce fichier. Il garantit la sécurité et l'intégrité du fichier en :
        - Le verrouillant pour éviter les modifications simultanées.
        - Effectuant des vérifications de syntaxe pour prévenir les erreurs critiques.
        - Le déverrouillant une fois les modifications enregistrées avec succès.

        ### Pourquoi est-ce important ?
        Le fichier `/etc/sudoers` contrôle qui peut exécuter des commandes avec les privilèges d'un autre utilisateur (généralement **root**) et quelles commandes peuvent être exécutées. Une configuration incorrecte peut entraîner des **failles de sécurité majeures** ou rendre votre système **inutilisable** (par exemple, vous empêcher de vous connecter ou d'exécuter des commandes administratives).

        ### Comment l'utiliser ?
        Pour modifier le fichier `sudoers`, ouvrez un terminal et tapez :
        `sudo visudo`

        Par défaut, `visudo` ouvrira le fichier avec l'éditeur de texte configuré dans votre environnement (souvent `vi` ou `nano`). Une fois vos modifications faites, enregistrez et quittez. `visudo` vérifiera la syntaxe avant d'appliquer les changements.
        """
        add_scrollable_text_to_content_frame("1. Introduction", intro_text)

        # --- Tab 2: Format de Base ---
        format_text = """
        Le format de base d'une entrée dans le fichier `sudoers` est le suivant :

        `User_Name Host_Name = (Runas_User:Runas_Group) Command`

        ### Explication des Composants :

        1.  **User_Name**:
            - L'utilisateur ou le groupe (préfixé par '%') qui est autorisé à exécuter la commande.
            - Ex: `john` (utilisateur unique)
            - Ex: `%admin` (membres du groupe 'admin')

        2.  **Host_Name**:
            - Le nom d'hôte ou l'adresse IP sur lequel la commande peut être exécutée.
            - `ALL` est couramment utilisé pour n'importe quel hôte.
            - Ex: `server1.example.com`
            - Ex: `192.168.1.10`
            - Ex: `ALL`

        3.  **(Runas_User:Runas_Group)**: (Optionnel, entre parenthèses)
            - Spécifie sous quel utilisateur et/ou groupe la commande sera exécutée.
            - Si omis, `root` est la valeur par défaut pour l'utilisateur. Le groupe par défaut est généralement le groupe principal de `root` (`root` ou `wheel`).
            - `(ALL)`: Permet d'exécuter la commande en tant que n'importe quel utilisateur.
            - `(ALL:ALL)`: Permet d'exécuter la commande en tant que n'importe quel utilisateur et n'importe quel groupe.
            - Ex: `(root)` (exécuter en tant que root)
            - Ex: `(john:developers)` (exécuter en tant que l'utilisateur john et le groupe developers)

        4.  **Command**:
            - Le chemin complet de la commande à exécuter.
            - `ALL` autorise toutes les commandes (à utiliser avec extrême prudence).
            - Il est fortement recommandé d'utiliser des **chemins absolus** pour les commandes (ex: `/usr/bin/apt` au lieu de `apt`) pour éviter les vulnérabilités de "PATH hijacking".

        ### Exemples Concrets :

        -   **Permettre à l'utilisateur 'john' d'exécuter toutes les commandes en tant que root, sur tous les hôtes :**
            `john ALL=(ALL) ALL`

        -   **Permettre aux membres du groupe 'admin' d'exécuter 'apt update' et 'apt upgrade' en tant que root, sans mot de passe :**
            `%admin ALL=(ALL) NOPASSWD: /usr/bin/apt update, /usr/bin/apt upgrade`

        -   **Permettre à 'jane' d'exécuter `/bin/bash` en tant qu'utilisateur 'appuser' sur 'webserver1' :**
            `jane webserver1=(appuser) /bin/bash`
        """
        add_scrollable_text_to_content_frame("2. Format de Base", format_text)

        # --- Tab 3: Alias Utilisateurs/Groupes ---
        user_alias_text = """
        Les **alias** sont des groupes nommés qui permettent de simplifier la gestion des permissions pour plusieurs utilisateurs, groupes, hôtes ou commandes. Ils améliorent la lisibilité et la maintenabilité de votre fichier `sudoers`.

        ### User_Alias (Alias Utilisateurs)
        Permettent de définir un groupe d'utilisateurs ou de groupes d'utilisateurs.

        **Syntaxe :**
        `User_Alias ALIAS_NOM = user1, user2, %group1, user3`

        -   `ALIAS_NOM`: Doit commencer par une lettre majuscule.
        -   `user1, user2, ...`: Liste des utilisateurs.
        -   `%group1, ...`: Liste des groupes (notez le préfixe `%`).

        **Exemple :**
        ```sudoers
        User_Alias DEVOPS = jane, john, mike
        User_Alias PROD_ADMINS = %sysadmins, david
        ```

        ### Utilisation dans les Règles Sudoers :
        Vous pouvez ensuite utiliser cet alias dans vos règles :

        ```sudoers
        DEVOPS ALL=(ALL) /usr/bin/git, /usr/bin/docker
        PROD_ADMINS ALL=(root) NOPASSWD: ALL
        ```
        Dans cet exemple :
        -   `jane`, `john`, et `mike` peuvent exécuter `/usr/bin/git` et `/usr/bin/docker` en tant que root sur tous les hôtes.
        -   Les membres du groupe `sysadmins` et l'utilisateur `david` peuvent exécuter n'importe quelle commande en tant que root sur tous les hôtes sans mot de passe.

        ### Avantages :
        -   **Simplicité :** Moins de répétitions de noms d'utilisateurs.
        -   **Maintenance :** Si un utilisateur change de rôle ou quitte l'entreprise, vous n'avez qu'à modifier l'alias au lieu de chaque règle individuelle.
        -   **Clarté :** Rend le fichier `sudoers` plus facile à lire et à comprendre.
        """
        add_scrollable_text_to_content_frame("3. Alias Utilisateurs/Groupes", user_alias_text)

        # --- Tab 4: Alias Hôtes ---
        host_alias_text = """
        Les **Host_Alias** sont particulièrement utiles dans des environnements avec de multiples machines où les configurations `sudoers` pourraient être centralisées ou partagées.

        ### Syntaxe :
        `Host_Alias ALIAS_NOM = host1, host2, 192.168.1.0/24, host_alias_existant`

        -   `ALIAS_NOM`: Doit commencer par une lettre majuscule.
        -   `host1, host2, ...`: Peuvent être des noms d'hôtes (FQDN), des adresses IP, ou des blocs CIDR pour des sous-réseaux.
        -   Vous pouvez aussi inclure d'autres alias d'hôtes existants.

        ### Exemples :
        ```sudoers
        Host_Alias WEB_SERVERS = webserver1.example.com, webserver2, 10.0.0.10
        Host_Alias DEV_MACHINES = devpc1, devpc2, 192.168.1.0/24
        ```

        ### Utilisation dans les Règles Sudoers :

        ```sudoers
        john WEB_SERVERS=(ALL) /usr/sbin/apachectl graceful
        jane DEV_MACHINES=(root) /usr/bin/gdb
        ```
        Dans cet exemple :
        -   `john` peut redémarrer Apache gracieusement sur `webserver1.example.com`, `webserver2`, et `10.0.0.10`.
        -   `jane` peut utiliser le débogueur `gdb` en tant que root sur `devpc1`, `devpc2`, et toutes les machines du sous-réseau `192.168.1.0/24`.

        ### Avantages :
        -   **Centralisation :** Définissez un ensemble d'hôtes une fois et réutilisez-le.
        -   **Flexibilité :** Facilite la gestion des permissions sur des groupes de serveurs logiques.
        -   **Sécurité :** Réduit le risque d'erreurs en définissant des ensembles clairs d'hôtes.
        """
        add_scrollable_text_to_content_frame("4. Alias Hôtes", host_alias_text)

        # --- Tab 5: Alias Commandes ---
        command_alias_text = """
        Les **Cmnd_Alias** permettent de regrouper des commandes spécifiques, y compris la possibilité d'exclure certaines commandes.

        ### Syntaxe :
        `Cmnd_Alias ALIAS_NOM = /path/to/command1, /path/to/command2, !/path/to/forbidden_command`

        -   `ALIAS_NOM`: Doit commencer par une lettre majuscule.
        -   `!`: Le point d'exclamation permet d'**exclure** une commande spécifique d'un alias. C'est crucial pour la sécurité !
        -   Toujours utiliser les **chemins absolus** pour les commandes.

        ### Exemples :
        ```sudoers
        Cmnd_Alias NETWORKING = /usr/sbin/ifconfig, /usr/sbin/ip, /usr/bin/ping
        Cmnd_Alias WEB_CMDS = /usr/sbin/apachectl, /usr/sbin/nginx, /bin/systemctl reload apache2
        Cmnd_Alias APT_UPDATE = /usr/bin/apt update, /usr/bin/apt upgrade, /usr/bin/apt dist-upgrade
        Cmnd_Alias REBOOT_SHUTDOWN = /sbin/reboot, /sbin/shutdown
        Cmnd_Alias LOG_CMDS = /usr/bin/tail, /usr/bin/cat /var/log/*, !/usr/bin/cat /var/log/secure
        ```

        ### Utilisation dans les Règles Sudoers :

        ```sudoers
        sysadmin ALL=(ALL) NETWORKING, WEB_CMDS
        devuser ALL=(ALL) APT_UPDATE
        opsuser ALL=(root) REBOOT_SHUTDOWN
        logreader ALL=(ALL) LOG_CMDS
        ```
        Dans ces exemples :
        -   `sysadmin` peut exécuter les commandes définies dans `NETWORKING` et `WEB_CMDS`.
        -   `devuser` peut mettre à jour et mettre à niveau les paquets via `apt`.
        -   `opsuser` peut redémarrer ou arrêter le système en tant que root.
        -   `logreader` peut lire les fichiers de log avec `tail` ou `cat`, **SAUF** `/var/log/secure`. Cette exclusion est un bon exemple de sécurité granulaire.

        ### Avantages :
        -   **Granularité :** Contrôlez précisément quelles commandes sont autorisées.
        -   **Sécurité :** L'opérateur `!` est fondamental pour refuser des commandes spécifiques qui seraient autrement incluses dans un alias plus large.
        -   **Organisation :** Maintient une structure claire pour les commandes autorisées.
        """
        add_scrollable_text_to_content_frame("5. Alias Commandes", command_alias_text)

        # --- Tab 6: NOPASSWD et Options ---
        nopasswd_text = """
        ### L'option NOPASSWD:
        L'option `NOPASSWD:` permet à l'utilisateur d'exécuter la commande spécifiée **sans avoir à entrer son mot de passe**.

        **À utiliser avec une EXTRÊME PRUDENCE !** Cela peut créer des failles de sécurité majeures si mal configuré, car un utilisateur n'aura pas besoin d'une authentification supplémentaire pour les commandes spécifiées.

        **Exemple :**
        `sysadmin ALL=(ALL) NOPASSWD: /usr/bin/apt update, /usr/bin/apt upgrade`
        (Permet à `sysadmin` de mettre à jour et mettre à niveau les paquets sans mot de passe.)

        ### Autres Options Importantes :

        -   **PASSWD:** (Par défaut si aucune option n'est spécifiée) Demande le mot de passe de l'utilisateur qui exécute `sudo`.
            `%developers ALL=(ALL) PASSWD: /usr/bin/git push`
            (Les développeurs doivent entrer leur mot de passe pour pousser du code via git en tant que root.)

        -   **SETENV:** Permet à l'utilisateur de conserver certaines variables d'environnement spécifiées lors de l'exécution de la commande. `sudo` nettoie normalement l'environnement pour des raisons de sécurité.
            `john ALL=(ALL) SETENV: PATH,LD_LIBRARY_PATH /usr/local/bin/my_script.sh`
            (Conserve les variables PATH et LD_LIBRARY_PATH pour l'exécution du script.)

        -   **NOSETENV:** Supprime toutes les variables d'environnement de l'utilisateur appelant avant d'exécuter la commande. C'est souvent le comportement par défaut de `sudo` pour des raisons de sécurité.

        -   **ENV_RESET:** (Comportement par défaut) Réinitialise l'environnement et n'hérite que d'un ensemble limité de variables sûres.

        -   **!authenticate:** Similaire à `NOPASSWD`, mais spécifiquement pour des politiques de sécurité avancées. En général, `NOPASSWD` est plus couramment utilisé.

        ### Principe du Moindre Privilège :
        Toujours privilégier le **principe du moindre privilège**. N'accordez que le minimum de permissions nécessaires à un utilisateur pour accomplir sa tâche. Évitez `NOPASSWD` autant que possible et ne l'utilisez que pour des commandes très spécifiques et sans risque.
        """
        add_scrollable_text_to_content_frame("6. NOPASSWD & Options", nopasswd_text)

        # --- Tab 7: Permissions et Refus ---
        permissions_text = """
        Comprendre comment `sudoers` gère les autorisations et les refus est crucial pour une configuration sécurisée.

        ### Ordre d'Évaluation des Règles :
        Les règles dans le fichier `sudoers` sont traitées dans l'ordre où elles apparaissent. La **dernière règle correspondante l'emporte**. Cela signifie que si une commande est autorisée par une règle, mais refusée par une règle ultérieure pour le même utilisateur/groupe, la règle de refus prévaut.

        ### Refuser Spécifiquement une Commande :
        Pour refuser une commande, vous utilisez le préfixe `!` (point d'exclamation) devant la commande.

        **Exemple Simple de Refus :**
        Supposons que `devuser` puisse exécuter `ALL` les commandes sauf la commande `reboot`.

        ```sudoers
        devuser ALL=(ALL) ALL, !/sbin/reboot
        ```
        Ici, `devuser` peut exécuter toutes les commandes, mais `/sbin/reboot` sera explicitement refusé.

        ### Refus dans les Alias de Commandes :
        Ceci est très puissant pour créer des ensembles de commandes avec des exceptions.

        **Exemple avec Cmnd_Alias :**
        Vous voulez que le groupe `app_managers` puisse gérer les services (start, stop, status), mais ne puisse **jamais** utiliser `systemctl poweroff` ou `systemctl reboot`.

        ```sudoers
        Cmnd_Alias SERVICE_CMDS = /bin/systemctl start *, /bin/systemctl stop *, /bin/systemctl status *
        Cmnd_Alias FORBIDDEN_POWER = /bin/systemctl poweroff, /bin/systemctl reboot

        %app_managers ALL=(ALL) SERVICE_CMDS, !FORBIDDEN_POWER
        ```
        Dans cet exemple :
        -   Le groupe `app_managers` est autorisé à exécuter toutes les commandes de `SERVICE_CMDS`.
        -   Cependant, même si `systemctl` est une commande de service, les entrées `/bin/systemctl poweroff` et `/bin/systemctl reboot` sont explicitement **refusées** par `!FORBIDDEN_POWER`.

        ### Conséquences d'un Refus :
        Si un utilisateur tente d'exécuter une commande qui lui est refusée, `sudo` affichera un message similaire à :
        `Sorry, user [username] is not allowed to execute '[command]' as [user] on [hostname]. This incident will be reported.`
        Et l'action sera loggée (rapportée) aux administrateurs système.

        ### Importance de l'Ordre :
        Soyez toujours conscient de l'ordre des règles. Une règle plus générique qui autorise "tout" pourrait annuler un refus spécifique si le refus vient avant la règle générique.
        ```sudoers
        # MAUVAISE PRATIQUE - Le "ALL" l'emporte !
        john ALL=(ALL) !/sbin/shutdown
        john ALL=(ALL) ALL
        ```
        Dans ce cas, `john` pourra toujours exécuter `shutdown` car la deuxième règle `ALL` annule le refus précédent. L'ordre correct est celui montré dans les exemples ci-dessus, où le refus est sur la **même ligne** que l'autorisation ou après une règle plus générique mais avant une règle plus spécifique.
        """
        add_scrollable_text_to_content_frame("7. Permissions & Refus", permissions_text)

        # --- NEW Tab 8: Commandes Groupées/Options ---
        complex_cmds_text = """
        Gérer les commandes avec des arguments ou des options spécifiques dans `sudoers` nécessite une attention particulière.

        ### Utilisation des Wildcards (`*`)
        Le caractère `*` peut être utilisé comme un **joker** pour correspondre à n'importe quelle séquence de caractères. C'est très utile pour les commandes qui acceptent de nombreux arguments ou sous-commandes.

        **Exemple avec `apt` (systèmes Debian/Ubuntu) :**
        Vous voulez autoriser un utilisateur à exécuter `apt update`, `apt upgrade` et `apt install <paquet>`, mais pas `apt remove`.

        ```sudoers
        Cmnd_Alias APT_SAFE = /usr/bin/apt update, /usr/bin/apt upgrade, /usr/bin/apt install *
        Cmnd_Alias APT_UNSAFE = /usr/bin/apt remove *, /usr/bin/apt purge *

        %devops ALL=(ALL) APT_SAFE, !APT_UNSAFE
        ```
        Ici, `%devops` peut installer n'importe quel paquet, mais ne peut ni supprimer ni purger.

        ---

        ### Commandes comme `ls`, `cat`, `grep` avec Arguments :
        Pour les commandes utilitaires, vous pouvez les autoriser avec des arguments spécifiques, ou des wildcards.

        **Exemple avec `ls` :**
        Permettre à un utilisateur de lister le contenu de `/var/log` et de son sous-répertoire `nginx`, mais pas le contenu de `/root`.

        ```sudoers
        Cmnd_Alias LS_LOGS = /usr/bin/ls /var/log/*, /usr/bin/ls /var/log/nginx/*
        Cmnd_Alias LS_ROOT = /usr/bin/ls /root/*

        log_user ALL=(ALL) LS_LOGS, !LS_ROOT
        ```
        Notez l'importance des chemins absolus et des wildcards.

        ---

        ### Gestionnaire de Paquets (DNF, APT, YUM, Zypper) :
        Ces commandes sont souvent des cibles privilégiées pour des permissions granulaires.

        **Exemple avec `dnf` (systèmes RHEL/Fedora) :**
        Autoriser la mise à jour et l'installation, mais interdire la suppression.

        ```sudoers
        Cmnd_Alias DNF_SAFE = /usr/bin/dnf update *, /usr/bin/dnf install *
        Cmnd_Alias DNF_UNSAFE = /usr/bin/dnf remove *, /usr/bin/dnf erase *

        %sysadmins ALL=(root) NOPASSWD: DNF_SAFE, !DNF_UNSAFE
        ```

        ---

        ### Commandes `systemctl` :
        Contrôler les services système est une tâche courante.

        **Exemple avec `systemctl` :**
        Autoriser le redémarrage d'Apache et Nginx, mais rien d'autre.

        ```sudoers
        Cmnd_Alias WEB_SERVICE_RESTART = /usr/bin/systemctl restart apache2.service, /usr/bin/systemctl restart nginx.service

        web_admin ALL=(root) WEB_SERVICE_RESTART
        ```
        Vous pouvez utiliser des wildcards pour tous les services de redémarrage si nécessaire, mais soyez prudent.
        `Cmnd_Alias ALL_RESTARTS = /usr/bin/systemctl restart *`

        ---

        ### Flatpak :
        Gérer les applications Flatpak peut aussi nécessiter des permissions sudo.

        **Exemple avec `flatpak` :**
        Autoriser l'installation et la mise à jour des applications Flatpak.

        ```sudoers
        Cmnd_Alias FLATPAK_MANAGE = /usr/bin/flatpak install *, /usr/bin/flatpak update *

        desktop_user ALL=(ALL) FLATPAK_MANAGE
        ```

        ### Points Clés pour les Commandes Complexes :
        -   **Chemins Absolus :** Toujours utiliser le chemin complet de la commande (ex: `/usr/bin/ls`).
        -   **Wildcards (`*`) :** Utilisez-les pour correspondre à des arguments multiples, mais soyez vigilant à ne pas autoriser trop.
        -   **Exclusions (`!`) :** Essentielles pour créer des politiques précises en refusant des sous-commandes ou des arguments spécifiques.
        -   **Testez :** Après chaque modification, utilisez `sudo -l` en tant qu'utilisateur pour vérifier que les permissions sont celles attendues.
        """
        add_scrollable_text_to_content_frame("8. Commandes Groupées/Options", complex_cmds_text)

        # --- Tab 9: Bonnes Pratiques et Dépannage ---
        best_practices_text = """
        ### Bonnes Pratiques pour une Configuration Sûre et Efficace :

        1.  **Utilisez TOUJOURS `visudo` :** N'éditez JAMAIS le fichier `/etc/sudoers` directement avec un éditeur de texte (comme `vi /etc/sudoers`). `visudo` effectue des vérifications de syntaxe essentielles qui empêchent de bloquer votre système en cas d'erreur.
        2.  **Principe du Moindre Privilège :** N'accordez que les permissions absolument nécessaires à un utilisateur ou un groupe pour accomplir sa tâche. Moins de privilèges = moins de surface d'attaque.
        3.  **Utilisez des Alias :** `User_Alias`, `Host_Alias`, `Cmnd_Alias` améliorent considérablement la lisibilité, la maintenabilité et la sécurité de votre fichier `sudoers`.
        4.  **Préférez les Groupes aux Utilisateurs :** Gérez les permissions par groupe plutôt que par utilisateur individuel. C'est beaucoup plus facile à maintenir dans le temps.
        5.  **Chemins Absolus pour les Commandes :** Spécifiez toujours le chemin complet des commandes (ex: `/usr/bin/apt`). Cela évite les attaques par détournement de chemin (PATH hijacking) où un utilisateur malveillant pourrait placer un script avec le même nom dans un répertoire dans le PATH et le faire exécuter avec des privilèges élevés.
        6.  **Commentez votre Fichier :** Ajoutez des commentaires (avec `#`) pour expliquer vos configurations, surtout si elles sont complexes. Cela aide énormément les futurs administrateurs (ou vous-même dans 6 mois !).
        7.  **Sauvegardes :** Faites des sauvegardes du fichier `sudoers` avant des modifications majeures. Vous pouvez le copier (par exemple, `sudo cp /etc/sudoers /etc/sudoers.bak`) ou utiliser un système de gestion de configuration.
        8.  **Vérifiez avec `sudo -l` :** Après avoir effectué des modifications, testez-les en vous connectant en tant qu'utilisateur affecté et en exécutant `sudo -l`. Cela listera les commandes que cet utilisateur est autorisé à exécuter.

        ### Dépannage Courant :

        -   **Erreurs de syntaxe :** `visudo` vous alertera immédiatement si vous avez fait une erreur de syntaxe. Corrigez-les avant de quitter l'éditeur. Si vous quittez sans corriger, `visudo` vous demandera quoi faire (souvent 'e' pour éditer à nouveau).
        -   **"User is not in the sudoers file. This incident will be reported." :**
            Ce message signifie que l'utilisateur n'a pas les permissions requises pour exécuter la commande.
            -   Vérifiez l'orthographe du nom d'utilisateur ou du groupe dans `sudoers`.
            -   Assurez-vous que l'utilisateur fait bien partie du groupe spécifié (si vous utilisez un groupe alias).
            -   Vérifiez que la commande est correctement spécifiée (chemin absolu) et autorisée.
        -   **Problèmes de chemins de commandes :** Si une commande ne fonctionne pas, assurez-vous que le chemin absolu est correct (ex: `/usr/bin/python3` au lieu de `/usr/bin/python`).
        -   **Ordre des règles :** Rappelez-vous que la dernière règle correspondante l'emporte. Si une autorisation est annulée par un refus, assurez-vous que le refus est la règle la plus spécifique appliquée.
        -   **Vérifier les logs :** Les incidents `sudo` sont souvent logués dans `/var/log/auth.log` (Debian/Ubuntu) ou `/var/log/secure` (RHEL/CentOS). Ces logs peuvent fournir des indices précieux sur les échecs d'autorisation.
        """
        add_scrollable_text_to_content_frame("9. Bonnes Pratiques", best_practices_text)


if __name__ == "__main__":
    app = VisudoConfigApp()
    app.mainloop()