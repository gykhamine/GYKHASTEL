import customtkinter as ctk
import numpy as np
import cv2  # Importation d'OpenCV
import threading
import time
from tkinter import Toplevel, Label

class NumPyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre principale ---
        self.title("Guide Ultime : NumPy et OpenCV")
        self.geometry("1200x900")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # --- Création du cadre de navigation latéral ---
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side="left", fill="y", padx=(10, 0), pady=10)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Menu de navigation",
                                                   compound="left", font=ctk.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.pack(padx=20, pady=(20, 10))

        # --- Création des boutons de navigation ---
        self.intro_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Introduction à NumPy",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_intro)
        self.intro_button.pack(fill="x", padx=10, pady=5)
        
        self.ndim_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Tableaux N-dimensionnels",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_ndim)
        self.ndim_button.pack(fill="x", padx=10, pady=5)
        
        self.basic_ops_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Opérations de base",
                                          fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                          anchor="w", command=self.show_basic_ops)
        self.basic_ops_button.pack(fill="x", padx=10, pady=5)

        self.opencv_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="NumPy et OpenCV",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_opencv)
        self.opencv_button.pack(fill="x", padx=10, pady=5)

        self.masking_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Masquage et Filtrage",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_masking)
        self.masking_button.pack(fill="x", padx=10, pady=5)

        self.linear_algebra_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Algèbre linéaire",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            anchor="w", command=self.show_linear_algebra)
        self.linear_algebra_button.pack(fill="x", padx=10, pady=5)

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
            "**Introduction à NumPy** 🤖\n\n"
            "**NumPy** est la pierre angulaire de l'écosystème scientifique de Python. Sa structure de données principale, le **`ndarray`**, est une grille de valeurs multi-dimensionnelle qui permet des opérations numériques complexes de manière incroyablement rapide et efficace.\n\n"
            "**Pourquoi NumPy est-il si puissant ?**\n"
            "- **Optimisation en C et Fortran :** Les opérations sont compilées et s'exécutent à des vitesses proches du C, bien plus rapidement que les boucles `for` de Python.\n"
            "- **Efficacité mémoire :** Les `ndarrays` allouent des blocs de mémoire contigus, ce qui permet de stocker et d'accéder aux données de manière très efficace, surtout pour les grands ensembles de données.\n"
            "- **La base de tout :** NumPy est la fondation sur laquelle sont bâties de nombreuses bibliothèques populaires comme **Pandas**, **SciPy**, **Matplotlib** et **Scikit-learn**."
        )
        self.set_content("Introduction à NumPy", content)

    def show_ndim(self):
        code_example = (
            "import numpy as np\n\n"
            "# Tableau 1D : un vecteur\n"
            "vec = np.array([1, 2, 3, 4])\n"
            "print(f'Tableau 1D : {vec}')\n"
            "print(f'Dimensions (ndim) : {vec.ndim}')\n"
            "print(f'Forme (shape) : {vec.shape}')\n\n"
            "# Tableau 2D : une matrice (lignes x colonnes)\n"
            "mat = np.array([[10, 20], [30, 40], [50, 60]])\n"
            "print(f'\\nTableau 2D :\\n{mat}')\n"
            "print(f'Dimensions (ndim) : {mat.ndim}')\n"
            "print(f'Forme (shape) : {mat.shape}')\n\n"
            "# Tableau 3D : un tenseur (profondeur x lignes x colonnes)\n"
            "tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])\n"
            "print(f'\\nTableau 3D :\\n{tensor}')\n"
            "print(f'Dimensions (ndim) : {tensor.ndim}')\n"
            "print(f'Forme (shape) : {tensor.shape}')\n\n"
            "# Accéder à un élément dans un tableau 3D\n"
            "print(f'\\nPremier élément du tenseur : {tensor[0, 0, 0]}')\n"
            "print(f'Deuxième ligne de la première matrice : {tensor[0, 1, :]}')\n"
        )
        content = (
            "**Les tableaux à N dimensions (ndarrays)** 📈\n\n"
            "Le **`ndarray`** est le cœur de NumPy. Il est caractérisé par sa **forme** (`shape`) et son **nombre de dimensions** (`ndim`). C'est cette capacité à manipuler facilement des données de n'importe quelle dimension qui rend NumPy si polyvalent.\n\n"
            "**- `ndim` (Nombre de dimensions) :** Un simple entier qui représente le nombre d'axes du tableau.\n"
            "    - `ndim = 1` pour un **vecteur**.\n"
            "    - `ndim = 2` pour une **matrice** (utile pour les données tabulaires).\n"
            "    - `ndim = 3` ou plus pour un **tenseur** (essentiel en apprentissage automatique et en traitement d'images).\n\n"
            "**- `shape` (Forme) :** Un tuple d'entiers qui donne la taille du tableau le long de chaque dimension. Par exemple, `(3, 4)` signifie 3 lignes et 4 colonnes. Pour un tableau 3D, `(2, 2, 2)` signifie 2 matrices, chacune ayant 2 lignes et 2 colonnes."
        )
        self.set_content("Tableaux N-dimensionnels", content, code_example)
        
    def show_basic_ops(self):
        code_example = (
            "import numpy as np\n\n"
            "arr1 = np.array([10, 20, 30])\n"
            "arr2 = np.array([1, 2, 3])\n"
            "mat = np.array([[1, 2, 3], [4, 5, 6]])\n\n"
            "# --- Opérations mathématiques élément par élément --- \n"
            "sum_arr = arr1 + arr2\n"
            "mult_arr = arr1 * 2\n"
            "print(f'Somme des tableaux : {sum_arr}')\n"
            "print(f'Multiplication par 2 : {mult_arr}')\n\n"
            "# --- Indexation et slicing --- \n"
            "print(f'\\nPremier élément de arr1 : {arr1[0]}')\n"
            "print(f'Troisième colonne de mat : {mat[:, 2]}')\n"
            "print(f'Sous-matrice :\\n{mat[0:1, 1:3]}')\n"
        )
        content = (
            "**Opérations de base : calcul, indexation et slicing** 🔢\n\n"
            "NumPy se distingue par sa **vectorisation**. Au lieu d'utiliser des boucles, les opérations mathématiques s'appliquent sur chaque élément de manière parallèle, ce qui est extrêmement rapide.\n\n"
            "**1. Opérations mathématiques vectorisées :**\n"
            "   - Des opérateurs comme `+`, `-`, `*` sont surchargés pour opérer sur les tableaux de manière élément par élément. Par exemple, `arr1 + arr2` additionne l'élément 0 d'arr1 avec l'élément 0 d'arr2, et ainsi de suite.\n\n"
            "**2. Indexation et découpage (`slicing`) :**\n"
            "   - L'indexation est plus puissante que celle des listes Python. `mat[ligne, colonne]` vous donne un accès direct à n'importe quel élément. Vous pouvez utiliser le slicing (`[début:fin]`) pour sélectionner des sous-ensembles du tableau, comme une ligne entière (`mat[0, :]`) ou une colonne entière (`mat[:, 2]`)."
        )
        self.set_content("Opérations de base", content, code_example)

    def show_opencv(self):
        # Affiche le code d'exemple dans la zone de texte
        code_example = (
            "import numpy as np\n"
            "import cv2\n\n"
            "# Créer une image noire de 480x640 pixels avec 3 canaux (couleur BGR)\n"
            "image = np.zeros((480, 640, 3), dtype=np.uint8)\n\n"
            "# Les images dans OpenCV sont des tableaux NumPy !\n"
            "print(f'Type de l\\'objet image : {type(image)}')\n"
            "print(f'Forme de l\\'image (hauteur, largeur, canaux) : {image.shape}')\n\n"
            "# Dessiner un cercle blanc au centre de l'image\n"
            "cv2.circle(image, (320, 240), 100, (255, 255, 255), -1)\n\n"
            "# Dessiner une ligne rouge\n"
            "cv2.line(image, (0, 0), (640, 480), (0, 0, 255), 5)\n\n"
            "# Créer une fenêtre OpenCV pour afficher l'image\n"
            "cv2.imshow('Image de demonstration', image)\n\n"
            "# Attendre l'appui sur une touche et fermer la fenêtre\n"
            "cv2.waitKey(0)\n"
            "cv2.destroyAllWindows()\n"
        )
        
        content = (
            "**NumPy et OpenCV : la vision par ordinateur** 👁️\n\n"
            "**OpenCV** est une bibliothèque leader en **vision par ordinateur**. Son intégration avec NumPy est fondamentale : elle représente les images comme des tableaux NumPy. Un tableau NumPy est une structure de données idéale pour manipuler les pixels d'une image de manière efficace.\n\n"
            "**Comment ça marche ?**\n"
            "   - Une image en couleur est un tableau 3D : `(hauteur, largeur, canaux)`. Chaque pixel est un tableau 1D de 3 valeurs (`[B, G, R]` pour le Bleu, le Vert et le Rouge).\n"
            "   - Le traitement d'image devient une simple manipulation de tableaux. Par exemple, pour mettre une image en noir et blanc, il suffit de manipuler les valeurs des pixels dans le tableau NumPy correspondant.\n\n"
            "**Exécution de l'exemple :**\n"
            "L'exemple ci-dessous va créer une image dans une fenêtre distincte d'OpenCV. L'exécution de ce code montrera une fenêtre pop-up avec une image générée par NumPy. Il vous suffira de fermer la fenêtre pour continuer."
        )

        # Créer l'image et l'afficher dans un thread séparé
        threading.Thread(target=self.run_opencv_demo).start()
        self.set_content("NumPy et OpenCV", content, code_example)
        
    def run_opencv_demo(self):
        try:
            demo_image = np.zeros((480, 640, 3), dtype=np.uint8)
            cv2.circle(demo_image, (320, 240), 100, (255, 255, 255), -1)
            cv2.line(demo_image, (0, 0), (640, 480), (0, 0, 255), 5)
            
            # Afficher l'image dans une fenêtre OpenCV
            cv2.imshow('Image de demonstration', demo_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except cv2.error as e:
            print(f"Erreur OpenCV : {e}")

    def show_masking(self):
        code_example = (
            "import numpy as np\n\n"
            "arr = np.array([10, 5, 20, 8, 15, 30])\n\n"
            "# --- Créer un masque booléen --- \n"
            "mask = arr > 12\n"
            "print(f'Tableau original : {arr}')\n"
            "print(f'Masque booléen : {mask}')\n\n"
            "# --- Appliquer le masque pour filtrer le tableau --- \n"
            "filtered_arr = arr[mask]\n"
            "print(f'\\nÉléments filtrés (> 12) : {filtered_arr}')\n\n"
            "# --- Remplacer les valeurs qui correspondent au masque --- \n"
            "arr[arr > 20] = 99\n"
            "print(f'\\nTableau avec les valeurs modifiées : {arr}')\n"
        )
        content = (
            "**Masquage et filtrage de tableaux** 🎭\n\n"
            "Une des fonctionnalités les plus puissantes de NumPy est l'**indexation booléenne**, également appelée **masquage**. Elle permet de sélectionner des éléments d'un tableau en fonction d'une condition.\n\n"
            "**Comment ça marche ?**\n"
            "   - Vous commencez par créer un tableau de booléens (`True` ou `False`) en utilisant une condition de comparaison (par exemple, `arr > 12`). Ce tableau est appelé un **masque**.\n"
            "   - Lorsque vous utilisez ce masque pour indexer le tableau original (`arr[mask]`), NumPy renvoie uniquement les éléments qui correspondent à la valeur `True`.\n"
            "   - Cette technique est incroyablement utile pour le nettoyage de données, le remplacement de valeurs ou le filtrage complexe, et est beaucoup plus lisible et performante qu'une boucle `for` classique en Python."
        )
        self.set_content("Masquage et Filtrage", content, code_example)

    def show_linear_algebra(self):
        code_example = (
            "import numpy as np\n\n"
            "A = np.array([[1, 2], [3, 4]])\n"
            "B = np.array([[5, 6], [7, 8]])\n\n"
            "print(f'Matrice A :\\n{A}')\n"
            "print(f'\\nMatrice B :\\n{B}')\n\n"
            "# --- Produit matriciel --- \n"
            "dot_product = A @ B  # ou np.dot(A, B)\n"
            "print(f'\\nProduit matriciel (A @ B) :\\n{dot_product}')\n\n"
            "# --- Transposition --- \n"
            "A_transposed = A.T\n"
            "print(f'\\nTransposée de A :\\n{A_transposed}')\n\n"
            "# --- Déterminant --- \n"
            "det_A = np.linalg.det(A)\n"
            "print(f'\\nDéterminant de A : {det_A:.2f}')\n\n"
            "# --- Inversion de matrice --- \n"
            "inv_A = np.linalg.inv(A)\n"
            "print(f'\\nInverse de A :\\n{inv_A}')\n"
        )
        content = (
            "**Algèbre linéaire avec NumPy** 📐\n\n"
            "NumPy est le couteau suisse pour les opérations d'algèbre linéaire. Le sous-module **`np.linalg`** est une collection de fonctions pour les calculs matriciels.\n\n"
            "**Opérations courantes :**\n"
            "- **Produit matriciel :** L'opérateur `@` (ou la fonction `np.dot()`) est utilisé pour effectuer le produit matriciel, qui est un concept central en algèbre linéaire.\n"
            "- **Transposition :** L'attribut `.T` permet de transposer une matrice.\n"
            "- **Déterminant :** `np.linalg.det()` calcule le déterminant d'une matrice.\n"
            "- **Inverse :** `np.linalg.inv()` calcule l'inverse d'une matrice, ce qui est essentiel pour résoudre des systèmes d'équations linéaires.\n\n"
            "Ces fonctions sont extrêmement optimisées et constituent la base de nombreuses applications en science des données et en apprentissage automatique."
        )
        self.set_content("Algèbre linéaire", content, code_example)

if __name__ == "__main__":
    app = NumPyApp()
    app.mainloop()