import customtkinter

# --- Les données complètes des mots-clés, types et constantes de PHP ---
php_keywords_details = {
    "__CLASS__": {
        "explication": "Une constante magique qui renvoie le nom de la classe actuelle.",
        "exemple": "<?php\nclass MyClass {\n    public function getName() {\n        return __CLASS__;\n    }\n}\n?>"
    },
    "__DIR__": {
        "explication": "Une constante magique qui renvoie le chemin du répertoire du fichier.",
        "exemple": "<?php\necho __DIR__;\n?>"
    },
    "__FILE__": {
        "explication": "Une constante magique qui renvoie le chemin complet du fichier.",
        "exemple": "<?php\necho __FILE__;\n?>"
    },
    "__FUNCTION__": {
        "explication": "Une constante magique qui renvoie le nom de la fonction actuelle.",
        "exemple": "<?php\nfunction myFunction() {\n    echo __FUNCTION__;\n}\n?>"
    },
    "__LINE__": {
        "explication": "Une constante magique qui renvoie le numéro de ligne du fichier.",
        "exemple": "<?php\necho __LINE__;\n?>"
    },
    "__METHOD__": {
        "explication": "Une constante magique qui renvoie le nom de la méthode de la classe actuelle.",
        "exemple": "<?php\nclass MyClass {\n    public function myMethod() {\n        return __METHOD__;\n    }\n}\n?>"
    },
    "__NAMESPACE__": {
        "explication": "Une constante magique qui renvoie le nom de l'espace de noms actuel.",
        "exemple": "<?php\nnamespace App;\nclass MyClass {}\necho __NAMESPACE__;\n?>"
    },
    "__TRAIT__": {
        "explication": "Une constante magique qui renvoie le nom du trait en cours d'utilisation.",
        "exemple": "<?php\ntrait MyTrait {\n    public function getTraitName() {\n        return __TRAIT__;\n    }\n}\n?>"
    },
    "abstract": {
        "explication": "Indique qu'une classe ne peut pas être instanciée et qu'une méthode n'a pas de corps et doit être implémentée par les sous-classes.",
        "exemple": "<?php\nabstract class Animal {\n    abstract public function makeSound();\n?>"
    },
    "and": {
        "explication": "Opérateur logique 'et', équivalent à '&&', mais avec une précédence plus faible.",
        "exemple": "<?php\nif (true and false) {\n    // ...\n?>"
    },
    "array": {
        "explication": "Déclare un tableau. Peut être utilisé comme un hint de type.",
        "exemple": "<?php\nfunction processArray(array $arr) {\n    // ...\n}\n?>"
    },
    "as": {
        "explication": "Utilisé pour la boucle `foreach` pour parcourir les éléments d'un tableau et pour les alias avec `use`.",
        "exemple": "<?php\nforeach ($fruits as $fruit) {\n    echo $fruit;\n}\n?>"
    },
    "bool": {
        "explication": "Un type de données pour les valeurs booléennes `true` ou `false`.",
        "exemple": "<?php\nfunction is_valid(bool $val) {\n    return $val;\n?>"
    },
    "break": {
        "explication": "Termine la boucle la plus proche ou une instruction `switch`.",
        "exemple": "<?php\nfor ($i = 0; $i < 5; $i++) {\n    if ($i == 3) {\n        break;\n    }\n}"
    },
    "callable": {
        "explication": "Un hint de type qui indique que le paramètre doit être une fonction. Introduit en PHP 5.4.",
        "exemple": "<?php\nfunction call_func(callable $callback) {\n    $callback();\n}"
    },
    "case": {
        "explication": "Définit un bloc de code à exécuter dans une instruction `switch`.",
        "exemple": "<?php\nswitch ($day) {\n    case 1:\n        echo 'Lundi';\n        break;\n}"
    },
    "catch": {
        "explication": "Capture et gère une exception levée par un bloc `try`.",
        "exemple": "<?php\ntry {\n    throw new Exception();\n} catch (Exception $e) {\n    // ...\n}\n?>"
    },
    "class": {
        "explication": "Définit une classe, un modèle pour la création d'objets.",
        "exemple": "<?php\nclass User {\n    public string $name;\n}\n?>"
    },
    "clone": {
        "explication": "Crée une copie peu profonde d'un objet.",
        "exemple": "<?php\n$obj2 = clone $obj1;\n?>"
    },
    "const": {
        "explication": "Déclare une constante dans une classe ou un fichier. Une fois définie, sa valeur ne peut pas être changée.",
        "exemple": "<?php\nclass MaClasse {\n    const MA_CONST = 10;\n}\n?>"
    },
    "continue": {
        "explication": "Passe à l'itération suivante de la boucle, ignorant le reste du code de l'itération actuelle.",
        "exemple": "<?php\nfor ($i = 0; $i < 5; $i++) {\n    if ($i == 2) {\n        continue;\n    }\n}"
    },
    "declare": {
        "explication": "Définit des directives d'exécution pour un bloc de code (par exemple, `strict_types=1`).",
        "exemple": "<?php\ndeclare(strict_types=1);\n?>"
    },
    "default": {
        "explication": "Le cas par défaut dans une instruction `switch` si aucune correspondance n'est trouvée.",
        "exemple": "<?php\nswitch ($x) {\n    default:\n        echo 'Autre';\n}\n?>"
    },
    "die": {
        "explication": "Affiche un message et termine l'exécution du script. Alias de `exit()`.",
        "exemple": "<?php\n$file = fopen('file.txt', 'r') or die('Fichier introuvable');\n?>"
    },
    "do": {
        "explication": "Démarre une boucle `do-while`, qui s'exécute au moins une fois.",
        "exemple": "<?php\n$i = 0;\ndo {\n    $i++;\n} while ($i < 3);\n?>"
    },
    "echo": {
        "explication": "Affiche une ou plusieurs chaînes de caractères. Moins coûteux que `print()`.",
        "exemple": "<?php\necho 'Hello World!';\n?>"
    },
    "else": {
        "explication": "Le bloc de code à exécuter si la condition `if` est fausse.",
        "exemple": "<?php\nif ($age >= 18) {\n    echo 'Majeur';\n} else {\n    echo 'Mineur';\n}\n?>"
    },
    "elseif": {
        "explication": "Une condition alternative qui est vérifiée si la condition `if` précédente était fausse.",
        "exemple": "<?php\nif ($x == 1) { /* ... */ } elseif ($x == 2) { /* ... */ }\n?>"
    },
    "empty": {
        "explication": "Vérifie si une variable est vide. Renvoie `true` pour 0, '', null, false, un tableau vide, etc. C'est une construction de langage, pas une fonction.",
        "exemple": "<?php\nif (empty($var)) { /* ... */ }\n?>"
    },
    "enum": {
        "explication": "Définit un type d'énumération, qui représente un ensemble de valeurs nommées. Introduit en PHP 8.1.",
        "exemple": "<?php\nenum Status {\n    case DRAFT;\n    case PUBLISHED;\n}\n?>"
    },
    "exit": {
        "explication": "Termine l'exécution du script. Peut renvoyer un code de statut. Alias de `die()`.",
        "exemple": "<?php\nexit(1);\n?>"
    },
    "extends": {
        "explication": "Permet à une classe d'hériter des propriétés et des méthodes d'une autre classe.",
        "exemple": "<?php\nclass Dog extends Animal {\n    // ...\n}\n?>"
    },
    "final": {
        "explication": "Empêche une classe d'être héritée ou une méthode d'être surchargée dans une sous-classe.",
        "exemple": "<?php\nfinal class MyClass {\n    // ...\n}\n?>"
    },
    "finally": {
        "explication": "Définit un bloc de code qui s'exécute toujours, que des exceptions soient levées ou non. Introduit en PHP 5.5.",
        "exemple": "<?php\ntry { /* ... */ } finally {\n    echo 'Toujours exécuté';\n}\n?>"
    },
    "float": {
        "explication": "Un type de données pour les nombres à virgule flottante.",
        "exemple": "<?php\nfunction getPrice(): float {\n    return 9.99;\n}\n?>"
    },
    "fn": {
        "explication": "Définit une fonction fléchée (arrow function). Permet de capturer les variables de la portée parente par valeur. Introduit en PHP 7.4.",
        "exemple": "<?php\n$x = 10;\n$y = fn($z) => $x + $z;\n?>"
    },
    "for": {
        "explication": "Crée une boucle qui s'exécute un nombre de fois déterminé.",
        "exemple": "<?php\nfor ($i = 0; $i < 3; $i++) {\n    echo $i;\n}\n?>"
    },
    "foreach": {
        "explication": "Parcourt les éléments d'un tableau ou d'un objet. Recommandé pour les itérations.",
        "exemple": "<?php\nforeach ($array as $value) {\n    echo $value;\n}\n?>"
    },
    "function": {
        "explication": "Définit une fonction nommée.",
        "exemple": "<?php\nfunction add(int $a, int $b): int {\n    return $a + $b;\n}\n?>"
    },
    "global": {
        "explication": "Utilisé à l'intérieur d'une fonction pour accéder à une variable globale.",
        "exemple": "<?php\n$x = 10;\nfunction test() {\n    global $x;\n    echo $x;\n}\n?>"
    },
    "goto": {
        "explication": "Permet un saut inconditionnel vers une étiquette dans la même fonction. Déconseillé.",
        "exemple": "<?php\ngoto start;\n// ...\nstart: echo 'Hello';\n?>"
    },
    "if": {
        "explication": "Utilisé pour l'exécution conditionnelle du code.",
        "exemple": "<?php\nif ($score > 10) {\n    echo 'Gagné';\n}\n?>"
    },
    "implements": {
        "explication": "Utilisé dans une déclaration de classe pour implémenter une interface.",
        "exemple": "<?php\nclass MaClasse implements MonInterface {\n    // ...\n}\n?>"
    },
    "include": {
        "explication": "Inclut et évalue le fichier spécifié.",
        "exemple": "<?php\ninclude 'header.php';\n?>"
    },
    "include_once": {
        "explication": "Inclut et évalue le fichier spécifié, seulement si il n'a pas déjà été inclus.",
        "exemple": "<?php\ninclude_once 'config.php';\n?>"
    },
    "instanceof": {
        "explication": "Vérifie si un objet est une instance d'une classe ou si il implémente une interface.",
        "exemple": "<?php\nif ($obj instanceof MyClass) {\n    // ...\n}\n?>"
    },
    "int": {
        "explication": "Un type de données pour les entiers. Souvent utilisé pour le typage des paramètres et des retours.",
        "exemple": "<?php\nfunction add(int $a, int $b): int {\n    return $a + $b;\n}?>"
    },
    "interface": {
        "explication": "Définit un contrat pour les classes. Il peut contenir des méthodes `abstract`.",
        "exemple": "<?php\ninterface MaInterface {\n    public function maMethode();\n}\n?>"
    },
    "isset": {
        "explication": "Détermine si une variable est déclarée et différente de `null`. C'est une construction de langage, pas une fonction.",
        "exemple": "<?php\nif (isset($var)) {\n    echo '$var est définie';\n}\n?>"
    },
    "list": {
        "explication": "Assigne des variables à des valeurs d'un tableau. Fonctionne comme un opérateur.",
        "exemple": "<?php\n$arr = [1, 2, 3];\nlist($a, $b, $c) = $arr;\n?>"
    },
    "match": {
        "explication": "Une expression de contrôle plus stricte et plus concise que `switch`, qui retourne une valeur et utilise la comparaison `===`. Introduit en PHP 8.",
        "exemple": "<?php\n$status = 200;\n$message = match($status) {\n    200 => 'OK',\n    404 => 'Not Found',\n    default => 'Error',\n};\n?>"
    },
    "mixed": {
        "explication": "Un type de données indiquant qu'un paramètre ou un retour peut être de n'importe quel type. Équivalent à une union de tous les types. Introduit en PHP 8.",
        "exemple": "<?php\nfunction process(mixed $data): mixed {\n    // ...\n}\n?>"
    },
    "namespace": {
        "explication": "Organise les classes et autres types en hiérarchies logiques pour éviter les conflits de noms.",
        "exemple": "<?php\nnamespace App\\Controllers;\n?>"
    },
    "new": {
        "explication": "Crée une nouvelle instance d'une classe.",
        "exemple": "<?php\n$obj = new User();\n?>"
    },
    "null": {
        "explication": "Représente l'absence de valeur. Une variable sans valeur a `null`.",
        "exemple": "<?php\n$x = null;\n?>"
    },
    "object": {
        "explication": "Un type de données pour les instances de classes.",
        "exemple": "<?php\nfunction processObject(object $obj) {\n    // ...\n}\n?>"
    },
    "or": {
        "explication": "Opérateur logique 'ou', équivalent à `||`, mais avec une précédence plus faible.",
        "exemple": "<?php\nif (true or false) {\n    // ...\n}\n?>"
    },
    "parent": {
        "explication": "Fait référence à la classe parente. Utilisé pour appeler les méthodes ou propriétés de la classe mère.",
        "exemple": "<?php\nparent::myMethod();\n?>"
    },
    "print": {
        "explication": "Affiche une chaîne de caractères et renvoie toujours 1. Plus lent que `echo`.",
        "exemple": "<?php\nprint 'Hello World!';\n?>"
    },
    "private": {
        "explication": "Modificateur d'accès. Les membres sont accessibles uniquement au sein de la classe elle-même.",
        "exemple": "<?php\nprivate $password;\n?>"
    },
    "protected": {
        "explication": "Modificateur d'accès. Les membres sont accessibles au sein de la classe et des classes dérivées.",
        "exemple": "<?php\nprotected $age;\n?>"
    },
    "public": {
        "explication": "Modificateur d'accès. Les membres sont accessibles de n'importe où.",
        "exemple": "<?php\npublic $name;\n?>"
    },
    "readonly": {
        "explication": "Indique qu'une propriété de classe ne peut être modifiée qu'à partir de son constructeur. Introduit en PHP 8.1.",
        "exemple": "<?php\nclass Post {\n    public readonly string $title;\n    public function __construct(string $title) {\n        $this->title = $title;\n    }\n}\n?>"
    },
    "require": {
        "explication": "Inclut et évalue un fichier. Lève une erreur fatale si le fichier n'est pas trouvé.",
        "exemple": "<?php\nrequire 'database.php';\n?>"
    },
    "require_once": {
        "explication": "Inclut et évalue un fichier, mais seulement si il n'a pas déjà été inclus. Lève une erreur fatale.",
        "exemple": "<?php\nrequire_once 'vendor/autoload.php';\n?>"
    },
    "return": {
        "explication": "Termine l'exécution d'une fonction et renvoie une valeur.",
        "exemple": "<?php\nreturn $a + $b;\n?>"
    },
    "self": {
        "explication": "Fait référence au type de la classe actuelle. Peut être utilisé comme un hint de type.",
        "exemple": "<?php\nclass MyClass {\n    public static function create(): self {\n        return new self();\n    }\n}\n?>"
    },
    "static": {
        "explication": "Indique qu'un membre appartient à la classe elle-même, et non à une instance spécifique. Peut aussi être un hint de type.",
        "exemple": "<?php\nclass MaClasse {\n    public static $count = 0;\n    public function getCount(): static {\n        return new static();\n    }\n}\n?>"
    },
    "string": {
        "explication": "Un type de données pour les chaînes de caractères. Souvent utilisé pour le typage des paramètres et des retours.",
        "exemple": "<?php\nfunction greet(string $name): string {\n    return 'Hello, ' . $name;\n}?>"
    },
    "switch": {
        "explication": "Permet d'exécuter un bloc de code parmi plusieurs en fonction d'une expression.",
        "exemple": "<?php\nswitch ($choice) {\n    case 1: /* ... */ break;\n}\n?>"
    },
    "throw": {
        "explication": "Lève une exception personnalisée.",
        "exemple": "<?php\nthrow new Exception('Erreur');\n?>"
    },
    "trait": {
        "explication": "Permet de réutiliser du code dans différentes classes, sans héritage. Introduit en PHP 5.4.",
        "exemple": "<?php\ntrait Logger {\n    // ...\n}\n?>"
    },
    "true": {
        "explication": "La valeur booléenne 'vraie'.",
        "exemple": "<?php\n$is_active = true;\n?>"
    },
    "try": {
        "explication": "Démarre un bloc de code à tester pour des erreurs potentielles.",
        "exemple": "<?php\ntry {\n    // ...\n} catch (Exception $e) { /* ... */ }\n?>"
    },
    "unset": {
        "explication": "Détruit la variable spécifiée. C'est une construction de langage, pas une fonction.",
        "exemple": "<?php\n$var = 10;\nunset($var);\n?>"
    },
    "use": {
        "explication": "Utilisé pour importer des espaces de noms ou des 'traits'.",
        "exemple": "<?php\nuse App\\Controllers\\Controller;\n?>"
    },
    "void": {
        "explication": "Un type de retour qui indique qu'une fonction ne retourne aucune valeur.",
        "exemple": "<?php\nfunction do_something(): void {\n    echo 'Doing something...';\n}?>"
    },
    "while": {
        "explication": "Crée une boucle qui s'exécute tant qu'une condition est vraie.",
        "exemple": "<?php\n$i = 0;\nwhile ($i < 3) {\n    $i++;\n}\n?>"
    },
    "xor": {
        "explication": "Opérateur logique 'ou exclusif', équivalent à `^`, mais avec une précédence plus faible.",
        "exemple": "<?php\nif (true xor true) { /* ... */ } // false\n?>"
    },
    "yield": {
        "explication": "Utilisé pour créer des générateurs, qui sont des fonctions itératives. Introduit en PHP 5.5.",
        "exemple": "<?php\nfunction gen() {\n    yield 1;\n    yield 2;\n}\n?>"
    },
    "yield from": {
        "explication": "Délègue à un autre générateur, itérable ou tableau. Introduit en PHP 7.",
        "exemple": "<?php\nfunction gen() {\n    yield from [1, 2];\n}\n?>"
    }
}

