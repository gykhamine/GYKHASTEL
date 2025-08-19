import customtkinter as ctk
import numpy as np
from scipy import (
    integrate,
    optimize,
    interpolate,
    signal,
    stats,
    linalg,
    fft,
    spatial,
    cluster,
)
import threading
import time
from tkinter import Toplevel, Label

class SciPyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre principale ---
        self.title("Documentation Complète : SciPy")
        self.geometry("1200x900")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # --- Création du cadre de navigation latéral ---
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.pack(side="left", fill="y", padx=(10, 0), pady=10)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="Menu de navigation",
                                                   compound="left", font=ctk.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.pack(padx=20, pady=(20, 10))

        # --- Création des boutons de navigation par section ---
        self.scipy_label = ctk.CTkLabel(self.navigation_frame, text="SciPy", font=ctk.CTkFont(size=16, weight="bold"))
        self.scipy_label.pack(fill="x", padx=10, pady=(10, 0))
        self.scipy_buttons = self.create_buttons(self.navigation_frame, [
            ("Introduction à SciPy", self.show_scipy_intro),
            ("Intégration numérique", self.show_scipy_integrate),
            ("Optimisation", self.show_scipy_optimize),
            ("Interpolation", self.show_scipy_interpolate),
            ("Algèbre linéaire", self.show_scipy_linalg),
            ("Traitement du signal", self.show_scipy_signal),
            ("Transformée de Fourier (FFT)", self.show_scipy_fft),
            ("Statistiques", self.show_scipy_stats),
            ("Clustering", self.show_scipy_cluster),
            ("Calculs spatiaux", self.show_scipy_spatial),
        ])

        # --- Création du cadre principal pour le contenu ---
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)
        
        self.content_textbox = ctk.CTkTextbox(self.content_frame, wrap="word", font=ctk.CTkFont(size=14))
        self.content_textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.content_textbox.configure(state="disabled")
        
        # --- Démarrage sur le premier onglet ---
        self.show_scipy_intro()

    def create_buttons(self, parent, button_list):
        buttons = []
        for text, command in button_list:
            button = ctk.CTkButton(parent, corner_radius=0, height=40, border_spacing=10, text=text,
                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                   anchor="w", command=command)
            button.pack(fill="x", padx=10, pady=2)
            buttons.append(button)
        return buttons

    def set_content(self, title, text, code=None):
        self.content_textbox.configure(state="normal")
        self.content_textbox.delete("1.0", "end")
        
        self.content_textbox.insert("1.0", f"**{title}**\n\n{text}")
        if code:
            self.content_textbox.insert("end", f"\n\n```python\n{code}\n```")
        
        self.content_textbox.configure(state="disabled")

    # --- Modules SciPy et leurs calculs ---

    def show_scipy_intro(self):
        content = (
            "**Introduction à SciPy** 🔬\n\n"
            "**SciPy** (Scientific Python) est une bibliothèque de calcul scientifique construite sur **NumPy**. Elle offre une collection exhaustive de modules pour résoudre des problèmes mathématiques, statistiques et d'ingénierie. Chaque sous-module est spécialisé dans un domaine précis et fournit une multitude d'outils optimisés."
        )
        self.set_content("Introduction à SciPy", content)

    def show_scipy_integrate(self):
        code_example = (
            "from scipy import integrate\n"
            "import numpy as np\n\n"
            "def f(x, a, b): return a*x**2 + b\n"
            "result_quad, _ = integrate.quad(f, 0, 1, args=(1, 2))\n"
            "print(f'Intégrale de x^2+2 de 0 à 1 : {result_quad:.6f}')\n\n"
            "x_data = np.linspace(0, 1, 100)\n"
            "y_data = x_data**2\n"
            "result_trapz = integrate.trapz(y_data, x_data)\n"
            "print(f'Intégrale par la méthode des trapèzes : {result_trapz:.6f}')\n\n"
            "def ode_system(y, t): return [y[1], -y[0]]\n"
            "y0 = [1, 0]\n"
            "t = np.linspace(0, 10, 101)\n"
            "sol = integrate.odeint(ode_system, y0, t)\n"
            "print(f'Solution de l\\'équation différentielle (5 premiers points) :\\n{sol[:5].round(2)}')\n"
        )
        content = (
            "**Intégration numérique (`scipy.integrate`)** ✍️\n\n"
            "Ce module est essentiel pour les calculs d'intégrales définies et la résolution d'équations différentielles ordinaires (EDO).\n\n"
            "**Calculs imaginables :**\n"
            "- **`integrate.quad()` :** Intégration de fonctions à une seule variable avec des arguments supplémentaires (`args`).\n"
            "- **`integrate.dblquad()` et `integrate.tplquad()` :** Intégration double et triple.\n"
            "- **`integrate.nquad()` :** Intégration de fonctions à N variables.\n"
            "- **`integrate.trapz()` :** Intégration numérique à partir de points de données discrets (méthode des trapèzes).\n"
            "- **`integrate.simpson()` :** Intégration à partir de points de données (méthode de Simpson).\n"
            "- **`integrate.odeint()` :** Résolution d'équations différentielles ordinaires de la forme `dy/dt = f(y, t)`."
        )
        self.set_content("Intégration numérique", content, code_example)

    def show_scipy_optimize(self):
        code_example = (
            "from scipy import optimize\n"
            "import numpy as np\n\n"
            "# Minimisation d'une fonction multivariable\n"
            "def rosen(x): return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)\n"
            "x0 = np.array([0, 0])\n"
            "res = optimize.minimize(rosen, x0, method='nelder-mead')\n"
            "print(f'Minimum de la fonction de Rosenbrock : {res.x.round(4)}')\n\n"
            "# Recherche de racines de systèmes d'équations non-linéaires\n"
            "def f(x): return [x[0]**2 + x[1]**2 - 1, x[0] + x[1] - 1]\n"
            "sol = optimize.root(f, [0.5, 0.5])\n"
            "print(f'\\nSolution du système d\\'équations : {sol.x.round(4)}')\n"
        )
        content = (
            "**Optimisation (`scipy.optimize`)** 📈\n\n"
            "Ce module est une boîte à outils complète pour la minimisation, le *fitting* de courbes et la recherche de racines.\n\n"
            "**Calculs imaginables :**\n"
            "- **`optimize.minimize()` :** Minimisation de fonctions multivariables (nombreuses méthodes : `nelder-mead`, `BFGS`, `SLSQP`, etc.).\n"
            "- **`optimize.minimize_scalar()` :** Minimisation de fonctions à une seule variable, plus rapide et plus précise.\n"
            "- **`optimize.root()` :** Recherche de la racine d'un système d'équations non-linéaires (`f(x) = 0`).\n"
            "- **`optimize.curve_fit()` :** Ajustement de données à une fonction, retournant les paramètres optimaux pour le modèle.\n"
            "- **`optimize.least_squares()` :** Résolution de problèmes des moindres carrés non-linéaires."
        )
        self.set_content("Optimisation", content, code_example)

    def show_scipy_interpolate(self):
        code_example = (
            "from scipy import interpolate\n"
            "import numpy as np\n\n"
            "x_points = np.linspace(0, 10, 10)\n"
            "y_points = np.sin(x_points)\n\n"
            "linear_interp = interpolate.interp1d(x_points, y_points, kind='linear')\n"
            "cubic_interp = interpolate.interp1d(x_points, y_points, kind='cubic')\n\n"
            "print(f'Interpolation linéaire à x=5.5 : {linear_interp(5.5):.4f}')\n"
            "print(f'Interpolation cubique à x=5.5 : {cubic_interp(5.5):.4f}')\n\n"
            "grid_x, grid_y = np.mgrid[0:10:100j, 0:10:100j]\n"
            "points = np.random.rand(100, 2) * 10\n"
            "values = np.sin(points[:, 0]) + np.cos(points[:, 1])\n"
            "grid_z = interpolate.griddata(points, values, (grid_x, grid_y), method='cubic')\n"
            "print(f'\\nInterpolation 2D sur grille (première valeur) : {grid_z[0, 0]:.4f}')"
        )
        content = (
            "**Interpolation (`scipy.interpolate`)** 📏\n\n"
            "Ce module est spécialisé dans l'estimation de valeurs intermédiaires à partir de points de données connus.\n\n"
            "**Calculs imaginables :**\n"
            "- **`interpolate.interp1d()` :** Fonctions d'interpolation à une dimension (linéaire, cubique, etc.).\n"
            "- **`interpolate.splrep()` et `interpolate.splev()` :** Création et évaluation de splines, idéales pour des courbes lisses.\n"
            "- **`interpolate.griddata()` :** Interpolation de données dispersées en N dimensions sur une grille régulière.\n"
            "- **`interpolate.Rbf()` :** Fonctions de base radiales (RBF) pour l'interpolation de données dispersées en haute dimension."
        )
        self.set_content("Interpolation", content, code_example)
    
    def show_scipy_linalg(self):
        code_example = (
            "from scipy import linalg\n"
            "import numpy as np\n\n"
            "A = np.array([[1, 2], [3, 4]])\n"
            "b = np.array([5, 6])\n"
            "x = linalg.solve(A, b)\n"
            "print(f'Solution de Ax=b : x = {x.round(2)}')\n\n"
            "det_A = linalg.det(A)\n"
            "print(f'Déterminant de A : {det_A:.2f}')\n\n"
            "eigvals, eigvecs = linalg.eig(A)\n"
            "print(f'Valeurs propres de A : {eigvals.round(2)}')\n\n"
            "inv_A = linalg.inv(A)\n"
            "print(f'\\nInverse de A :\\n{inv_A.round(2)}')\n"
        )
        content = (
            "**Algèbre linéaire avancée (`scipy.linalg`)** 🔢\n\n"
            "Bien que NumPy dispose de son propre module d'algèbre linéaire, `scipy.linalg` offre des fonctions plus complètes, optimisées pour des matrices spécifiques et des problèmes complexes.\n\n"
            "**Calculs imaginables :**\n"
            "- **`linalg.solve()` :** Résolution de systèmes d'équations linéaires (`Ax = b`).\n"
            "- **`linalg.inv()` :** Calcul de l'inverse d'une matrice.\n"
            "- **`linalg.det()` :** Calcul du déterminant d'une matrice.\n"
            "- **`linalg.eig()` et `linalg.eigh()` :** Calcul des valeurs et vecteurs propres (pour les matrices générales et hermitiennes/symétriques).\n"
            "- **`linalg.svd()` :** Décomposition en valeurs singulières (SVD).\n"
            "- **`linalg.lu()` :** Décomposition LU, Cholesky, QR, et autres décompositions matricielles.\n"
            "- **`linalg.expm()` :** Calcul de l'exponentielle d'une matrice."
        )
        self.set_content("Algèbre linéaire", content, code_example)
        
    def show_scipy_signal(self):
        code_example = (
            "from scipy import signal\n"
            "import numpy as np\n\n"
            "t = np.linspace(0, 1, 500, endpoint=False)\n"
            "sig = np.sin(2*np.pi*10*t) + 0.5*np.random.randn(len(t))\n\n"
            "b, a = signal.iirfilter(4, 0.1, btype='low', analog=False, ftype='butter')\n"
            "filtered_sig = signal.lfilter(b, a, sig)\n"
            "print(f'Signal original (5 premiers points) : {sig[:5].round(2)}')\n"
            "print(f'Signal filtré (5 premiers points) : {filtered_sig[:5].round(2)}')\n\n"
            "corr = signal.correlate(sig, sig, mode='full')\n"
            "print(f'\\nAuto-corrélation (taille) : {corr.size}')\n"
        )
        content = (
            "**Traitement du signal (`scipy.signal`)** 📻\n\n"
            "Ce module est une boîte à outils puissante pour l'analyse de signaux analogiques et numériques, de la conception de filtres à la convolution.\n\n"
            "**Calculs imaginables :**\n"
            "- **Filtrage :** `signal.butter()`, `signal.iirfilter()` pour concevoir des filtres IIR. `signal.lfilter()` pour appliquer un filtre au signal.\n"
            "- **Convolution et corrélation :** `signal.convolve()` et `signal.correlate()` pour analyser les relations entre signaux.\n"
            "- **Analyse spectrale :** `signal.welch()` pour estimer la densité spectrale de puissance. `signal.spectrogram()` pour l'analyse temps-fréquence.\n"
            "- **Génération de signaux :** `signal.chirp()`, `signal.square()` pour créer des formes d'onde.\n"
            "- **Fenêtrage :** `signal.windows` pour appliquer des fenêtres (Hanning, Hamming, etc.) aux signaux."
        )
        self.set_content("Traitement du signal", content, code_example)

    def show_scipy_fft(self):
        code_example = (
            "from scipy import fft\n"
            "import numpy as np\n\n"
            "N = 1000\n"
            "T = 1.0 / 800.0\n"
            "x = np.linspace(0.0, N*T, N, endpoint=False)\n"
            "y = np.cos(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)\n\n"
            "yf = fft.fft(y)\n"
            "xf = fft.fftfreq(N, T)[:N//2]\n\n"
            "print(f'Fréquences principales (valeurs positives) :')\n"
            "print(f'  - Fréquence 1 : {xf[np.argmax(np.abs(yf[0:N//2]))]} Hz')\n"
            "print(f'  - Fréquence 2 (proche) : {xf[np.argmax(np.abs(yf[40:N//2]))]} Hz')\n\n"
            "# 2D FFT pour le traitement d'image\n"
            "img = np.random.rand(64, 64)\n"
            "fft_img = fft.fft2(img)\n"
            "print(f'\\nTransformée de Fourier 2D (forme) : {fft_img.shape}')\n"
        )
        content = (
            "**Transformée de Fourier (FFT - `scipy.fft`)** 🌌\n\n"
            "Ce module contient des implémentations rapides et efficaces de la Transformée de Fourier (FFT) en une et plusieurs dimensions, un outil central dans de nombreux domaines scientifiques.\n\n"
            "**Calculs imaginables :**\n"
            "- **`fft.fft()` :** Calcul de la Transformée de Fourier rapide 1D. Permet de passer du domaine temporel au domaine fréquentiel.\n"
            "- **`fft.ifft()` :** Calcul de la transformée inverse, pour reconstruire le signal original.\n"
            "- **`fft.fft2()` et `fft.fftn()` :** Fonctions pour les FFT à 2 dimensions (utile pour les images) et N dimensions.\n"
            "- **`fft.fftfreq()` et `fft.fftshift()` :** Fonctions utilitaires pour obtenir les fréquences et centrer le spectre."
        )
        self.set_content("Transformée de Fourier (FFT)", content, code_example)
        
    def show_scipy_stats(self):
        code_example = (
            "from scipy import stats\n"
            "import numpy as np\n\n"
            "data = np.array([12, 14, 15, 17, 18, 20, 22, 25])\n"
            "mean, std = stats.tmean(data), stats.tstd(data)\n"
            "print(f'Moyenne et écart-type tronqués : {mean:.2f}, {std:.2f}')\n\n"
            "t_stat, p_val = stats.ttest_1samp(data, popmean=15)\n"
            "print(f'\\nTest t de Student (p-value) : {p_val:.4f}')\n\n"
            "norm = stats.norm(loc=10, scale=2)\n"
            "print(f'Probabilité de P(X < 8) pour une loi normale (10, 2) : {norm.cdf(8):.4f}')"
        )
        content = (
            "**Statistiques (`scipy.stats`)** 📊\n\n"
            "Ce module est une bibliothèque statistique complète, couvrant les statistiques descriptives, les tests d'hypothèses et les distributions de probabilité.\n\n"
            "**Calculs imaginables :**\n"
            "- **Statistiques descriptives :** `stats.tmean()`, `stats.tvar()`, `stats.skew()`, `stats.kurtosis()` pour des mesures avancées d'asymétrie et d'aplatissement.\n"
            "- **Tests d'hypothèses :** `stats.ttest_1samp()`, `stats.chi2_contingency()`, `stats.f_oneway()` pour comparer des échantillons ou des distributions.\n"
            "- **Distributions de probabilité :** Plus de 80 distributions continues et discrètes (`norm`, `binom`, `poisson`, etc.). Chaque distribution a des méthodes pour la fonction de densité de probabilité (`pdf`), la fonction de répartition cumulée (`cdf`), l'inverse de la cdf (`ppf`) et la génération de nombres aléatoires (`rvs`)."
        )
        self.set_content("Statistiques", content, code_example)
    
    def show_scipy_cluster(self):
        code_example = (
            "from scipy import cluster, spatial\n"
            "import numpy as np\n\n"
            "X = np.random.rand(10, 2) * 10\n"
            "Z = cluster.hierarchy.linkage(X, 'ward')\n"
            "print(f'Matrice de liaison pour le clustering hiérarchique :\\n{Z.round(2)}')\n\n"
            "labels = cluster.hierarchy.fcluster(Z, 5, criterion='maxclust')\n"
            "print(f'\\nÉtiquettes des 5 clusters : {labels}')\n\n"
            "centroids, _ = cluster.vq.kmeans(X, 3)\n"
            "print(f'\\nCentroïdes pour 3 clusters K-means :\\n{centroids.round(2)}')\n"
        )
        content = (
            "**Clustering (`scipy.cluster`)** 👥\n\n"
            "Ce module offre des algorithmes de clustering pour regrouper des points de données similaires. Il est essentiel pour l'apprentissage automatique non supervisé.\n\n"
            "**Calculs imaginables :**\n"
            "- **Clustering hiérarchique :** Le sous-module `cluster.hierarchy` propose des méthodes d'agrégation (`linkage()`) pour créer des hiérarchies de clusters, qui peuvent ensuite être visualisées sous forme de dendrogrammes.\n"
            "- **Quantification vectorielle :** Le sous-module `cluster.vq` contient des algorithmes comme `kmeans()`, qui est une implémentation de l'algorithme K-means pour trouver les centroïdes de clusters."
        )
        self.set_content("Clustering", content, code_example)
    
    def show_scipy_spatial(self):
        code_example = (
            "from scipy import spatial\n"
            "import numpy as np\n\n"
            "A = np.array([1, 0, 0])\n"
            "B = np.array([0, 1, 0])\n"
            "dist_euclid = spatial.distance.euclidean(A, B)\n"
            "print(f'Distance euclidienne entre A et B : {dist_euclid:.2f}')\n\n"
            "points = np.random.rand(10, 3)\n"
            "tree = spatial.KDTree(points)\n"
            "nearest_dist, nearest_idx = tree.query([0.5, 0.5, 0.5])\n"
            "print(f'\\nPoint le plus proche de [0.5, 0.5, 0.5] a une distance de {nearest_dist:.2f}')\n"
        )
        content = (
            "**Calculs spatiaux (`scipy.spatial`)** 🌍\n\n"
            "Ce module est dédié à la géométrie computationnelle et aux calculs de distance entre des points. Il est fondamental pour la reconnaissance de motifs et la modélisation géométrique.\n\n"
            "**Calculs imaginables :**\n"
            "- **`spatial.distance` :** Calcul d'une grande variété de distances entre des points (Euclidienne, Manhattan, cosinus, etc.).\n"
            "- **`spatial.KDTree` :** Une structure de données optimisée pour la recherche de voisins les plus proches en N dimensions.\n"
            "- **`spatial.Delaunay` :** Calcul de la triangulation de Delaunay d'un ensemble de points.\n"
            "- **`spatial.ConvexHull` :** Calcul de l'enveloppe convexe d'un ensemble de points."
        )
        self.set_content("Calculs spatiaux", content, code_example)

if __name__ == "__main__":
    app = SciPyApp()
    app.mainloop()