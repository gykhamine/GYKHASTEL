import customtkinter

# --- Les données complètes des mots-clés JavaScript ---
js_keywords_details = {
    "abstract": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "abstract class Shape { /* ... */ }"
    },
    "arguments": {
        "explication": "Objet de type tableau disponible à l'intérieur de toutes les fonctions non fléchées, contenant les arguments passés à la fonction.",
        "exemple": "function f() {\n  console.log(arguments[0]); // Affiche le premier argument\n}"
    },
    "await": {
        "explication": "Fait une pause dans l'exécution d'une fonction 'async' jusqu'à ce qu'une Promise soit résolue. Introduit en ES2017.",
        "exemple": "async function fetchData() {\n  const response = await fetch('...');\n}"
    },
    "break": {
        "explication": "Termine une boucle ('for', 'while') ou une instruction 'switch' et passe au code qui suit.",
        "exemple": "for (let i = 0; i < 5; i++) {\n  if (i === 3) {\n    break;\n  }\n}"
    },
    "case": {
        "explication": "Définit un bloc de code à exécuter dans une instruction 'switch'.",
        "exemple": "switch(fruit) {\n  case 'pomme':\n    console.log('C'est une pomme');\n    break;\n}"
    },
    "catch": {
        "explication": "Capture et gère une exception levée par un bloc 'try'.",
        "exemple": "try {\n  throw new Error('Erreur');\n} catch (e) {\n  console.log(e.message);\n}"
    },
    "class": {
        "explication": "Définit une classe, un modèle pour la création d'objets. Introduit en ES6.",
        "exemple": "class Personne {\n  constructor(nom) {\n    this.nom = nom;\n  }\n}"
    },
    "const": {
        "explication": "Déclare une variable avec une valeur qui ne peut pas être réassignée. Introduit en ES6.",
        "exemple": "const PI = 3.14159;"
    },
    "continue": {
        "explication": "Passe à l'itération suivante de la boucle, ignorant le reste du code de l'itération actuelle.",
        "exemple": "for (let i = 0; i < 5; i++) {\n  if (i === 2) {\n    continue;\n  }\n}"
    },
    "debugger": {
        "explication": "Déclenche une interruption d'exécution pour le débogage. Utile dans les outils de développement du navigateur.",
        "exemple": "function f() {\n  debugger;\n  console.log('Pause');\n}"
    },
    "default": {
        "explication": "Le cas par défaut dans une instruction 'switch' si aucune correspondance n'est trouvée.",
        "exemple": "switch(x) {\n  default:\n    console.log('Autre');\n}"
    },
    "delete": {
        "explication": "Supprime une propriété d'un objet.",
        "exemple": "const obj = { a: 1, b: 2 };\ndelete obj.a;\nconsole.log(obj); // { b: 2 }"
    },
    "do": {
        "explication": "Démarre une boucle 'do-while', qui s'exécute au moins une fois avant de vérifier la condition.",
        "exemple": "let i = 0;\ndo {\n  i++;\n} while (i < 3);"
    },
    "else": {
        "explication": "Le bloc de code à exécuter si la condition 'if' est fausse.",
        "exemple": "let age = 15;\nif (age >= 18) {\n  console.log('Majeur');\n} else {\n  console.log('Mineur');\n}"
    },
    "enum": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "// Non implémenté en JavaScript"
    },
    "export": {
        "explication": "Exporte des fonctions, objets ou primitives depuis un module pour qu'ils soient utilisés dans d'autres fichiers. Introduit en ES6.",
        "exemple": "// dans fichier.js\nexport const maConst = 10;"
    },
    "extends": {
        "explication": "Utilisé dans une déclaration de classe pour créer une classe enfant qui hérite d'une classe parente. Introduit en ES6.",
        "exemple": "class Chien extends Animal {\n  /* ... */\n}"
    },
    "for": {
        "explication": "Crée une boucle qui s'exécute tant qu'une condition est vraie. Il existe aussi 'for...of' et 'for...in'.",
        "exemple": "for (let i = 0; i < 3; i++) {\n  console.log(i);\n}"
    },
    "function": {
        "explication": "Définit une fonction. C'est la manière principale de créer des fonctions avant ES6.",
        "exemple": "function addition(a, b) {\n  return a + b;\n}"
    },
    "if": {
        "explication": "Utilisé pour l'exécution conditionnelle du code.",
        "exemple": "if (score > 10) {\n  console.log('Gagné');\n}"
    },
    "implements": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "// Non implémenté en JavaScript"
    },
    "import": {
        "explication": "Importe des déclarations exportées par un autre module. Introduit en ES6.",
        "exemple": "import { maConst } from './fichier.js';"
    },
    "in": {
        "explication": "Vérifie si une propriété est présente dans un objet (y compris dans la chaîne de prototype).",
        "exemple": "const obj = { a: 1 };\nconsole.log('a' in obj); // true"
    },
    "instanceof": {
        "explication": "Vérifie si un objet est une instance d'un type de données particulier (classe).",
        "exemple": "class Voiture {}\nconst maVoiture = new Voiture();\nconsole.log(maVoiture instanceof Voiture); // true"
    },
    "interface": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "// Non implémenté en JavaScript"
    },
    "let": {
        "explication": "Déclare une variable de portée de bloc. Introduit en ES6.",
        "exemple": "let compteur = 0;"
    },
    "new": {
        "explication": "Crée une instance d'un objet défini par un constructeur.",
        "exemple": "const date = new Date();"
    },
    "package": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "// Non implémenté en JavaScript"
    },
    "private": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "// Non implémenté en JavaScript"
    },
    "protected": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "// Non implémenté en JavaScript"
    },
    "public": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "// Non implémenté en JavaScript"
    },
    "return": {
        "explication": "Termine l'exécution d'une fonction et renvoie une valeur.",
        "exemple": "function carre(n) {\n  return n * n;\n}"
    },
    "static": {
        "explication": "Mot-clé réservé pour une utilisation future. Il n'a pas de fonctionnalité actuelle.",
        "exemple": "// Non implémenté en JavaScript"
    },
    "super": {
        "explication": "Appelle les méthodes de l'objet parent d'une classe, souvent utilisé pour appeler le constructeur. Introduit en ES6.",
        "exemple": "class Enfant extends Parent {\n  constructor() {\n    super();\n  }\n}"
    },
    "switch": {
        "explication": "Permet d'exécuter un bloc de code parmi plusieurs en fonction d'une expression.",
        "exemple": "let day = 2;\nswitch(day) { /* ... */ }"
    },
    "this": {
        "explication": "Fait référence à l'objet courant d'exécution du code.",
        "exemple": "const obj = {\n  val: 10,\n  f: function() { return this.val; }\n};"
    },
    "throw": {
        "explication": "Lève une exception personnalisée.",
        "exemple": "function f(n) {\n  if (n < 0) throw new Error('Négatif');\n}"
    },
    "try": {
        "explication": "Démarre un bloc de code à tester pour des erreurs potentielles.",
        "exemple": "try {\n  // Code qui peut échouer\n} catch (e) { /* ... */ }"
    },
    "typeof": {
        "explication": "Renvoie une chaîne de caractères indiquant le type d'un opérande non évalué.",
        "exemple": "typeof 42; // 'number'"
    },
    "var": {
        "explication": "Déclare une variable de portée de fonction ou globale. La manière traditionnelle de déclarer des variables.",
        "exemple": "var x = 10;"
    },
    "void": {
        "explication": "Évalue une expression et renvoie 'undefined'.",
        "exemple": "void(0); // undefined"
    },
    "while": {
        "explication": "Crée une boucle qui s'exécute tant qu'une condition est vraie.",
        "exemple": "let i = 0;\nwhile (i < 3) {\n  console.log(i);\n  i++;\n}"
    },
    "with": {
        "explication": "Ajoute l'objet spécifié à la portée de la chaîne de l'instruction. Déconseillé.",
        "exemple": "with (Math) {\n  console.log(cos(PI));\n}"
    },
    "yield": {
        "explication": "Met en pause l'exécution d'un générateur et renvoie une valeur. Introduit en ES6.",
        "exemple": "function* generator() {\n  yield 1;\n  yield 2;\n}"
    }
}