# --- Fonction pour afficher les détails du mot-clé sélectionné ---
def afficher_details(mot_cle):
    """Met à jour le panneau de détails avec les informations du mot-clé PHP sélectionné."""
    
    details = php_keywords_details.get(mot_cle, {"explication": "Détails non disponibles.", "exemple": "Pas d'exemple."})
    explication = details["explication"]
    exemple = details["exemple"]
    
    texte_complet = f"Explication :\n{explication}\n\nExemple (PHP) :\n\n{exemple}"
    
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
app.title("Guide des Mots-clés de PHP")

# --- Créer les deux cadres principaux ---
frame_liste = customtkinter.CTkFrame(master=app, width=250)
frame_liste.pack(pady=20, padx=20, fill="y", side="left")

frame_details = customtkinter.CTkFrame(master=app)
frame_details.pack(pady=20, padx=20, fill="both", expand=True, side="right")

# --- Contenu du cadre de la liste (gauche) ---
liste_label = customtkinter.CTkLabel(master=frame_liste, text="Mots-clés PHP", font=("Helvetica", 18, "bold"))
liste_label.pack(pady=10, padx=10)

liste_frame = customtkinter.CTkScrollableFrame(master=frame_liste, width=200)
liste_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Ajouter un bouton pour chaque mot-clé
mots_cles_php = sorted(php_keywords_details.keys())
for mot in mots_cles_php:
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