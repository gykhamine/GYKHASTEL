import customtkinter as ctk

class PolkitConfigApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Configuration de Polkit (PolicyKit)")
        self.geometry("1100x750")

        # Configure grid layout for the main window (1 row, 2 columns)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- Vertical Navigation Frame (Navbar) ---
        self.navigation_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(10, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame,
                                                    text="Polkit Guide",
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
        self.select_frame_by_name("1. Introduction à Polkit")

    def create_navigation_buttons(self):
        button_info = [
            ("1. Introduction à Polkit", 1),
            ("2. Concepts Clés", 2),
            ("3. Architecture de Polkit", 3),
            ("4. Fichiers de Règles (.rules)", 4),
            ("5. Fichiers d'Actions (.policy)", 5),
            ("6. Authentification et Implicit Auth", 6),
            ("7. Débogage et Audit", 7),
            ("8. Exemples Pratiques", 8),
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

        # --- Tab 1: Introduction à Polkit ---
        intro_text = """
        ### Introduction à Polkit (anciennement PolicyKit)

        **Qu'est-ce que Polkit ?**
        Polkit est un **système d'autorisation** qui permet aux applications non privilégiées d'interagir avec les services privilégiés du système de manière sécurisée. Contrairement à `sudo` qui exécute des commandes en tant que root, Polkit est conçu pour un contrôle d'accès plus **granulaire** et basé sur des **politiques** pour des actions spécifiques.

        Il ne s'agit pas d'un remplacement de `sudo`, mais plutôt d'un complément, particulièrement dans les environnements de bureau modernes et les systèmes de gestion de services.

        **Pourquoi Polkit est-il important ?**
        -   **Sécurité Granulaire :** Permet de définir des règles d'autorisation très spécifiques (par exemple, "seul l'utilisateur connecté peut éteindre l'ordinateur", ou "tout utilisateur du groupe 'admin' peut monter un système de fichiers").
        -   **Flexibilité :** Les règles peuvent être dynamiques et dépendre du contexte (qui est l'utilisateur, d'où vient la demande, etc.).
        -   **Interopérabilité :** Il est utilisé par de nombreux démons système et applications pour leurs besoins d'autorisation, par exemple UDisks2 (montage de périphériques), NetworkManager (gestion réseau), systemd (gestion de services).
        -   **Transparence :** Lorsque l'autorisation est requise, Polkit peut déclencher une boîte de dialogue graphique pour demander l'authentification de l'utilisateur.

        **Historique Bref :**
        Polkit a évolué depuis PolicyKit. Bien que le nom "PolicyKit" soit encore couramment utilisé, le projet est maintenant connu sous le nom de "Polkit".
        """
        add_scrollable_text_to_content_frame("1. Introduction à Polkit", intro_text)

        # --- Tab 2: Concepts Clés ---
        concepts_text = """
        ### Concepts Clés de Polkit

        Pour comprendre Polkit, il est essentiel de maîtriser quelques concepts fondamentaux :

        1.  **Actions (Actions)** :
            -   Une action représente une opération privilégiée spécifique qu'un programme peut vouloir exécuter.
            -   Chaque action a un nom unique (par exemple, `org.freedesktop.udisks2.mount`, `org.freedesktop.NetworkManager.settings.modify`).
            -   Les actions sont définies dans des fichiers **.policy** (XML).

        2.  **Identités (Identities)** :
            -   L'identité de l'entité qui tente d'exécuter une action. Cela peut être :
                -   Un utilisateur Unix (par exemple, `unix-user:john`).
                -   Un groupe Unix (par exemple, `unix-group:admin`).
                -   Le superutilisateur (`unix-user:root`).
                -   La session active (`active`).
                -   Une identité particulière pour les sessions graphiques (par exemple, `local-console`).

        3.  **Autorisation (Authorization)** :
            -   Le processus de décision si une identité est autorisée à effectuer une action spécifique.
            -   Polkit évalue les règles pour prendre cette décision.

        4.  **Règles d'Autorisation (Authorization Rules)** :
            -   Définissent les critères selon lesquels une action est autorisée ou non.
            -   Elles sont écrites en JavaScript et stockées dans des fichiers **.rules** (JavaScript).
            -   Les règles peuvent être temporaires (authentification requise) ou permanentes (toujours autorisée/refusée).

        5.  **Explicite vs. Implicite (Explicit vs. Implicit Authorization)** :
            -   **Implicit Authorization:** La décision est prise par les règles par défaut définies dans les fichiers .policy ou par les règles système générales.
            -   **Explicit Authorization:** La décision est prise par des règles personnalisées dans les fichiers .rules, qui peuvent outrepasser les règles implicites.

        6.  **Contexte (Context)** :
            -   La décision d'autorisation peut dépendre du contexte de la demande :
                -   L'identité de l'utilisateur.
                -   La session (locale, distante, console, graphique).
                -   Des détails spécifiques à l'action.

        Ensemble, ces concepts permettent à Polkit de fournir un cadre flexible et puissant pour la gestion des privilèges.
        """
        add_scrollable_text_to_content_frame("2. Concepts Clés", concepts_text)

        # --- Tab 3: Architecture de Polkit ---
        architecture_text = """
        ### Architecture de Polkit

        Polkit fonctionne comme un service D-Bus centralisé qui gère les demandes d'autorisation. Comprendre son architecture aide à situer les fichiers de configuration.

        #### Composants Principaux :

        1.  **Client (Application non privilégiée)** :
            -   Une application (par exemple, un gestionnaire de périphériques, un outil de configuration réseau) qui souhaite effectuer une opération privilégiée.
            -   Elle ne peut pas effectuer l'opération directement.
            -   Elle envoie une **requête d'autorisation** au démon Polkit via D-Bus.

        2.  **Démon Polkit (`polkitd`)** :
            -   Le cœur de Polkit, un service qui s'exécute en arrière-plan (souvent via systemd).
            -   Reçoit les requêtes d'autorisation des clients.
            -   Évalue la demande en fonction des fichiers de politique et des règles.
            -   Si nécessaire, il peut interagir avec un agent d'authentification pour demander le mot de passe de l'utilisateur.
            -   Renvoie une réponse (autorisé/refusé) au client.

        3.  **Agent d'Authentification (Authentication Agent)** :
            -   Une application graphique (ou console) qui est responsable de l'interface utilisateur pour la demande de mot de passe.
            -   Par exemple, `gnome-shell`, `kde-polkit-agent`, `lxqt-policykit-agent`.
            -   Le démon Polkit interagit avec cet agent lorsque l'authentification est requise pour une action.

        4.  **Backend Privilégié (Privileged Backend)** :
            -   Le service système réel qui effectue l'opération privilégiée (par exemple, `udisksd` pour le montage, `NetworkManager` pour les modifications réseau).
            -   Ce backend *lui-même* s'assure que le client a l'autorisation via Polkit *avant* d'exécuter l'action.

        #### Flux d'Autorisation Typique :

        1.  Un utilisateur tente de monter une clé USB via le gestionnaire de fichiers (client).
        2.  Le gestionnaire de fichiers envoie une demande d'autorisation (`org.freedesktop.udisks2.mount`) au démon `polkitd`.
        3.  `polkitd` évalue les règles :
            -   Il consulte les fichiers **.policy** pour voir les autorisations par défaut.
            -   Il consulte les fichiers **.rules** personnalisés pour des dérogations.
        4.  Si la politique requiert une authentification, `polkitd` envoie un message à l'agent d'authentification actif.
        5.  L'agent d'authentification affiche une boîte de dialogue de mot de passe à l'utilisateur.
        6.  Si l'utilisateur s'authentifie avec succès, l'agent informe `polkitd`.
        7.  `polkitd` répond au gestionnaire de fichiers (client) que l'action est autorisée.
        8.  Le gestionnaire de fichiers demande ensuite à `udisksd` (backend privilégié) de monter la clé USB.
        9.  `udisksd` effectue l'opération.

        Cette architecture assure que les privilèges ne sont accordés que lorsqu'ils sont nécessaires et autorisés par la politique système.
        """
        add_scrollable_text_to_content_frame("3. Architecture de Polkit", architecture_text)

        # --- Tab 4: Fichiers de Règles (.rules) ---
        rules_text = """
        ### Fichiers de Règles de Polkit (.rules)

        Les fichiers de règles sont le principal moyen de personnaliser le comportement d'autorisation de Polkit. Ils sont écrits en **JavaScript** et sont évalués par le démon `polkitd`.

        #### Emplacements des Fichiers de Règles :

        Les règles sont lues dans un ordre spécifique :
        -   `/etc/polkit-1/rules.d/` (pour les règles personnalisées des administrateurs - **priorité la plus élevée**)
        -   `/usr/share/polkit-1/rules.d/` (pour les règles par défaut fournies par les paquets - **priorité plus faible**)

        Les fichiers sont lus par ordre alphabétique. Une règle définie dans un fichier avec un nom lexicographiquement plus grand (par exemple `90-my-custom-rules.rules`) prévaut sur une règle définie dans un fichier avec un nom plus petit (par exemple `50-default-rules.rules`).

        #### Structure d'un Fichier de Règles Exemple (`.rules`) :

        ```javascript
        /*
         * Fichier : /etc/polkit-1/rules.d/50-my-custom-rules.rules
         * Description : Autorisations personnalisées pour Polkit
         */

        polkit.addRule(function(action, subject) {
            // Règle 1 : Autoriser tous les utilisateurs du groupe 'admin' à monter des systèmes de fichiers
            if (action.id == "org.freedesktop.udisks2.mount-filesystem" &&
                subject.isInGroup("admin")) {
                return polkit.Result.YES; // Autoriser sans mot de passe
            }

            // Règle 2 : Demander une authentification pour éteindre le système si l'utilisateur n'est pas actif
            if (action.id == "org.freedesktop.login1.power-off" &&
                !subject.active) { // Si l'utilisateur n'est pas actif (par exemple, via SSH)
                return polkit.Result.AUTH_ADMIN_REQUIRED; // Demander mot de passe administrateur
            }

            // Règle 3 : Refuser à l'utilisateur 'guest' d'installer des paquets Flatpak
            if (action.id == "org.freedesktop.Flatpak.install" &&
                subject.user == "guest") {
                return polkit.Result.NO; // Refuser
            }

            // Règle par défaut : laisser Polkit décider si aucune des règles ci-dessus ne correspond
            return polkit.Result.NOT_HANDLED;
        });
        ```

        #### Explication des Éléments Clés en JavaScript :

        -   `polkit.addRule(function(action, subject) { ... });`: Définit une nouvelle règle.
        -   `action`: Objet représentant l'action demandée (par exemple, `action.id` pour le nom de l'action).
        -   `subject`: Objet représentant l'identité qui effectue la demande (par exemple, `subject.user` pour le nom d'utilisateur, `subject.isInGroup("groupname")`, `subject.active` pour vérifier si l'utilisateur est dans une session locale active).
        -   `polkit.Result`:
            -   `polkit.Result.YES`: Autorise l'action sans authentification.
            -   `polkit.Result.NO`: Refuse l'action.
            -   `polkit.Result.AUTH_REQUIRED`: Demande l'authentification de l'utilisateur courant.
            -   `polkit.Result.AUTH_ADMIN_REQUIRED`: Demande l'authentification de l'administrateur.
            -   `polkit.Result.NOT_HANDLED`: La règle ne prend pas de décision ; Polkit passera à la règle suivante ou à la politique par défaut.

        #### Bonnes Pratiques :
        -   Toujours utiliser l'extension `.rules`.
        -   Nommer les fichiers de manière à contrôler l'ordre d'évaluation (ex: `10-my-policy.rules`, `90-override.rules`).
        -   Utiliser `polkit.Result.NOT_HANDLED` si votre règle n'est pas censée prendre une décision pour une action donnée, permettant à d'autres règles de s'appliquer.
        """
        add_scrollable_text_to_content_frame("4. Fichiers de Règles (.rules)", rules_text)

        # --- Tab 5: Fichiers d'Actions (.policy) ---
        policy_text = """
        ### Fichiers d'Actions de Polkit (.policy)

        Les fichiers `.policy` définissent les actions que Polkit peut gérer et les comportements d'autorisation par défaut pour ces actions. Ils sont écrits en **XML**.

        #### Emplacements des Fichiers d'Actions :

        -   `/usr/share/polkit-1/actions/` (emplacement standard pour les paquets, **ne pas modifier manuellement**).
        -   Ces fichiers sont généralement fournis par les applications ou les démons système qui utilisent Polkit.

        #### Structure d'un Fichier d'Actions Exemple (`.policy`) :

        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE policyconfig PUBLIC
         "-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
         "[http://www.freedesktop.org/software/polkit/policyconfig-1.0.dtd](http://www.freedesktop.org/software/polkit/policyconfig-1.0.dtd)">
        <policyconfig>
          <action id="org.freedesktop.udisks2.mount-filesystem">
            <description>Mount a filesystem</description>
            <message>Authentication is required to mount the filesystem</message>
            <defaults>
              <allow_any>no</allow_any>
              <allow_inactive>no</allow_inactive>
              <allow_active>yes</allow_active>
            </defaults>
            <annotate key="org.freedesktop.policykit.exec.path">/usr/bin/udisksctl</annotate>
          </action>

          <action id="org.freedesktop.login1.power-off">
            <description>Power off the system</description>
            <message>Authentication is required to power off the system</message>
            <defaults>
              <allow_any>auth_admin_keep</allow_any>
              <allow_inactive>auth_admin_keep</allow_inactive>
              <allow_active>yes</allow_active>
            </defaults>
          </action>
        </policyconfig>
        ```

        #### Explication des Éléments Clés en XML :

        -   `<policyconfig>`: Élément racine.
        -   `<action id="...">`: Définit une action unique par son ID. C'est cet ID qui est utilisé dans les fichiers `.rules`.
        -   `<description>`: Description lisible de l'action.
        -   `<message>`: Message affiché à l'utilisateur si l'authentification est requise.
        -   `<defaults>`: Définit le comportement par défaut de l'action si aucune règle `.rules` ne s'applique.
            -   `<allow_any>`: Comportement pour toute session.
            -   `<allow_inactive>`: Comportement pour les sessions inactives (par exemple, via SSH).
            -   `<allow_active>`: Comportement pour les sessions actives (généralement la session graphique locale).
        -   Valeurs possibles pour `allow_any`, `allow_inactive`, `allow_active` :
            -   `yes`: Autorisé sans authentification.
            -   `no`: Refusé.
            -   `auth_self`: Demande le mot de passe de l'utilisateur courant.
            -   `auth_self_keep`: Demande le mot de passe de l'utilisateur courant, et la session est gardée authentifiée pour de futures actions.
            -   `auth_admin`: Demande le mot de passe de l'administrateur (root ou un utilisateur du groupe `wheel`/`sudo`).
            -   `auth_admin_keep`: Demande le mot de passe de l'administrateur, et la session est gardée authentifiée pour de futures actions.
        -   `<annotate key="...">`: Métadonnées supplémentaires sur l'action, par exemple, le chemin du binaire (`org.freedesktop.policykit.exec.path`).

        #### Quand utiliser `.policy` vs `.rules` :
        -   **`.policy` :** Définit ce qu'une action est et son comportement par défaut. C'est le domaine des développeurs d'applications et de services. Vous ne devez pas les modifier manuellement, car ils seraient écrasés lors des mises à jour du système.
        -   **`.rules` :** Permet aux administrateurs de surcharger ou d'ajouter des règles d'autorisation personnalisées. C'est l'endroit où vous mettez vos configurations spécifiques au système.
        """
        add_scrollable_text_to_content_frame("5. Fichiers d'Actions (.policy)", policy_text)

        # --- Tab 6: Authentification et Implicit Auth ---
        auth_implicit_text = """
        ### Authentification et Autorisation Implicite

        Polkit gère différentes exigences d'authentification et un concept d'autorisation implicite basé sur le contexte.

        #### Types d'Authentification :

        Lorsqu'une règle Polkit demande une authentification, il y a plusieurs niveaux :

        1.  **`auth_self` / `auth_self_keep`**:
            -   Requiert l'authentification de l'utilisateur qui a initié la demande.
            -   `auth_self_keep` garde l'authentification valide pour une période (souvent 5 minutes par défaut) pour d'autres actions nécessitant `auth_self`.

        2.  **`auth_admin` / `auth_admin_keep`**:
            -   Requiert l'authentification d'un administrateur (utilisateur `root` ou membre d'un groupe sudo/wheel).
            -   `auth_admin_keep` garde l'authentification valide.

        Quand une authentification est requise, l'agent Polkit (par exemple, une fenêtre de mot de passe graphique) s'affiche pour l'utilisateur.

        #### Autorisation Implicite :

        L'autorisation implicite fait référence au comportement par défaut défini dans les fichiers `.policy` (les fichiers XML). C'est la décision que Polkit prendra si aucune règle dans les fichiers `.rules` ne prend une décision (`polkit.Result.NOT_HANDLED`).

        Les attributs `<allow_any>`, `<allow_inactive>`, et `<allow_active>` dans la section `<defaults>` d'un fichier `.policy` déterminent cette autorisation implicite.

        -   **`allow_any`**: S'applique à toutes les sessions, qu'elles soient actives ou inactives, locales ou distantes.
        -   **`allow_inactive`**: S'applique aux sessions non actives. Une session inactive est typiquement une session SSH ou un utilisateur qui n'est pas physiquement à la console.
        -   **`allow_active`**: S'applique aux sessions actives. Une session active est généralement l'utilisateur physiquement connecté à la console graphique (ou textuelle) du système.

        **Exemples de Comportements Implicites :**

        -   **`org.freedesktop.udisks2.mount-filesystem`** (montage de périphériques) :
            ```xml
            <defaults>
              <allow_any>no</allow_any>
              <allow_inactive>no</allow_inactive>
              <allow_active>yes</allow_active>
            </defaults>
            ```
            -   Par défaut : N'importe qui sur une session active peut monter des systèmes de fichiers sans mot de passe.
            -   N'importe qui sur une session inactive (SSH) ne peut pas le faire.

        -   **`org.freedesktop.login1.reboot`** (redémarrage du système) :
            ```xml
            <defaults>
              <allow_any>auth_admin_keep</allow_any>
              <allow_inactive>auth_admin_keep</allow_inactive>
              <allow_active>yes</allow_active>
            </defaults>
            ```
            -   Par défaut : N'importe qui sur une session active peut redémarrer sans mot de passe.
            -   Sur une session inactive (SSH), ou si la règle `allow_active` ne s'applique pas, il faut un mot de passe administrateur (`auth_admin_keep`).

        #### Importance de `allow_active` :
        `allow_active` est une distinction importante pour la sécurité des postes de travail. Elle permet aux utilisateurs interactifs et physiques d'effectuer des tâches courantes (comme monter une clé USB, gérer leur connexion Wi-Fi) sans taper leur mot de passe constamment, tout en exigeant une authentification ou interdisant l'action pour les sessions distantes ou non-graphiques.

        Les règles `.rules` dans `/etc/polkit-1/rules.d/` peuvent toujours **outrepasser** ces comportements par défaut.
        """
        add_scrollable_text_to_content_frame("6. Authentification et Implicit Auth", auth_implicit_text)

        # --- Tab 7: Débogage et Audit ---
        debug_audit_text = """
        ### Débogage et Audit de Polkit

        Comprendre pourquoi une action est autorisée ou refusée est essentiel pour le dépannage de Polkit.

        #### 1. Vérifier les Logs du Système :

        Polkit logue ses décisions et les tentatives d'autorisation/refus.
        -   Sur les systèmes utilisant `systemd` (la plupart des distributions modernes) :
            `journalctl -u polkit -f` (pour suivre les logs en temps réel)
            `journalctl -u polkit` (pour voir l'historique des logs)
        -   Les logs peuvent également se trouver dans `/var/log/auth.log` (Debian/Ubuntu) ou `/var/log/secure` (RHEL/CentOS) pour les tentatives d'authentification.

        Les logs de Polkit sont très détaillés et indiquent quelle règle a été évaluée, le résultat, et pourquoi une décision a été prise.

        #### 2. Utilisation de `pkcheck` :

        L'outil en ligne de commande `pkcheck` permet de tester si une action serait autorisée pour un utilisateur donné.

        **Syntaxe :**
        `pkcheck --action-id <action_id> [--user <username>] [--process <pid>]`

        **Exemples :**

        -   **Vérifier si l'utilisateur actuel peut éteindre la machine :**
            `pkcheck --action-id org.freedesktop.login1.power-off`
            Si autorisé, il ne renverra rien et le code de sortie sera 0. S'il demande l'authentification, une boîte de dialogue s'affichera. S'il refuse, il affichera un message d'erreur.

        -   **Vérifier si l'utilisateur 'john' peut monter un système de fichiers (en simulant une session non active) :**
            `pkcheck --action-id org.freedesktop.udisks2.mount-filesystem --user john --no-active`
            L'option `--no-active` est utile pour simuler une connexion SSH.

        -   **Vérifier une action avec des détails supplémentaires (si l'action en a) :**
            Certaines actions acceptent des détails, par exemple pour monter un périphérique spécifique.
            `pkcheck --action-id org.freedesktop.udisks2.filesystem-mount --property device=/dev/sdb1`

        `pkcheck` est un outil de diagnostic indispensable pour comprendre et valider vos règles Polkit sans avoir à relancer le service ou à redémarrer la machine.

        #### 3. Erreurs de Syntaxe dans les Fichiers `.rules` :

        Si un fichier `.rules` contient une erreur de syntaxe JavaScript, `polkitd` ne pourra pas le charger. Cela sera visible dans les logs de `polkitd` via `journalctl -u polkit`.

        Redémarrez `polkitd` après chaque modification de fichier `.rules` pour vous assurer que les changements sont pris en compte :
        `sudo systemctl restart polkit`
        """
        add_scrollable_text_to_content_frame("7. Débogage et Audit", debug_audit_text)

        # --- Tab 8: Exemples Pratiques ---
        examples_text = """
        ### Exemples Pratiques de Configuration Polkit

        Voici des scénarios courants et comment les adresser avec des règles Polkit.

        #### 1. Autoriser un Groupe à Redémarrer sans Mot de Passe (sur session active)

        Objectif : Permettre aux membres du groupe `ops` de redémarrer le système sans avoir à entrer leur mot de passe s'ils sont sur une session active.

        Fichier : `/etc/polkit-1/rules.d/60-ops-power.rules`
        ```javascript
        polkit.addRule(function(action, subject) {
            if (action.id == "org.freedesktop.login1.reboot" &&
                subject.isInGroup("ops") &&
                subject.active) {
                return polkit.Result.YES;
            }
        });
        ```

        #### 2. Interdire Totalement l'Installation de Paquets pour l'Utilisateur 'guest'

        Objectif : Empêcher l'utilisateur `guest` d'utiliser Flatpak pour installer des applications.

        Fichier : `/etc/polkit-1/rules.d/99-guest-restrictions.rules`
        ```javascript
        polkit.addRule(function(action, subject) {
            if (action.id == "org.freedesktop.Flatpak.install" &&
                subject.user == "guest") {
                return polkit.Result.NO;
            }
        });
        ```

        #### 3. Demander le Mot de Passe Admin pour Gérer NetworkManager (même pour l'utilisateur actif)

        Objectif : Sur un serveur, exiger toujours une authentification administrateur pour modifier les paramètres réseau, même pour l'utilisateur connecté en local.

        Fichier : `/etc/polkit-1/rules.d/70-network-strict.rules`
        ```javascript
        polkit.addRule(function(action, subject) {
            if (action.id == "org.freedesktop.NetworkManager.settings.modify" ||
                action.id == "org.freedesktop.NetworkManager.settings.system.modify") {
                return polkit.Result.AUTH_ADMIN_REQUIRED;
            }
        });
        ```

        #### 4. Permettre à un Utilisateur Spécifique de Monter des Partages NFS sans Mot de Passe

        Objectif : L'utilisateur `nfsuser` peut monter des partages NFS sans authentification, tandis que d'autres doivent s'authentifier.

        Fichier : `/etc/polkit-1/rules.d/50-nfs-mount.rules`
        ```javascript
        polkit.addRule(function(action, subject) {
            // S'applique à l'action de montage de système de fichiers UDisks2
            if (action.id == "org.freedesktop.udisks2.mount-filesystem") {
                // Et si le point de montage est de type 'nfs' (vérifier action.lookup ou action.details si disponible)
                // Ou si l'action est spécifique au montage NFS si elle existe (ex: 'org.gnome.Nautilus.mount-nfs')
                // Pour UDisks2, on peut souvent inspecter les propriétés de l'action si elles sont passées
                // Simplicité ici: on suppose une action générique et on se base sur l'utilisateur
                if (subject.user == "nfsuser") {
                    return polkit.Result.YES;
                }
            }
            return polkit.Result.NOT_HANDLED; // Laissez d'autres règles ou le défaut gérer le reste
        });
        ```
        **Note :** Pour des cas plus complexes comme le type de système de fichiers (`nfs`), il faut vérifier si l'application cliente transmet cette information comme un *détail* de l'action Polkit, que l'on peut alors inspecter via `action.lookup("type")` ou `action.details["fstype"]` si l'action le supporte. Sinon, on peut se baser uniquement sur l'identité de l'utilisateur.

        #### 5. Empêcher les utilisateurs distants d'utiliser la fonction de veille/hibernation

        Objectif : Seuls les utilisateurs connectés physiquement à la console peuvent mettre le système en veille prolongée.

        Fichier : `/etc/polkit-1/rules.d/75-remote-suspend-restrict.rules`
        ```javascript
        polkit.addRule(function(action, subject) {
            if (action.id == "org.freedesktop.login1.suspend" ||
                action.id == "org.freedesktop.login1.hibernate") {
                if (!subject.active) { // Si l'utilisateur n'est PAS actif (i.e., session distante)
                    return polkit.Result.NO; // Refuser
                }
            }
            return polkit.Result.NOT_HANDLED;
        });
        ```
        Ces exemples démontrent la flexibilité de Polkit pour définir des politiques d'autorisation adaptées à des besoins spécifiques.
        """
        add_scrollable_text_to_content_frame("8. Exemples Pratiques", examples_text)

        # --- Tab 9: Bonnes Pratiques ---
        best_practices_text = """
        ### Bonnes Pratiques pour la Configuration de Polkit

        1.  **Utilisez `/etc/polkit-1/rules.d/` pour vos règles personnalisées :** C'est le seul endroit sûr pour ajouter vos propres règles. Ne modifiez jamais les fichiers dans `/usr/share/polkit-1/`.
        2.  **Nommez vos fichiers de règles intelligemment :** Utilisez des préfixes numériques (ex: `10-custom.rules`, `90-override.rules`) pour contrôler l'ordre d'évaluation. Les règles sont évaluées par ordre alphabétique.
        3.  **Soyez le plus spécifique possible :** Évitez les règles trop générales qui pourraient involontairement ouvrir des failles de sécurité. Identifiez précisément les actions et les sujets.
        4.  **Principe du moindre privilège :** N'accordez que les permissions nécessaires. Si une action ne doit jamais être autorisée, utilisez `polkit.Result.NO`.
        5.  **Testez vos règles :** Utilisez `pkcheck` pour vérifier l'effet de vos règles sur des actions spécifiques et pour des utilisateurs différents (`--user`, `--active`, `--no-active`).
        6.  **Vérifiez les logs :** Utilisez `journalctl -u polkit` pour surveiller les décisions de Polkit et détecter les erreurs de syntaxe ou les comportements inattendus.
        7.  **Commentez vos règles :** Les fichiers `.rules` sont en JavaScript, utilisez `/* ... */` ou `//` pour commenter vos règles et expliquer leur but. Cela facilite la maintenance future.
        8.  **Redémarrez le service Polkit :** Après avoir modifié un fichier `.rules`, redémarrez le démon Polkit pour que les changements soient pris en compte : `sudo systemctl restart polkit`.
        9.  **Comprenez les `defaults` dans les fichiers `.policy` :** Souvenez-vous que vos règles `.rules` peuvent outrepasser ces défauts. Si votre règle ne prend pas de décision (`NOT_HANDLED`), c'est la politique par défaut qui sera appliquée.
        10. **Sécurité de la session active (`subject.active`) :** Utilisez cette propriété avec discernement. Elle est utile pour distinguer les utilisateurs connectés physiquement des utilisateurs distants (via SSH, par exemple) pour des tâches sensibles.

        En suivant ces bonnes pratiques, vous pouvez maintenir une configuration Polkit robuste, sécurisée et facile à gérer pour votre système.
        """
        add_scrollable_text_to_content_frame("9. Bonnes Pratiques", best_practices_text)


if __name__ == "__main__":
    app = PolkitConfigApp()
    app.mainloop()