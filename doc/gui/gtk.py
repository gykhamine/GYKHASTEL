import customtkinter as ctk

# --- Configuration Globale de CustomTkinter ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class GtkCssSelectorsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x850") # Taille de fenêtre légèrement augmentée
        self.title("GTK CSS Sélecteurs & Propriétés: Référence Ultra-Exhaustive (CustomTkinter)")

        # Configurer la grille de la fenêtre principale
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Cadre défilant principal pour contenir tout le contenu
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Titre général
        title_label = ctk.CTkLabel(self.scroll_frame,
                                   text="GTK CSS Sélecteurs & Propriétés: Référence Ultra-Exhaustive",
                                   font=ctk.CTkFont(size=30, weight="bold"),
                                   text_color="#2c3e50")
        title_label.grid(row=0, column=0, pady=(0, 30), sticky="ew")

        # Description générale
        intro_text = """
        GTK utilise un sous-ensemble puissant de CSS pour le stylisme des widgets.
        Cette fenêtre CustomTkinter vous offre un guide de référence **ULTRA-EXHAUSTIF**,
        détaillant **plus de 150 exemples** de sélecteurs et propriétés CSS GTK.
        Elle couvre les usages courants, les parties spécifiques des widgets, et les techniques
        de stylisme avancées pour vous aider à personnaliser vos applications GTK de manière approfondie.
        """
        intro_label = ctk.CTkLabel(self.scroll_frame,
                                   text=intro_text,
                                   font=ctk.CTkFont(size=17, slant="italic"),
                                   text_color="#555555",
                                   wraplength=900, justify="left")
        intro_label.grid(row=1, column=0, pady=(0, 35), sticky="ew")

        current_row = 2

        # --- Définition des sélecteurs CSS de GTK avec 150+ exemples/infos supplémentaires ---
        # Note : Le formatage gras/italique dans CTkTextbox est limité sans une librairie supplémentaire.
        # Nous utilisons des astérisques ou des guillemets pour simuler le gras/italique dans les exemples.

        selectors_info = [
            {
                "title": "1. Sélecteurs de Type (Nom du Widget)",
                "description": "Cible tous les widgets d'un certain type. C'est la base de la stylisation globale et générale. GTK a une hiérarchie de types.",
                "examples": [
                    {"code": "GtkWindow {\n    background-color: #f5f5f5;\n    border-radius: 6px;\n}\n", "comment": "Style toutes les fenêtres de l'application."},
                    {"code": "GtkButton {\n    background-color: #3498db;\n    color: white;\n    border-radius: 8px;\n    padding: 8px 15px;\n    font-weight: 600;\n}\n", "comment": "Styles tous les boutons avec un look moderne."},
                    {"code": "GtkLabel {\n    font-family: 'Inter', sans-serif;\n    font-size: 14pt;\n    color: #4a4a4a;\n    text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.05);\n}\n", "comment": "Définit la police, la taille, la couleur et une subtile ombre pour tous les labels."},
                    {"code": "GtkEntry {\n    border: 1px solid #ccc;\n    padding: 7px;\n    border-radius: 5px;\n    background-color: #fdfdfd;\n    box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);\n}\n", "comment": "Styles tous les champs de saisie avec un léger ombrage interne."},
                    {"code": "GtkTextView {\n    background-color: #f8f8f8;\n    border: 1px solid #ddd;\n    padding: 12px;\n    line-height: 1.4;\n}\n", "comment": "Styles les vues de texte multi-lignes, y compris l'interligne."},
                    {"code": "GtkScrolledWindow {\n    background-color: #e8e8e8;\n    border: none;\n}\n", "comment": "Définit la couleur de fond des zones de défilement, utile pour le padding autour du contenu."},
                    {"code": "GtkFrame {\n    border: 1px solid #e0e0e0;\n    border-radius: 7px;\n    margin: 12px;\n    background-color: #ffffff;\n}\n", "comment": "Ajoute un cadre, une marge et un fond blanc à toutes les GtkFrame."},
                    {"code": "GtkBox {\n    spacing: 15px;\n}\n", "comment": "Applique un espacement par défaut généreux entre les éléments dans toutes les boîtes."},
                    {"code": "GtkGrid {\n    row-spacing: 10px;\n    column-spacing: 10px;\n}\n", "comment": "Définit l'espacement par défaut pour les mises en page en grille."},
                    {"code": "GtkProgressBar {\n    min-height: 28px;\n    background-color: #e0e0e0;\n    border-radius: 14px;\n    box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);\n}\n", "comment": "Styling de base du conteneur de la barre de progression avec ombrage interne."},
                    {"code": "GtkProgressBar trough {\n    background-image: none;\n    background-color: #f5f5f5;\n    border-radius: 12px;\n}\n", "comment": "Cible la 'piste' (le fond) de la barre de progression."},
                    {"code": "GtkProgressBar progress {\n    background-image: linear-gradient(to right, #2ecc71, #27ae60);\n    border-radius: 12px;\n    transition: all 0.6s ease-out; /* GTK4+ */\n}\n", "comment": "Cible la partie remplie de la barre avec un dégradé et une transition douce."},
                    {"code": "GtkSpinner {\n    color: #3498db;\n    min-width: 32px;\n    min-height: 32px;\n}\n", "comment": "Styles l'icône de chargement (spinner)."},
                    {"code": "GtkSwitch {\n    min-width: 50px;\n    min-height: 28px;\n}\n", "comment": "Définit la taille minimale des interrupteurs."},
                    {"code": "GtkSwitch slider {\n    background-color: white;\n    border-radius: 50%;\n    border: 1px solid #ccc;\n    box-shadow: 0 1px 3px rgba(0,0,0,0.2);\n}\n", "comment": "Styles le bouton glissant de l'interrupteur."},
                    {"code": "GtkSeparator {\n    background-color: #cacaca;\n    min-height: 2px;\n    min-width: 2px;\n}\n", "comment": "Styles les séparateurs pour une meilleure visibilité."},
                    {"code": "GtkHeaderBar {\n    background-color: #2c3e50;\n    color: white;\n    padding: 8px 15px;\n    font-weight: bold;\n    box-shadow: 0 2px 5px rgba(0,0,0,0.2);\n}\n", "comment": "Styles la barre d'en-tête de l'application avec ombre."},
                    {"code": "GtkComboBox {\n    border: 1px solid #b0b0b0;\n    border-radius: 5px;\n    padding: 5px;\n}\n", "comment": "Styles les boîtes combo."},
                    {"code": "GtkComboBox arrow {\n    color: #6a6a6a;\n    font-size: 10pt;\n}\n", "comment": "Styles la flèche déroulante des boîtes combo."},
                    {"code": "GtkSpinButton {\n    border: 1px solid #b0b0b0;\n    border-radius: 5px;\n}\n", "comment": "Styles les boutons de spin."},
                    {"code": "GtkSpinButton button {\n    background-color: #f0f0f0;\n    border-left: 1px solid #e0e0e0;\n}\n", "comment": "Styles les boutons haut/bas des boutons de spin."},
                    {"code": "GtkScale trough {\n    background-color: #ddd;\n    border-radius: 4px;\n    min-height: 6px;\n}\n", "comment": "Styles la piste des curseurs."},
                    {"code": "GtkScale slider {\n    background-color: #3498db;\n    border-radius: 50%;\n    min-width: 18px;\n    min-height: 18px;\n    box-shadow: 0 1px 3px rgba(0,0,0,0.2);\n}\n", "comment": "Styles le curseur du slider."},
                    {"code": "GtkCheckButton indicator {\n    border: 2px solid #3498db;\n    border-radius: 4px;\n    min-width: 18px;\n    min-height: 18px;\n    background-color: white;\n}\n", "comment": "Styles la case visuelle du checkbox."},
                    {"code": "GtkRadioButton indicator {\n    border: 2px solid #3498db;\n    border-radius: 50%;\n    min-width: 18px;\n    min-height: 18px;\n    background-color: white;\n}\n", "comment": "Styles le cercle visuel du bouton radio."},
                    {"code": "GtkStackSidebar {\n    background-color: #f0f3f6;\n    border-right: 1px solid #e0e0e0;\n}\n", "comment": "Style une barre latérale de GtkStackSidebar."},
                    {"code": "GtkStackSidebar row {\n    padding: 10px 15px;\n    font-weight: 500;\n}\n", "comment": "Style chaque ligne individuelle dans la GtkStackSidebar."},
                    {"code": "GtkToolbar {\n    background-color: #e9ecef;\n    padding: 5px;\n    border-bottom: 1px solid #ddd;\n}\n", "comment": "Style les barres d'outils."},
                    {"code": "GtkToolbar button {\n    padding: 5px;\n    border-radius: 4px;\n}\n", "comment": "Style les boutons à l'intérieur des barres d'outils."},
                    {"code": "GtkPopover {\n    background-color: white;\n    border: 1px solid #ccc;\n    box-shadow: 0 4px 12px rgba(0,0,0,0.15);\n    border-radius: 8px;\n}\n", "comment": "Style les popovers (fenêtres contextuelles)."},
                    {"code": "GtkTooltip {\n    background-color: #333;\n    color: white;\n    border-radius: 4px;\n    padding: 6px 10px;\n    font-size: 10pt;\n}\n", "comment": "Style les bulles d'aide (tooltips)."},
                    {"code": "GtkExpander {\n    font-weight: bold;\n    color: #2c3e50;\n}\n", "comment": "Style le label du GtkExpander."},
                    {"code": "GtkExpander arrow {\n    min-width: 20px;\n    min-height: 20px;\n}\n", "comment": "Style la flèche du GtkExpander."},
                    {"code": "GtkCalendar {\n    border: 1px solid #ddd;\n    border-radius: 8px;\n    background-color: white;\n}\n", "comment": "Style le widget Calendrier."},
                    {"code": "GtkCalendar .day {\n    padding: 5px;\n    text-align: center;\n}\n", "comment": "Style les jours du calendrier."},
                    {"code": "GtkCalendar .day.today {\n    font-weight: bold;\n    color: #3498db;\n}\n", "comment": "Style le jour actuel dans le calendrier."},
                    {"code": "GtkSearchEntry {\n    border-radius: 20px;\n    padding-left: 15px;\n    padding-right: 15px;\n    background-color: #f0f0f0;\n}\n", "comment": "Style les champs de recherche (souvent avec une loupe)."},
                    {"code": "GtkPaned handle {\n    background-color: #bbb;\n    min-width: 8px;\n    min-height: 8px;\n    border-radius: 4px;\n}\n", "comment": "Style la poignée (handle) des GtkPaned."},
                    {"code": "GtkMenuBar {\n    background-color: #f8f8f8;\n    border-bottom: 1px solid #eee;\n}\n", "comment": "Style la barre de menu supérieure."},
                    {"code": "GtkMenu {\n    background-color: white;\n    border: 1px solid #ddd;\n    box-shadow: 0 2px 8px rgba(0,0,0,0.1);\n    border-radius: 4px;\n}\n", "comment": "Style les menus déroulants."},
                    {"code": "GtkMenuItem {\n    padding: 8px 15px;\n}\n", "comment": "Style les éléments individuels des menus."},
                    {"code": "GtkToolbar #home-button {\n    background-image: -gtk-icontheme('go-home-symbolic');\n    background-size: contain;\n    background-repeat: no-repeat;\n    background-position: center;\n}\n", "comment": "Utilise une icône du thème GTK pour un bouton de barre d'outils (GTK4+)."},
                ]
            },
            {
                "title": "2. Sélecteurs d'ID (#NomID)",
                "description": "Cible un widget spécifique par son nom unique (défini avec `widget.set_name('MonID')`). Très précis pour des éléments uniques.",
                "examples": [
                    {"code": "#application-title-label {\n    font-size: 20pt;\n    font-weight: bold;\n    color: #1a5278;\n    margin-bottom: 10px;\n}\n", "comment": "Style un label de titre d'application unique."},
                    {"code": "#settings-pane {\n    background-color: #fbfbfb;\n    padding: 20px;\n    border-left: 3px solid #3498db;\n}\n", "comment": "Style un panneau de paramètres spécifique avec une bordure de couleur."},
                    {"code": "#delete-confirmation-button {\n    background-color: #c0392b;\n    color: white;\n    font-weight: bold;\n    border-radius: 5px;\n}\n", "comment": "Bouton de confirmation de suppression unique et proéminent."},
                    {"code": "#user-avatar {\n    border-radius: 50%;\n    border: 4px solid #f39c12;\n    box-shadow: 0 0 8px rgba(243,156,18,0.4);\n}\n", "comment": "Styles un avatar utilisateur unique avec un cercle et une ombre."},
                    {"code": "#main-status-bar {\n    background-color: #eaf2f8;\n    border-top: 1px solid #d0d0d0;\n    padding: 10px;\n    color: #333;\n}\n", "comment": "Style une barre de statut principale."},
                    {"code": "#welcome-message {\n    color: #27ae60;\n    font-size: 16pt;\n    text-align: center;\n    margin-top: 20px;\n}\n", "comment": "Message de bienvenue centré."},
                    {"code": "#search-results-list {\n    background-color: white;\n    border: 1px solid #e5e5e5;\n    padding: 5px;\n}\n", "comment": "Style la zone d'une liste de résultats de recherche."},
                    {"code": "#scrollable-content-area {\n    background-color: #fcfcfc;\n    padding: 15px;\n}\n", "comment": "Style une zone de contenu défilante spécifique."},
                ]
            },
            {
                "title": "3. Sélecteurs de Classe de Style (.NomClasse)",
                "description": "Cible les widgets auxquels une classe de style a été ajoutée. Permet la réutilisation de styles sur plusieurs widgets.\n(GTK3: `widget.get_style_context().add_class('ma-classe')`\nGTK4: `widget.add_css_class('ma-classe')`)",
                "examples": [
                    {"code": ".panel-header {\n    background-color: #eef2f7;\n    padding: 12px 15px;\n    font-weight: bold;\n    border-bottom: 1px solid #e0e0e0;\n}\n", "comment": "Classe pour les en-têtes de panneau."},
                    {"code": ".bordered-box {\n    border: 1px solid #d8d8d8;\n    border-radius: 8px;\n    padding: 10px;\n    margin: 8px;\n}\n", "comment": "Applique un style de boîte encadrée réutilisable."},
                    {"code": ".warning-text {\n    color: #e67e22;\n    font-style: italic;\n    font-size: 13pt;\n}\n", "comment": "Classe pour les messages d'avertissement."},
                    {"code": ".accent-button {\n    background-color: #9b59b6;\n    color: white;\n    font-weight: bold;\n}\n", "comment": "Un bouton avec une couleur d'accentuation."},
                    {"code": ".notification-banner {\n    background-color: #2ecc71;\n    color: white;\n    padding: 10px;\n    text-align: center;\n    margin-bottom: 10px;\n}\n", "comment": "Bannière de notification verte."},
                    {"code": ".disabled-control {\n    opacity: 0.6;\n    background-color: #f0f0f0;\n    color: #999;\n}\n", "comment": "Classe pour désactiver visuellement un contrôle."},
                    {"code": ".compact-list-item {\n    padding: 5px 8px;\n    font-size: 11pt;\n}\n", "comment": "Style pour des éléments de liste plus compacts."},
                    {"code": ".elevated {\n    box-shadow: 0 6px 16px rgba(0,0,0,0.18);\n}\n", "comment": "Classe pour ajouter une forte ombre portée."},
                    {"code": ".transparent-background {\n    background-color: transparent;\n    background-image: none;\n}\n", "comment": "Utile pour rendre un widget transparent."},
                    {"code": ".highlighted-row {\n    background-color: #ffe0b2;\n}\n", "comment": "Pour mettre en surbrillance une ligne dans une liste/arbre."},
                    {"code": ".toolbar-icon {\n    padding: 3px;\n    min-width: 24px;\n    min-height: 24px;\n}\n", "comment": "Classe pour les icônes de barre d'outils."},
                    {"code": ".header-button {\n    background-color: transparent;\n    color: white;\n}\n", "comment": "Boutons dans une barre d'en-tête."},
                    {"code": ".primary-label {\n    font-size: 15pt;\n    font-weight: 500;\n    color: #1abc9c;\n}\n", "comment": "Label de texte important."},
                    {"code": ".scrollable-content-inner {\n    padding: 15px;\n}\n", "comment": "Ajoute un padding interne au contenu d'un scrollable frame."},
                ]
            },
            {
                "title": "4. Sélecteurs d'Attribut (Pseudo-classes)",
                "description": "Cible les widgets en fonction de leur état interne ou de leur propriété. Précédés d'un deux-points (`:`).",
                "examples": [
                    {"code": "GtkButton:hover {\n    background-color: #2980b9;\n    transform: translateY(-1px); /* GTK4+ */\n    box-shadow: 0 2px 4px rgba(0,0,0,0.2);\n}\n", "comment": "Effet de survol avec légère élévation et ombre."},
                    {"code": "GtkEntry:focus {\n    border-color: #f39c12;\n    box-shadow: 0 0 10px rgba(243, 156, 18, 0.7);\n}\n", "comment": "Mise en évidence forte de l'entrée quand elle a le focus."},
                    {"code": "GtkButton:active {\n    background-color: #1a5278;\n    transform: translateY(2px); /* GTK4+ */\n    box-shadow: none;\n}\n", "comment": "Styles le bouton quand il est pressé, avec un effet d'enfoncement."},
                    {"code": "GtkButton:disabled {\n    opacity: 0.4;\n    color: #cccccc;\n    background-color: #f0f0f0;\n}\n", "comment": "Rend les boutons désactivés très estompés."},
                    {"code": "GtkCheckButton:checked indicator {\n    background-color: #4CAF50;\n    border-color: #4CAF50;\n    border-radius: 4px;\n}\n", "comment": "Styles l'indicateur du checkbox quand il est coché."},
                    {"code": "GtkRadioButton:checked indicator {\n    background-color: #007bff;\n    border-color: #007bff;\n    border-radius: 50%;\n}\n", "comment": "Styles l'indicateur du radio button quand il est sélectionné."},
                    {"code": "GtkSwitch:checked slider {\n    background-color: white;\n    transform: translateX(22px); /* GTK4+ */\n}\n", "comment": "Déplace et style le curseur du switch quand il est activé."},
                    {"code": "GtkEntry:disabled {\n    background-color: #f5f5f5;\n    color: #a0a0a0;\n    font-style: italic;\n}\n", "comment": "Style une entrée désactivée."},
                    {"code": "GtkScale:disabled trough {\n    background-color: #e5e5e5;\n    opacity: 0.7;\n}\n", "comment": "Cible la piste d'un curseur désactivé avec une opacité."},
                    {"code": "GtkButton.suggested-action:hover {\n    background-color: #2ecc71;\n}\n", "comment": "Effet de survol pour un bouton d'action suggérée."},
                    {"code": "GtkButton.destructive-action:active {\n    background-color: #a02d38;\n}\n", "comment": "Effet de pression pour un bouton d'action destructive."},
                    {"code": "GtkEntry:not(:focus):not(:disabled) {\n    background-color: #fefefe;\n}\n", "comment": "Style une entrée qui n'a NI le focus NI n'est désactivée (combinaison de :not())."},
                    {"code": "GtkMenuItem:selected {\n    background-color: #e0f2f7;\n    color: #004d40;\n    font-weight: bold;\n}\n", "comment": "Style un élément de menu sélectionné."},
                    {"code": "GtkWindow:fullscreen {\n    background-color: black;\n    border-radius: 0;\n}\n", "comment": "Styles la fenêtre en mode plein écran."},
                    {"code": "GtkSearchEntry:empty {\n    font-style: italic;\n    color: #a0a0a0;\n}\n", "comment": "Style un champ de recherche vide (placeholder text)."},
                    {"code": "GtkButton:dir(rtl) {\n    margin-left: 10px; /* Adjust margin for RTL languages */\n}\n", "comment": "Exemple de pseudo-classe directionnelle (GTK4+)."},
                    {"code": "GtkImage:backdrop {\n    opacity: 0.7;\n}\n", "comment": "Style un widget en arrière-plan (quand la fenêtre n'est pas active, GTK4+)."},
                    {"code": "GtkCellView:selected {\n    background-color: #d1ecf1;\n}\n", "comment": "Style une cellule sélectionnée dans une GtkCellView."},
                ]
            },
            {
                "title": "5. Sélecteurs de Relation (Combinateurs)",
                "description": "Ciblent les widgets en fonction de leur position ou de leur hiérarchie par rapport à d'autres widgets.",
                "sub_sections": [
                    {
                        "sub_title": "  a. Combinateur Descendant (Espace) `parent descendant`",
                        "sub_examples": [
                            {"code": "GtkBox GtkLabel {\n    color: #3f51b5;\n    font-weight: 500;\n}\n", "comment": "Cible tous les `GtkLabel` *à l'intérieur* de n'importe quelle `GtkBox`."},
                            {"code": "GtkScrolledWindow GtkTextView {\n    padding: 15px;\n}\n", "comment": "Ajoute un padding au GtkTextView contenu dans une GtkScrolledWindow."},
                            {"code": "GtkToolbar GtkButton {\n    background-color: transparent;\n    border: none;\n    padding: 4px;\n}\n", "comment": "Rend les boutons de barre d'outils transparents et sans bordure."},
                            {"code": "GtkRevealer GtkLabel {\n    color: #7f8c8d;\n}\n", "comment": "Style les labels à l'intérieur d'un widget révélateur."},
                            {"code": "GtkDialog GtkButton.destructive-action {\n    margin-left: 10px;\n}\n", "comment": "Marge pour un bouton de suppression spécifique dans un dialogue."},
                        ]
                    },
                    {
                        "sub_title": "  b. Combinateur Enfant Direct (>) `parent > child`",
                        "sub_examples": [
                            {"code": "GtkStack > GtkStackPage {\n    padding: 10px;\n}\n", "comment": "Cible seulement les `GtkStackPage` qui sont des *enfants directs* d'un `GtkStack`."},
                            {"code": "GtkHeaderBar > GtkLabel {\n    color: white;\n    font-size: 16pt;\n}\n", "comment": "Style le titre principal directement dans la barre d'en-tête."},
                            {"code": "GtkListBox > GtkListBoxRow {\n    border-bottom: 1px solid #eee;\n}\n", "comment": "Ajoute une bordure inférieure à chaque ligne directe d'une liste."},
                            {"code": "GtkOverlay > GtkSpinner {\n    margin: auto; /* Centre le spinner dans l'overlay */\n}\n", "comment": "Centre un spinner qui est un enfant direct d'un GtkOverlay (GTK4+)."},
                            {"code": "GtkViewport > GtkBox {\n    padding: 10px;\n}\n", "comment": "Padding pour la boîte principale dans un GtkViewport."},
                        ]
                    },
                    {
                        "sub_title": "  c. Combinateur Frère Adjacents (+) `element + adjacent-sibling`",
                        "sub_examples": [
                            {"code": "GtkImage + GtkLabel {\n    margin-left: 8px;\n    font-weight: bold;\n}\n", "comment": "Style un label qui suit immédiatement une image (ex: icône + texte)."},
                            {"code": "GtkCheckButton + GtkLabel {\n    color: #333;\n}\n", "comment": "Style un label suivant une case à cocher."},
                            {"code": "GtkEntry + GtkButton {\n    margin-left: 5px;\n}\n", "comment": "Espacement entre une entrée et le bouton qui la suit."},
                        ]
                    },
                    {
                        "sub_title": "  d. Combinateur Frère Général (~) `element ~ general-siblings`",
                        "sub_examples": [
                            {"code": "GtkSeparator ~ GtkLabel {\n    margin-top: 15px;\n}\n", "comment": "Ajoute une marge supérieure à tous les labels qui suivent un séparateur."},
                            {"code": "GtkButton ~ GtkEntry {\n    background-color: #f0f8ff;\n}\n", "comment": "Change le fond de toutes les entrées qui suivent un bouton (au même niveau)."},
                        ]
                    },
                ]
            },
            {
                "title": "6. Sélecteurs d'Enfants Nth (:nth-child(), :nth-of-type())",
                "description": "Ciblent des enfants basés sur leur position (parmi tous les enfants ou parmi les enfants du même type). Très utile pour des listes, des tables, ou des alternances de styles.",
                "examples": [
                    {"code": "GtkListBoxRow:nth-child(2n+1) {\n    background-color: #f8f8f8;\n}\n", "comment": "Style les lignes impaires (1, 3, 5...) d'une GtkListBox."},
                    {"code": "GtkListBoxRow:nth-child(2n) {\n    background-color: #ffffff;\n}\n", "comment": "Style les lignes paires (2, 4, 6...) d'une GtkListBox."},
                    {"code": "GtkBox > *:nth-child(1) {\n    font-weight: bold;\n}\n", "comment": "Cible le premier enfant (n'importe quel type) d'une GtkBox."},
                    {"code": "GtkBox > GtkLabel:nth-of-type(1) {\n    font-size: 16pt;\n}\n", "comment": "Cible le premier label (parmi d'autres labels) d'une GtkBox."},
                    {"code": "GtkGrid > *:nth-child(4) {\n    background-color: #ffe0b2;\n}\n", "comment": "Cible le 4ème enfant (widget) dans une GtkGrid, utile pour des mises en page spécifiques."},
                    {"code": "GtkFlowBoxChild:nth-child(3n+1) {\n    margin-left: 0;\n}\n", "comment": "Pour aligner des éléments dans une GtkFlowBox (ex: tous les 3 éléments, reset la marge gauche)."},
                    {"code": "GtkStackPage:first-child {\n    border-top: 2px solid #3498db;\n}\n", "comment": "Cible la première page d'un GtkStack pour une bordure supérieure."},
                    {"code": "GtkRevealer:only-child {\n    margin: 20px;\n}\n", "comment": "Si un GtkRevealer est le seul enfant de son parent."},
                ]
            },
            {
                "title": "7. Propriétés CSS GTK Courantes et Avancées (Exemples Supplémentaires)",
                "description": "Une collection étendue de propriétés CSS fréquemment utilisées dans GTK, y compris des options plus avancées et spécifiques à GTK4.",
                "examples": [
                    {"code": "background-color: #f0f0f0; /* Couleur de fond */\nbackground-image: linear-gradient(to bottom, #f0f0f0, #e0e0e0); /* Dégradé */", "comment": "Couleurs de fond solides et dégradés linéaires."},
                    {"code": "color: #333; /* Couleur du texte */", "comment": "Définition de la couleur du texte."},
                    {"code": "border: 1px solid #ccc; /* Bordure uniforme */\nborder-top: 2px solid blue; /* Bordure spécifique */\nborder-bottom: none; /* Supprimer une bordure */", "comment": "Gestion complète des bordures."},
                    {"code": "border-radius: 5px; /* Tous les coins */\nborder-top-left-radius: 10px;\nborder-bottom-right-radius: 10px; /* Coins spécifiques */", "comment": "Arrondis des coins (uniformes ou spécifiques)."},
                    {"code": "padding: 10px 15px; /* Haut/Bas Gauche/Droite */\npadding-top: 5px;\npadding-left: 20px;", "comment": "Rembourrage interne (padding) pour le contenu des widgets."},
                    {"code": "margin: 8px 0; /* Haut/Bas Gauche/Droite */\nmargin-bottom: 12px;\nmargin-left: auto; /* Pousser à droite */", "comment": "Marge externe pour l'espacement entre widgets. `auto` pour l'alignement flexible."},
                    {"code": "font-family: 'Roboto Condensed', sans-serif;\nfont-size: 11pt;\nfont-weight: 500;\nfont-style: italic;\ntext-decoration: underline overline;", "comment": "Stylisme de police complet, y compris soulignement et surlignement."},
                    {"code": "min-width: 150px;\nmin-height: 30px;\nmax-width: 300px;\nmax-height: 100px;", "comment": "Définition des dimensions minimales et maximales."},
                    {"code": "opacity: 0.65; /* Transparence */", "comment": "Rend un widget semi-transparent."},
                    {"code": "box-shadow: 0 5px 15px rgba(0,0,0,0.25) inset; /* Ombre portée interne */\nbox-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Ombre portée externe */", "comment": "Ombres portées (internes et externes) pour la profondeur."},
                    {"code": "text-shadow: 1px 1px 4px rgba(0,0,0,0.5);", "comment": "Ombre pour le texte, améliore la lisibilité sur certains fonds."},
                    {"code": "transform: scale(1.1) rotate(5deg); /* GTK4+ */\ntransition: all 0.4s cubic-bezier(0.25, 0.1, 0.25, 1.0); /* GTK4+ */", "comment": "Combinaison de transformations (échelle, rotation) et transitions avec fonction de courbe."},
                    {"code": "outline: 2px solid #555;\noutline-offset: 3px;\noutline-radius: 6px; /* GTK4+ */", "comment": "Stylisme du contour de focus, avec décalage et rayon d'angle."},
                    {"code": "border-image: url('assets/pattern.png') 30 round;", "comment": "Utilisation d'une image répétée pour la bordure (avancé)."},
                    {"code": "cursor: zoom-in; /* GTK4+ */", "comment": "Changer le type de curseur de la souris (ex: pour des actions de zoom)."},
                    {"code": "color: @theme_primary_color; /* Variables de thème */\nbackground-color: @theme_accent_color;", "comment": "Référencement des couleurs définies par le thème GTK actif."},
                    {"code": "background-color: transparent;\nbackground-image: none;", "comment": "Rendre un widget complètement transparent (fond et image)."},
                    {"code": "background-clip: content-box; /* GTK4+ */", "comment": "Contrôle comment le fond s'étend (ici, seulement à la zone de contenu)."},
                    {"code": "border-style: dotted;\nborder-style: double;", "comment": "Styles de bordure alternatifs (pointillé, double)."},
                    {"code": "text-align: right; /* GTK4+ */", "comment": "Alignement du texte à droite."},
                    {"code": "text-transform: capitalize; /* GTK4+ */", "comment": "Mettre la première lettre de chaque mot en majuscule."},
                    {"code": "line-height: 1.6; /* Interligne plus grand */", "comment": "Augmentation de l'espacement entre les lignes de texte."},
                    {"code": "letter-spacing: 1px; /* Espacement des lettres */", "comment": "Augmentation de l'espacement entre les lettres."},
                    {"code": "font-feature-settings: 'smcp' on; /* GTK4+ */", "comment": "Contrôle des fonctionnalités OpenType (ex: petites capitales)."},
                    {"code": "padding-bottom: -3px; /* Padding négatif (GTK4+) */", "comment": "Permet un léger chevauchement ou ajustement fin."},
                    {"code": "GtkCheckButton:checked indicator {\n    background-image: -gtk-icontheme('emblem-ok-symbolic');\n    background-size: 80%;\n}\n", "comment": "Utilise une icône du thème GTK pour l'indicateur de coche (avancé, GTK4+)."},
                    {"code": "GtkTreeView row {\n    min-height: 30px;\n}\n", "comment": "Définit la hauteur minimale des lignes dans une vue en arborescence."},
                    {"code": "GtkToolButton:checked {\n    background-color: #a7d9f7;\n}\n", "comment": "Style un bouton de barre d'outils quand il est basculé (checked)."},
                    {"code": "GtkLinkButton {\n    color: #007bff;\n    text-decoration: underline;\n}\n", "comment": "Style un bouton de lien."},
                    {"code": "GtkLevelBar fill {\n    background-color: #2ecc71;\n}\n", "comment": "Style la barre de niveau (remplie)."},
                    {"code": "GtkLevelBar empty {\n    background-color: #e0e0e0;\n}\n", "comment": "Style la barre de niveau (vide)."},
                    {"code": "GtkAssistant page {\n    padding: 20px;\n}\n", "comment": "Style les pages d'un assistant."},
                    {"code": "GtkFixed {\n    border: 2px dashed #999;\n}\n", "comment": "Style un conteneur GtkFixed (utile pour le débogage de la disposition)."},
                    {"code": "GtkSearchBar {\n    background-color: #f7f9fb;\n    border-bottom: 1px solid #ddd;\n}\n", "comment": "Style la barre de recherche (souvent en haut de la fenêtre)."},
                    {"code": "GtkRevealer:transitioning {\n    opacity: 0.7;\n}\n", "comment": "Style le révélateur pendant sa transition d'affichage/masquage (GTK4+)."},
                    {"code": "GtkStack switcher {\n    background-color: #e8e8e8;\n    border-radius: 5px;\n}\n", "comment": "Style le sélecteur de page d'un GtkStack."},
                    {"code": "GtkStack switcher button {\n    padding: 8px 12px;\n}\n", "comment": "Style les boutons individuels du sélecteur de GtkStack."},
                    {"code": "GtkStack switcher button:checked {\n    background-color: #3498db;\n    color: white;\n}\n", "comment": "Style le bouton sélectionné du sélecteur de GtkStack."},
                    {"code": "GtkViewport {\n    background-color: #fcfcfc;\n    border: 1px solid #eee;\n}\n", "comment": "Style un GtkViewport (zone visible à l'intérieur d'un scrollable)."},
                    {"code": "GtkMenuScrollButton {\n    background-color: #ddd;\n}\n", "comment": "Style les boutons de défilement dans les longs menus."},
                    {"code": "GtkAboutDialog {\n    background-color: #fff;\n}\n", "comment": "Style une boîte de dialogue 'À propos'."},
                    {"code": "GtkSearchEntry .search-icon {\n    color: #888;\n}\n", "comment": "Style l'icône de recherche (GTK4+)."},
                    {"code": "GtkBox.linked > GtkButton {\n    border-radius: 0;\n}\n", "comment": "Enlève les bordures arrondies des boutons liés dans une boîte."},
                    {"code": "GtkBox.linked > GtkButton:first-child {\n    border-top-left-radius: 5px;\n    border-bottom-left-radius: 5px;\n}\n", "comment": "Arrondi le coin gauche du premier bouton lié."},
                    {"code": "GtkBox.linked > GtkButton:last-child {\n    border-top-right-radius: 5px;\n    border-bottom-right-radius: 5px;\n}\n", "comment": "Arrondi le coin droit du dernier bouton lié."},
                    {"code": "GtkShortcutsWindow {\n    background-color: #fcfcfc;\n}\n", "comment": "Style la fenêtre des raccourcis clavier."},
                    {"code": "GtkProgressBar:indeterminate progress {\n    background-image: linear-gradient(to right, #ccc, #666);\n    animation: pulse 1s infinite alternate; /* GTK4+ animation */\n}\n", "comment": "Style une barre de progression indéterminée avec une animation."},
                    {"code": "@keyframes pulse {\n    from { opacity: 0.6; }\n    to { opacity: 1; }\n}\n", "comment": "Définition d'une animation CSS Keyframes (GTK4+)."},
                    {"code": "GtkButton.circular {\n    border-radius: 50%;\n    min-width: 40px;\n    min-height: 40px;\n    padding: 0;\n}\n", "comment": "Rend un bouton parfaitement circulaire."},
                    {"code": "GtkWindow handle {\n    background-color: @theme_accent_color;\n}\n", "comment": "Style les poignées de redimensionnement de la fenêtre (GTK4+)."},
                    {"code": "GtkPicture {\n    border: 1px solid #ddd;\n    border-radius: 5px;\n}\n", "comment": "Style le nouveau widget GtkPicture (GTK4+)."},
                    {"code": "GtkOverlay .dim-overlay {\n    background-color: rgba(0,0,0,0.5);\n}\n", "comment": "Classe pour un overlay semi-transparent (pour assombrir le contenu en dessous)."},
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
                                                  font=ctk.CTkFont(size=19, weight="medium"),
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
    app = GtkCssSelectorsApp()