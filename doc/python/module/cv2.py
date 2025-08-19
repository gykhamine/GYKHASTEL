import customtkinter as ctk
import cv2
import numpy as np

class Cv2App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre principale ---
        self.title("Guide Ultime : Introduction à OpenCV (cv2)")
        self.geometry("1200x900")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        # --- Création du cadre de navigation latéral ---
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side="left", fill="y", padx=(10, 0), pady=10)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Menu de navigation",
                                                   compound="left", font=ctk.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.pack(padx=20, pady=(20, 10))

        # --- Création des boutons de navigation ---
        self.intro_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Introduction à OpenCV",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_intro)
        self.intro_button.pack(fill="x", padx=10, pady=5)
        
        self.files_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Fichiers et Sauvegarde",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_files)
        self.files_button.pack(fill="x", padx=10, pady=5)

        self.load_image_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Charger et Afficher une Image",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_load_image)
        self.load_image_button.pack(fill="x", padx=10, pady=5)

        self.manipulation_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Manipulation de Base",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_manipulation)
        self.manipulation_button.pack(fill="x", padx=10, pady=5)
        
        self.colors_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Espaces de Couleurs (HSV)",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               anchor="w", command=self.show_colors)
        self.colors_button.pack(fill="x", padx=10, pady=5)

        self.processing_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Traitement d'Image de Base",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               anchor="w", command=self.show_processing)
        self.processing_button.pack(fill="x", padx=10, pady=5)

        self.thresholding_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Seuillage (Thresholding)",
                                               fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                               anchor="w", command=self.show_thresholding)
        self.thresholding_button.pack(fill="x", padx=10, pady=5)

        self.edges_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Détection des contours (Canny)",
                                           fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.show_edges)
        self.edges_button.pack(fill="x", padx=10, pady=5)

        self.lines_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Détection de lignes (Hough)",
                                           fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.show_lines)
        self.lines_button.pack(fill="x", padx=10, pady=5)

        self.morphology_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Opérations de Morphologie",
                                           fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.show_morphology)
        self.morphology_button.pack(fill="x", padx=10, pady=5)
        
        self.pixels_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Opérations sur les Pixels",
                                           fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                           anchor="w", command=self.show_pixels)
        self.pixels_button.pack(fill="x", padx=10, pady=5)
        
        self.drawing_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Dessin sur une Image",
                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                       anchor="w", command=self.show_drawing)
        self.drawing_button.pack(fill="x", padx=10, pady=5)
        
        self.video_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Gestion de la Vidéo",
                                                 fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                 anchor="w", command=self.show_video)
        self.video_button.pack(fill="x", padx=10, pady=5)
        
        self.object_detection_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Détection d'objets",
                                                 fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                 anchor="w", command=self.show_object_detection)
        self.object_detection_button.pack(fill="x", padx=10, pady=5)
        

        # --- Création du cadre principal pour le contenu ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        
        self.content_textbox = ctk.CTkTextbox(self.content_frame, wrap="word", font=ctk.CTkFont(size=14))
        self.content_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.content_textbox.configure(state="disabled")

        # --- Démarrage sur le premier onglet ---
        self.show_intro()
        
    def set_content(self, title, text, code=None):
        self.content_textbox.configure(state="normal")
        self.content_textbox.delete("1.0", "end")
        
        self.content_textbox.insert("1.0", f"**{title}**\n\n{text}")
        if code:
            self.content_textbox.insert("end", f"\n\n```python\n{code}\n```")
        
        self.content_textbox.configure(state="disabled")

    def show_intro(self):
        content = (
            "**Introduction à la bibliothèque OpenCV (cv2)** 🤖\n\n"
            "**OpenCV** (Open Source Computer Vision Library) est une bibliothèque open source très populaire, conçue pour la vision par ordinateur et l'apprentissage automatique. Elle contient des milliers d'algorithmes optimisés pour le traitement d'images, la détection d'objets, le suivi de mouvement, et bien plus encore.\n\n"
            "En Python, on l'importe généralement sous l'alias **`cv2`**.\n\n"
            "**Concepts Clés :**\n"
            "- **Images comme des tableaux NumPy :** OpenCV représente les images comme des tableaux NumPy. Cela permet d'appliquer facilement des opérations mathématiques et des manipulations de tableaux, rendant le traitement d'image très performant.\n"
            "- **Formats de couleur BGR :** Contrairement à d'autres bibliothèques qui utilisent le format RGB (Rouge, Vert, Bleu), OpenCV stocke les couleurs dans l'ordre **BGR** (Bleu, Vert, Rouge). C'est une chose à garder en tête lorsque vous manipulez les canaux de couleur."
        )
        self.set_content("Introduction à OpenCV", content)
        
    def show_files(self):
        code_example = (
            "import cv2\n\n"
            "# Sauvegarder une image dans un format spécifique (ici JPG avec qualité 90)\n"
            "image = cv2.imread('image.png')\n"
            "cv2.imwrite('image_sauvegardee.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, 90])\n\n"
            "# Sauvegarder une vidéo avec un codec spécifié\n"
            "cap = cv2.VideoCapture(0)\n"
            "fourcc = cv2.VideoWriter_fourcc(*'XVID')\n"
            "out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))\n\n"
            "# Boucle de capture et d'écriture\n"
            "# (code ommis pour la clarté, voir section vidéo pour le code complet)\n\n"
            "# Gestion des erreurs : Vérifier si l'image a été lue avec succès\n"
            "image_corrompue = cv2.imread('fichier_inconnu.jpg')\n"
            "if image_corrompue is None:\n"
            "    print('Erreur: Le fichier image n\\'a pas pu être lu.')\n"
            "else:\n"
            "    print('Image lue avec succès.')"
        )
        content = (
            "**Gestion des fichiers et des sauvegardes** 📂\n\n"
            "OpenCV prend en charge une grande variété de formats de fichiers image et vidéo. La qualité des fichiers de sortie est un paramètre important à prendre en compte.\n\n"
            "**1. Formats d'images :**\n"
            "   - `cv2.imread()` et `cv2.imwrite()` supportent la plupart des formats courants, tels que `.png`, `.jpg`, `.bmp`, `.tiff`, etc. L'extension du nom de fichier passé à `imwrite()` détermine le format de sortie.\n"
            "   - **Qualité JPEG :** Pour les formats avec perte comme le JPEG, vous pouvez spécifier la qualité (de 0 à 100) en utilisant un paramètre optionnel. Une qualité de 90 est un bon compromis entre la taille du fichier et la fidélité visuelle.\n\n"
            "**2. Formats vidéo :**\n"
            "   - La fonction `cv2.VideoWriter()` nécessite un **codec** pour compresser les trames. Le `fourcc` (Four Character Code) est un identifiant unique pour le codec. Les codecs courants sont `XVID` (pour AVI), `MP4V` (pour MP4) et `MJPG`.\n\n"
            "**3. Gestion des erreurs :**\n"
            "   - Il est crucial de vérifier si les fonctions de lecture ont réussi. `cv2.imread()` renvoie `None` si le fichier n'est pas trouvé ou est corrompu. De même, l'attribut `isOpened()` de l'objet `VideoCapture` vérifie si une caméra est disponible. Intégrer ces vérifications dans votre code rendra votre application plus robuste."
        )
        self.set_content("Fichiers et Sauvegarde", content, code_example)

    def show_load_image(self):
        code_example = (
            "import cv2\n\n"
            "# Charger une image\n"
            "image = cv2.imread('chemin/vers/image.jpg')\n\n"
            "# Afficher l'image dans une fenêtre\n"
            "cv2.imshow('Ma Première Image', image)\n\n"
            "# Attendre une pression de touche\n"
            "cv2.waitKey(0)\n\n"
            "# Détruire toutes les fenêtres\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Charger, Afficher et Enregistrer une Image** 🖼️\n\n"
            "La base de tout traitement d'image est de savoir comment interagir avec les fichiers image. Les fonctions principales sont `cv2.imread()`, `cv2.imshow()`, et `cv2.imwrite()`.\n\n"
            "**1. Charger une image :**\n"
            "   - `cv2.imread('chemin/vers/image.jpg', [flag])` lit une image depuis un fichier. Le second argument est optionnel et permet de spécifier le mode de lecture (couleur, niveaux de gris, etc.).\n\n"
            "**2. Afficher une image :**\n"
            "   - `cv2.imshow('Nom de la fenêtre', image)` crée une fenêtre et y affiche l'image.\n\n"
            "**3. Enregistrer une image :**\n"
            "   - `cv2.imwrite('nouvelle_image.png', image)` enregistre l'image sur le disque.\n\n"
            "**4. Contrôle de la fenêtre :**\n"
            "   - `cv2.waitKey(0)` met le programme en pause et attend qu'une touche soit pressée. Si l'argument est `1`, il attend 1 milliseconde et continue.\n"
            "   - `cv2.destroyAllWindows()` ferme toutes les fenêtres créées par OpenCV."
        )
        self.set_content("Charger et Afficher une Image", content, code_example)
        
    def show_manipulation(self):
        code_example = (
            "import cv2\n\n"
            "image = cv2.imread('image.jpg')\n\n"
            "# Redimensionner l'image à 200x200 pixels\n"
            "resized = cv2.resize(image, (200, 200))\n\n"
            "# Récupérer les dimensions de l'image\n"
            "h, w, c = image.shape\n"
            "# Redimensionner avec un facteur d'échelle (50% de la taille originale)\n"
            "resized_scale = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)\n\n"
            "# Recadrer une partie de l'image (de la ligne 50 à 150 et de la colonne 100 à 300)\n"
            "cropped = image[50:150, 100:300]\n\n"
            "# Afficher les images (redimensionnée et recadrée)\n"
            "cv2.imshow('Original', image)\n"
            "cv2.imshow('Recadrée', cropped)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Manipulation d'Images : Redimensionnement et Recadrage** ✂️\n\n"
            "Les images sont des tableaux NumPy, ce qui rend les manipulations très intuitives.\n\n"
            "**1. Redimensionnement :**\n"
            "   - La fonction `cv2.resize()` permet de changer la taille d'une image. Vous pouvez spécifier les dimensions exactes ou utiliser des facteurs d'échelle (`fx`, `fy`).\n\n"
            "**2. Recadrage (Cropping) :**\n"
            "   - Comme pour n'importe quel tableau NumPy, vous pouvez accéder à des portions d'image en utilisant le découpage (`slicing`). Une image est un tableau `[hauteur, largeur, canaux]`. Un recadrage se fait donc via `image[y_start:y_end, x_start:x_end]`."
        )
        self.set_content("Manipulation d'Images de Base", content, code_example)

    def show_colors(self):
        code_example = (
            "import cv2\n\n"
            "image = cv2.imread('image.jpg')\n\n"
            "# Convertir l'image de l'espace BGR vers HSV\n"
            "hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)\n\n"
            "# Définir la plage de couleurs pour la détection (ex: pour la couleur verte)\n"
            "lower_green = np.array([35, 100, 100])\n"
            "upper_green = np.array([85, 255, 255])\n\n"
            "# Créer un masque qui ne garde que les pixels dans la plage verte\n"
            "mask = cv2.inRange(hsv_image, lower_green, upper_green)\n\n"
            "# Afficher les images\n"
            "cv2.imshow('Image Originale', image)\n"
            "cv2.imshow('Masque Vert', mask)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Espaces de Couleurs (BGR, HSV)** 🎨\n\n"
            "Les images peuvent être représentées dans différents espaces de couleurs. En plus du BGR, le format **HSV (Hue, Saturation, Value)** est particulièrement utile pour la détection d'objets par couleur, car il sépare la teinte de la luminosité.\n\n"
            "**1. Conversion BGR vers HSV :**\n"
            "   - `cv2.cvtColor()` est la fonction clé pour passer d'un espace de couleur à un autre.\n\n"
            "**2. Création d'un masque :**\n"
            "   - `cv2.inRange()` est une fonction très puissante qui permet de créer un **masque binaire**. Ce masque est une image en noir et blanc où les pixels blancs correspondent aux pixels dont la couleur se trouve dans la plage spécifiée (ici, la plage de vert), et les pixels noirs aux autres. C'est la base de la segmentation par couleur."
        )
        self.set_content("Espaces de Couleurs (HSV)", content, code_example)

    def show_processing(self):
        code_example = (
            "import cv2\n\n"
            "image = cv2.imread('image.jpg')\n\n"
            "# Convertir en niveaux de gris\n"
            "gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n\n"
            "# Appliquer un flou gaussien\n"
            "blurred_image = cv2.GaussianBlur(image, (5, 5), 0)\n\n"
            "# Afficher les images\n"
            "cv2.imshow('Original', image)\n"
            "cv2.imshow('Niveaux de gris', gray_image)\n"
            "cv2.imshow('Flou', blurred_image)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Traitement d'Image de Base : Niveaux de gris et Flou** 🌫️\n\n"
            "OpenCV propose de nombreuses fonctions pour modifier l'apparence et le contenu des images.\n\n"
            "**1. Conversion en niveaux de gris :**\n"
            "   - La fonction `cv2.cvtColor()` est l'une des plus utilisées. Elle permet de convertir une image d'un espace de couleur à un autre, comme de BGR vers les niveaux de gris (`cv2.COLOR_BGR2GRAY`).\n\n"
            "**2. Flou gaussien :**\n"
            "   - `cv2.GaussianBlur()` applique un flou à l'image. Le second argument est la taille du noyau du filtre (ici `(5, 5)`), qui doit être un nombre impair. Plus le noyau est grand, plus le flou est prononcé."
        )
        self.set_content("Traitement d'Image de Base", content, code_example)
        
    def show_thresholding(self):
        code_example = (
            "import cv2\n\n"
            "image = cv2.imread('image.jpg', 0) # Charger directement en niveaux de gris\n\n"
            "# Seuillage binaire. Les pixels > 127 deviennent 255 (blanc), les autres 0 (noir)\n"
            "ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)\n\n"
            "# Seuillage adaptatif. Le seuil est calculé localement pour chaque zone\n"
            "adaptive_thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)\n\n"
            "cv2.imshow('Original (gris)', image)\n"
            "cv2.imshow('Seuillage Binaire', thresh)\n"
            "cv2.imshow('Seuillage Adaptatif', adaptive_thresh)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Seuillage (Thresholding)** 🔳\n\n"
            "Le seuillage est une technique fondamentale qui consiste à convertir une image en niveaux de gris en une image binaire (noir et blanc). Cela permet d'isoler des objets de l'arrière-plan en éliminant les variations de lumière.\n\n"
            "**1. Seuillage simple :**\n"
            "   - `cv2.threshold()` applique un seuil global à l'image. Si la valeur d'un pixel est supérieure au seuil, elle prend une valeur, sinon elle en prend une autre.\n\n"
            "**2. Seuillage adaptatif :**\n"
            "   - `cv2.adaptiveThreshold()` est plus avancé. Il ne définit pas un seuil unique pour toute l'image, mais calcule un seuil différent pour chaque petite zone. C'est très utile pour les images avec un éclairage variable."
        )
        self.set_content("Seuillage (Thresholding)", content, code_example)

    def show_edges(self):
        code_example = (
            "import cv2\n\n"
            "image = cv2.imread('image.jpg', 0) # Charger en niveaux de gris\n\n"
            "# Détection de contours avec l'algorithme de Canny\n"
            "edges = cv2.Canny(image, 100, 200)\n\n"
            "# Les valeurs 100 et 200 sont des seuils minimaux et maximaux pour la détection.\n\n"
            "cv2.imshow('Original (gris)', image)\n"
            "cv2.imshow('Détection de contours (Canny)', edges)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Détection des contours (Edge Detection) avec Canny** 🔲\n\n"
            "La détection de contours est une technique qui permet de trouver les limites des objets. L'algorithme de **Canny** est l'un des plus populaires pour cette tâche.\n\n"
            "**Fonctionnement de `cv2.Canny()` :**\n"
            "   - La fonction prend l'image en niveaux de gris et deux seuils : `minVal` et `maxVal`. Elle trouve les gradients d'intensité, et les pixels dont le gradient est supérieur à `maxVal` sont considérés comme des contours forts. Les pixels entre `minVal` et `maxVal` sont considérés comme des contours s'ils sont connectés à des contours forts. Les pixels sous `minVal` sont ignorés.\n\n"
            "**Utilité :**\n"
            "   - Les contours sont des informations essentielles pour l'identification d'objets, la reconnaissance de formes, et d'autres tâches complexes en vision par ordinateur."
        )
        self.set_content("Détection des contours (Canny)", content, code_example)
        
    def show_lines(self):
        code_example = (
            "import cv2\n"
            "import numpy as np\n\n"
            "image = cv2.imread('image_avec_lignes.jpg')\n"
            "gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n"
            "edges = cv2.Canny(gray, 50, 150, apertureSize=3)\n\n"
            "# Détection de lignes avec la transformée de Hough\n"
            "lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)\n\n"
            "if lines is not None:\n"
            "    for line in lines:\n"
            "        x1, y1, x2, y2 = line[0]\n"
            "        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)\n\n"
            "cv2.imshow('Image avec lignes detectees', image)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Détection de lignes avec la transformée de Hough** 📏\n\n"
            "La détection de lignes est une étape clé pour des applications comme la détection des voies sur une route. L'approche la plus courante est la **transformée de Hough**.\n\n"
            "**Fonctionnement :**\n"
            "   - La méthode `cv2.HoughLinesP()` est une version optimisée qui détecte des segments de ligne, ce qui est plus utile en pratique. Elle prend en entrée une image avec des contours (obtenue avec Canny), puis recherche des alignements de pixels qui pourraient former des lignes.\n\n"
            "**Paramètres clés :**\n"
            "   - `rho` et `theta` : la résolution de l'accumulateur de Hough.\n"
            "   - `threshold` : le nombre minimal de points qui doivent se trouver sur une ligne pour qu'elle soit détectée.\n"
            "   - `minLineLength` et `maxLineGap` : permettent de contrôler la longueur minimale d'une ligne détectée et l'espace maximal entre des segments de ligne pour qu'ils soient considérés comme une seule ligne."
        )
        self.set_content("Détection de lignes (Hough)", content, code_example)


    def show_morphology(self):
        code_example = (
            "import cv2\n"
            "import numpy as np\n\n"
            "image = cv2.imread('image.jpg', 0)\n"
            "ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)\n\n"
            "# Créer un noyau 3x3\n"
            "kernel = np.ones((3,3), np.uint8)\n\n"
            "# Opération de dilatation (épaissit les contours)\n"
            "dilated = cv2.dilate(thresh, kernel, iterations=1)\n\n"
            "# Opération d'érosion (amincit les contours)\n"
            "eroded = cv2.erode(thresh, kernel, iterations=1)\n\n"
            "cv2.imshow('Original Binaire', thresh)\n"
            "cv2.imshow('Dilatation', dilated)\n"
            "cv2.imshow('Érosion', eroded)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Opérations de Morphologie (Érosion et Dilatation)** ➕➖\n\n"
            "Les opérations de morphologie sont des techniques de traitement d'images basées sur les formes. Elles sont principalement utilisées sur des images binaires (noir et blanc) pour nettoyer les résultats du seuillage ou de la détection de contours.\n\n"
            "**1. Dilatation :**\n"
            "   - `cv2.dilate()` « épaissit » les objets d'une image binaire. Cela peut aider à combler de petits trous ou à connecter des objets qui sont très proches.\n\n"
            "**2. Érosion :**\n"
            "   - `cv2.erode()` « amincit » les objets. Cette opération est utile pour retirer le bruit indésirable ou pour séparer des objets qui sont légèrement connectés.\n\n"
            "Ces deux opérations utilisent un **noyau (kernel)**, qui est une petite matrice déterminant la forme et la taille de l'opération."
        )
        self.set_content("Opérations de Morphologie", content, code_example)

    def show_pixels(self):
        code_example = (
            "import cv2\n\n"
            "image = cv2.imread('image.jpg')\n\n"
            "# Accéder à la valeur d'un pixel (Bleu, Vert, Rouge) à la position (100, 150)\n"
            "pixel_value = image[100, 150]\n"
            "print(f'Valeur du pixel (B, G, R) à (150, 100) : {pixel_value}')\n\n"
            "# Modifier la valeur d'un pixel pour le rendre blanc (255, 255, 255)\n"
            "image[100, 150] = [255, 255, 255]\n\n"
            "# Accéder uniquement au canal Bleu du pixel\n"
            "blue_value = image[100, 150, 0]\n"
            "print(f'Valeur du canal bleu du pixel : {blue_value}')\n\n"
            "cv2.imshow('Image modifiée', image)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Opérations sur les Pixels** 🎨\n\n"
            "Puisque les images sont des tableaux NumPy, vous pouvez accéder et modifier chaque pixel individuellement.\n\n"
            "**Accès et modification :**\n"
            "- L'accès à un pixel se fait par ses coordonnées `y` et `x` (`image[y, x]`). L'ordre est important : `[hauteur, largeur]`, et non l'inverse.\n"
            "- La valeur renvoyée est un tableau à 3 éléments, représentant les canaux de couleur **B, G, R** (Bleu, Vert, Rouge).\n"
            "- Vous pouvez accéder à un canal spécifique en ajoutant l'indice à la fin : `image[y, x, canal]` où `0` est le bleu, `1` est le vert, et `2` est le rouge."
        )
        self.set_content("Opérations sur les Pixels", content, code_example)
        
    def show_drawing(self):
        code_example = (
            "import cv2\n"
            "import numpy as np\n\n"
            "# Créer une image vide noire (500x500 pixels)\n"
            "image = np.zeros((500, 500, 3), dtype='uint8')\n\n"
            "# Dessiner une ligne verte (de (0,0) à (500,500))\n"
            "cv2.line(image, (0, 0), (500, 500), (0, 255, 0), 2)\n\n"
            "# Dessiner un rectangle bleu\n"
            "cv2.rectangle(image, (100, 100), (300, 300), (255, 0, 0), -1)\n\n"
            "# Dessiner un cercle rouge\n"
            "cv2.circle(image, (250, 250), 75, (0, 0, 255), 5)\n\n"
            "# Ajouter du texte blanc\n"
            "cv2.putText(image, 'OpenCV', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)\n\n"
            "cv2.imshow('Dessins', image)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Dessiner des formes et du texte sur une image** 🖊️\n\n"
            "OpenCV offre des fonctions pratiques pour dessiner des formes géométriques et du texte directement sur un tableau NumPy.\n\n"
            "**1. Dessiner des lignes et des formes :**\n"
            "   - `cv2.line()`, `cv2.rectangle()`, `cv2.circle()`. Ces fonctions prennent en arguments l'image, les coordonnées, la couleur (en BGR), et l'épaisseur du trait. Pour remplir une forme, l'épaisseur doit être `-1`.\n\n"
            "**2. Ajouter du texte :**\n"
            "   - `cv2.putText()` est utilisée pour ajouter du texte. Elle prend en arguments le texte, les coordonnées du point de départ, la police de caractères, l'échelle, la couleur et l'épaisseur."
        )
        self.set_content("Dessin sur une Image", content, code_example)
    
    def show_video(self):
        code_example = (
            "import cv2\n\n"
            "# Capture depuis une webcam (0) ou une caméra IP (URL)\n"
            "# Pour une caméra IP, utilisez une URL comme: 'rtsp://user:pass@ip:port/stream_path'\n"
            "cap = cv2.VideoCapture(0) # 'http://ip:port/video' ou 'rtsp://user:pass@ip:port/stream'\n\n"
            "# Configuration de l'enregistrement\n"
            "fourcc = cv2.VideoWriter_fourcc(*'XVID')\n"
            "out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))\n\n"
            "if not cap.isOpened():\n"
            "    print('Erreur: Impossible d\\'ouvrir la caméra ou la source vidéo')\n"
            "else:\n"
            "    while True:\n"
            "        ret, frame = cap.read()\n"
            "        if not ret:\n"
            "            break\n\n"
            "        # Enregistrer la trame\n"
            "        out.write(frame)\n\n"
            "        # Afficher la trame\n"
            "        cv2.imshow('Webcam/IP Camera', frame)\n\n"
            "        if cv2.waitKey(1) & 0xFF == ord('q'):\n"
            "            break\n\n"
            "cap.release()\n"
            "out.release()\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Gestion des flux vidéo et caméras IP** 📹\n\n"
            "OpenCV est conçu pour gérer non seulement les images, mais aussi les flux vidéo en direct. Cela inclut la capture depuis une webcam, un fichier vidéo, ou une **caméra IP**.\n\n"
            "**1. Lecture depuis une caméra IP :**\n"
            "   - Au lieu de l'index de la caméra (`0`), vous passez l'URL de streaming de votre caméra IP à `cv2.VideoCapture()`. Le format de l'URL varie selon le modèle de la caméra et le protocole (généralement `rtsp://` ou `http://`). Vous pouvez trouver le bon format dans la documentation de votre caméra.\n\n"
            "**2. Enregistrement d'un flux vidéo :**\n"
            "   - L'objet `cv2.VideoWriter()` vous permet de créer un fichier vidéo et d'y écrire chaque trame capturée. Vous devez spécifier le nom du fichier, le codec (`fourcc`), le nombre d'images par seconde (`fps`) et les dimensions (`frameSize`)."
        )
        self.set_content("Gestion de la Vidéo", content, code_example)
        
    def show_object_detection(self):
        code_example = (
            "import cv2\n\n"
            "# Il faut un fichier de classifieur en cascade (haarcascade)\n"
            "# Ce fichier est généralement inclus dans l'installation d'OpenCV\n"
            "face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n\n"
            "image = cv2.imread('visages.jpg')\n"
            "gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n\n"
            "# Détecter les visages dans l'image en niveaux de gris\n"
            "faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)\n\n"
            "# Dessiner des rectangles autour des visages détectés\n"
            "for (x, y, w, h) in faces:\n"
            "    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)\n\n"
            "cv2.imshow('Detection de visages', image)\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()"
        )
        content = (
            "**Détection d'objets : classifieurs en cascade** 🕵️\n\n"
            "OpenCV inclut des algorithmes de détection d'objets, dont le plus connu est le **classifieur en cascade de Haar**. Il est souvent utilisé pour la détection de visages, d'yeux ou de corps, car des modèles pré-entraînés sont disponibles.\n\n"
            "**Fonctionnement :**\n"
            "   - `cv2.CascadeClassifier()` charge un modèle pré-entraîné (ici, pour les visages).\n"
            "   - `face_cascade.detectMultiScale()` effectue la détection. Il renvoie une liste de rectangles `(x, y, w, h)` qui correspondent aux objets détectés.\n"
            "   - Vous pouvez ensuite dessiner ces rectangles sur l'image originale pour visualiser les résultats.\n\n"
            "**Note :** Pour la détection d'objets plus modernes et performante, on utilise aujourd'hui des réseaux de neurones profonds (`cv2.dnn`), mais l'approche par classifieur de cascade est un excellent point de départ."
        )
        self.set_content("Détection d'objets", content, code_example)

if __name__ == "__main__":
    app = Cv2App()
    app.mainloop()