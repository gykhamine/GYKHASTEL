import customtkinter as ctk

# --- Configuration Globale de CustomTkinter ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class GnomeShellCssApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x850")
        self.title("GNOME Shell CSS : Référence Exhaustive (CustomTkinter)")

        # Configurer la grille de la fenêtre principale
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Cadre défilant principal pour contenir tout le contenu
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Titre général
        title_label = ctk.CTkLabel(self.scroll_frame,
                                   text="GNOME Shell CSS : Sélecteurs et Propriétés",
                                   font=ctk.CTkFont(size=30, weight="bold"),
                                   text_color="#2c3e50")
        title_label.grid(row=0, column=0, pady=(0, 30), sticky="ew")

        # Description générale
        intro_text = """
        GNOME Shell utilise sa propre feuille de style CSS pour son interface utilisateur,
        distincte du thème des applications GTK. Ce guide présente les sélecteurs et
        propriétés CSS spécifiques au Shell, que l'on trouve typiquement dans
        `~/.local/share/gnome-shell/themes/<YourTheme>/gnome-shell.css`
        ou dans les styles des extensions.
        Les éléments de GNOME Shell sont souvent des 'actors' (Clutter actors) stylisés.
        """
        intro_label = ctk.CTkLabel(self.scroll_frame,
                                   text=intro_text,
                                   font=ctk.CTkFont(size=17, slant="italic"),
                                   text_color="#555555",
                                   wraplength=900, justify="left")
        intro_label.grid(row=1, column=0, pady=(0, 35), sticky="ew")

        current_row = 2

        # --- Définition des sélecteurs CSS de GNOME Shell ---

        selectors_info = [
            {
                "title": "1. Sélecteurs de Type (Noms d'éléments du Shell)",
                "description": "Cible des éléments spécifiques de l'interface GNOME Shell. Ces noms correspondent aux 'actors' ou aux composants du Shell.",
                "examples": [
                    {"code": "#panel {\n    background-color: rgba(30, 30, 30, 0.8);\n    color: white;\n    font-weight: bold;\n    height: 30px;\n}\n", "comment": "Style la barre supérieure de GNOME Shell."},
                    {"code": ".panel-button {\n    font-size: 13pt;\n    padding: 0 8px;\n    border-radius: 4px;\n}\n", "comment": "Style les boutons génériques sur le panel (heure, activités, menu système)."},
                    {"code": ".panel-button:hover {\n    background-color: rgba(255, 255, 255, 0.1);\n}\n", "comment": "Effet de survol pour les boutons du panel."},
                    {"code": "#dash {\n    background-color: rgba(40, 40, 40, 0.9);\n    border-radius: 10px;\n    padding: 10px;\n}\n", "comment": "Style le dock des favoris (Dash)."},
                    {"code": "#overview {\n    background-color: rgba(0, 0, 0, 0.7);\n}\n", "comment": "Style l'arrière-plan de la vue d'ensemble (Activités)."},
                    {"code": ".app-folder-dialog {\n    background-color: #3e3e3e;\n    border-radius: 12px;\n}\n", "comment": "Style la fenêtre de dossier d'applications dans la vue d'ensemble."},
                    {"code": ".app-well-app .app-state-indicator {\n    background-color: #3498db;\n    height: 3px;\n}\n", "comment": "Style l'indicateur d'application en cours d'exécution dans le Dash."},
                    {"code": ".workspace-thumbnails {\n    spacing: 15px;\n}\n", "comment": "Espacement entre les vignettes d'espaces de travail."},
                    {"code": ".app-grid {\n    spacing: 20px;\n    padding: 20px;\n}\n", "comment": "Espacement et padding de la grille des applications."},
                    {"code": ".icon-grid {\n    spacing: 10px;\n}\n", "comment": "Espacement générique pour les grilles d'icônes."},
                    {"code": ".system-status-icon {\n    icon-size: 16px;\n}\n", "comment": "Taille des icônes de statut du système (réseau, batterie, etc.)."},
                    {"code": ".notification-banner {\n    background-color: rgba(50, 50, 50, 0.95);\n    color: white;\n    padding: 10px;\n    border-radius: 6px;\n    box-shadow: 0 2px 8px rgba(0,0,0,0.3);\n}\n", "comment": "Style les bannières de notification."},
                    {"code": ".osd-window {\n    background-color: rgba(0, 0, 0, 0.7);\n    color: white;\n    border-radius: 8px;\n    padding: 15px;\n}\n", "comment": "Style les indicateurs OSD (volume, luminosité)."},
                    {"code": ".modal-dialog {\n    background-color: rgba(25, 25, 25, 0.9);\n    border-radius: 15px;\n    padding: 20px;\n    box-shadow: 0 5px 20px rgba(0,0,0,0.5);\n}\n", "comment": "Style les dialogues modaux (ex: éteindre, déverrouiller)."},
                    {"code": ".candidate-box {\n    background-color: #333;\n    border-radius: 5px;\n}\n", "comment": "Style la boîte de candidats pour la saisie de texte (IME)."},
                    {"code": ".popup-menu-box {\n    background-color: #3a3a3a;\n    border-radius: 8px;\n    padding: 5px;\n    box-shadow: 0 4px 10px rgba(0,0,0,0.2);\n}\n", "comment": "Style les conteneurs des menus pop-up (menu système, date/heure)."},
                    {"code": ".popup-menu-item {\n    padding: 8px 12px;\n    border-radius: 4px;\n}\n", "comment": "Style chaque élément dans les menus pop-up."},
                    {"code": ".popup-menu-item:hover {\n    background-color: rgba(255, 255, 255, 0.1);\n}\n", "comment": "Effet de survol pour les éléments de menu pop-up."},
                    {"code": ".popup-separator-menu-item {\n    -gtk-icon-effect: none;\n    background-color: #555;\n    height: 1px;\n    margin: 5px 0;\n}\n", "comment": "Style les séparateurs dans les menus pop-up."},
                    {"code": ".popup-slider-menu-item {\n    -slider-height: 8px;\n}\n", "comment": "Hauteur du slider dans les menus (volume, luminosité)."},
                    {"code": ".date-menu-weekday {\n    font-weight: bold;\n    color: #bbb;\n}\n", "comment": "Style les jours de la semaine dans le calendrier du menu date/heure."},
                    {"code": ".calendar-day-base {\n    padding: 5px;\n}\n", "comment": "Padding de base pour les jours du calendrier."},
                    {"code": ".calendar-today {\n    background-color: #3498db;\n    border-radius: 50%;\n}\n", "comment": "Style le jour actuel dans le calendrier."},
                    {"code": ".message-list-section-title {\n    font-weight: bold;\n    color: #aaa;\n    padding: 5px 10px;\n}\n", "comment": "Style les titres de section dans le centre de notifications."},
                    {"code": ".login-screen {\n    background-image: url(\"file:///path/to/your/image.jpg\");\n    background-size: cover;\n    background-repeat: no-repeat;\n}\n", "comment": "Définir une image de fond pour l'écran de connexion/verrouillage."},
                    {"code": "#unlock-dialog {\n    background-color: rgba(0,0,0,0.6);\n    border-radius: 20px;\n}\n", "comment": "Style le dialogue de déverrouillage."},
                    {"code": ".user-icon {\n    border-radius: 50%;\n    border: 2px solid #3498db;\n}\n", "comment": "Style les icônes d'utilisateur (avatars)."},
                    {"code": ".notification-list {\n    spacing: 10px;\n}\n", "comment": "Espacement entre les notifications dans la liste."},
                    {"code": ".search-section-title {\n    color: #bbb;\n    font-weight: bold;\n}\n", "comment": "Style les titres de section dans la barre de recherche des activités."},
                    {"code": ".hot-corners-layout-manager-pointer-region {\n    background-color: transparent;\n    border: 1px dashed red; /* Pour le débogage */\n}\n", "comment": "Zone invisible des coins actifs (utile pour le débogage)."},
                    {"code": ".alt-tab-switcher {\n    background-color: rgba(30, 30, 30, 0.9);\n    border-radius: 10px;\n    padding: 10px;\n    box-shadow: 0 0 15px rgba(0,0,0,0.5);\n}\n", "comment": "Style le sélecteur Alt+Tab."},
                    {"code": ".alt-tab-app-thumbnail {\n    border: 2px solid transparent;\n}\n", "comment": "Bordure transparente par défaut pour les vignettes Alt+Tab."},
                    {"code": ".alt-tab-app-thumbnail:selected {\n    border-color: #3498db;\n}\n", "comment": "Bordure bleue pour la vignette sélectionnée dans Alt+Tab."},
                    {"code": ".window-picker-box {\n    spacing: 20px;\n}\n", "comment": "Espacement des fenêtres dans le sélecteur de fenêtres."},
                    {"code": ".control-center-panel .label {\n    font-weight: bold;\n}\n", "comment": "Styles les labels des éléments du centre de contrôle via le panel."},
                ]
            },
            {
                "title": "2. Sélecteurs d'ID (#NomID)",
                "description": "Cible un élément spécifique du Shell par son ID unique, défini dans le code source de GNOME Shell. Très précis.",
                "examples": [
                    {"code": "#activities-button {\n    background-color: #3498db;\n    color: white;\n    border-radius: 5px;\n    padding: 0 10px;\n}\n", "comment": "Style le bouton 'Activités'."},
                    {"code": "#app-menu-button {\n    font-weight: bold;\n    color: #e0e0e0;\n}\n", "comment": "Style le bouton du menu de l'application active."},
                    {"code": "#looking-glass-content {\n    background-color: rgba(0,0,0,0.9);\n    border: 1px solid #555;\n    border-radius: 10px;\n    padding: 20px;\n}\n", "comment": "Style la console Looking Glass (outil de débogage)."},
                    {"code": "#no-notifications-message {\n    color: #aaaaaa;\n    font-style: italic;\n}\n", "comment": "Style le message 'Aucune notification'."},
                    {"code": "#user-menu {\n    background-color: #333;\n    border-radius: 8px;\n}\n", "comment": "Style le menu utilisateur dans le coin supérieur droit."},
                    {"code": "#datemenu {\n    background-color: #333;\n    border-radius: 8px;\n}\n", "comment": "Style le menu date/heure."},
                    {"code": "#screen-shield-background {\n    background-color: black;\n    opacity: 0.9;\n}\n", "comment": "Style l'arrière-plan de l'écran de verrouillage avant le dialogue de déverrouillage."},
                    {"code": "#keyboard-layout-menu {\n    min-width: 200px;\n}\n", "comment": "Largeur minimale pour le menu de disposition du clavier."},
                ]
            },
            {
                "title": "3. Sélecteurs de Classe de Style (.NomClasse)",
                "description": "Cible les éléments du Shell auxquels une classe de style a été attribuée. Permet de réutiliser des styles.",
                "examples": [
                    {"code": ".system-menu-item {\n    padding: 10px 15px;\n    font-size: 13pt;\n}\n", "comment": "Classe pour les éléments du menu système (volume, power, etc.)."},
                    {"code": ".system-menu-item:hover {\n    background-color: rgba(255, 255, 255, 0.15);\n}\n", "comment": "Effet de survol pour les éléments du menu système."},
                    {"code": ".notification-item {\n    background-color: rgba(60, 60, 60, 0.9);\n    border-radius: 8px;\n    padding: 10px;\n    margin-bottom: 8px;\n}\n", "comment": "Style pour chaque notification individuelle dans la liste."},
                    {"code": ".message-content {\n    color: #e0e0e0;\n}\n", "comment": "Couleur du texte principal d'un message."},
                    {"code": ".dash-label {\n    color: white;\n    font-size: 11pt;\n}\n", "comment": "Style les labels sous les icônes du Dash."},
                    {"code": ".workspace-thumbnail:selected {\n    border: 3px solid #3498db;\n}\n", "comment": "Bordure pour la vignette d'espace de travail sélectionnée."},
                    {"code": ".user-status-indicator {\n    background-color: #2ecc71;\n    border-radius: 50%;\n    width: 8px;\n    height: 8px;\n}\n", "comment": "Indicateur de statut utilisateur (en ligne, absent)."},
                    {"code": ".search-entry {\n    border-radius: 20px;\n    background-color: rgba(255, 255, 255, 0.1);\n    color: white;\n    padding: 8px 15px;\n}\n", "comment": "Style la barre de recherche dans la vue d'ensemble."},
                    {"code": ".search-entry:focus {\n    background-color: rgba(255, 255, 255, 0.2);\n}\n", "comment": "Effet de focus sur la barre de recherche."},
                    {"code": ".overview-group-actor {\n    spacing: 10px;\n}\n", "comment": "Espacement des groupes d'applications dans la vue d'ensemble."},
                    {"code": ".app-list .folder-icon {\n    icon-size: 48px;\n}\n", "comment": "Taille d'icône pour les dossiers d'applications."},
                    {"code": ".quick-toggle-button {\n    background-color: rgba(255, 255, 255, 0.05);\n    border-radius: 8px;\n    padding: 8px;\n}\n", "comment": "Style les boutons de basculement rapide (Wi-Fi, Bluetooth) dans le menu système."},
                    {"code": ".quick-toggle-button:checked {\n    background-color: #3498db;\n}\n", "comment": "Style un bouton de basculement rapide quand il est activé."},
                    {"code": ".icon-grid-item-container {\n    padding: 5px;\n}\n", "comment": "Conteneur pour les éléments dans les grilles d'icônes."},
                    {"code": ".source-box {\n    background-color: rgba(255,255,255,0.05);\n    border-radius: 5px;\n    padding: 5px;\n}\n", "comment": "Boîte source pour les résultats de recherche (ex: fichiers)."},
                ]
            },
            {
                "title": "4. Sélecteurs d'Attribut (Pseudo-classes)",
                "description": "Cible les éléments du Shell en fonction de leur état. Similaire à GTK, mais pour les éléments du Shell.",
                "examples": [
                    {"code": ".panel-button:active {\n    background-color: rgba(0, 0, 0, 0.2);\n}\n", "comment": "Style les boutons du panel quand ils sont cliqués."},
                    {"code": ".popup-menu-item:selected {\n    background-color: #3498db;\n    color: white;\n}\n", "comment": "Style l'élément sélectionné dans un menu pop-up."},
                    {"code": ".popup-menu-item:disabled {\n    color: #888;\n    font-style: italic;\n}\n", "comment": "Style un élément de menu désactivé."},
                    {"code": ".toggle-switch:checked {\n    background-color: #2ecc71;\n}\n", "comment": "Style un interrupteur personnalisé quand il est activé."},
                    {"code": ".notification-item:hover {\n    background-color: rgba(70, 70, 70, 0.9);\n}\n", "comment": "Effet de survol sur les notifications."},
                    {"code": ".calendar-day-base:selected {\n    background-color: #3498db;\n    color: white;\n    border-radius: 50%;\n}\n", "comment": "Style le jour sélectionné dans le calendrier."},
                    {"code": ".calendar-day-base:off-month {\n    color: #888;\n}\n", "comment": "Style les jours du mois précédent/suivant dans le calendrier."},
                    {"code": ".app-well-app:hover .app-state-indicator {\n    background-color: #2ecc71;\n}\n", "comment": "Change la couleur de l'indicateur d'état au survol de l'application."},
                    {"code": "#activities-button:focus {\n    box-shadow: 0 0 0 2px #3498db;\n}\n", "comment": "Ajoute un anneau de focus autour du bouton Activités."},
                    {"code": ".dash-item-container:drag {\n    border: 2px dashed #3498db;\n}\n", "comment": "Style un élément du Dash pendant un glisser-déposer."},
                    {"code": ".panel-button:rtl {\n    padding-right: 8px; /* Ajustement pour les langues RTL */\n}\n", "comment": "Ajustement de padding pour les boutons de panel en mode RTL."},
                    {"code": ".app-well-app:running {\n    opacity: 1;\n}\n", "comment": "Garantit l'opacité complète pour les applications en cours d'exécution (si une opacité par défaut est définie)."},
                    {"code": ".app-well-app:favorite {\n    font-weight: bold;\n}\n", "comment": "Style les applications favorites dans le Dash."},
                ]
            },
            {
                "title": "5. Sélecteurs de Relation (Combinateurs)",
                "description": "Ciblent des éléments du Shell en fonction de leur position ou de leur hiérarchie par rapport à d'autres éléments.",
                "sub_sections": [
                    {
                        "sub_title": "  a. Combinateur Descendant (Espace) `parent descendant`",
                        "sub_examples": [
                            {"code": "#panel .panel-button .system-status-icon {\n    icon-size: 18px;\n    color: #e0e0e0;\n}\n", "comment": "Cible les icônes de statut *à l'intérieur* des boutons du panel."},
                            {"code": ".popup-menu-box .popup-menu-item .label {\n    color: #eee;\n}\n", "comment": "Cible les labels *à l'intérieur* des éléments de menu pop-up."},
                            {"code": "#dash .app-well-app .app-icon {\n    box-shadow: 0 2px 5px rgba(0,0,0,0.3);\n}\n", "comment": "Ajoute une ombre aux icônes d'application dans le Dash."},
                            {"code": ".notification-banner .notification-body {\n    font-size: 11pt;\n}\n", "comment": "Style le corps du texte dans une bannière de notification."},
                        ]
                    },
                    {
                        "sub_title": "  b. Combinateur Enfant Direct (>) `parent > child`",
                        "sub_examples": [
                            {"code": "#panel > StBoxLayout > .panel-button {\n    margin: 0 2px;\n}\n", "comment": "Cible les boutons qui sont des *enfants directs* d'un StBoxLayout dans le panel."},
                            {"code": ".alt-tab-switcher > StIcon {\n    icon-size: 64px;\n}\n", "comment": "Taille les icônes directement dans le sélecteur Alt+Tab."},
                            {"code": "#dash > StBoxLayout {\n    spacing: 0;\n}\n", "comment": "Supprime l'espacement de la boîte principale du dash."},
                        ]
                    },
                    {
                        "sub_title": "  c. Combinateur Frère Adjacents (+) `element + adjacent-sibling`",
                        "sub_examples": [
                            {"code": ".panel-button + .panel-button {\n    margin-left: 5px;\n}\n", "comment": "Ajoute un espacement entre les boutons de panel adjacents."},
                            {"code": ".notification-item + .notification-item {\n    margin-top: 10px;\n}\n", "comment": "Espacement entre les notifications consécutives."},
                        ]
                    },
                ]
            },
            {
                "title": "6. Propriétés CSS de GNOME Shell Courantes et Spécifiques",
                "description": "Propriétés CSS courantes et celles spécifiques à l'environnement Clutter/Mutter/GJS de GNOME Shell.",
                "examples": [
                    {"code": "background-color: rgba(0, 0, 0, 0.7); /* Couleur avec opacité */\nbackground-image: url(\"file:///path/to/image.png\"); /* Image de fond */\nbackground-size: cover; /* Recouvrir l'élément */\nbackground-repeat: no-repeat; /* Ne pas répéter l'image */\nbackground-position: center; /* Centrer l'image */", "comment": "Gestion complète de l'arrière-plan avec opacité, images et positionnement."},
                    {"code": "color: white; /* Couleur du texte */", "comment": "Couleur du texte."},
                    {"code": "font-family: 'Cantarell', sans-serif;\nfont-size: 12pt;\nfont-weight: bold;\nfont-style: italic;", "comment": "Propriétés de police classiques."},
                    {"code": "text-shadow: 1px 1px 2px rgba(0,0,0,0.5);", "comment": "Ombre portée sur le texte."},
                    {"code": "border: 1px solid #555;\nborder-radius: 8px;", "comment": "Bordures et arrondis."},
                    {"code": "padding: 10px 15px;\nmargin: 5px;", "comment": "Rembourrage interne (padding) et marges externes."},
                    {"code": "box-shadow: 0 4px 12px rgba(0,0,0,0.3);", "comment": "Ombre portée pour les boîtes."},
                    {"code": "opacity: 0.9;", "comment": "Transparence de l'élément."},
                    {"code": "width: 200px;\nheight: 50px;\nmin-width: 100px;\nmax-height: 300px;", "comment": "Dimensions fixes et min/max."},
                    {"code": "icon-size: 24px; /* Spécifique au Shell pour les icônes */", "comment": "Taille des icônes dans de nombreux contextes du Shell."},
                    {"code": "spacing: 10px; /* Espacement entre les enfants directs */", "comment": "Propriété de mise en page pour les conteneurs (StBoxLayout, StFlowLayout)."},
                    {"code": "text-align: center; /* Alignement du texte */", "comment": "Alignement du texte dans un label ou un bouton."},
                    {"code": "caret-color: #3498db; /* Couleur du curseur de texte */", "comment": "Couleur du curseur de texte dans les champs de saisie (StEntry)."},
                    {"code": "transition-duration: 300ms; /* Durée des transitions */\ntransition-timing-function: ease-out; /* Fonction de timing */", "comment": "Propriétés pour animer les changements de style (similaires à CSS3 transitions)."},
                    {"code": "-shell-slide-direction: left; /* Direction pour les transitions de glissement */", "comment": "Propriété spécifique au Shell pour les transitions de slide."},
                    {"code": "-shell-grid-horizontal-spacing: 10px; /* Espacement horizontal de grille */\n-shell-grid-vertical-spacing: 10px;", "comment": "Espacement des éléments dans certaines grilles du Shell."},
                    {"code": "-shell-panel-box-spacing: 5px; /* Espacement dans les boîtes de panel */", "comment": "Espacement entre les éléments du panel."},
                    {"code": "-shell-border-width: 2px; /* Largeur de bordure interne */", "comment": "Utilisé pour certaines bordures internes stylisées."},
                    {"code": "-shell-system-action-icon-size: 32px; /* Taille d'icône des actions système */", "comment": "Taille spécifique pour les icônes des actions d'arrêt, etc."},
                    {"code": "-shell-dash-icon-size: 48px; /* Taille des icônes du Dash */", "comment": "Taille des icônes dans le Dash."},
                    {"code": "-shell-app-icon-size: 64px; /* Taille des icônes d'applications dans la vue d'ensemble */", "comment": "Taille des icônes des applications dans la grille des activités."},
                    {"code": "-shell-calendar-today-background: #3498db; /* Couleur de fond du jour actuel dans le calendrier */", "comment": "Variable pour la couleur de fond du jour actuel du calendrier."},
                    {"code": "-shell-calendar-today-color: white; /* Couleur du texte du jour actuel */", "comment": "Variable pour la couleur du texte du jour actuel du calendrier."},
                    {"code": "-shell-height-reduction: 5px; /* Réduction de hauteur pour certains éléments */", "comment": "Propriété d'ajustement de hauteur."},
                    {"code": "-shell-action-area-background: rgba(0,0,0,0.1); /* Fond de la zone d'action dans les dialogues */", "comment": "Fond pour les zones d'action (boutons) dans les dialogues modaux."},
                    {"code": "-shell-active-indicator-width: 4px; /* Largeur de l'indicateur d'activité */", "comment": "Largeur de la barre d'activité sous les icônes."},
                    {"code": "border-image: url(\"resource:///org/gnome/shell/theme/panel-border.svg\") 10 / 10px stretch; /* Image de bordure avancée */", "comment": "Utilisation d'une image SVG comme bordure (ressource interne)."},
                    {"code": "box-fit: none; /* GTK4+ style property, may apply in some contexts */", "comment": "Contrôle comment un élément remplit sa boîte (rare pour Shell)."},
                    {"code": "z-index: 10; /* Ordre de superposition (si applicable) */", "comment": "Contrôle l'ordre de superposition des éléments (rare mais possible)."},
                ]
            }
        ]

        # Boucle pour ajouter toutes les sections et leurs exemples
        for selector_info in selectors_info:
            # Titre de la section du sélecteur
            title_label = ctk.CTkLabel(self.scroll_frame,
                                       text=selector_info["title"],
                                       font=ctk.CTkFont(size=24, weight="bold"),
                                       text_color="#34495e",
                                       wraplength=900, justify="left")
            title_label.grid(row=current_row, column=0, sticky="w", pady=(25, 12))
            current_row += 1

            # Description du sélecteur
            desc_label = ctk.CTkLabel(self.scroll_frame,
                                      text=selector_info["description"],
                                      font=ctk.CTkFont(size=15),
                                      text_color="#555555",
                                      wraplength=900, justify="left")
            desc_label.grid(row=current_row, column=0, sticky="w", padx=10, pady=(0, 15))
            current_row += 1

            # Traitement des exemples ou sous-sections
            if "examples" in selector_info:
                for example in selector_info["examples"]:
                    # Affichage du code
                    code_height = max(40, len(example["code"].splitlines()) * 18 + 10)
                    code_textbox = ctk.CTkTextbox(self.scroll_frame,
                                                  width=850, height=code_height,
                                                  font=ctk.CTkFont(family="monospace", size=14),
                                                  fg_color="#ecf0f1", text_color="#2c3e50",
                                                  wrap="word", state="normal")
                    code_textbox.insert("0.0", example["code"].strip())
                    code_textbox.configure(state="disabled")
                    code_textbox.grid(row=current_row, column=0, sticky="ew", padx=40, pady=(0, 2))
                    current_row += 1

                    # Affichage du commentaire
                    comment_label = ctk.CTkLabel(self.scroll_frame,
                                                 text=f"« {example['comment']} »",
                                                 font=ctk.CTkFont(size=13, slant="italic"),
                                                 text_color="#666666",
                                                 wraplength=850, justify="left")
                    comment_label.grid(row=current_row, column=0, sticky="ew", padx=40, pady=(0, 18))
                    current_row += 1

            elif "sub_sections" in selector_info:
                for sub_sec in selector_info["sub_sections"]:
                    sub_title_label = ctk.CTkLabel(self.scroll_frame,
                                                  text=sub_sec["sub_title"],
                                                  font=ctk.CTkFont(size=19, weight="normal"), # Corrected: "medium" to "normal"
                                                  text_color="#4a698c",
                                                  wraplength=900, justify="left")
                    sub_title_label.grid(row=current_row, column=0, sticky="w", padx=25, pady=(12, 5))
                    current_row += 1

                    for sub_example in sub_sec["sub_examples"]:
                        sub_code_height = max(40, len(sub_example["code"].splitlines()) * 18 + 10)
                        sub_code_textbox = ctk.CTkTextbox(self.scroll_frame,
                                                          width=850, height=sub_code_height,
                                                          font=ctk.CTkFont(family="monospace", size=14),
                                                          fg_color="#ecf0f1", text_color="#2c3e50",
                                                          wrap="word", state="normal")
                        sub_code_textbox.insert("0.0", sub_example["code"].strip())
                        sub_code_textbox.configure(state="disabled")
                        sub_code_textbox.grid(row=current_row, column=0, sticky="ew", padx=60, pady=(0, 2))
                        current_row += 1

                        sub_comment_label = ctk.CTkLabel(self.scroll_frame,
                                                        text=f"« {sub_example['comment']} »",
                                                        font=ctk.CTkFont(size=13, slant="italic"),
                                                        text_color="#666666",
                                                        wraplength=850, justify="left")
                        sub_comment_label.grid(row=current_row, column=0, sticky="ew", padx=60, pady=(0, 18))
                        current_row += 1
            
            # Ajouter un séparateur après chaque section principale, sauf la dernière
            if selector_info != selectors_info[-1]:
                separator = ctk.CTkFrame(self.scroll_frame, height=3, fg_color="gray60")
                separator.grid(row=current_row, column=0, columnspan=1, sticky="ew", pady=(30, 30))
                current_row += 1

        self.mainloop()

# --- Exécution du Script ---
if __name__ == "__main__":
    app = GnomeShellCssApp()