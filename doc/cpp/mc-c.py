import customtkinter

# --- Les données complètes des mots-clés C ---
# Dictionnaire contenant tous les mots-clés C, leurs explications et des exemples.
mots_cles_c_details = {
    "auto": {
        "explication": "Indique qu'une variable a une durée de vie automatique (par défaut pour les variables locales). Souvent omis.",
        "exemple": "int main() {\n    auto int i = 10; // 'auto' est implicite\n    return 0;\n}"
    },
    "break": {
        "explication": "Sort immédiatement de la boucle ou de l'instruction switch la plus proche.",
        "exemple": "for (int i = 0; i < 5; i++) {\n    if (i == 3) {\n        break;\n    }\n    printf(\"%d\\n\", i);\n}"
    },
    "case": {
        "explication": "Définit un bloc de code à exécuter dans une instruction switch.",
        "exemple": "int num = 2;\nswitch(num) {\n    case 1:\n        printf(\"Un\");\n        break;\n    case 2:\n        printf(\"Deux\");\n        break;\n}"
    },
    "char": {
        "explication": "Le type de données pour un seul caractère (généralement 1 octet).",
        "exemple": "char lettre = 'A';"
    },
    "const": {
        "explication": "Indique qu'une variable ne peut pas être modifiée après son initialisation.",
        "exemple": "const float PI = 3.14159f;"
    },
    "continue": {
        "explication": "Passe à l'itération suivante de la boucle, ignorant le reste du code dans l'itération actuelle.",
        "exemple": "for (int i = 0; i < 5; i++) {\n    if (i == 2) {\n        continue;\n    }\n    printf(\"%d\\n\", i);\n}"
    },
    "default": {
        "explication": "Le cas par défaut dans une instruction switch si aucune autre correspondance n'est trouvée.",
        "exemple": "switch(num) {\n    //... cases\n    default:\n        printf(\"Autre\");\n        break;\n}"
    },
    "do": {
        "explication": "Démarre une boucle 'do-while', qui s'exécute au moins une fois avant de vérifier la condition.",
        "exemple": "int i = 0;\ndo {\n    printf(\"%d\\n\", i);\n    i++;\n} while (i < 3);"
    },
    "double": {
        "explication": "Le type de données pour les nombres à virgule flottante de double précision.",
        "exemple": "double pi = 3.14159265359;"
    },
    "else": {
        "explication": "Le bloc de code à exécuter si la condition 'if' est fausse.",
        "exemple": "int age = 15;\nif (age >= 18) {\n    printf(\"Majeur\");\n} else {\n    printf(\"Mineur\");\n}"
    },
    "enum": {
        "explication": "Définit un type de données consistant en un ensemble de constantes entières nommées.",
        "exemple": "enum Couleur { ROUGE, VERT, BLEU };"
    },
    "extern": {
        "explication": "Déclare une variable ou une fonction définie dans un autre fichier source. Le lieur la trouvera lors de la compilation.",
        "exemple": "extern int mon_entier_global;\nvoid ma_fonction() { /* ... */ }"
    },
    "float": {
        "explication": "Le type de données pour les nombres à virgule flottante de simple précision.",
        "exemple": "float taux = 0.5f;"
    },
    "for": {
        "explication": "Crée une boucle qui s'exécute un nombre de fois déterminé.",
        "exemple": "for (int i = 0; i < 5; i++) {\n    printf(\"%d\\n\", i);\n}"
    },
    "goto": {
        "explication": "Permet un saut inconditionnel vers une étiquette dans la fonction.",
        "exemple": "int i = 0;\nma_label:\nprintf(\"%d\\n\", i);\ni++;\nif (i < 3) goto ma_label;"
    },
    "if": {
        "explication": "Utilisé pour l'exécution conditionnelle du code.",
        "exemple": "int x = 10;\nif (x > 5) {\n    printf(\"x est > 5\");\n}"
    },
    "inline": {
        "explication": "Suggère au compilateur d'insérer le code d'une fonction directement à l'appel, pour améliorer les performances. Ajouté en C99.",
        "exemple": "inline int somme(int a, int b) {\n    return a + b;\n}"
    },
    "int": {
        "explication": "Le type de données pour les nombres entiers.",
        "exemple": "int annee = 2024;"
    },
    "long": {
        "explication": "Un modificateur de type pour les nombres entiers de plus grande taille.",
        "exemple": "long grande_valeur = 1234567890L;"
    },
    "register": {
        "explication": "Suggère au compilateur de stocker une variable dans un registre du CPU pour un accès rapide. L'adresse ne peut pas être prise.",
        "exemple": "register int x = 10;"
    },
    "restrict": {
        "explication": "Utilisé pour les pointeurs. C'est une promesse au compilateur que le pointeur ne s'aliase pas avec d'autres. Ajouté en C99.",
        "exemple": "void copy(float *restrict dest, float *restrict src) { /* ... */ }"
    },
    "return": {
        "explication": "Termine l'exécution d'une fonction et renvoie une valeur.",
        "exemple": "int addition(int a, int b) {\n    return a + b;\n}"
    },
    "short": {
        "explication": "Un modificateur de type pour des nombres entiers de plus petite taille.",
        "exemple": "short petit_nombre = 100;"
    },
    "signed": {
        "explication": "Un modificateur pour spécifier un type entier avec un signe (nombres positifs et négatifs).",
        "exemple": "signed int x = -10;"
    },
    "sizeof": {
        "explication": "Un opérateur qui renvoie la taille en octets d'une variable ou d'un type de données.",
        "exemple": "int x;\nprintf(\"Taille de x: %zu\", sizeof(x));"
    },
    "static": {
        "explication": "Indique qu'une variable a une durée de vie statique (existe pendant toute l'exécution du programme).",
        "exemple": "void compteur() {\n    static int i = 0;\n    i++;\n}"
    },
    "struct": {
        "explication": "Définit un type de données qui regroupe des variables de différents types.",
        "exemple": "struct Point {\n    int x;\n    int y;\n};"
    },
    "switch": {
        "explication": "Permet de choisir un chemin d'exécution parmi plusieurs en fonction de la valeur d'une variable.",
        "exemple": "int choix = 1;\nswitch(choix) {\n    case 1:\n        printf(\"Option 1\");\n        break;\n}"
    },
    "typedef": {
        "explication": "Permet de créer un alias pour un type de données existant.",
        "exemple": "typedef long long ll;\nll ma_variable = 123456789012345LL;"
    },
    "union": {
        "explication": "Un type de données spécial qui permet de stocker des membres différents dans le même emplacement de mémoire.",
        "exemple": "union MaUnion {\n    int i;\n    float f;\n};"
    },
    "unsigned": {
        "explication": "Un modificateur pour spécifier un type entier non signé (uniquement des nombres positifs).",
        "exemple": "unsigned int x = 10;"
    },
    "void": {
        "explication": "Indique qu'une fonction ne renvoie aucune valeur ou qu'un pointeur ne pointe vers aucun type de données spécifique.",
        "exemple": "void ma_fonction() {\n    printf(\"Hello\");\n}"
    },
    "volatile": {
        "explication": "Indique au compilateur qu'une variable peut être modifiée à tout moment par un autre processus.",
        "exemple": "volatile int etat_registre;"
    },
    "while": {
        "explication": "Crée une boucle qui s'exécute tant qu'une condition est vraie.",
        "exemple": "int i = 0;\nwhile (i < 3) {\n    printf(\"%d\\n\", i);\n    i++;\n}"
    },
    "_Alignas": {
        "explication": "Spécifie l'alignement d'une variable. Ajouté en C11.",
        "exemple": "_Alignas(16) char buffer[32];"
    },
    "_Alignof": {
        "explication": "Renvoie l'alignement en octets d'un type de données. Ajouté en C11.",
        "exemple": "size_t a = _Alignof(int);"
    },
    "_Atomic": {
        "explication": "Définit un type de données comme atomique, assurant qu'il ne peut pas être modifié simultanément par plusieurs threads. Ajouté en C11.",
        "exemple": "_Atomic int x = 0;"
    },
    "_Bool": {
        "explication": "Le type de données booléen en C99. Les valeurs possibles sont 0 ou 1.",
        "exemple": "_Bool est_vrai = 1;"
    },
    "_Complex": {
        "explication": "Un type de données pour les nombres complexes. Ajouté en C99.",
        "exemple": "double _Complex z = 1.0 + 2.0 * I;"
    },
    "_Generic": {
        "explication": "Permet de choisir une fonction à appeler en fonction du type de l'argument. Ajouté en C11.",
        "exemple": "#define print(x) _Generic((x), int: print_int, double: print_double)(x);"
    },
    "_Imaginary": {
        "explication": "Un type de données pour les nombres imaginaires. Ajouté en C99.",
        "exemple": "double _Imaginary i = 1.0 * I;"
    },
    "_Noreturn": {
        "explication": "Indique que la fonction ne retournera jamais à l'appelant. Ajouté en C11.",
        "exemple": "_Noreturn void erreur() { exit(1); }"
    },
    "_Static_assert": {
        "explication": "Vérifie une assertion au moment de la compilation. Ajouté en C11.",
        "exemple": "_Static_assert(sizeof(int) == 4, \"int doit être 4 octets\");"
    },
    "_Thread_local": {
        "explication": "Indique qu'une variable est unique pour chaque thread. Ajouté en C11.",
        "exemple": "_Thread_local int x = 0;"
    }
}

