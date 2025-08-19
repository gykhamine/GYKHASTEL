import customtkinter
import keyword

# Un dictionnaire pour stocker les informations pour chaque mot-clé
mots_cles_details = {
    "if": {
        "explication": "Utilisé pour l'exécution conditionnelle du code. Le code s'exécute si la condition est vraie.",
        "exemple": "age = 20\nif age >= 18:\n    print('Majeur')"
    },
    "elif": {
        "explication": "Abréviation de 'else if', utilisé pour vérifier une autre condition si la première est fausse.",
        "exemple": "temp = 25\nif temp < 0:\n    print('Froid')\nelif temp > 20:\n    print('Chaud')"
    },
    "else": {
        "explication": "Le bloc de code à exécuter si toutes les conditions précédentes sont fausses.",
        "exemple": "heure = 8\nif heure < 7:\n    print('Tôt')\nelse:\n    print('À l'heure')"
    },
    "for": {
        "explication": "Crée une boucle qui itère sur une séquence (liste, chaîne, etc.).",
        "exemple": "fruits = ['pomme', 'banane']\nfor f in fruits:\n    print(f)"
    },
    "while": {
        "explication": "Crée une boucle qui s'exécute tant qu'une condition est vraie.",
        "exemple": "i = 0\nwhile i < 3:\n    print(i)\n    i += 1"
    },
    "def": {
        "explication": "Définit une fonction ou une méthode.",
        "exemple": "def bonjour(nom):\n    return f'Bonjour, {nom}'"
    },
    "return": {
        "explication": "Renvoie une valeur depuis une fonction.",
        "exemple": "def double(x):\n    return x * 2"
    },
    "class": {
        "explication": "Définit une classe, un modèle pour créer des objets.",
        "exemple": "class Voiture:\n    def __init__(self, marque):\n        self.marque = marque"
    },
    "import": {
        "explication": "Importe un module externe pour l'utiliser dans le script.",
        "exemple": "import math\nprint(math.pi)"
    },
    "from": {
        "explication": "Importe des objets spécifiques d'un module, au lieu du module entier.",
        "exemple": "from random import randint\nprint(randint(1, 10))"
    },
    "as": {
        "explication": "Donne un alias (un nom plus court) à un module ou un objet importé.",
        "exemple": "import numpy as np"
    },
    "try": {
        "explication": "Démarre un bloc de code à tester pour des erreurs.",
        "exemple": "try:\n    print(1/0)\nexcept ZeroDivisionError:\n    print('Erreur')"
    },
    "except": {
        "explication": "Capture et gère une exception (erreur) levée dans le bloc 'try'.",
        "exemple": "voir 'try'"
    },
    "finally": {
        "explication": "Le bloc de code qui s'exécute toujours, qu'il y ait eu une erreur ou non.",
        "exemple": "try:\n    pass\nfinally:\n    print('Fini')"
    },
    "raise": {
        "explication": "Déclenche manuellement une exception.",
        "exemple": "def verifier_age(age):\n    if age < 0:\n        raise ValueError('Âge invalide')"
    },
    "lambda": {
        "explication": "Crée une petite fonction anonyme, souvent utilisée pour des opérations simples.",
        "exemple": "f = lambda x: x * 2\nprint(f(5))"
    },
    "True": {
        "explication": "La valeur booléenne 'vrai'.",
        "exemple": "est_vrai = True"
    },
    "False": {
        "explication": "La valeur booléenne 'faux'.",
        "exemple": "est_faux = False"
    },
    "None": {
        "explication": "Représente l'absence de valeur ou une valeur nulle.",
        "exemple": "valeur = None"
    },
    "is": {
        "explication": "Vérifie si deux variables font référence au même objet en mémoire.",
        "exemple": "liste1 = [1]; liste2 = liste1\nprint(liste1 is liste2)"
    },
    "in": {
        "explication": "Vérifie si un élément est présent dans une séquence (liste, chaîne, etc.).",
        "exemple": "lettres = 'abc'\nprint('a' in lettres)"
    },
    "and": {
        "explication": "Opérateur logique 'et'. Renvoie True si les deux conditions sont vraies.",
        "exemple": "a, b = True, False\nprint(a and b)"
    },
    "or": {
        "explication": "Opérateur logique 'ou'. Renvoie True si au moins une condition est vraie.",
        "exemple": "a, b = True, False\nprint(a or b)"
    },
    "not": {
        "explication": "Opérateur logique de négation. Inverse la valeur booléenne.",
        "exemple": "a = True\nprint(not a)"
    },
    "with": {
        "explication": "Utilisé pour la gestion de contexte, par exemple pour ouvrir et fermer automatiquement un fichier.",
        "exemple": "with open('f.txt', 'w') as f:\n    f.write('Salut')"
    },
    "break": {
        "explication": "Sort immédiatement de la boucle la plus proche.",
        "exemple": "for i in range(5):\n    if i == 2:\n        break"
    },
    "continue": {
        "explication": "Passe à l'itération suivante de la boucle, ignorant le reste du code dans l'itération actuelle.",
        "exemple": "for i in range(5):\n    if i == 2:\n        continue"
    },
    "pass": {
        "explication": "Instruction 'placeholder' qui ne fait rien, utilisée quand un bloc de code est requis mais vide.",
        "exemple": "def a_venir():\n    pass"
    },
    "global": {
        "explication": "Permet de modifier une variable globale depuis une fonction.",
        "exemple": "x = 10\ndef f():\n    global x\n    x = 20"
    },
    "nonlocal": {
        "explication": "Permet de modifier une variable d'une fonction englobante, mais pas globale.",
        "exemple": "def f():\n    x = 10\n    def g():\n        nonlocal x\n        x = 20"
    },
    "del": {
        "explication": "Supprime un objet ou un élément d'une séquence.",
        "exemple": "liste = [1, 2, 3]\ndel liste[1]"
    },
    "async": {
        "explication": "Définit une fonction asynchrone (coroutine).",
        "exemple": "import asyncio\nasync def ma_tache():\n    await asyncio.sleep(1)"
    },
    "await": {
        "explication": "Permet à une fonction asynchrone de s'arrêter temporairement en attendant qu'une autre tâche se termine.",
        "exemple": "voir 'async'"
    },
    "is not": {
        "explication": "Le contraire de 'is'. Vérifie si deux variables ne pointent PAS vers le même objet.",
        "exemple": "x = 1\ny = 2\nprint(x is not y)"
    },
    "not in": {
        "explication": "Le contraire de 'in'. Vérifie si un élément n'est PAS présent dans une séquence.",
        "exemple": "liste = [1]\nprint(2 not in liste)"
    },
    "assert": {
        "explication": "Pour des tests de débuggage. Si la condition est fausse, une AssertionError est levée.",
        "exemple": "x = 5\nassert x == 5, 'x doit être 5'"
    },
    "yield": {
        "explication": "Utilisé dans les générateurs. Renvoie une valeur et suspend l'exécution, pour la reprendre plus tard.",
        "exemple": "def nombres():\n    yield 1\n    yield 2\n\ngen = nombres()\nprint(next(gen))"
    }
}

