import customtkinter as ctk

class RpmRepoConfigApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Configuration des Dépôts RPM (DNF/YUM)")
        self.geometry("1100x750")

        # Configure grid layout for the main window (1 row, 2 columns)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Vertical Navigation Frame (Navbar) ---
        self.navigation_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame,
                                                    text="Dépôts RPM",
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
        self.select_frame_by_name("1. Introduction aux Dépôts RPM")

    def create_navigation_buttons(self):
        button_info = [
            ("1. Introduction aux Dépôts RPM", 1),
            ("2. Fichiers de Configuration (.repo)", 2),
            ("3. Paramètres Essentiels", 3),
            ("4. Gestion avec DNF/YUM", 4),
            ("5. Dépôts Communs (EPEL, RPM Fusion)", 5),
            ("6. Créer un Dépôt Local", 6),
            ("7. Signatures GPG & Sécurité", 7),
            ("8. Dépannage Courant", 8),
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

        # --- Tab 1: Introduction aux Dépôts RPM ---
        intro_text = """
        ### Introduction aux Dépôts RPM (DNF/YUM)

        Les systèmes d'exploitation Linux basés sur RPM (comme Red Hat Enterprise Linux, CentOS, Fedora, AlmaLinux, Rocky Linux) utilisent des **dépôts de paquets** pour organiser et distribuer les logiciels.

        **Qu'est-ce qu'un Dépôt RPM ?**
        Un dépôt RPM est un emplacement centralisé (local ou distant via HTTP/HTTPS, FTP, ou même un chemin de fichier local) qui stocke des paquets logiciels au format `.rpm` ainsi que des **métadonnées**. Ces métadonnées contiennent des informations sur les paquets (dépendances, versions, descriptions, etc.) et sont utilisées par les outils de gestion de paquets.

        **Rôle des Outils de Gestion de Paquets (DNF / YUM) :**
        -   **DNF (Dandified YUM) :** Le gestionnaire de paquets par défaut sur les versions récentes de Fedora, RHEL 8+, AlmaLinux, Rocky Linux. C'est le successeur de YUM.
        -   **YUM (Yellowdog Updater, Modified) :** Le gestionnaire de paquets traditionnel sur les versions plus anciennes de RHEL/CentOS 7 et antérieures.

        Ces outils utilisent les fichiers de configuration des dépôts pour :
        -   Rechercher des paquets.
        -   Résoudre les dépendances.
        -   Installer, mettre à jour, et supprimer des paquets.
        -   Vérifier l'intégrité des paquets via les signatures GPG.

        **Pourquoi les Dépôts sont-ils Essentiels ?**
        -   **Facilité d'Installation :** Simplifie l'installation de logiciels et de leurs dépendances.
        -   **Mises à Jour Cohérentes :** Permet de maintenir le système à jour et stable.
        -   **Sécurité :** Les paquets sont souvent signés cryptographiquement, garantissant leur authenticité.
        -   **Gestion des Dépendances :** DNF/YUM résolvent automatiquement les dépendances entre les paquets.
        """
        add_scrollable_text_to_content_frame("1. Introduction aux Dépôts RPM", intro_text)

        # --- Tab 2: Fichiers de Configuration (.repo) ---
        config_files_text = """
        ### Fichiers de Configuration des Dépôts (.repo)

        Les dépôts RPM sont définis dans des fichiers de configuration avec l'extension `.repo`.

        #### Emplacement Standard :
        Tous les fichiers de configuration des dépôts sont stockés dans le répertoire :
        **`/etc/yum.repos.d/`**

        Chaque fichier `.repo` définit généralement un ou plusieurs dépôts. Le nom du fichier n'a pas d'importance pour DNF/YUM, seule l'extension `.repo` est reconnue. Par exemple, `my-custom-repo.repo`.

        #### Structure d'un Fichier `.repo` :
        Un fichier `.repo` est un fichier texte simple au format INI. Chaque section (`[repo_id]`) représente un dépôt individuel.

        **Exemple :**
        ```ini
        [baseos]
        name=Red Hat Enterprise Linux 8 - BaseOS
        # Chemin vers l'AppStream pour RHEL/AlmaLinux/Rocky
        baseurl=[http://mirror.centos.org/centos/8/BaseOS/$basearch/os/](http://mirror.centos.org/centos/8/BaseOS/$basearch/os/)
        # ou pour un serveur local:
        # baseurl=file:///mnt/iso/BaseOS/

        enabled=1
        gpgcheck=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-8

        [epel]
        name=Extra Packages for Enterprise Linux $releasever - $basearch
        # mirrors.fedoraproject.org gère les miroirs pour EPEL
        metalink=[https://mirrors.fedoraproject.org/metalink?repo=epel-$releasever&arch=$basearch&infra=$infra&content=$contentdir](https://mirrors.fedoraproject.org/metalink?repo=epel-$releasever&arch=$basearch&infra=$infra&content=$contentdir)
        # Ou un baseurl direct si vous connaissez le miroir
        # baseurl=[https://download.fedoraproject.org/pub/epel/$releasever/Everything/$basearch/](https://download.fedoraproject.org/pub/epel/$releasever/Everything/$basearch/)

        enabled=1
        gpgcheck=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-$releasever
        ```

        #### Ordre de Priorité :
        DNF/YUM considèrent tous les fichiers `.repo` activés. Il n'y a pas d'ordre de priorité strict basé sur le nom du fichier comme avec Polkit. La priorité est gérée par le paramètre `priority` (voir le prochain onglet).

        #### Édition :
        Vous pouvez modifier ces fichiers avec n'importe quel éditeur de texte (par exemple, `sudo vi /etc/yum.repos.d/myrepo.repo`). Après modification, les changements sont immédiatement pris en compte par DNF/YUM. Il est souvent recommandé d'exécuter `sudo dnf clean all` ou `sudo yum clean all` pour rafraîchir le cache des métadonnées, bien que ce ne soit pas toujours strictement nécessaire.
        """
        add_scrollable_text_to_content_frame("2. Fichiers de Configuration (.repo)", config_files_text)

        # --- Tab 3: Paramètres Essentiels ---
        essential_params_text = """
        ### Paramètres Essentiels dans un Fichier `.repo`

        Chaque section de dépôt (`[repo_id]`) dans un fichier `.repo` peut contenir plusieurs directives. Voici les plus importantes :

        1.  **`id_du_dépôt` (Ex: `[epel]`) :**
            -   Le nom unique du dépôt, utilisé par DNF/YUM pour l'identifier. Doit être unique.

        2.  **`name` :**
            -   Une description lisible du dépôt. Utile pour l'affichage dans les messages de DNF/YUM.
            -   Ex: `name=Extra Packages for Enterprise Linux $releasever - $basearch`
            -   Variables comme `$releasever`, `$basearch` sont automatiquement remplacées (voir ci-dessous).

        3.  **`baseurl` :**
            -   L'URL directe où se trouvent les paquets et les métadonnées du dépôt.
            -   Peut être HTTP/HTTPS, FTP, ou un chemin local (`file:///`).
            -   Ex: `baseurl=http://mirror.centos.org/centos/8/BaseOS/$basearch/os/`
            -   **Attention :** Si vous utilisez `baseurl`, assurez-vous qu'il pointe vers le répertoire racine du dépôt où se trouve le sous-répertoire `repodata/`.

        4.  **`metalink` / `mirrorlist` :**
            -   Une alternative à `baseurl`. Indique une URL qui contient une liste de miroirs valides pour le dépôt. Le gestionnaire de paquets choisira automatiquement le meilleur miroir.
            -   `metalink` est plus moderne et préféré.
            -   Ex: `metalink=https://mirrors.fedoraproject.org/metalink?repo=epel-$releasever&arch=$basearch&infra=$infra&content=$contentdir`
            -   Utilisez `metalink` OU `baseurl`, pas les deux.

        5.  **`enabled` :**
            -   `1` ou `0`. Indique si le dépôt est activé (`1`) ou désactivé (`0`).
            -   Utile pour désactiver temporairement un dépôt sans supprimer le fichier.
            -   Ex: `enabled=1`

        6.  **`gpgcheck` :**
            -   `1` ou `0`. Indique si DNF/YUM doit vérifier la signature GPG des paquets provenant de ce dépôt.
            -   **Fortement recommandé d'être à `1` pour la sécurité !**
            -   Ex: `gpgcheck=1`

        7.  **`gpgkey` :**
            -   L'URL ou le chemin local vers la clé publique GPG utilisée pour vérifier les signatures.
            -   Ex: `gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-8`
            -   Les clés sont souvent importées dans le système avec `rpm --import`.

        8.  **`priority` (déprécié dans DNF, remplacé par `module_hotfixes` et gestion des versions) :**
            -   Un entier (1-99) indiquant la priorité du dépôt. Un nombre plus petit signifie une priorité plus élevée.
            -   Utilisé par YUM. DNF gère mieux les dépendances et les versions de modules, rendant `priority` moins pertinent, mais il peut toujours être utilisé via le plugin `dnf-plugins-core` (installable via `sudo dnf install dnf-plugins-core`).

        9.  **`exclude` / `includepkgs` :**
            -   Permet d'exclure ou d'inclure des paquets spécifiques (supporte les jokers `*`).
            -   `exclude=httpd*,nginx*` (exclut tous les paquets commençant par httpd ou nginx de ce dépôt).
            -   `includepkgs=kernel*` (inclut seulement les paquets commençant par kernel).

        #### Variables Communes :
        DNF/YUM remplacent automatiquement ces variables :
        -   `$releasever` : La version de la distribution (ex: `8` pour RHEL 8, `39` pour Fedora 39).
        -   `$basearch` : L'architecture de base du système (ex: `x86_64`).
        -   `$arch` : L'architecture de la machine (peut être différente de `$basearch`).
        -   `$uuid` : L'UUID de l'installation (rarement utilisé dans les dépôts publics).
        """
        add_scrollable_text_to_content_frame("3. Paramètres Essentiels", essential_params_text)

        # --- Tab 4: Gestion avec DNF/YUM ---
        management_text = """
        ### Gestion des Dépôts et des Paquets avec DNF / YUM

        Ces commandes vous permettent d'interagir avec les dépôts et de gérer les paquets.

        #### Commandes DNF (pour RHEL 8+, Fedora, AlmaLinux, Rocky Linux) :

        -   **Lister les dépôts activés :**
            `sudo dnf repolist`
            `sudo dnf repolist enabled`

        -   **Lister TOUS les dépôts (activés et désactivés) :**
            `sudo dnf repolist all`

        -   **Vérifier le cache des dépôts (télécharge les métadonnées) :**
            `sudo dnf makecache`

        -   **Nettoyer le cache des dépôts :**
            `sudo dnf clean all` (Nettoie toutes les métadonnées et paquets mis en cache)

        -   **Activer temporairement un dépôt désactivé pour une commande :**
            `sudo dnf --enablerepo=epel install <paquet>`
            `sudo dnf --enablerepo=epel update`

        -   **Désactiver temporairement un dépôt pour une commande :**
            `sudo dnf --disablerepo=repo_id install <paquet>`

        -   **Rechercher un paquet :**
            `sudo dnf search <nom_paquet>`

        -   **Obtenir des informations sur un paquet :**
            `sudo dnf info <nom_paquet>`

        -   **Installer un paquet :**
            `sudo dnf install <nom_paquet>`

        -   **Mettre à jour tous les paquets du système :**
            `sudo dnf update`

        -   **Supprimer un paquet :**
            `sudo dnf remove <nom_paquet>`

        -   **Installer un paquet RPM local :**
            `sudo dnf install /chemin/vers/mon_paquet.rpm`
            (DNF résoudra les dépendances manquantes des dépôts activés)

        #### Commandes YUM (pour RHEL 7 et versions antérieures, CentOS 7 et antérieures) :
        La plupart des commandes sont similaires à DNF, remplacez simplement `dnf` par `yum`.

        -   `sudo yum repolist`
        -   `sudo yum clean all`
        -   `sudo yum --enablerepo=epel install <paquet>`
        -   `sudo yum search <nom_paquet>`
        -   `sudo yum install <nom_paquet>`
        -   `sudo yum update`
        -   `sudo yum remove <nom_paquet>`
        """
        add_scrollable_text_to_content_frame("4. Gestion avec DNF/YUM", management_text)

        # --- Tab 5: Dépôts Communs (EPEL, RPM Fusion) ---
        common_repos_text = """
        ### Dépôts Communs et Essentiels

        Sur les systèmes basés sur RHEL, certains dépôts tiers sont presque indispensables pour accéder à une plus grande variété de logiciels.

        #### 1. EPEL (Extra Packages for Enterprise Linux) :
        -   **Objectif :** Fournit un ensemble de paquets supplémentaires de haute qualité pour les distributions Enterprise Linux (RHEL, CentOS, AlmaLinux, Rocky Linux) qui ne sont pas incluses dans les dépôts officiels.
        -   **Pourquoi l'utiliser :** Accès à de nombreux outils système, utilitaires, et applications qui améliorent la fonctionnalité du système sans compromettre la stabilité.
        -   **Installation :**
            `sudo dnf install epel-release` (pour DNF)
            `sudo yum install epel-release` (pour YUM)
            Cette commande télécharge et installe le fichier `.repo` pour EPEL dans `/etc/yum.repos.d/`.

        #### 2. RPM Fusion :
        -   **Objectif :** Fournit des paquets qui ne peuvent pas être inclus dans Fedora ou RHEL (y compris leurs clones) pour des raisons légales (ex: brevets) ou de licence (ex: logiciels non-libres).
        -   **Catégories :**
            -   **`free` :** Logiciels open-source qui ne peuvent pas être distribués avec Fedora/RHEL pour d'autres raisons (ex: brevets logiciels dans certains pays).
            -   **`nonfree` :** Logiciels propriétaires (ex: pilotes graphiques Nvidia, codecs multimédia propriétaires).
        -   **Pourquoi l'utiliser :** Essentiel pour la lecture de certains formats multimédia, les jeux, et l'utilisation de certains matériels propriétaires.
        -   **Installation (exemple pour Fedora/RHEL) :**
            Pour RPM Fusion Free :
            `sudo dnf install "https://download1.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm"` (pour RHEL/Alma/Rocky)
            `sudo dnf install "https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm"` (pour Fedora)

            Pour RPM Fusion Nonfree (si nécessaire) :
            `sudo dnf install "https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm"`
            `sudo dnf install "https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm"`

            Ces commandes installent les fichiers `.repo` correspondants.

        #### Autres Dépôts :
        De nombreuses applications tierces fournissent également leurs propres dépôts (ex: Google Chrome, Docker, VirtualBox). Installez-les uniquement si vous faites confiance à la source et comprenez les implications. Vérifiez toujours la configuration GPG.
        """
        add_scrollable_text_to_content_frame("5. Dépôts Communs (EPEL, RPM Fusion)", common_repos_text)

        # --- Tab 6: Créer un Dépôt Local ---
        local_repo_text = """
        ### Créer et Gérer un Dépôt RPM Local

        Il est parfois utile de créer un dépôt RPM local, par exemple pour :
        -   Déployer des applications internes non disponibles publiquement.
        -   Gérer des environnements hors ligne ou avec une bande passante limitée.
        -   Assurer la cohérence des paquets sur plusieurs systèmes.

        #### Étapes pour Créer un Dépôt Local :

        1.  **Installer `createrepo` (ou `createrepo_c`) :**
            Cet outil est nécessaire pour générer les métadonnées du dépôt.
            `sudo dnf install createrepo_c` (recommandé pour les systèmes modernes)
            ou
            `sudo dnf install createrepo` (pour les systèmes plus anciens)

        2.  **Préparer le Répertoire du Dépôt :**
            Créez un répertoire où vous stockerez vos paquets RPM.
            `sudo mkdir -p /var/www/html/myrepo` (si vous voulez le servir via HTTP)
            `sudo cp /chemin/vers/vos_paquets/*.rpm /var/www/html/myrepo/`

        3.  **Générer les Métadonnées du Dépôt :**
            Naviguez vers le répertoire du dépôt et exécutez `createrepo_c`.
            `cd /var/www/html/myrepo`
            `sudo createrepo_c .`
            Cela créera un sous-répertoire `repodata/` contenant les fichiers de métadonnées XML.

        4.  **Mettre à Jour le Dépôt :**
            Lorsque vous ajoutez de nouveaux paquets ou en supprimez, vous devez régénérer les métadonnées.
            `sudo createrepo_c --update .` (met à jour uniquement les métadonnées pour les paquets modifiés/ajoutés)

        #### Servir le Dépôt Local :

        Vous pouvez servir le dépôt de plusieurs manières :

        1.  **Via le Système de Fichiers Local :**
            Utile pour un seul système ou des clés USB.
            Fichier `.repo` :
            ```ini
            [my_local_repo]
            name=Mon Dépôt Local
            baseurl=file:///var/www/html/myrepo
            enabled=1
            gpgcheck=0  # Ou 1 si vous signez vos propres paquets
            ```

        2.  **Via HTTP (Serveur Web comme Apache ou Nginx) :**
            Idéal pour partager le dépôt sur un réseau.
            -   Assurez-vous qu'un serveur web est installé et en cours d'exécution (ex: `sudo dnf install httpd`).
            -   Configurez votre serveur web pour servir le répertoire `/var/www/html/myrepo`.
            -   Assurez-vous que le pare-feu autorise le trafic HTTP/HTTPS.

            Fichier `.repo` :
            ```ini
            [my_http_repo]
            name=Mon Dépôt HTTP
            baseurl=http://votre_ip_ou_hostname/myrepo
            enabled=1
            gpgcheck=0 # Ou 1 si vous signez vos propres paquets
            ```

        #### Signatures GPG pour les Dépôts Locaux :
        Pour une sécurité maximale, vous devriez **signer vos propres paquets RPM** et le dépôt lui-même.
        1.  Créez votre propre clé GPG.
        2.  Signez vos paquets RPM avec cette clé.
        3.  Exportez votre clé publique et placez-la dans un endroit accessible (ex: `/etc/pki/rpm-gpg/`).
        4.  Définissez `gpgcheck=1` et `gpgkey=file:///etc/pki/rpm-gpg/MA-CLE-GPG-PUBLIQUE` dans votre fichier `.repo`.
        """
        add_scrollable_text_to_content_frame("6. Créer un Dépôt Local", local_repo_text)

        # --- Tab 7: Signatures GPG & Sécurité ---
        gpg_security_text = """
        ### Signatures GPG et Sécurité des Dépôts RPM

        La vérification des signatures GPG est une fonctionnalité de sécurité cruciale pour s'assurer que les paquets que vous installez sont authentiques et n'ont pas été altérés.

        #### Pourquoi GPG ?
        -   **Authenticité :** Confirme que le paquet provient de la source déclarée (le développeur ou le dépôt officiel).
        -   **Intégrité :** Garantit que le paquet n'a pas été modifié ou corrompu depuis qu'il a été signé.

        #### Comment ça Fonctionne :
        1.  Les développeurs/mainteneurs de paquets utilisent une **clé privée GPG** pour signer les paquets RPM.
        2.  La **clé publique GPG** correspondante est mise à disposition (souvent sur les serveurs de clés ou fournie avec le dépôt lui-même).
        3.  Votre système importe cette clé publique.
        4.  Lorsque DNF/YUM télécharge un paquet, il utilise la clé publique importée pour vérifier la signature apposée sur le paquet.

        #### Fichiers de Clés GPG :
        Les clés GPG pour les dépôts sont généralement stockées dans :
        **`/etc/pki/rpm-gpg/`**

        #### Paramètres `gpgcheck` et `gpgkey` :

        -   **`gpgcheck=1` :** Ce paramètre (dans le fichier `.repo`) indique à DNF/YUM de **toujours** vérifier la signature GPG des paquets provenant de ce dépôt. C'est le réglage le plus sûr et **fortement recommandé**.
        -   **`gpgkey=file:///chemin/vers/la/cle/publique.gpg` :** Spécifie l'emplacement de la clé publique GPG à utiliser pour la vérification.

        **Exemple :**
        ```ini
        [my_secure_repo]
        name=Mon Dépôt Sécurisé
        baseurl=[https://mon.serveur.com/repo](https://mon.serveur.com/repo)
        enabled=1
        gpgcheck=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-MonRepo
        ```

        #### Importer une Clé GPG Manuellement :

        Si un dépôt ne fournit pas automatiquement sa clé via un paquet `*-release`, vous devrez l'importer manuellement :

        1.  **Téléchargez la clé :**
            `wget https://example.com/RPM-GPG-KEY-MonRepo`
        2.  **Importez la clé :**
            `sudo rpm --import RPM-GPG-KEY-MonRepo`
            (Cette commande ajoute la clé au trousseau GPG de RPM.)
        3.  **Déplacez la clé (optionnel mais recommandé pour la persistance) :**
            `sudo mv RPM-GPG-KEY-MonRepo /etc/pki/rpm-gpg/`
            Puis mettez à jour le chemin dans votre fichier `.repo`.

        #### Désactivation de `gpgcheck` (À ÉVITER !) :
        Définir `gpgcheck=0` dans un dépôt désactive la vérification de signature. **C'est une pratique dangereuse** qui expose votre système à des paquets falsifiés ou corrompus. Ne faites cela que si vous êtes absolument certain de la source, et même dans ce cas, c'est un risque.

        **Message d'Avertissement :**
        Si vous tentez d'installer un paquet sans clé GPG importée et que `gpgcheck=1`, DNF/YUM vous demandera d'importer la clé. Acceptez uniquement si vous avez vérifié l'empreinte digitale de la clé auprès d'une source fiable.
        """
        add_scrollable_text_to_content_frame("7. Signatures GPG & Sécurité", gpg_security_text)

        # --- Tab 8: Dépannage Courant ---
        troubleshooting_text = """
        ### Dépannage Courant des Dépôts RPM

        Voici quelques problèmes courants que vous pourriez rencontrer avec les dépôts DNF/YUM et comment les résoudre.

        #### 1. "Error: Failed to download metadata for repo '<repo_id>': Cannot download repomd.xml"

        **Cause :** Le gestionnaire de paquets n'arrive pas à accéder aux métadonnées du dépôt.
        **Solutions :**
        -   **Vérifiez l'URL du `baseurl` ou `metalink` :** Assurez-vous qu'elle est correcte et accessible (pas d'erreur de frappe).
        -   **Connectivité réseau :** Vérifiez votre connexion Internet.
        -   **Pare-feu :** Assurez-vous que le pare-feu du serveur ou du client ne bloque pas l'accès au dépôt (ports 80/443 pour HTTP/HTTPS).
        -   **Problème côté dépôt :** Le dépôt peut être temporairement hors ligne ou en maintenance. Essayez plus tard.
        -   **Nettoyez le cache :** `sudo dnf clean all` puis `sudo dnf update`.

        #### 2. "Public key for <package>.rpm is not installed" ou "GPG check FAILED"

        **Cause :** La clé GPG requise pour vérifier la signature des paquets n'est pas importée ou est incorrecte.
        **Solutions :**
        -   **Importez la clé GPG :** Trouvez la clé publique GPG fournie par le dépôt (souvent indiquée dans le fichier `.repo` avec `gpgkey=`) et importez-la : `sudo rpm --import /chemin/vers/la/clé.gpg`.
        -   **Vérifiez le chemin `gpgkey` :** Assurez-vous que le chemin spécifié dans le fichier `.repo` est correct.
        -   **Méfiance :** Si vous n'êtes pas certain de la source de la clé, ne l'importez pas. Il pourrait s'agir d'une attaque.

        #### 3. "No match for argument: <paquet>" ou "No package <paquet> available."

        **Cause :** Le paquet que vous essayez d'installer n'est pas trouvé dans les dépôts activés.
        **Solutions :**
        -   **Orthographe du paquet :** Vérifiez l'orthographe du nom du paquet.
        -   **Dépôt non activé :** Le paquet se trouve peut-être dans un dépôt désactivé. Utilisez `sudo dnf repolist all` pour voir tous les dépôts, puis activez-le temporairement (`--enablerepo`) ou de manière permanente (`enabled=1` dans le fichier `.repo`).
        -   **Dépôt manquant :** Le dépôt contenant le paquet n'est pas configuré sur votre système. Trouvez le dépôt approprié et ajoutez son fichier `.repo`.
        -   **Nom du paquet différent :** Le paquet peut avoir un nom différent sur votre distribution. Utilisez `sudo dnf search <mot_clé>` pour le trouver.

        #### 4. Conflits de Dépendances

        **Cause :** Deux paquets (souvent de dépôts différents) fournissent le même fichier ou ont des exigences contradictoires.
        **Solutions :**
        -   **Désactiver des dépôts :** Essayez de désactiver temporairement les dépôts tiers qui pourraient être en conflit avec les dépôts système (par exemple, `--disablerepo=rpmfusion-free`).
        -   **Vérifier les priorités :** Si le plugin `priority` est activé, ajustez les priorités des dépôts.
        -   **Exclure des paquets :** Utilisez le paramètre `exclude=` dans le fichier `.repo` pour empêcher un dépôt de fournir des paquets qui causent des conflits.
        -   **Contacter le support/la communauté :** Si les conflits sont persistants, cela peut indiquer un problème plus profond avec les paquets ou les dépôts.

        #### 5. Cache de Métadonnées Obsolet :
        **Cause :** Le cache local de DNF/YUM est ancien et ne reflète pas les dernières modifications des dépôts.
        **Solution :** `sudo dnf clean all` suivi de `sudo dnf update` ou `sudo dnf makecache`.
        """
        add_scrollable_text_to_content_frame("8. Dépannage Courant", troubleshooting_text)

        # --- Tab 9: Bonnes Pratiques ---
        best_practices_text = """
        ### Bonnes Pratiques pour la Gestion des Dépôts RPM

        Suivre ces bonnes pratiques vous aidera à maintenir un système stable, sécurisé et facile à gérer.

        1.  **Utilisez TOUJOURS `gpgcheck=1` :** C'est le paramètre de sécurité le plus important. Ne désactivez jamais la vérification GPG à moins d'avoir une raison impérieuse et de comprendre les risques de sécurité majeurs que cela implique.
        2.  **Utilisez `metalink` ou `mirrorlist` plutôt que `baseurl` :** Si disponible, cela permet à DNF/YUM de choisir le miroir le plus rapide et le plus fiable, et d'éviter les points de défaillance uniques.
        3.  **Installez uniquement les dépôts nécessaires :** Chaque dépôt supplémentaire augmente le risque de conflits de paquets et de vulnérabilités. N'activez que ce dont vous avez réellement besoin.
        4.  **Gardez les dépôts tiers au minimum :** Les dépôts non-officiels peuvent contenir des paquets qui ne sont pas testés de manière aussi approfondie avec votre distribution, ce qui peut entraîner des problèmes de stabilité ou de sécurité.
        5.  **Comprenez les priorités (si utilisées) :** Si vous activez le plugin `priority` de DNF ou utilisez un ancien YUM, assurez-vous de bien comprendre comment les priorités affectent la résolution des paquets. Généralement, les dépôts officiels ont une priorité plus élevée.
        6.  **Faites des sauvegardes :** Avant de modifier les fichiers `.repo` ou d'ajouter de nouveaux dépôts majeurs, faites une copie de sauvegarde de votre répertoire `/etc/yum.repos.d/`.
        7.  **Nettoyez régulièrement le cache :** `sudo dnf clean all` peut aider à résoudre les problèmes de métadonnées et à libérer de l'espace disque.
        8.  **Vérifiez les versions (`$releasever`, `$basearch`) :** Assurez-vous que les variables dans les `baseurl` ou `metalink` correspondent à votre version de distribution et à votre architecture pour éviter les problèmes de compatibilité des paquets.
        9.  **Lisez la documentation du dépôt :** Avant d'ajouter un nouveau dépôt, consultez la documentation officielle de ce dépôt. Elle contiendra souvent des instructions spécifiques et des avertissements.
        10. **Automatisation :** Pour la gestion de multiples systèmes, utilisez des outils d'automatisation (comme Ansible, Puppet, Chef) pour garantir une configuration cohérente des dépôts.
        """
        add_scrollable_text_to_content_frame("9. Bonnes Pratiques", best_practices_text)

if __name__ == "__main__":
    app = RpmRepoConfigApp()
    app.mainloop()