import customtkinter as ctk

class EtcCfgApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Exploration du Dossier /etc")
        self.geometry("1100x750")

        # Configure grid layout for the main window (1 row, 2 columns)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Vertical Navigation Frame (Navbar) ---
        self.navigation_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame,
                                                    text="Dossier /etc",
                                                    compound="left",
                                                    font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # --- Content Frame (where tab content will be displayed) ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.content_frame.grid_rowconfigure(0, weight=1)
        # Fix: Changed 'self.content_columnconfigure' to 'self.content_frame.grid_columnconfigure'
        self.content_frame.grid_columnconfigure(0, weight=1) 

        # Dictionary to hold tab content as CTkTextbox widgets
        self.tab_content_widgets = {}

        # --- Navigation Buttons ---
        self.create_navigation_buttons()

        # Set initial content
        self.select_frame_by_name("1. Introduction au Dossier /etc")

    def create_navigation_buttons(self):
        button_info = [
            ("1. Introduction au Dossier /etc", 1),
            ("2. Fichiers Essentiels", 2),
            ("3. Sous-répertoires Clés", 3),
            ("4. Gestion du Répertoire", 4),
            ("5. Sécurité et Permissions", 5),
            ("6. Bonnes Pratiques", 6)
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
        buttons = [getattr(self, f"nav_button_{i}") for i in range(1, 7)] # Adjust range based on button_info size
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

        # --- Tab 1: Introduction au Dossier /etc ---
        intro_text = """
        ### Introduction au Dossier `/etc`

        Le répertoire `/etc` est l'un des répertoires les plus importants d'un système Linux. Son nom vient historiquement de "et cetera" (et le reste), mais il est maintenant reconnu comme le répertoire des **fichiers de configuration spécifiques à l'hôte**.

        **Rôle et Importance :**
        -   **Configuration Système :** Il contient la grande majorité des fichiers de configuration pour le système d'exploitation et les applications installées.
        -   **Statut Local :** Contrairement à d'autres répertoires (`/bin`, `/usr/bin`) qui contiennent des exécutables ou des bibliothèques, les fichiers de `/etc` sont généralement statiques et propres à la configuration de cette machine spécifique. Ils ne sont pas des exécutables binaires.
        -   **Lisibilité :** La plupart des fichiers sont des fichiers texte ASCII, ce qui les rend lisibles et modifiables avec un simple éditeur de texte.
        -   **Sauvegarde Essentielle :** En raison de leur importance pour le fonctionnement du système, les fichiers de `/etc` sont souvent inclus dans les sauvegardes du système.

        **Structure Générale :**
        `/etc` contient à la fois des fichiers individuels et de nombreux sous-répertoires, chacun dédié à la configuration d'un service ou d'une fonctionnalité particulière.

        Ce guide vous aidera à naviguer dans ce répertoire crucial et à comprendre les fichiers et sous-répertoires les plus courants.
        """
        add_scrollable_text_to_content_frame("1. Introduction au Dossier /etc", intro_text)

        # --- Tab 2: Fichiers Essentiels ---
        essential_files_text = """
        ### Fichiers Essentiels dans `/etc`

        Voici quelques-uns des fichiers les plus critiques et les plus fréquemment consultés ou modifiés dans le répertoire `/etc` :

        1.  **`/etc/passwd`**
            -   **Fonction :** Contient des informations de base sur les **comptes utilisateurs** du système (nom d'utilisateur, ID utilisateur (UID), ID de groupe (GID) principal, répertoire personnel, shell par défaut, et un "x" indiquant que le mot de passe est dans `/etc/shadow`).
            -   **Permissions :** Lisible par tous.
            -   **Exemple de ligne :** `utilisateur:x:1000:1000:Nom Complet:/home/utilisateur:/bin/bash`

        2.  **`/etc/shadow`**
            -   **Fonction :** Stocke les **mots de passe hachés** des utilisateurs et les informations sur leur expiration.
            -   **Permissions :** Accessible uniquement par l'utilisateur `root` pour des raisons de sécurité.
            -   **Exemple de ligne :** `utilisateur:$6$salt$hashedpassword:19760:0:99999:7:::`

        3.  **`/etc/group`**
            -   **Fonction :** Liste les **groupes** et leurs membres.
            -   **Permissions :** Lisible par tous.
            -   **Exemple de ligne :** `groupe:x:1001:membre1,membre2`

        4.  **`/etc/fstab`**
            -   **Fonction :** Définit les **systèmes de fichiers** à monter au démarrage du système.
            -   **Format :** Point de montage, type de système de fichiers, options de montage, option `dump`, option `pass` (pour `fsck`).
            -   **Permissions :** Généralement `0644` (propriétaire root lecture/écriture, autres lecture).
            -   **Attention :** Une erreur dans ce fichier peut empêcher le système de démarrer.

        5.  **`/etc/hostname`**
            -   **Fonction :** Contient le **nom d'hôte** du système.

        6.  **`/etc/hosts`**
            -   **Fonction :** Mappe les adresses IP aux noms d'hôtes locaux. Agit comme un DNS local rudimentaire.
            -   **Exemple de ligne :** `127.0.0.1    localhost`

        7.  **`/etc/resolv.conf`**
            -   **Fonction :** Configure les **serveurs DNS** que le système utilise pour résoudre les noms de domaine. Peut être généré dynamiquement par NetworkManager ou systemd-resolved.

        8.  **`/etc/network/interfaces`** (sur Debian/Ubuntu) ou **`/etc/sysconfig/network-scripts/ifcfg-*`** (sur Red Hat/CentOS)
            -   **Fonction :** Fichiers de configuration des **interfaces réseau**.

        9.  **`/etc/sysctl.conf`**
            -   **Fonction :** Configure les paramètres du **noyau Linux (kernel)** au démarrage.
            -   **Exemple :** Ajuster les paramètres TCP/IP pour la performance réseau.

        10. **`/etc/default/*`**
            -   **Fonction :** Répertoire contenant des fichiers de configuration par défaut pour divers services ou applications. Par exemple, `/etc/default/grub` pour GRUB, ou `/etc/default/useradd` pour les valeurs par défaut de la commande `useradd`.

        11. **`/etc/sudoers`**
            -   **Fonction :** Définit quels utilisateurs ou groupes peuvent exécuter des commandes avec les privilèges de `root` (ou d'un autre utilisateur) via la commande `sudo`.
            -   **Outil de modification :** Doit être modifié avec `visudo` pour éviter les erreurs de syntaxe qui pourraient bloquer l'accès `sudo`.
            -   **Permissions :** Très strictes, généralement `0440` (propriétaire `root` lecture, groupe `root` lecture).

        12. **`/etc/crontab`** et **`/etc/cron.*`**
            -   **Fonction :** Définit les tâches planifiées (jobs cron) à exécuter régulièrement.
            -   `/etc/crontab` : Le crontab système global.
            -   `/etc/cron.d/` : Contient des crontabs spécifiques à des applications.
            -   `/etc/cron.hourly/`, `/etc/cron.daily/`, etc. : Scripts exécutés toutes les heures, jours, semaines, mois.

        Comprendre ces fichiers est la clé pour administrer efficacement un système Linux.
        """
        add_scrollable_text_to_content_frame("2. Fichiers Essentiels", essential_files_text)

        # --- Tab 3: Sous-répertoires Clés ---
        subdirectories_text = """
        ### Sous-répertoires Clés dans `/etc`

        Le répertoire `/etc` est organisé en de nombreux sous-répertoires, chacun contenant la configuration d'un service ou d'un composant système spécifique.

        1.  **`/etc/apt/` ou `/etc/yum.repos.d/`**
            -   **Fonction :** Contient les fichiers de configuration des **dépôts de paquets** pour les gestionnaires de paquets.
                -   `/etc/apt/` : Pour les systèmes basés sur Debian/Ubuntu (APT). Contient `sources.list`.
                -   `/etc/yum.repos.d/` : Pour les systèmes basés sur Red Hat/CentOS/Fedora (YUM/DNF). Contient des fichiers `.repo`.

        2.  **`/etc/default/`**
            -   **Fonction :** Contient des fichiers qui définissent les **valeurs par défaut** pour divers programmes et scripts de démarrage. Non pas des scripts eux-mêmes, mais des variables que les scripts liront.
            -   **Exemples :** `useradd`, `grub`, `locale`.

        3.  **`/etc/ssh/`**
            -   **Fonction :** Fichiers de configuration pour le **service SSH (Secure Shell)**.
            -   **Fichiers clés :**
                -   `sshd_config` : Configuration du démon SSH (le serveur).
                -   `ssh_config` : Configuration du client SSH.
                -   Clés d'hôte du serveur SSH.

        4.  **`/etc/systemd/`**
            -   **Fonction :** Contient les fichiers de configuration pour le **système d'initialisation `systemd`**.
            -   Inclut les définitions d'unités pour les services, les points de montage, les timers, etc.
            -   **Sous-répertoires importants :** `system/`, `user/`, `journald.conf`, `logind.conf`.

        5.  **`/etc/network/`** (sur Debian/Ubuntu) ou **`/etc/sysconfig/network-scripts/`** (sur Red Hat/CentOS)
            -   **Fonction :** Configuration détaillée du **réseau**.
            -   `interfaces` (Debian/Ubuntu) : Configure les interfaces réseau.
            -   `ifcfg-*` (Red Hat/CentOS) : Fichiers spécifiques à chaque interface.

        6.  **`/etc/apache2/` ou `/etc/httpd/`**
            -   **Fonction :** Configuration du **serveur web Apache HTTP Server**.
            -   `apache2/` (Debian/Ubuntu) ou `httpd/` (Red Hat/CentOS).
            -   **Fichiers clés :** `apache2.conf` ou `httpd.conf`, répertoires pour les sites activés (`sites-enabled`), les modules (`mods-enabled`).

        7.  **`/etc/nginx/`**
            -   **Fonction :** Configuration du **serveur web Nginx**.
            -   **Fichiers clés :** `nginx.conf`, répertoires pour les sites activés (`sites-enabled`), les conf.d.

        8.  **`/etc/samba/`**
            -   **Fonction :** Configuration du **serveur de fichiers Samba** (partage de fichiers avec Windows).
            -   **Fichier clé :** `smb.conf`.

        9.  **`/etc/pam.d/`**
            -   **Fonction :** Fichiers de configuration pour les **PAM (Pluggable Authentication Modules)**. Ces modules gèrent l'authentification, l'autorisation, la gestion de session et la gestion des mots de passe pour diverses applications (login, sudo, sshd, etc.).
            -   Chaque fichier correspond à une application (ex: `login`, `passwd`, `sshd`).

        10. **`/etc/cron.d/`, `/etc/cron.daily/`, `/etc/cron.hourly/`, `/etc/cron.monthly/`, `/etc/cron.weekly/`**
            -   **Fonction :** Répertoires pour les scripts de tâches planifiées (cron jobs) exécutés automatiquement.

        11. **`/etc/skel/`**
            -   **Fonction :** Contient les fichiers et répertoires qui sont **copiés dans le répertoire personnel** d'un nouvel utilisateur lors de sa création.
            -   **Exemples :** `.bashrc`, `.profile`, `.config/`.

        12. **`/etc/opt/`**
            -   **Fonction :** Répertoire pour les fichiers de configuration des applications installées dans `/opt` (applications tierces ou propriétaires).

        Cette organisation logique aide à maintenir la configuration propre et facile à gérer, même avec de nombreux services installés.
        """
        add_scrollable_text_to_content_frame("3. Sous-répertoires Clés", subdirectories_text)

        # --- Tab 4: Gestion du Répertoire ---
        management_text = """
        ### Gestion et Manipulation du Répertoire `/etc`

        Travailler avec les fichiers de configuration dans `/etc` nécessite des précautions pour éviter de casser le système.

        #### 1. Édition des Fichiers :
        -   Utilisez un éditeur de texte en ligne de commande comme **`nano`**, **`vi`**, ou **`vim`**.
        -   Utilisez toujours `sudo` pour éditer les fichiers de `/etc`, car ils appartiennent généralement à `root` et nécessitent des privilèges élevés.
            **Exemple :** `sudo nano /etc/hostname`

        #### 2. Sauvegarde Avant Modification :
        -   **Toujours sauvegarder un fichier avant de le modifier !** C'est une règle d'or.
        -   Utilisez `cp` pour créer une copie de sauvegarde.
            **Exemple :** `sudo cp /etc/fstab /etc/fstab.bak_$(date +%Y%m%d)`
            *Cela crée une sauvegarde avec la date actuelle.*

        #### 3. Redémarrage des Services :
        -   Après la modification de la plupart des fichiers de configuration de services, vous devez **redémarrer le service** associé pour que les changements prennent effet.
        -   Utilisez `systemctl` (pour les systèmes basés sur systemd) :
            `sudo systemctl restart nom_du_service`
            **Exemple :** `sudo systemctl restart sshd`
            *Ou pour recharger la configuration sans interrompre les connexions existantes (si supporté par le service) :*
            `sudo systemctl reload nom_du_service`

        -   Pour les systèmes basés sur SysVinit (plus anciens) :
            `sudo /etc/init.d/nom_du_service restart`

        #### 4. Vérification de la Syntaxe :
        -   Certains services (comme Apache, Nginx, ou SSH) ont des outils pour **vérifier la syntaxe** de leurs fichiers de configuration avant de redémarrer le service. C'est crucial pour éviter de bloquer le service.
            -   **Apache :** `sudo apachectl configtest`
            -   **Nginx :** `sudo nginx -t`
            -   **SSH :** `sudo sshd -t`

        #### 5. Gestion des Fichiers de Configuration par les Paquets :
        -   Lorsque vous installez, mettez à jour ou supprimez des paquets, le gestionnaire de paquets (APT, DNF, YUM) gère souvent les fichiers de configuration dans `/etc`.
        -   Si un fichier de configuration a été modifié localement, le gestionnaire de paquets peut vous demander s'il faut le remplacer par la nouvelle version du paquet, conserver l'ancienne, ou afficher les différences.
        -   Soyez attentif à ces messages (`.dpkg-old`, `.rpmsave`, `.rpmnew` sont des suffixes courants).

        #### 6. Versionnement des Fichiers de Configuration :
        -   Pour les systèmes critiques ou complexes, envisagez d'utiliser un **système de contrôle de version** (comme Git) pour les fichiers de `/etc`. Cela permet de suivre les changements, de revenir à des versions précédentes et de collaborer.
        -   Outils comme `etckeeper` peuvent automatiser la gestion de Git pour `/etc`.

        #### 7. Ne Supprimez Pas Aveuglément :
        -   Ne supprimez jamais un fichier de `/etc` à moins d'être absolument certain de ce que vous faites. Une suppression incorrecte peut rendre le système inutilisable.
        -   Préférez renommer un fichier (ex: `fichier.conf.desactive`) ou désactiver une fonction dans le fichier.
        """
        add_scrollable_text_to_content_frame("4. Gestion du Répertoire", management_text)

        # --- Tab 5: Sécurité et Permissions ---
        security_permissions_text = """
        ### Sécurité et Permissions dans `/etc`

        La sécurité du répertoire `/etc` est primordiale, car il contient des informations sensibles et contrôle le comportement du système. Des permissions incorrectes peuvent entraîner des vulnérabilités majeures.

        #### 1. Propriété (`chown`) :
        -   La plupart des fichiers et répertoires dans `/etc` doivent appartenir à l'utilisateur **`root`** et au groupe **`root`**.
        -   Ceci garantit que seuls l'administrateur système peut modifier ces fichiers.
        -   **Exemple :** `ls -l /etc/passwd` devrait afficher `root root`.
        -   **Vérification :** `find /etc ! -user root -o ! -group root` (Cherche les fichiers dans /etc qui n'appartiennent pas à root:root)

        #### 2. Permissions (`chmod`) :
        -   Les permissions doivent être très strictes.
        -   **Fichiers de configuration sensibles :** (`/etc/shadow`, `/etc/sudoers`) doivent avoir des permissions très restrictives (ex: `0400`, `0440`). Seul `root` devrait pouvoir les lire.
            -   `/etc/shadow` : `0400` (seul `root` peut lire).
            -   `/etc/sudoers` : `0440` (seul `root` peut lire, le groupe `root` peut lire).
        -   **Fichiers de configuration publics :** (`/etc/passwd`, `/etc/group`, `/etc/fstab`) sont lisibles par tous, mais ne devraient être modifiables que par `root`.
            -   `/etc/passwd` : `0644` (root lecture/écriture, autres lecture).
            -   `/etc/fstab` : `0644`.
        -   **Répertoires :** Les répertoires doivent avoir des permissions qui permettent à `root` de gérer leur contenu, mais limitent l'accès pour les autres. Souvent `0755` (propriétaire: tout, groupe/autres: lecture/exécution seulement).

        **Exemple de vérification de permissions (et correction si nécessaire) :**
        `sudo chmod 0400 /etc/shadow`
        `sudo chmod 0440 /etc/sudoers`
        `sudo chown root:root /etc/shadow /etc/sudoers`

        #### 3. Suivi des Modifications :
        -   Comme `/etc` est si critique, toute modification doit être surveillée.
        -   Utilisez des outils comme `auditd` pour loguer les accès et modifications aux fichiers sensibles.
        -   Considérez `etckeeper` pour le versionnement des fichiers de `/etc` avec Git. Cela vous permet de voir qui a modifié quoi et de revenir en arrière si nécessaire.

        #### 4. Intégrité des Fichiers :
        -   Les attaquants ciblent souvent les fichiers dans `/etc` pour compromettre un système (ex: ajout d'utilisateurs malveillants, modification de SSH pour collecter des informations d'identification).
        -   Utilisez des outils d'intégrité de fichiers (comme `aide` ou `chkrootkit`) pour détecter les modifications non autorisées dans `/etc`. Ces outils créent une base de référence et vous alertent si des fichiers sont modifiés.

        #### 5. Évitez les Symlinks Suspects :
        -   Assurez-vous qu'il n'y a pas de liens symboliques suspects pointant vers des emplacements non sécurisés dans `/etc`.

        #### 6. Le `umask` :
        -   Le `umask` (voir l'onglet précédent) est une protection préventive qui garantit que les nouveaux fichiers créés par les utilisateurs (y compris `root`) n'ont pas de permissions trop permissives par défaut.

        En bref, les permissions et la propriété dans `/etc` doivent être gérées avec une extrême rigueur. Une petite erreur ici peut avoir des conséquences de sécurité majeures.
        """
        add_scrollable_text_to_content_frame("5. Sécurité et Permissions", security_permissions_text)

        # --- Tab 6: Bonnes Pratiques ---
        best_practices_text = """
        ### Bonnes Pratiques pour la Gestion du Dossier `/etc`

        Gérer `/etc` efficacement et en toute sécurité est un signe d'un bon administrateur système.

        1.  **Sauvegardez TOUJOURS avant de modifier :** Avant d'éditer un fichier dans `/etc`, faites-en une copie de sauvegarde. Utilisez des noms descriptifs avec la date (`fichier.conf.bak_YYYYMMDD`).
            `sudo cp /etc/fichier.conf /etc/fichier.conf.bak_$(date +%Y%m%d)`

        2.  **Utilisez `sudo` avec parcimonie :** N'exécutez des commandes en tant que `root` (via `sudo`) que lorsque c'est absolument nécessaire pour les fichiers de `/etc`.

        3.  **Vérifiez la syntaxe après modification :** Pour les services critiques (Apache, Nginx, SSH), utilisez les outils de vérification de syntaxe (`apachectl configtest`, `nginx -t`, `sshd -t`) **avant** de redémarrer le service.

        4.  **Redémarrez les services proprement :** Utilisez `systemctl restart` (ou `reload` si approprié) pour appliquer les changements de configuration.

        5.  **Comprenez les permissions :** Assurez-vous que les permissions et la propriété des fichiers dans `/etc` sont toujours appropriées et restrictives. Revérifiez régulièrement les fichiers sensibles comme `/etc/shadow` et `/etc/sudoers`.

        6.  **Ne supprimez pas, désactivez ou renommez :** Si vous souhaitez désactiver une configuration, préférez renommer le fichier (ex: `fichier.conf.disabled`) ou commenter les lignes pertinentes plutôt que de le supprimer.

        7.  **Explorez les sous-répertoires :** Familiarisez-vous avec les sous-répertoires importants (`/etc/ssh/`, `/etc/systemd/`, `/etc/apt/`, etc.) pour savoir où trouver la configuration des services.

        8.  **Utilisez `etckeeper` :** Pour les serveurs critiques, envisagez d'installer `etckeeper`. Il s'intègre avec un système de contrôle de version (comme Git) et automatise les validations des modifications dans `/etc`, vous permettant de suivre les changements et de revenir en arrière.

        9.  **Surveillez les logs :** Gardez un œil sur les logs système (`/var/log/auth.log`, `/var/log/syslog`, `journalctl`) pour toute activité suspecte, en particulier après des modifications dans `/etc`.

        10. **Lisez la documentation :** Avant de modifier un fichier de configuration pour un service que vous ne connaissez pas bien, lisez sa page de manuel (`man service.conf`) ou sa documentation officielle.

        En suivant ces bonnes pratiques, vous pouvez maintenir la stabilité et la sécurité de votre système Linux tout en gérant efficacement ses configurations.
        """
        add_scrollable_text_to_content_frame("6. Bonnes Pratiques", best_practices_text)

if __name__ == "__main__":
    app = EtcCfgApp()
    app.mainloop()