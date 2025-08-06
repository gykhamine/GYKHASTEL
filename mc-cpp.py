import customtkinter
import sys

# --- Les données complètes des mots-clés C++ ---
mots_cles_cpp_details = {
    "alignas": {
        "explication": "Spécifie l'alignement d'une variable ou d'un type. Introduit dans C++11.",
        "exemple": "alignas(16) int mon_tableau[4];"
    },
    "alignof": {
        "explication": "Renvoie l'alignement en octets d'un type de données. Introduit dans C++11.",
        "exemple": "size_t alignment = alignof(int);"
    },
    "and": {
        "explication": "Opérateur logique 'et', équivalent à '&&'.",
        "exemple": "bool a = true, b = false;\nif (a and b) { /* ... */ }"
    },
    "and_eq": {
        "explication": "Opérateur d'assignation 'et', équivalent à '&='.",
        "exemple": "int x = 5;\nx and_eq 2; // x devient 0"
    },
    "asm": {
        "explication": "Permet d'inclure du code assembleur dans un programme C++.",
        "exemple": "asm(\"movl $1, %eax\");"
    },
    "auto": {
        "explication": "Déduit automatiquement le type d'une variable à partir de son initialisation. Introduit dans C++11.",
        "exemple": "auto x = 5; // x est un int"
    },
    "bitand": {
        "explication": "Opérateur binaire 'et', équivalent à '&'.",
        "exemple": "int x = 5, y = 3;\nint z = x bitand y; // z est 1"
    },
    "bitor": {
        "explication": "Opérateur binaire 'ou', équivalent à '|'.",
        "exemple": "int x = 5, y = 3;\nint z = x bitor y; // z est 7"
    },
    "bool": {
        "explication": "Type de données pour les valeurs booléennes (vrai ou faux).",
        "exemple": "bool is_valid = true;"
    },
    "break": {
        "explication": "Sort immédiatement de la boucle ou de l'instruction switch la plus proche.",
        "exemple": "for (int i = 0; i < 5; ++i) {\n    if (i == 3) {\n        break;\n    }\n}"
    },
    "case": {
        "explication": "Définit un bloc de code à exécuter dans une instruction switch.",
        "exemple": "switch(num) {\n    case 1:\n        // code\n        break;\n}"
    },
    "catch": {
        "explication": "Capture et gère une exception levée par un bloc 'try'.",
        "exemple": "try {\n    // ...\n} catch (const std::exception& e) {\n    // ...\n}"
    },
    "char": {
        "explication": "Type de données pour un seul caractère.",
        "exemple": "char lettre = 'A';"
    },
    "char8_t": {
        "explication": "Type de caractère pour les chaînes UTF-8. Introduit dans C++20.",
        "exemple": "char8_t u8_char = u8'a';"
    },
    "char16_t": {
        "explication": "Type de caractère pour les chaînes UTF-16. Introduit dans C++11.",
        "exemple": "char16_t u16_char = u'a';"
    },
    "char32_t": {
        "explication": "Type de caractère pour les chaînes UTF-32. Introduit dans C++11.",
        "exemple": "char32_t u32_char = U'a';"
    },
    "class": {
        "explication": "Définit une classe, un modèle pour la création d'objets.",
        "exemple": "class MaClasse {\npublic:\n    int ma_donnee;\n};"
    },
    "compl": {
        "explication": "Opérateur binaire de complément, équivalent à '~'.",
        "exemple": "int x = 5; // binaire 0101\nint y = compl x; // binaire ...11111010"
    },
    "concept": {
        "explication": "Spécifie des contraintes sur les paramètres de template. Introduit dans C++20.",
        "exemple": "template<typename T> concept C = requires(T x) { x+x; };"
    },
    "const": {
        "explication": "Indique qu'une variable ne peut pas être modifiée après son initialisation.",
        "exemple": "const double PI = 3.14159;"
    },
    "const_cast": {
        "explication": "Supprime la 'constness' d'une variable. À utiliser avec prudence.",
        "exemple": "const int a = 10;\nint& b = const_cast<int&>(a);"
    },
    "consteval": {
        "explication": "Indique que la fonction doit être évaluée à la compilation. Introduit dans C++20.",
        "exemple": "consteval int f() { return 5; }"
    },
    "constexpr": {
        "explication": "Indique que la valeur peut être évaluée à la compilation. Introduit dans C++11, amélioré dans C++14.",
        "exemple": "constexpr int carre(int n) { return n * n; }"
    },
    "constinit": {
        "explication": "Garantit que la variable est initialisée de manière statique. Introduit dans C++20.",
        "exemple": "constinit int x = 10;"
    },
    "continue": {
        "explication": "Passe à l'itération suivante de la boucle.",
        "exemple": "for (int i = 0; i < 5; ++i) {\n    if (i == 2) {\n        continue;\n    }\n}"
    },
    "co_await": {
        "explication": "Suspend et reprend une coroutine. Utilisé avec 'co_return' et 'co_yield'. Introduit dans C++20.",
        "exemple": "co_await std::suspend_always{};"
    },
    "co_return": {
        "explication": "Termine une coroutine et renvoie une valeur. Introduit dans C++20.",
        "exemple": "co_return 5;"
    },
    "co_yield": {
        "explication": "Suspend une coroutine, renvoie une valeur et attend une reprise. Introduit dans C++20.",
        "exemple": "co_yield 10;"
    },
    "decltype": {
        "explication": "Obtient le type de données d'une expression. Introduit dans C++11.",
        "exemple": "int x = 5;\ndecltype(x) y = 10; // y est un int"
    },
    "default": {
        "explication": "Le cas par défaut dans une instruction switch. Également utilisé pour les fonctions par défaut.",
        "exemple": "switch(num) {\n    default:\n        std::cout << \"Autre\";\n        break;\n}"
    },
    "delete": {
        "explication": "Libère la mémoire allouée par l'opérateur 'new'.",
        "exemple": "int* ptr = new int;\ndelete ptr;"
    },
    "do": {
        "explication": "Démarre une boucle 'do-while', qui s'exécute au moins une fois.",
        "exemple": "int i = 0;\ndo {\n    std::cout << i;\n    i++;\n} while (i < 3);"
    },
    "double": {
        "explication": "Le type de données pour les nombres à virgule flottante de double précision.",
        "exemple": "double pi = 3.14;"
    },
    "dynamic_cast": {
        "explication": "Effectue une conversion de type sécurisée pour les pointeurs de classes polymorphiques.",
        "exemple": "Base* b = new Derived;\nDerived* d = dynamic_cast<Derived*>(b);"
    },
    "else": {
        "explication": "Le bloc de code à exécuter si la condition 'if' est fausse.",
        "exemple": "if (age >= 18) {\n    // ...\n} else {\n    // ...\n}"
    },
    "enum": {
        "explication": "Définit un type de données consistant en un ensemble de constantes entières.",
        "exemple": "enum Couleur { ROUGE, VERT, BLEU };"
    },
    "explicit": {
        "explication": "Empêche les conversions de type implicites pour les constructeurs et les fonctions de conversion. Introduit dans C++11.",
        "exemple": "class A { explicit A(int x); };\nA a = 5; // Erreur de compilation"
    },
    "export": {
        "explication": "Utilisé pour la modularisation. Marque une déclaration comme étant disponible pour d'autres modules. Introduit dans C++20.",
        "exemple": "export module MonModule;"
    },
    "extern": {
        "explication": "Déclare une variable ou une fonction définie ailleurs, généralement dans un autre fichier.",
        "exemple": "extern int x;"
    },
    "false": {
        "explication": "Une valeur booléenne 'faux'.",
        "exemple": "bool is_ok = false;"
    },
    "final": {
        "explication": "Empêche une classe d'être héritée ou une fonction virtuelle d'être redéfinie. Introduit dans C++11.",
        "exemple": "class Base final { /* ... */ };"
    },
    "float": {
        "explication": "Le type de données pour les nombres à virgule flottante de simple précision.",
        "exemple": "float taux = 0.5f;"
    },
    "for": {
        "explication": "Crée une boucle qui s'exécute un nombre de fois déterminé.",
        "exemple": "for (int i = 0; i < 5; ++i) {\n    // ...\n}"
    },
    "friend": {
        "explication": "Accorde à une fonction ou une classe l'accès aux membres privés et protégés d'une autre classe.",
        "exemple": "class A {\n    friend void ma_fonction(A& a);\nprivate:\n    int x;\n};"
    },
    "goto": {
        "explication": "Permet un saut inconditionnel vers une étiquette dans la fonction.",
        "exemple": "goto ma_label;\n// ...\nma_label:\nstd::cout << \"Ici\";"
    },
    "if": {
        "explication": "Utilisé pour l'exécution conditionnelle du code.",
        "exemple": "if (score > 100) {\n    // ...\n}"
    },
    "import": {
        "explication": "Importe des déclarations depuis un module. Introduit dans C++20.",
        "exemple": "import std.core;"
    },
    "inline": {
        "explication": "Suggère au compilateur d'insérer le code d'une fonction directement à l'appel.",
        "exemple": "inline int somme(int a, int b) { return a+b; }"
    },
    "int": {
        "explication": "Le type de données pour les nombres entiers.",
        "exemple": "int annee = 2024;"
    },
    "long": {
        "explication": "Un modificateur de type pour les nombres entiers de plus grande taille.",
        "exemple": "long grande_valeur = 1234567890L;"
    },
    "module": {
        "explication": "Déclare un module, une nouvelle façon d'organiser le code. Introduit dans C++20.",
        "exemple": "export module MonModule;"
    },
    "mutable": {
        "explication": "Permet à un membre d'une classe d'être modifié même s'il fait partie d'un objet 'const'.",
        "exemple": "class MaClasse {\nprivate:\n    mutable int compteur;\n};"
    },
    "namespace": {
        "explication": "Permet de regrouper des déclarations pour éviter les conflits de noms.",
        "exemple": "namespace MonProjet {\n    int ma_variable;\n}"
    },
    "new": {
        "explication": "Alloue dynamiquement de la mémoire pour un objet et renvoie un pointeur.",
        "exemple": "int* ptr = new int;"
    },
    "noexcept": {
        "explication": "Spécifie qu'une fonction ne lève pas d'exceptions. Introduit dans C++11.",
        "exemple": "void ma_fonction() noexcept { /* ... */ }"
    },
    "not": {
        "explication": "Opérateur logique de négation, équivalent à '!'.",
        "exemple": "bool a = true;\nif (not a) { /* ... */ }"
    },
    "not_eq": {
        "explication": "Opérateur de comparaison 'différent de', équivalent à '!='.",
        "exemple": "if (a not_eq b) { /* ... */ }"
    },
    "nullptr": {
        "explication": "Une constante de pointeur nul. Introduit dans C++11.",
        "exemple": "int* ptr = nullptr;"
    },
    "operator": {
        "explication": "Définit une surcharge d'opérateur pour un type de classe.",
        "exemple": "class A { A operator+(const A& other); };"
    },
    "or": {
        "explication": "Opérateur logique 'ou', équivalent à '||'.",
        "exemple": "bool a = true, b = false;\nif (a or b) { /* ... */ }"
    },
    "or_eq": {
        "explication": "Opérateur d'assignation 'ou', équivalent à '|=. ",
        "exemple": "int x = 5;\nx or_eq 2; // x devient 7"
    },
    "override": {
        "explication": "Garantit qu'une fonction membre d'une classe dérivée redéfinit une fonction virtuelle de la classe de base. Introduit dans C++11.",
        "exemple": "class D : public B {\n    void f() override { /* ... */ }\n};"
    },
    "private": {
        "explication": "Spécificateur d'accès. Les membres de classe sont accessibles uniquement au sein de la classe elle-même.",
        "exemple": "class MaClasse {\nprivate:\n    int ma_donnee;\n};"
    },
    "protected": {
        "explication": "Spécificateur d'accès. Les membres sont accessibles au sein de la classe et des classes dérivées.",
        "exemple": "class MaClasse {\nprotected:\n    int ma_donnee;\n};"
    },
    "public": {
        "explication": "Spécificateur d'accès. Les membres sont accessibles de n'importe où.",
        "exemple": "class MaClasse {\npublic:\n    int ma_donnee;\n};"
    },
    "register": {
        "explication": "Suggère au compilateur de stocker une variable dans un registre. Déprécié en C++11 et retiré en C++17.",
        "exemple": "register int x;"
    },
    "reinterpret_cast": {
        "explication": "Convertit un pointeur vers un type de pointeur différent. À utiliser avec extrême prudence.",
        "exemple": "int* p = new int;\nchar* c = reinterpret_cast<char*>(p);"
    },
    "requires": {
        "explication": "Spécifie des contraintes sur les paramètres d'un template. Utilisé avec des concepts. Introduit dans C++20.",
        "exemple": "template<typename T> requires std::integral<T>\nvoid f(T t) { /* ... */ }"
    },
    "return": {
        "explication": "Termine l'exécution d'une fonction et renvoie une valeur.",
        "exemple": "int addition(int a, int b) { return a + b; }"
    },
    "short": {
        "explication": "Un modificateur de type pour des nombres entiers de plus petite taille.",
        "exemple": "short petit_nombre = 100;"
    },
    "signed": {
        "explication": "Spécifie un type entier avec un signe (positif et négatif).",
        "exemple": "signed int x = -10;"
    },
    "sizeof": {
        "explication": "Opérateur qui renvoie la taille en octets d'une variable ou d'un type de données.",
        "exemple": "int x;\nsize_t s = sizeof(x);"
    },
    "static": {
        "explication": "Indique une durée de vie statique. Peut aussi être utilisé pour les membres de classe.",
        "exemple": "void f() { static int compteur = 0; compteur++; }"
    },
    "static_assert": {
        "explication": "Vérifie une assertion au moment de la compilation. Introduit dans C++11.",
        "exemple": "static_assert(sizeof(int) == 4, \"int n'est pas 4 octets\");"
    },
    "static_cast": {
        "explication": "Effectue une conversion de type sûre et simple.",
        "exemple": "int i = 10;\nfloat f = static_cast<float>(i);"
    },
    "struct": {
        "explication": "Définit un type de données qui regroupe des variables. Les membres sont publics par défaut.",
        "exemple": "struct Point { int x; int y; };"
    },
    "switch": {
        "explication": "Permet de choisir un chemin d'exécution en fonction de la valeur d'une variable.",
        "exemple": "int choix = 1;\nswitch(choix) { case 1: /* ... */ }"
    },
    "template": {
        "explication": "Définit des fonctions ou des classes génériques qui peuvent opérer sur différents types de données.",
        "exemple": "template <typename T>\nT max(T a, T b) { /* ... */ }"
    },
    "this": {
        "explication": "Un pointeur vers l'objet courant d'une classe.",
        "exemple": "class A { void set_val(int v) { this->val = v; } };"
    },
    "thread_local": {
        "explication": "Indique qu'une variable est unique pour chaque thread. Introduit dans C++11.",
        "exemple": "thread_local int x = 0;"
    },
    "throw": {
        "explication": "Lève une exception pour signaler une erreur.",
        "exemple": "throw std::runtime_error(\"Erreur\");"
    },
    "true": {
        "explication": "Une valeur booléenne 'vrai'.",
        "exemple": "bool is_ok = true;"
    },
    "try": {
        "explication": "Démarre un bloc de code à surveiller pour d'éventuelles exceptions.",
        "exemple": "try { /* ... */ } catch (/* ... */) { /* ... */ }"
    },
    "typedef": {
        "explication": "Crée un alias pour un type de données existant.",
        "exemple": "typedef long long ll;\nll ma_variable = 1234;"
    },
    "typeid": {
        "explication": "Retourne un objet 'std::type_info' contenant des informations sur un type de données.",
        "exemple": "int x;\nstd::cout << typeid(x).name();"
    },
    "typename": {
        "explication": "Utilisé dans les templates pour indiquer que le nom qui suit est un type de données.",
        "exemple": "template <typename T>\nvoid ma_fonction(typename T::Iterateur arg) { /* ... */ }"
    },
    "union": {
        "explication": "Un type de données qui stocke différents membres dans le même emplacement de mémoire.",
        "exemple": "union MaUnion { int i; float f; };"
    },
    "unsigned": {
        "explication": "Modificateur pour spécifier un type entier non signé (uniquement des nombres positifs).",
        "exemple": "unsigned int x = 10;"
    },
    "using": {
        "explication": "Permet d'introduire des noms d'un espace de noms, ou de créer un alias de type.",
        "exemple": "using namespace std;\nusing Point = std::pair<int, int>;"
    },
    "virtual": {
        "explication": "Déclare une fonction membre dans une classe de base qui doit être redéfinie dans une classe dérivée.",
        "exemple": "class Base { public: virtual void f(); };"
    },
    "void": {
        "explication": "Indique qu'une fonction ne renvoie aucune valeur ou qu'un pointeur ne pointe vers aucun type spécifique.",
        "exemple": "void ma_fonction() { /* ... */ }"
    },
    "volatile": {
        "explication": "Indique au compilateur qu'une variable peut être modifiée à tout moment par un autre processus.",
        "exemple": "volatile int etat_registre;"
    },
    "wchar_t": {
        "explication": "Type de caractère large. Généralement utilisé pour les caractères Unicode.",
        "exemple": "wchar_t wc = L'a';"
    },
    "while": {
        "explication": "Crée une boucle qui s'exécute tant qu'une condition est vraie.",
        "exemple": "int i = 0;\nwhile (i < 3) {\n    i++;\n}"
    },
    "xor": {
        "explication": "Opérateur binaire 'ou exclusif', équivalent à '^'.",
        "exemple": "int x = 5, y = 3;\nint z = x xor y; // z est 6"
    },
    "xor_eq": {
        "explication": "Opérateur d'assignation 'ou exclusif', équivalent à '^='.",
        "exemple": "int x = 5;\nx xor_eq 2; // x devient 7"
    }
}

