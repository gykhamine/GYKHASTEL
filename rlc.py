import customtkinter as ctk

class LinuxDirsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Exploration Détaillée des Répertoires Linux Clés")
        self.geometry("1200x800") # Slightly larger window

        # Configure grid layout for the main window (1 row, 2 columns)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Vertical Navigation Frame (Navbar) ---
        self.navigation_frame = ctk.CTkFrame(self, width=220, corner_radius=0) # Wider navbar
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame,
                                                    text="Guide des Répertoires Linux",
                                                    compound="left",
                                                    font=ctk.CTkFont(size=16, weight="bold"))
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
        self.select_frame_by_name("1. Introduction Générale")

    def create_navigation_buttons(self):
        button_info = [
            ("1. Introduction Générale", 1),
            ("2. Répertoire /var (Données Variables)", 2),
            ("3. Répertoire /usr/share (Données Partagées)", 3),
            ("4. Répertoire /dev (Fichiers de Périphériques)", 4),
            ("5. Répertoire /run (Données d'Exécution Volatiles)", 5),
            ("6. Répertoire /proc (Système de Fichiers Virtuel du Noyau)", 6),
            ("7. Bonnes Pratiques et Synthèse", 7)
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
        buttons = [getattr(self, f"nav_button_{i}") for i in range(1, 8)] # Adjust range based on button_info size
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
            text_widget = ctk.CTkTextbox(frame, wrap="word", width=900, height=650) # Wider and taller
            text_widget.insert("0.0", text_content)
            text_widget.configure(state="disabled")
            text_widget.pack(padx=10, pady=10, fill="both", expand=True)
            self.tab_content_widgets[name] = frame

        # --- Tab 1: Introduction Générale ---
        intro_text = """
        ### Introduction aux Répertoires Linux Clés : Le Cœur du Système de Fichiers

        Le **système de fichiers Linux** est bien plus qu'une simple collection de dossiers ; c'est une structure hiérarchique et organisée, conçue selon la **Filesystem Hierarchy Standard (FHS)**. Chaque répertoire à la racine a un rôle bien défini, ce qui rend le système à la fois robuste et prévisible. Comprendre cette organisation est fondamental pour toute personne interagissant avec Linux, qu'il s'agisse d'un utilisateur novice, d'un développeur ou d'un administrateur système expérimenté. En effet, une connaissance approfondie de ces emplacements vous permettra de localiser des fichiers, de diagnostiquer des problèmes, d'optimiser les performances et de renforcer la sécurité.

        Ce guide interactif a pour objectif d'explorer en profondeur cinq répertoires particulièrement importants, qui sont souvent mal compris ou sous-estimés par les débutants :

        * **/var (Variable Data)** : Ce répertoire est le gardien de toutes les données qui changent dynamiquement au cours de l'exécution du système. Pensez aux journaux d'activité, aux files d'attente de tâches, aux caches de données et aux fichiers de sites web. Sa gestion est cruciale pour éviter la saturation du disque et pour le dépannage.
        * **/usr/share (User System Resources - Shared Data)** : Ici résident les ressources et données qui sont indépendantes de l'architecture matérielle et partagées par plusieurs applications. Cela inclut la documentation, les pages de manuel, les icônes, les polices, les fichiers de localisation et les thèmes. C'est le dépôt des "bonnes pratiques" en matière de ressources système partagées.
        * **/dev (Devices)** : Un répertoire unique en son genre, `/dev` contient des "fichiers" qui ne sont pas de simples données stockées sur disque, mais plutôt des interfaces logiques vers les périphériques matériels (ou virtuels) connectés à votre système. Chaque périphérique, qu'il s'agisse d'un disque dur, d'une imprimante ou même du générateur de nombres aléatoires, est représenté ici comme un fichier, ce qui permet aux programmes d'interagir avec le matériel de manière standardisée.
        * **/run (Runtime Data)** : Ce répertoire, monté en mémoire vive (tmpfs) et effacé à chaque redémarrage, est le théâtre des opérations en cours. Il contient des informations éphémères mais vitales sur l'état d'exécution du système, telles que les identifiants de processus (PID), les sockets de communication inter-processus et d'autres données transitoires nécessaires au bon fonctionnement des services.
        * **/proc (Processes and Kernel Information)** : Véritable fenêtre sur l'âme de votre système, `/proc` est un système de fichiers virtuel généré en temps réel par le noyau Linux. Il ne réside pas sur le disque et offre une vue dynamique de l'état du noyau, des processus actifs, de l'utilisation de la mémoire, de l'état du réseau et de nombreux autres paramètres système. C'est une ressource inestimable pour le monitoring et le diagnostic.

        Chacun de ces répertoires joue un rôle distinct mais interconnecté dans le fonctionnement global d'un système Linux. En les explorant en détail, vous développerez une compréhension plus profonde de la façon dont Linux gère ses ressources, communique avec le matériel et fournit des informations en temps réel sur son état. Préparons-nous à plonger dans les entrailles de votre système !
        """
        add_scrollable_text_to_content_frame("1. Introduction Générale", intro_text)

        # --- Tab 2: /var ---
        var_text = """
        ### Répertoire `/var` : Le Cœur Battant des Données Dynamiques

        Le répertoire **/var** (de "variable data") est la zone de stockage des informations qui sont susceptibles de changer régulièrement pendant que le système est en fonctionnement normal. Sa raison d'être est de séparer les données statiques (comme les exécutables dans `/bin` ou les configurations dans `/etc`) des données dynamiques qui croissent, diminuent ou sont mises à jour constamment. Un espace disque insuffisant dans `/var` peut entraîner des pannes système graves, car de nombreux services ne pourront plus écrire leurs logs, gérer leurs files d'attente ou stocker leurs données temporaires.

        #### Principaux Sous-répertoires et Leur Rôle Approfondi :

        1.  **`/var/log/` : Les Annales du Système**
            C'est l'emplacement le plus fréquenté de `/var`. Il contient tous les **fichiers journaux (logs)** générés par le système d'exploitation, les applications et les services. Ces logs sont cruciaux pour le dépannage, l'audit de sécurité et la compréhension du comportement du système.
            * **`syslog` ou `messages` :** Le journal système général, enregistrant la plupart des événements non spécifiques.
            * **`auth.log` (ou `secure` sur Red Hat/CentOS) :** Contient les informations relatives aux tentatives d'authentification, aux connexions réussies et échouées (SSH, sudo, etc.). Indispensable pour la sécurité.
            * **`kern.log` :** Enregistre les messages du noyau Linux. Utile pour diagnostiquer les problèmes matériels ou les erreurs de pilote.
            * **`dpkg.log` (Debian/Ubuntu) / `yum.log` (Red Hat/CentOS) :** Suivent l'installation, la mise à jour et la suppression des paquets logiciels.
            * **Sous-répertoires spécifiques :** Des services comme Apache (`/var/log/apache2/`), Nginx (`/var/log/nginx/`), MySQL (`/var/log/mysql/`) ou Postfix (`/var/log/mail.log`) ont leurs propres sous-répertoires pour leurs journaux d'accès et d'erreurs.
            * **Gestion :** Des utilitaires comme `logrotate` sont configurés pour gérer la taille de ces fichiers, en les archivant, en les compressant et en les supprimant après un certain temps ou une certaine taille, afin d'éviter la saturation de l'espace disque.

        2.  **`/var/www/` : Le Cœur de Votre Présence Web**
            Traditionnellement, c'est le répertoire par défaut où les **serveurs web** (comme Apache ou Nginx) stockent les fichiers qui constituent vos sites web (HTML, CSS, JavaScript, images, scripts PHP/Python/Perl). Bien que ce ne soit pas une obligation stricte (les serveurs web peuvent être configurés pour servir des fichiers depuis d'autres emplacements), c'est une convention forte et un emplacement logique pour le contenu dynamique.
            * **Exemple :** `/var/www/html` est souvent le répertoire racine par défaut pour un serveur Apache. Chaque site web peut avoir son propre sous-répertoire.

        3.  **`/var/mail/` ou `/var/spool/mail/` : Votre Boîte aux Lettres Système**
            Ces emplacements (le chemin exact peut varier selon la distribution) abritent les **boîtes aux lettres des utilisateurs système**. Chaque fichier dans ce répertoire correspond à un utilisateur Linux et contient les e-mails qui lui sont adressés localement. Bien que moins courant dans les environnements de bureau modernes où les clients e-mail gèrent souvent des serveurs distants, c'est essentiel pour les notifications système et les e-mails générés localement.

        4.  **`/var/spool/` : Le Hall d'Attente des Tâches**
            Ce répertoire contient les données des **files d'attente (spool)** pour divers processus. Une "spool" est une zone tampon où des données sont placées avant d'être traitées par un autre processus.
            * **`cron/` :** Les fichiers de configuration pour les tâches planifiées spécifiques à l'utilisateur (`crontabs`).
            * **`lpd/` ou `cups/` :** Les documents en attente d'impression.
            * **`mqueue/` :** Les e-mails en attente d'envoi par un serveur de messagerie.
            * Ces files d'attente sont cruciales pour les opérations asynchrones, garantissant que les tâches sont exécutées même si le service principal est temporairement indisponible.

        5.  **`/var/lib/` : L'État Persistant des Applications**
            Ce sous-répertoire contient les **données d'état persistantes** des applications et services. Contrairement à `/var/cache`, ces données sont généralement essentielles au fonctionnement d'une application et ne peuvent pas être supprimées sans conséquence.
            * **Exemples :**
                * `/var/lib/mysql/` : Les bases de données MySQL/MariaDB.
                * `/var/lib/dpkg/` (Debian/Ubuntu) ou `/var/lib/rpm/` (Red Hat/CentOS) : Les bases de données des gestionnaires de paquets, qui gardent une trace des paquets installés, de leurs versions, et de leurs fichiers.
                * `/var/lib/systemd/` : Données d'état pour systemd.
                * `/var/lib/docker/` : Données et images Docker.
            * Ces données sont régulièrement modifiées par les services et doivent être protégées et sauvegardées.

        6.  **`/var/cache/` : Les Accélérateurs de Données**
            Contient les **données en cache** générées par les applications pour accélérer leurs opérations futures. Ces données peuvent être supprimées sans perte de fonctionnalité majeure, mais leur suppression forcera l'application à les recréer, ce qui peut entraîner une légère baisse de performance temporaire.
            * **Exemples :**
                * `/var/cache/apt/archives/` : Les paquets `.deb` téléchargés par APT avant leur installation.
                * `/var/cache/yum/` : Le cache des métadonnées et des paquets pour YUM/DNF.
                * Les caches web ou de navigateur.
            * Le nettoyage périodique de ce répertoire peut libérer de l'espace disque.

        7.  **`/var/tmp/` : Le Pansement à Long Terme**
            Semblable à `/tmp`, `/var/tmp` est destiné aux **fichiers temporaires**, mais avec une distinction cruciale : son contenu est **généralement conservé entre les redémarrages** du système. Cependant, il est censé être purgé périodiquement par des services système (comme `tmpwatch` sur Red Hat ou `systemd-tmpfiles-clean.service` sur systemd) après un certain délai d'inactivité. Les applications sont censées y stocker des fichiers temporaires qui peuvent être volumineux ou nécessaires pour des opérations prolongées.

        En résumé, `/var` est un répertoire dynamique essentiel. Sa gestion implique une surveillance constante de l'espace disque, une configuration appropriée de `logrotate`, et une compréhension de la nature des données stockées pour garantir la stabilité et la performance du système. Il est le point de départ pour le dépannage de la plupart des problèmes applicatifs et système.
        """
        add_scrollable_text_to_content_frame("2. Répertoire /var (Données Variables)", var_text)

        # --- Tab 3: /usr/share ---
        usr_share_text = """
        ### Répertoire `/usr/share` : Le Trésor des Ressources Partagées Indépendantes de l'Architecture

        Le répertoire **/usr/share** est un pilier de la **Filesystem Hierarchy Standard (FHS)**, conçu pour héberger des **données partagées qui sont indépendantes de l'architecture matérielle** du système. Cela le distingue des binaires exécutables qui se trouvent dans `/usr/bin` ou `/usr/sbin` et qui sont compilés spécifiquement pour une architecture (x86, ARM, etc.). En d'autres termes, les fichiers dans `/usr/share` sont du contenu générique (texte, images, sons, scripts interprétés) qui peut être utilisé par n'importe quel système Linux, quelle que soit son architecture sous-jacente. C'est le dépôt centralisé pour les ressources utilisées par les applications et le système lui-même.

        #### Contenu Essentiel et Explications Détaillées :

        1.  **`/usr/share/doc/` : Votre Bibliothèque de Documentation Locale**
            Ce sous-répertoire est une mine d'informations. Il contient la **documentation complète des paquets logiciels installés** sur votre système. Chaque paquet a généralement son propre sous-répertoire (par exemple, `/usr/share/doc/apache2/`, `/usr/share/doc/python3/`). Vous y trouverez des fichiers `README`, des fichiers `CHANGELOG` (historique des modifications), des licences, ainsi que parfois des manuels complets au format texte, HTML ou PDF.
            * **Utilité :** C'est la première place à regarder si vous avez besoin de comprendre comment fonctionne un logiciel spécifique ou de consulter sa documentation officielle sans avoir accès à Internet.

        2.  **`/usr/share/man/` : L'Encyclopédie des Commandes Linux**
            Incontournable pour tout utilisateur ou administrateur Linux, ce répertoire abrite toutes les **pages de manuel (man pages)**. C'est le système de documentation en ligne standard pour les commandes, les fichiers de configuration, les appels système, les bibliothèques, etc. Les pages sont organisées par sections numériques (par exemple, `man1` pour les commandes utilisateur, `man5` pour les formats de fichiers, `man8` pour les commandes d'administration).
            * **Exemple :** Taper `man ls` ou `man bash` affiche le contenu des fichiers correspondants situés ici.

        3.  **`/usr/share/info/` : La Documentation GNU Alternative**
            Similaire à `man`, mais utilisant le système de documentation **GNU Info**. Les documents Info sont souvent plus hypertextuels et interactifs que les pages de manuel traditionnelles, permettant une navigation plus aisée entre les sections. De nombreux projets GNU fournissent leur documentation dans ce format.
            * **Exemple :** `info coreutils` ou `info bash` pour des informations plus détaillées.

        4.  **`/usr/share/locale/` : Le Multilinguisme Système**
            Ce répertoire est essentiel pour la **localisation (i18n)** de votre système. Il contient les fichiers de traduction (`.mo` pour GNU gettext) qui permettent aux applications d'afficher leur interface utilisateur dans différentes langues. Chaque sous-répertoire représente un code de langue (par exemple, `fr/`, `en_US/`, `es/`).
            * **Fonctionnement :** Lorsque vous définissez votre variable d'environnement `LANG` ou `LC_ALL`, le système recherche les fichiers de traduction appropriés ici pour adapter l'interface utilisateur.

        5.  **`/usr/share/icons/` : La Galerie d'Icônes**
            Contient les **fichiers d'icônes** utilisés par l'environnement de bureau (GNOME, KDE, Xfce, LXQt, etc.) et les applications pour représenter des programmes, des fichiers, des actions et des éléments d'interface. Elles sont souvent organisées par thèmes et par tailles pour s'adapter à diverses résolutions et contextes.

        6.  **`/usr/share/fonts/` : La Librairie Typographique**
            Ce répertoire stocke les **fichiers de polices** système (`.ttf`, `.otf`, `.woff`, etc.) qui sont disponibles pour toutes les applications. Elles peuvent être organisées par type de police ou par paquet qui les a installées.

        7.  **`/usr/share/sounds/` : Les Sons du Système**
            Contient les **fichiers audio** utilisés par le système pour les événements (sons de démarrage, alertes, notifications, etc.).

        8.  **`/usr/share/themes/` : Le Dressing de Votre Bureau**
            Ce répertoire contient les **thèmes visuels** qui définissent l'apparence des widgets, des fenêtres et des éléments de l'interface graphique de votre environnement de bureau.

        9.  **`/usr/share/applications/` : Le Catalogue des Programmes**
            Contient des fichiers `.desktop` qui sont de petits fichiers de configuration décrivant les applications installées. Ces fichiers sont utilisés par les gestionnaires de menus et les lanceurs d'applications pour afficher les programmes, leur icône, leur catégorie et la commande à exécuter pour les lancer.

        10. **`/usr/share/pixmaps/` : Images pour les Applications**
            Un répertoire historique qui contient de petites images (`.xpm`, `.png`, etc.) souvent utilisées par des applications plus anciennes pour leurs icônes ou leurs éléments graphiques internes.

        #### Importance Stratégique :
        Le rôle de `/usr/share` est de garantir la **portabilité et la réutilisabilité** des ressources. En séparant les données indépendantes de l'architecture des binaires, les distributions Linux peuvent plus facilement créer des paquets et maintenir un écosystème logiciel cohérent. Pour l'utilisateur et l'administrateur, c'est l'endroit où trouver la documentation, les pages de manuel et toutes les ressources nécessaires au bon fonctionnement de l'environnement de bureau et des applications. Il n'est généralement pas conseillé d'y ajouter des fichiers manuellement ; les ressources y sont installées par les gestionnaires de paquets.
        """
        add_scrollable_text_to_content_frame("3. Répertoire /usr/share (Données Partagées)", usr_share_text)

        # --- Tab 4: /dev ---
        dev_text = """
        ### Répertoire `/dev` : La Passerelle vers le Matériel

        Le répertoire **/dev** (de "devices") est l'un des aspects les plus uniques et fondamentaux du système de fichiers Linux. Contrairement aux autres répertoires qui stockent des fichiers de données ou des programmes, `/dev` contient des **fichiers de périphériques (device files)**. Ces "fichiers" ne sont pas de la donnée stockée sur un disque, mais des interfaces logiques ou des points d'accès vers le matériel réel ou virtuel connecté au système. Ils permettent aux programmes de l'espace utilisateur d'interagir avec le matériel en utilisant les opérations de fichier standard (lecture, écriture).

        Le contenu de `/dev` est créé dynamiquement par le noyau Linux et le démon **udev** au démarrage du système et chaque fois qu'un périphérique est connecté ou déconnecté (connexion à chaud, "hotplug"). C'est pourquoi vous ne devriez jamais créer ou modifier manuellement des fichiers dans `/dev`, car udev se charge de maintenir ce répertoire à jour en fonction du matériel détecté.

        #### Catégories Principales de Fichiers de Périphériques :

        1.  **Fichiers de Périphériques Caractères (Character Devices) :**
            * **Identifiés par `c` dans `ls -l`.**
            * Ces périphériques transfèrent des données caractère par caractère, sans utiliser de tampon de blocage. Cela signifie que chaque lecture ou écriture est gérée immédiatement par le pilote du périphérique.
            * **Exemples Cruciaux :**
                * **`/dev/null` :** Le célèbre "trou noir" de Linux. Toute donnée écrite dans ce fichier est immédiatement jetée. Il est très utile pour rediriger la sortie non désirée d'une commande (par exemple, `commande > /dev/null 2>&1` pour masquer la sortie standard et l'erreur standard).
                * **`/dev/zero` :** Fournit un flux infini de caractères nuls (`\0`). Utile pour créer des fichiers de taille fixe remplis de zéros, ou pour tester des performances d'écriture (`dd if=/dev/zero of=fichier bs=1M count=100`).
                * **`/dev/random` et `/dev/urandom` :** Sources de nombres aléatoires. `/dev/random` génère des nombres aléatoires en collectant de l'entropie (aléatoire réel) de l'environnement matériel, pouvant bloquer si l'entropie est insuffisante. `/dev/urandom` est non-bloquant et génère des nombres pseudo-aléatoires de haute qualité, suffisants pour la plupart des applications cryptographiques.
                * **`/dev/tty` :** Représente le terminal de contrôle du processus appelant. Lorsque vous utilisez `echo "hello" > /dev/tty`, le texte s'affiche sur le terminal où la commande a été lancée.
                * **`/dev/console` :** Le terminal principal du système, souvent utilisé par le noyau pour les messages de démarrage.
                * **`/dev/pts/X` :** Les pseudo-terminaux (`pts` pour pseudo-terminal slave). Chaque fois que vous ouvrez une session SSH, une fenêtre de terminal graphique (comme GNOME Terminal ou Konsole), ou utilisez des multiplexeurs de terminal comme `screen` ou `tmux`, un nouveau pseudo-terminal est créé et interagit via un fichier dans `/dev/pts/` (par exemple, `/dev/pts/0`, `/dev/pts/1`).

        2.  **Fichiers de Périphériques Bloc (Block Devices) :**
            * **Identifiés par `b` dans `ls -l`.**
            * Ces périphériques transfèrent des données en blocs de taille fixe. Ils sont principalement utilisés pour les périphériques de stockage qui gèrent l'accès aux données en unités de blocs (disques durs, SSD, clés USB, lecteurs CD/DVD).
            * **Exemples Communs :**
                * **`/dev/sda`, `/dev/sdb`, etc. :** Représentent les disques durs entiers (SATA, SCSI, virtuels). `/dev/sda` est le premier disque détecté, `/dev/sdb` le deuxième, et ainsi de suite.
                * **`/dev/sda1`, `/dev/sda2`, etc. :** Représentent les partitions spécifiques sur un disque. `/dev/sda1` est la première partition sur `/dev/sda`.
                * **`/dev/nvme0n1` :** Représente un disque NVMe, où `n0` est le numéro du contrôleur et `n1` est le numéro du périphérique.
                * **`/dev/sr0` ou `/dev/cdrom` :** Représentent un lecteur de CD/DVD-ROM.
                * **`/dev/loop0`, `/dev/loop1`, etc. :** Les périphériques loopback. Ils permettent de traiter un fichier (par exemple, une image ISO ou un fichier d'image disque) comme un périphérique bloc, ce qui permet de le monter comme un système de fichiers.

        #### Autres Éléments Spéciaux dans `/dev` :

        * **`/dev/shm/` (Shared Memory) :**
            * Un système de fichiers virtuel pour la **mémoire partagée POSIX**. Souvent monté en tant que `tmpfs` (en mémoire vive). Il permet à des processus distincts de communiquer et de partager des données en accédant à la même région de la mémoire système. Indispensable pour de nombreuses applications complexes.

        * **`/dev/fd/` (File Descriptors) :**
            * Un répertoire spécial qui contient des liens symboliques vers les **descripteurs de fichiers ouverts** par le processus en cours d'exécution.
            * **`/dev/fd/0` :** Lié à l'entrée standard (stdin).
            * **`/dev/fd/1` :** Lié à la sortie standard (stdout).
            * **`/dev/fd/2` :** Lié à l'erreur standard (stderr).
            * C'est une abstraction pratique qui permet aux programmes d'interagir avec les flux d'entrée/sortie de manière uniforme.

        * **`/dev/stdin`, `/dev/stdout`, `/dev/stderr` :**
            * Ce sont des liens symboliques vers `/dev/fd/0`, `/dev/fd/1`, `/dev/fd/2` respectivement, offrant une syntaxe plus lisible pour la redirection.

        #### Importance et Considérations de Sécurité :
        `/dev` est un répertoire critique pour la sécurité et le fonctionnement du système. Une gestion incorrecte des permissions ici pourrait permettre à un utilisateur malveillant d'accéder directement au matériel ou à des données sensibles. Par exemple, des fichiers comme `/dev/mem` (mémoire physique du système) ou `/dev/kmem` (mémoire du noyau) ne sont accessibles qu'à l'utilisateur `root` pour éviter toute manipulation dangereuse.
        La règle d'or est de ne jamais tenter de manipuler manuellement les fichiers de `/dev`. L'udev et le noyau gèrent ce répertoire de manière dynamique et automatisée, assurant que les permissions et les entrées sont toujours correctes pour le matériel détecté. C'est une interface puissante qui, bien que rarement directement touchée par les utilisateurs, est au cœur de toutes les interactions avec le matériel.
        """
        add_scrollable_text_to_content_frame("4. Répertoire /dev (Fichiers de Périphériques)", dev_text)

        # --- Tab 5: /run ---
        run_text = """
        ### Répertoire `/run` : L'Éphémère Gardien des Données d'Exécution

        Le répertoire **/run** est un ajout relativement récent à la **Filesystem Hierarchy Standard (FHS)**, standardisé à partir de la version 2.3. Il remplace et consolide des fonctionnalités qui étaient auparavant dispersées dans `/var/run`, `/dev/shm` et parfois même `/tmp`. Sa principale caractéristique est qu'il est généralement monté comme un **`tmpfs`**, ce qui signifie qu'il réside entièrement en **mémoire vive (RAM)**. Par conséquent, tout son contenu est **effacé automatiquement à chaque redémarrage** du système. C'est le lieu idéal pour stocker des données temporaires mais vitales pour les processus en cours d'exécution.

        #### Rôle Fondamental et Avantages :

        1.  **Volatilité et Propreté au Démarrage :**
            Le fait que `/run` soit vidé à chaque redémarrage garantit un état de système propre. Il élimine les "restes" d'exécutions précédentes qui pourraient potentiellement causer des problèmes ou des comportements inattendus pour les services ou les applications qui se relancent. C'est un principe de conception clé pour la robustesse et la prévisibilité du système.

        2.  **Performance et Rapidité :**
            Étant en mémoire vive, l'accès aux fichiers et aux données stockées dans `/run` est extrêmement rapide. Ceci est crucial pour les processus qui doivent lire ou écrire fréquemment de petites quantités de données d'état, comme les identifiants de processus ou les informations de session.

        3.  **Standardisation des Données d'Exécution :**
            Avant `/run`, les développeurs et les administrateurs devaient deviner où trouver les fichiers PID, les sockets et autres données d'exécution. `/run` a résolu ce problème en fournissant un emplacement standardisé et prévisible pour toutes ces données transitoires.

        #### Contenu Clé Détaillé de `/run` :

        1.  **Fichiers PID (Process ID files) : `/run/*.pid`**
            * **Fonction :** Ce sont des petits fichiers texte qui contiennent l'**ID de processus (PID)** du démon ou du service principal. Un PID est un numéro unique attribué par le noyau à chaque processus en cours d'exécution.
            * **Utilité :** Les services utilisent ces fichiers pour savoir si une autre instance d'eux-mêmes est déjà en cours d'exécution, pour s'arrêter proprement, ou pour envoyer des signaux à un processus spécifique.
            * **Exemples :** `/run/sshd.pid` (PID du démon SSH), `/run/rsyslogd.pid` (PID du démon de journalisation), `/run/dhcpcd.pid` (PID du client DHCP).

        2.  **Fichiers de Socket UNIX (IPC Sockets) :**
            * **Fonction :** Ces fichiers spéciaux facilitent la **communication inter-processus (IPC)** au niveau local, permettant à différents programmes sur la même machine de communiquer entre eux sans passer par le réseau (ce qui serait le cas avec les sockets réseau).
            * **Utilité :** Ils sont utilisés par des démons qui offrent des services à d'autres applications.
            * **Exemples :**
                * `/run/systemd/private` : Socket principal pour le système d'initialisation `systemd`.
                * `/run/dbus/system_bus_socket` : Le socket du bus de communication D-Bus, utilisé pour la communication entre les applications et les composants du bureau.
                * `/run/user/UID/bus` : Sockets D-Bus spécifiques à chaque utilisateur.
                * `/run/snapd.socket` : Socket pour le service Snap.

        3.  **Informations sur les Sessions Utilisateur : `/run/user/UID/`**
            * Sur les systèmes modernes utilisant `systemd` et `logind`, chaque utilisateur connecté reçoit un répertoire unique dans `/run/user/` (par exemple, `/run/user/1000/` pour l'UID 1000).
            * **Contenu :** Ce répertoire contient des données d'exécution spécifiques à la session de l'utilisateur, comme des sockets D-Bus propres à l'utilisateur, des informations sur les sessions graphiques (Wayland, XDG_RUNTIME_DIR), et d'autres fichiers temporaires qui doivent exister tant que la session est active. Ces données sont nettoyées lorsque l'utilisateur se déconnecte complètement.

        4.  **Points de Montage Temporaires :**
            * `/run` peut contenir des sous-répertoires qui servent de points de montage temporaires pour des périphériques ou des systèmes de fichiers, gérés dynamiquement par des services système.

        5.  **Fichiers de Verrouillage (Lock Files) :**
            * Certains services peuvent créer des fichiers de verrouillage dans `/run` pour indiquer qu'une ressource ou un fichier est en cours d'utilisation par un processus, empêchant d'autres processus d'y accéder simultanément et d'introduire des conflits.

        #### `/run` vs. `/var/run` (Historique) vs. `/tmp` :

        * **`/var/run` :** Historiquement, `/var/run` était l'emplacement standard pour les fichiers PID et les sockets. Cependant, cela posait problème car `/var` n'est pas toujours monté en début de processus de démarrage (il peut être sur une partition distincte). Pour résoudre ce problème, `/run` a été créé comme un `tmpfs` monté très tôt dans le processus de démarrage. Sur la plupart des systèmes modernes, `/var/run` est désormais un **lien symbolique vers `/run`** (`/var/run -> /run`) pour des raisons de compatibilité ascendante. Il est donc préférable de considérer `/run` comme l'emplacement canonique.

        * **`/tmp` :** Bien que `/tmp` et `/run` contiennent tous deux des données temporaires, leur objectif est différent. `/tmp` est pour les fichiers temporaires généraux qui peuvent potentiellement persister entre les redémarrages (même s'ils sont souvent purgés par `systemd-tmpfiles-clean.service` ou `tmpwatch`). `/run` est spécifiquement pour les données d'exécution qui *doivent* être effacées à chaque démarrage du système pour garantir un état propre. `/run` est toujours un tmpfs (en RAM), tandis que `/tmp` peut être sur disque ou en RAM selon la configuration.

        En conclusion, `/run` est un répertoire crucial pour la stabilité et la propreté du système Linux. Il permet aux services de communiquer, de suivre leur état et d'assurer un démarrage cohérent en garantissant que les données d'exécution de la session précédente sont effacées, évitant ainsi les conflits et les états invalides. C'est un excellent exemple de la philosophie Linux de "tout est fichier" appliqué aux données transitoires du système.
        """
        add_scrollable_text_to_content_frame("5. Répertoire /run (Données d'Exécution Volatiles)", run_text)

        # --- Tab 6: /proc ---
        proc_text = """
        ### Répertoire `/proc` : La Fenêtre sur le Noyau et les Processus

        Le répertoire **/proc** (abréviation de "processes") est sans doute l'un des répertoires les plus fascinants et les plus uniques de tout le système de fichiers Linux. Il ne s'agit pas d'un répertoire stocké sur un disque physique. Au lieu de cela, `/proc` est un **système de fichiers virtuel et pseudo-système de fichiers** généré et maintenu en temps réel par le **noyau Linux (kernel)** lui-même. C'est une interface dynamique qui permet aux programmes de l'espace utilisateur d'accéder à des informations détaillées sur les processus en cours d'exécution et sur l'état interne du noyau. Chaque "fichier" ou "répertoire" dans `/proc` est une représentation directe d'une structure de données ou d'une information du noyau.

        #### Structure et Contenu Essentiel de `/proc` :

        Le contenu de `/proc` est organisé de manière logique pour faciliter l'accès aux informations. Il est principalement constitué de :

        1.  **Répertoires Numériques (PID) : Une Vue sur Chaque Processus**
            * Pour **chaque processus en cours d'exécution** sur le système, le noyau crée un sous-répertoire numérique dans `/proc/` dont le nom est l'**ID de processus (PID)** du processus. Par exemple, si un processus a le PID `1234`, vous trouverez un répertoire `/proc/1234/`.
            * **Contenu typique de `/proc/<PID>/` :**
                * **`cmdline` :** Contient la ligne de commande complète (avec tous les arguments) qui a été utilisée pour lancer ce processus. Très utile pour comprendre comment un programme a été démarré.
                * **`exe` :** Un lien symbolique vers le chemin absolu du fichier exécutable qui a lancé ce processus.
                * **`cwd` :** Un lien symbolique vers le répertoire de travail actuel (Current Working Directory) du processus.
                * **`environ` :** Les variables d'environnement actives pour ce processus. Elles sont stockées sous forme de paires clé=valeur séparées par des zéros.
                * **`fd/` :** Un sous-répertoire crucial contenant des liens symboliques vers tous les **descripteurs de fichiers ouverts** par le processus. Chaque lien symbolique est le numéro du descripteur de fichier et pointe vers le fichier (ou socket, pipe) réel.
                * **`status` :** Fournit un résumé de l'état du processus, y compris son nom, son état d'exécution (Running, Sleeping, etc.), son PID, son UID/GID, l'utilisation de la mémoire, le nombre de threads, et bien plus encore.
                * **`maps` :** Affiche une carte des régions de mémoire mappées par le processus (bibliothèques partagées, segments de code, données, pile, tas). Utile pour le débogage et l'analyse de sécurité.
                * **`comm` :** Le nom du fichier exécutable du processus (peut être tronqué à 16 caractères).
                * **`io` :** Statistiques d'entrée/sortie pour le processus.

        2.  **Fichiers d'Informations sur le Noyau : Une Fenêtre sur le Système Global**
            * En plus des informations par processus, `/proc` contient de nombreux fichiers qui exposent des statistiques et des configurations globales du noyau et du matériel.
            * **Exemples Notables :**
                * **`/proc/cpuinfo` :** Informations détaillées sur tous les processeurs (cœurs, threads) du système, y compris leur modèle, leur vitesse, leurs fonctionnalités (`flags`) et leur cache.
                * **`/proc/meminfo` :** Des statistiques complètes sur l'utilisation de la mémoire physique et de la mémoire d'échange (swap), y compris la mémoire totale, libre, les buffers, le cache, et d'autres mesures.
                * **`/proc/version` :** Affiche la version complète du noyau Linux, y compris le numéro de version, la date de compilation et des informations sur le compilateur.
                * **`/proc/cmdline` :** La ligne de commande exacte qui a été passée au noyau au moment du démarrage. Très utile pour vérifier les options de démarrage.
                * **`/proc/filesystems` :** Liste de tous les systèmes de fichiers pris en charge par le noyau compilé (ext4, XFS, NTFS, overlayfs, etc.).
                * **`/proc/partitions` :** Des informations sur les périphériques de bloc et leurs partitions (nom, major/minor number, taille).
                * **`/proc/modules` :** Liste de tous les modules du noyau actuellement chargés, avec leur taille, leur nombre d'utilisations et les modules dont ils dépendent.
                * **`/proc/mounts` :** Une liste des systèmes de fichiers actuellement montés, similaire à la sortie de la commande `mount`, mais reflétant l'état actuel du noyau.

        3.  **Le Sous-répertoire `/proc/sys/` : Paramètres Dynamiques du Noyau**
            * C'est un sous-ensemble très spécial de `/proc`. Les fichiers dans `/proc/sys/` ne fournissent pas seulement des informations, ils permettent également de **lire et de modifier les paramètres du noyau (sysctl) à la volée**, sans nécessiter de redémarrage.
            * **Exemples :**
                * `/proc/sys/net/ipv4/ip_forward` : Active ou désactive le routage IP. Écrire `1` active le routage, `0` le désactive.
                * `/proc/sys/vm/swappiness` : Contrôle la propension du noyau à utiliser l'espace de swap.
                * `/proc/sys/kernel/hostname` : Permet de lire ou de définir le nom d'hôte du système en cours.
            * **Attention :** Modifier ces valeurs doit être fait avec une grande prudence. Les modifications sont perdues au redémarrage, à moins d'être rendues persistantes via `/etc/sysctl.conf` ou des fichiers dans `/etc/sysctl.d/`.

        #### Importance et Précautions :
        `/proc` est un outil de diagnostic et de monitoring inestimable. Les outils système comme `ps`, `top`, `free`, `uptime`, `lspci`, `ifconfig`, `netstat`, et bien d'autres, puisent une grande partie de leurs informations directement de `/proc`.

        Cependant, il est crucial de ne **jamais tenter de créer ou de supprimer des fichiers** dans `/proc` (sauf dans `/proc/sys/` où la lecture/écriture est permise pour les paramètres du noyau et uniquement si vous savez exactement ce que vous faites). Toute manipulation incorrecte peut entraîner une instabilité du système ou des pannes. C'est un système de fichiers que vous lisez pour comprendre, plutôt que de le modifier directement. C'est la boîte noire transparente de votre système Linux.
        """
        add_scrollable_text_to_content_frame("6. Répertoire /proc (Système de Fichiers Virtuel du Noyau)", proc_text)


        # --- Tab 7: Bonnes Pratiques et Synthèse ---
        best_practices_text = """
        ### Bonnes Pratiques et Synthèse : Maîtriser les Répertoires Linux

        Comprendre et gérer efficacement les répertoires `/var`, `/usr/share`, `/dev`, `/run`, et `/proc` est une compétence fondamentale pour tout utilisateur ou administrateur Linux. Bien qu'ils aient des rôles très différents, ils sont tous essentiels au bon fonctionnement, à la stabilité et à la sécurité de votre système. Voici un récapitulatif des bonnes pratiques à adopter pour chacun, ainsi qu'une synthèse de leur importance :

        #### Règles Générales pour tous les Répertoires :

        1.  **Respectez la FHS (Filesystem Hierarchy Standard) :** La FHS n'est pas une suggestion, c'est une norme. Elle garantit que les applications et les scripts s'attendent à trouver les fichiers à des emplacements prévisibles, ce qui rend les systèmes Linux cohérents et faciles à gérer entre différentes distributions.
        2.  **Comprenez les Permissions :** La sécurité dans Linux repose fortement sur les permissions de fichiers et de répertoires. Assurez-vous que seuls les utilisateurs et les processus autorisés ont les droits de lecture, d'écriture ou d'exécution nécessaires pour chaque répertoire et fichier. Une permission trop permissive est une vulnérabilité.
        3.  **Utilisez les Outils Appropriés :** Plutôt que de manipuler des fichiers à la main, utilisez les outils système fournis (par exemple, `logrotate` pour les journaux, `systemctl` pour les services, `sysctl` pour le noyau).

        #### Bonnes Pratiques Spécifiques par Répertoire :

        1.  **Pour `/var` (Données Variables) :**
            * **Surveillance de l'Espace Disque :** C'est le répertoire qui est le plus susceptible de consommer de l'espace disque. Utilisez régulièrement des commandes comme `df -h /var` et `du -sh /var/*` pour surveiller son utilisation, en particulier `/var/log` et `/var/lib`.
            * **Gestion des Logs :** Configurez `logrotate` pour archiver, compresser et purger les journaux de manière régulière. Ne supprimez jamais les fichiers de log manuellement sans savoir pourquoi ni sans avoir pris en compte les besoins d'audit ou de rétention.
            * **Sauvegardes :** Les données critiques de `/var` (bases de données dans `/var/lib`, fichiers web dans `/var/www`, configurations spécifiques dans certains sous-dossiers de `/var/opt`) doivent absolument être incluses dans votre stratégie de sauvegarde régulière.

        2.  **Pour `/usr/share` (Données Partagées Indépendantes de l'Architecture) :**
            * **Utilisation des Ressources :** C'est un répertoire de lecture. Vous n'êtes généralement pas censé y ajouter des fichiers manuellement. Les paquets logiciels se chargent de placer leurs ressources ici.
            * **Documentation :** Exploitez pleinement les ressources de documentation disponibles via `/usr/share/doc/` et les pages de manuel (`man commande`) pour comprendre le fonctionnement des logiciels installés. C'est une ressource sous-estimée.

        3.  **Pour `/dev` (Fichiers de Périphériques) :**
            * **Ne Jamais Manipuler Manuellement :** C'est la règle d'or absolue. `/dev` est un système de fichiers virtuel géré dynamiquement par le noyau et `udev`. La création, la suppression ou la modification manuelle de fichiers ici peut rendre votre système instable ou inutilisable.
            * **Comprendre les Types :** Familiarisez-vous avec la distinction entre les périphériques caractère (`c`) et bloc (`b`) pour mieux comprendre comment les programmes interagissent avec le matériel.
            * **Sécurité des Permissions :** Soyez conscient que les permissions sur les fichiers de `/dev` sont cruciales pour la sécurité. Une mauvaise configuration pourrait permettre un accès non autorisé à des ressources matérielles.

        4.  **Pour `/run` (Données d'Exécution Volatiles) :**
            * **Nature Volatile :** Gardez toujours à l'esprit que le contenu de `/run` est effacé à chaque redémarrage. N'y stockez aucune donnée qui doit persister. C'est sa raison d'être.
            * **Dépannage Temporaire :** Peut être utile pour vérifier les fichiers PID ou les sockets de services temporaires lors du dépannage de problèmes de démarrage ou de communication inter-processus.

        5.  **Pour `/proc` (Système de Fichiers Virtuel du Noyau) :**
            * **Outil de Diagnostic Inestimable :** Utilisez `/proc` pour obtenir des informations en temps réel sur l'état du système, les processus, l'utilisation des ressources (CPU, mémoire), l'état du réseau, etc. Les outils comme `top`, `ps`, `free`, `netstat` en dépendent fortement.
            * **Modification des Paramètres du Noyau :** Bien que la plupart des fichiers soient en lecture seule, certains dans `/proc/sys/` peuvent être modifiés pour ajuster les paramètres du noyau à la volée. Faites-le avec extrême prudence et utilisez `sysctl -w` pour plus de sécurité. Pour des changements persistants, configurez `/etc/sysctl.conf` ou `/etc/sysctl.d/`.
            * **Ne pas créer/supprimer :** Comme pour `/dev`, ne créez ou ne supprimez jamais de fichiers arbitrairement dans `/proc`.

        En conclusion, ces cinq répertoires forment une partie essentielle du fonctionnement interne de Linux. En les comprenant bien, vous ne vous contentez pas de naviguer dans le système de fichiers ; vous en comprenez le flux de vie, les interactions entre le matériel, le noyau, les processus et les applications. C'est une étape clé pour devenir un utilisateur Linux plus compétent et un administrateur plus confiant. Continuez à explorer et à apprendre !
        """
        add_scrollable_text_to_content_frame("7. Bonnes Pratiques et Synthèse", best_practices_text)

if __name__ == "__main__":
    app = LinuxDirsApp()
    app.mainloop()