# --- Fonction pour afficher les détails du mot-clé sélectionné ---
def afficher_details(mot_cle):
    """Met à jour le panneau de détails avec les informations du mot-clé C sélectionné."""
    
    details = mots_cles_c_details.get(mot_cle, {"explication": "Détails non disponibles.", "exemple": "Pas d'exemple."})
    explication = details["explication"]
    exemple = details["exemple"]
    
    texte_complet = f"Explication :\n{explication}\n\nExemple (C) :\n\n{exemple}"
    
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
app.title("Guide des Mots-clés de C")

# --- Créer les deux cadres principaux ---
frame_liste = customtkinter.CTkFrame(master=app, width=250)
frame_liste.pack(pady=20, padx=20, fill="y", side="left")

frame_details = customtkinter.CTkFrame(master=app)
frame_details.pack(pady=20, padx=20, fill="both", expand=True, side="right")

# --- Contenu du cadre de la liste (gauche) ---
liste_label = customtkinter.CTkLabel(master=frame_liste, text="Mots-clés C", font=("Helvetica", 18, "bold"))
liste_label.pack(pady=10, padx=10)

liste_frame = customtkinter.CTkScrollableFrame(master=frame_liste, width=200)
liste_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Ajouter un bouton pour chaque mot-clé
mots_cles_c = sorted(mots_cles_c_details.keys())
for mot in mots_cles_c:
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