# --- Fonction pour afficher les détails du mot-clé sélectionné ---
def afficher_details(mot_cle):
    """Met à jour le panneau de détails avec les informations du mot-clé sélectionné."""
    
    details = mots_cles_details.get(mot_cle, {"explication": "Détails non disponibles.", "exemple": "Pas d'exemple."})
    explication = details["explication"]
    exemple = details["exemple"]
    
    texte_complet = f"Explication :\n{explication}\n\nExemple :\n\n{exemple}"
    
    details_label.configure(text=f"Détails pour '{mot_cle}'")
    details_textbox.configure(state="normal")
    details_textbox.delete("1.0", "end")
    details_textbox.insert("1.0", texte_complet)
    details_textbox.configure(state="disabled")

# --- Configuration de la fenêtre principale ---
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("1000x600")
app.title("Guide des Mots-clés de Python")

# --- Créer les deux cadres principaux ---
frame_liste = customtkinter.CTkFrame(master=app, width=250)
frame_liste.pack(pady=20, padx=20, fill="y", side="left")

frame_details = customtkinter.CTkFrame(master=app)
frame_details.pack(pady=20, padx=20, fill="both", expand=True, side="right")

# --- Contenu du cadre de la liste (gauche) ---
liste_label = customtkinter.CTkLabel(master=frame_liste, text="Mots-clés Python", font=("Helvetica", 18, "bold"))
liste_label.pack(pady=10, padx=10)

liste_frame = customtkinter.CTkScrollableFrame(master=frame_liste, width=200)
liste_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Ajouter un bouton pour chaque mot-clé
mots_cles = sorted(keyword.kwlist)
for mot in mots_cles:
    button = customtkinter.CTkButton(master=liste_frame, text=mot, command=lambda m=mot: afficher_details(m))
    button.pack(pady=5, padx=5, fill="x")

# --- Contenu du cadre des détails (droite) ---
details_label = customtkinter.CTkLabel(master=frame_details, text="Sélectionnez un mot-clé", font=("Helvetica", 18, "bold"))
details_label.pack(pady=10, padx=10)

details_textbox = customtkinter.CTkTextbox(master=frame_details, corner_radius=10, font=("Courier", 14), wrap="word")
details_textbox.pack(pady=10, padx=10, fill="both", expand=True)
details_textbox.configure(state="disabled")

# --- Lancer l'application ---
app.mainloop()