# --- Fonction pour afficher les détails du mot-clé sélectionné ---
def afficher_details(mot_cle):
    """Met à jour le panneau de détails avec les informations du mot-clé C++ sélectionné."""
    
    details = mots_cles_cpp_details.get(mot_cle, {"explication": "Détails non disponibles.", "exemple": "Pas d'exemple."})
    explication = details["explication"]
    exemple = details["exemple"]
    
    texte_complet = f"Explication :\n{explication}\n\nExemple (C++) :\n\n{exemple}"
    
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
app.title("Guide des Mots-clés de C++")

# --- Créer les deux cadres principaux ---
frame_liste = customtkinter.CTkFrame(master=app, width=250)
frame_liste.pack(pady=20, padx=20, fill="y", side="left")

frame_details = customtkinter.CTkFrame(master=app)
frame_details.pack(pady=20, padx=20, fill="both", expand=True, side="right")

# --- Contenu du cadre de la liste (gauche) ---
liste_label = customtkinter.CTkLabel(master=frame_liste, text="Mots-clés C++", font=("Helvetica", 18, "bold"))
liste_label.pack(pady=10, padx=10)

liste_frame = customtkinter.CTkScrollableFrame(master=frame_liste, width=200)
liste_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Ajouter un bouton pour chaque mot-clé
mots_cles_cpp = sorted(mots_cles_cpp_details.keys())
for mot in mots_cles_cpp:
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