# --- Fonction pour afficher les détails du mot-clé sélectionné ---
def afficher_details(mot_cle):
    """Met à jour le panneau de détails avec les informations du mot-clé JavaScript sélectionné."""
    
    details = js_keywords_details.get(mot_cle, {"explication": "Détails non disponibles.", "exemple": "Pas d'exemple."})
    explication = details["explication"]
    exemple = details["exemple"]
    
    texte_complet = f"Explication :\n{explication}\n\nExemple (JavaScript) :\n\n{exemple}"
    
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
app.title("Guide des Mots-clés de JavaScript")

# --- Créer les deux cadres principaux ---
frame_liste = customtkinter.CTkFrame(master=app, width=250)
frame_liste.pack(pady=20, padx=20, fill="y", side="left")

frame_details = customtkinter.CTkFrame(master=app)
frame_details.pack(pady=20, padx=20, fill="both", expand=True, side="right")

# --- Contenu du cadre de la liste (gauche) ---
liste_label = customtkinter.CTkLabel(master=frame_liste, text="Mots-clés JavaScript", font=("Helvetica", 18, "bold"))
liste_label.pack(pady=10, padx=10)

liste_frame = customtkinter.CTkScrollableFrame(master=frame_liste, width=200)
liste_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Ajouter un bouton pour chaque mot-clé
mots_cles_js = sorted(js_keywords_details.keys())
for mot in mots_cles_js:
    button = customtkinter.CTkButton(master=liste_frame, text=mot, command=lambda m=mot: afficher_details(m))
    button.pack(pady=5, padx=5, fill="x")

# --- Contenu du cadre des détails (droite) ---
details_label = customtkinter.CTkLabel(master=frame_details, text="Sélectionnez un mot-clé", font=("Helvetica", 18, "bold"))
details_label.pack(pady=10, padx=10)

details_textbox = customtkinter.CTkTextbox(master=frame_details, corner_radius=10, font=("Courier", 14), wrap="word")
details_textbox.pack(pady=10, padx=10, fill="both", expand=True)
details_textbox.configure(state="disabled")

# --- Lancer l'application ---
if __name__ == "__main__":
    app.mainloop()