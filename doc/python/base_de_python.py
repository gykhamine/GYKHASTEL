import customtkinter as ctk
import sys
import io

# --- Configuration de la fenêtre principale CustomTkinter ---
ctk.set_appearance_mode("System")  # Modes: "System" (par défaut), "Dark", "Light"
ctk.set_default_color_theme("blue") # Thèmes: "blue" (par défaut), "green", "dark-blue"

class PythonConceptExplorer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Explorateur de Concepts Python")
        self.geometry("1100x800")
        # CORRECTION ICI: Utiliser minsize() pour définir la taille minimale
        self.minsize(900, 700) # Définit la largeur et la hauteur minimales de la fenêtre

        # --- Création de la vue par onglets (CTkTabview) ---
        # Ajustement de la taille du tabview pour mieux s'adapter à la fenêtre
        self.tab_view = ctk.CTkTabview(self, width=1080, height=760)
        self.tab_view.pack(pady=10, padx=10, fill="both", expand=True)

        # --- Ajout des onglets pour chaque concept ---
        self.tab_view.add("Variables")
        self.tab_view.add("Fonctions")
        self.tab_view.add("Conditions")
        self.tab_view.add("Boucles")
        self.tab_view.add("Exceptions")
        self.tab_view.add("Classes")
        self.tab_view.add("Combinaison & Astuces")

        # --- Dictionnaire pour stocker les Textbox de résultat ---
        self.output_textboxes = {}

        # --- Contenu pour l'onglet "Variables" ---
        self.create_concept_tab(
            tab_frame=self.tab_view.tab("Variables"),
            title="Variables : Les Conteneurs de Données",
            explanation="""Au cœur de la programmation, il faut un endroit pour stocker les informations avant de les traiter. C'est le rôle des **variables**. Considérez une variable comme une boîte étiquetée ou un conteneur nommé dans la mémoire de votre ordinateur. Lorsque vous créez une variable, vous réservez un espace en mémoire pour stocker une donnée et lui donnez un nom mémorable. Ce nom vous permet de référencer, récupérer et manipuler la donnée stockée tout au long de votre programme.

La beauté des variables est que leur contenu peut *varier* – elles ne sont pas fixes. Vous pouvez y stocker une donnée, puis la remplacer plus tard par une autre. Cette nature dynamique est fondamentale pour la façon dont les programmes s'adaptent et répondent aux conditions changeantes ou aux entrées de l'utilisateur.

**Pourquoi sont-elles importantes ?**
Les variables sont la pierre angulaire de la manipulation des données. Sans elles, chaque donnée devrait être codée en dur dans vos instructions, rendant les programmes inflexibles, difficiles à modifier et impossibles à adapter. Les variables permettent :
1.  **Stockage de données :** Elles contiennent des nombres, du texte, des valeurs vrai/faux, des listes d'éléments et des structures de données plus complexes.
2.  **Flexibilité :** Les programmes peuvent travailler avec des données qui changent (ex: entrée utilisateur, lectures de capteurs).
3.  **Lisibilité :** Donner des noms significatifs aux données rend votre code beaucoup plus facile à comprendre. `prix_article + taxe_vente` est bien plus clair que `5 + 7`.
4.  **Réutilisabilité :** Vous pouvez utiliser le même nom de variable plusieurs fois pour représenter différentes valeurs à différents moments de l'exécution de votre programme, ou pour représenter une valeur cohérente qui pourrait être mise à jour de manière centralisée.

**Types de Données (Types de Variables) :**
Bien que les variables soient conceptuellement agnostiques au langage, le *type* de données qu'elles contiennent est crucial. Python est un langage à typage dynamique, ce qui signifie que le type est inféré lors de l'affectation.
* **Entiers (`int`) :** Nombres entiers (ex: `5`, `-100`, `0`).
* **Nombres à virgule flottante (`float`) :** Nombres décimaux (ex: `3.14`, `-0.5`).
* **Chaînes de caractères (`str`) :** Séquences de caractères, utilisées pour le texte (ex: `"Bonjour Monde"`, `'Python'`). Encadrées par des guillemets.
* **Booléens (`bool`) :** Représentent des valeurs de vérité, soit `True` (vrai) ou `False` (faux). Utilisés pour les opérations logiques et les conditions.
* **Collections :**
    * **Listes (`list`) :** Collections ordonnées et modifiables d'éléments (ex: `[1, 2, 3]`, `["pomme", "banane"]`).
    * **Dictionnaires (`dict`) :** Collections non ordonnées de paires clé-valeur (ex: `{"nom": "Alice", "age": 30}`).

**Conventions de Nommage :**
* **Noms significatifs :** Les noms doivent clairement indiquer le rôle de la variable.
* **`snake_case` :** Convention typique en Python (mots en minuscules séparés par des underscores, ex: `prix_total`).
* **Évitez les mots-clés :** N'utilisez pas les mots réservés du langage (ex: `if`, `for`, `class`).

**Portée (Scope) des Variables :**
La **portée** d'une variable désigne la région de votre programme où elle est accessible.
* **Variables globales :** Déclarées en dehors de toute fonction ou bloc, accessibles partout. Leur utilisation excessive peut rendre le code difficile à suivre.
* **Variables locales :** Déclarées à l'intérieur d'une fonction ou d'un bloc spécifique, accessibles uniquement dans ce contexte. Elles sont généralement détruites à la fin de la fonction, favorisant la modularité.
""",
            code_example="""# Python Code Exemple: Variables

# 1. Affectation de base
message = "Bonjour, Python !" # Variable chaîne de caractères
compteur = 10               # Variable entière
valeur_pi = 3.14159         # Variable flottante
est_actif = True            # Variable booléenne

print(f"Message: {message} (Type: {type(message)})")
print(f"Compteur: {compteur} (Type: {type(compteur)})")
print(f"Valeur de Pi: {valeur_pi} (Type: {type(valeur_pi)})")
print(f"Est actif: {est_actif} (Type: {type(est_actif)})")

# 2. Réaffectation de variables
temperature = 25
print(f"Température initiale: {temperature}")
temperature = 28.5 # Une variable peut changer de valeur et même de type
print(f"Température mise à jour: {temperature}")

# 3. Affectation multiple
x, y, z = 1, 2, "trois"
print(f"x: {x}, y: {y}, z: {z}")

# 4. Variables de liste et de dictionnaire
ma_liste = ["pomme", "banane", "cerise"]
mon_dictionnaire = {"nom": "Bob", "ville": "New York"}

print(f"Ma Liste: {ma_liste}")
print(f"Mon Dictionnaire: {mon_dictionnaire}")

# 5. Exemple de portée de variable
variable_globale = "Je suis globale !"

def ma_fonction():
    variable_locale = "Je suis locale à ma_fonction !"
    print(f"À l'intérieur de la fonction (globale): {variable_globale}")
    print(f"À l'intérieur de la fonction (locale): {variable_locale}")

ma_fonction()
print(f"À l'extérieur de la fonction (globale): {variable_globale}")
# print(variable_locale) # Ceci provoquerait une erreur (NameError)
"""
        )

        # --- Contenu pour l'onglet "Fonctions" ---
        self.create_concept_tab(
            tab_frame=self.tab_view.tab("Fonctions"),
            title="Fonctions : Les Blocs de Code Réutilisables",
            explanation="""Imaginez que vous ayez une recette complexe et qu'une étape, comme "fouetter la crème jusqu'à obtenir des pics fermes", apparaisse plusieurs fois. Au lieu d'écrire toutes les instructions pour fouetter la crème à chaque fois, vous diriez simplement "fouetter la crème". En programmation, les **fonctions** servent à cela.

Une fonction est un bloc de code nommé et autonome, conçu pour effectuer une tâche ou un calcul spécifique. Elle prend zéro ou plusieurs entrées (appelées **paramètres** ou **arguments**), exécute sa tâche, et peut ou non produire une sortie (une **valeur de retour**). Une fois définie, une fonction peut être **appelée** (exécutée) plusieurs fois depuis différentes parties de votre programme, vous évitant ainsi d'écrire le même code à répétition.

**Pourquoi sont-elles importantes ?**
Les fonctions sont les piliers d'une bonne conception logicielle, permettant :
1.  **Modularité :** Elles décomposent les problèmes complexes en morceaux plus petits, gérables et indépendants. Cela rend le programme global plus facile à comprendre, à développer et à déboguer.
2.  **Réutilisabilité :** Le code défini une fois dans une fonction peut être utilisé de nombreuses fois sans être réécrit. Cela permet de gagner du temps de développement et de réduire les risques d'erreurs.
3.  **Lisibilité :** Donner un nom significatif à une fonction (ex: `calculer_aire`, `valider_email`) indique immédiatement ce que ce bloc de code fait, améliorant la clarté du code.
4.  **Maintenabilité :** Si une logique doit être modifiée (ex: comment une aire est calculée), il suffit de la modifier à un seul endroit (la définition de la fonction), plutôt que de rechercher et de mettre à jour chaque instance où cette logique était dupliquée.
5.  **Abstraction :** Les fonctions vous permettent de vous concentrer sur *ce que* fait un morceau de code, plutôt que sur *comment* il le fait.

**Anatomie d'une Fonction :**
* **Mot-clé `def` :** Indique la définition d'une fonction.
* **Nom de la fonction :** Un identifiant unique qui décrit son objectif.
* **Paramètres :** Variables entre parenthèses dans la définition de la fonction. Ce sont des placeholders pour les valeurs passées lors de l'appel.
* **Corps de la fonction :** Le bloc de code indenté sous la définition, où la logique réside.
* **`return` :** L'instruction `return` renvoie une valeur à la partie du code qui a appelé la fonction. Une fonction peut ne rien retourner explicitement (elle retourne alors `None`).

**Appel d'une Fonction :**
Une fois définie, une fonction est exécutée en utilisant son nom suivi de parenthèses, en fournissant les arguments nécessaires.

**Types de Paramètres :**
* **Arguments positionnels :** Passés aux paramètres dans l'ordre de leur définition.
* **Arguments par mot-clé :** Identifiés par leurs noms de paramètres, permettant un ordre flexible (ex: `saluer(nom="Alice")`).
* **Paramètres par défaut :** Ont des valeurs par défaut, les rendant facultatifs lors de l'appel (ex: `envoyer_message(destinataire, message="Bonjour")`).
* **`*args` et `**kwargs` :** Permettent de gérer un nombre arbitraire d'arguments positionnels et par mot-clé, respectivement.

**Docstrings :**
Les fonctions bien conçues sont bien documentées. Les **docstrings** (chaînes de caractères entre triples guillemets) sont une pratique standard pour expliquer le but, les paramètres et la valeur de retour d'une fonction.
""",
            code_example="""# Python Code Exemple: Fonctions

# 1. Fonction sans paramètres et sans valeur de retour
def saluer():
    \"\"\"Affiche un simple message de salutation.\"\"\"
    print("Bonjour, Monde !")

saluer() # Appel de la fonction

# 2. Fonction avec paramètres et une valeur de retour
def additionner_nombres(nombre1, nombre2):
    \"\"\"
    Additionne deux nombres et retourne leur somme.
    Args:
        nombre1 (int/float): Le premier nombre.
        nombre2 (int/float): Le deuxième nombre.
    Returns:
        int/float: La somme de nombre1 et nombre2.
    \"\"\"
    resultat_somme = nombre1 + nombre2
    return resultat_somme

resultat = additionner_nombres(10, 5)
print(f"La somme de 10 et 5 est: {resultat}")

# 3. Fonction avec paramètres par défaut
def envoyer_message(destinataire, message="Salut !"):
    \"\"\"Envoie un message à un destinataire, avec un message par défaut.\"\"\"
    print(f"À: {destinataire} -> Message: {message}")

envoyer_message("Alice")
envoyer_message("Bob", "Comment vas-tu ?")

# 4. Fonction avec *args (arguments positionnels arbitraires)
def calculer_moyenne(*nombres):
    \"\"\"Calcule la moyenne d'un nombre variable d'arguments.\"\"\"
    if not nombres: # Condition pour éviter la division par zéro si aucun nombre n'est donné
        return 0
    return sum(nombres) / len(nombres)

moyenne1 = calculer_moyenne(1, 2, 3)
moyenne2 = calculer_moyenne(10, 20, 30, 40)
print(f"Moyenne de (1, 2, 3): {moyenne1}")
print(f"Moyenne de (10, 20, 30, 40): {moyenne2}")

# 5. Fonction avec **kwargs (arguments par mot-clé arbitraires)
def afficher_infos_utilisateur(**infos):
    \"\"\"Affiche les informations utilisateur à partir d'arguments par mot-clé.\"\"\"
    print("Infos Utilisateur:")
    for cle, valeur in infos.items():
        # Utilise .title() pour mettre la première lettre en majuscule, .replace() pour l'affichage
        print(f"  {cle.replace('_', ' ').title()}: {valeur}")

afficher_infos_utilisateur(nom="Charlie", age=28, ville="Londres")
afficher_infos_utilisateur(produit="Ordinateur Portable", prix=1200, categorie="Électronique")
"""
        )

        # --- Contenu pour l'onglet "Conditions" ---
        self.create_concept_tab(
            tab_frame=self.tab_view.tab("Conditions"),
            title="Conditions : Prendre des Décisions",
            explanation="""Imaginez que vous suivez un organigramme. À certains points, il y a un losange posant une question "oui/non". Selon votre réponse, vous suivez un chemin différent. En programmation, les **conditions** (ou instructions conditionnelles, ou structures de contrôle de flux) sont l'équivalent de ces points de décision.

Une condition permet à votre programme de faire des choix. Elle évalue une expression donnée (qui produit généralement une valeur booléenne `True` ou `False`) et exécute différents blocs de code en fonction de cette évaluation. Cette capacité est fondamentale pour créer des logiciels dynamiques et réactifs qui peuvent s'adapter à des entrées, des états ou des interactions utilisateur variés.

**Pourquoi sont-elles importantes ?**
Sans conditions, un programme serait une série linéaire d'instructions, exécutant les mêmes étapes à chaque fois, quelles que soient les données ou les circonstances. Les conditions fournissent la logique de branchement nécessaire pour :
1.  **Flexibilité :** Les programmes peuvent réagir différemment à diverses entrées (ex: "si l'utilisateur clique sur A, faire X ; si l'utilisateur clique sur B, faire Y").
2.  **Adaptabilité :** Le code peut ajuster son comportement en fonction de l'état actuel des données (ex: "si le solde bancaire est faible, ne pas autoriser le retrait").
3.  **Validation :** Les entrées peuvent être vérifiées pour leur exactitude avant d'être traitées (ex: "si l'âge est négatif, afficher une erreur").
4.  **Gestion des erreurs :** Des actions spécifiques peuvent être entreprises lorsque certaines conditions (comme des données introuvables) se produisent.
5.  **Expérience utilisateur :** Adaptation des réponses, des fonctionnalités ou des affichages en fonction des préférences ou des autorisations de l'utilisateur.

**La Structure Conditionnelle de Base (`if-elif-else`) :**
* `if` : Introduit la première condition. Si l'expression qui la suit est `True`, le bloc de code immédiatement après est exécuté.
* `elif` (raccourci de "else if") : Optionnel. Si la condition `if` était `False`, le programme vérifie alors cette condition `elif`. S'il est `True`, son bloc de code associé est exécuté. Vous pouvez avoir plusieurs clauses `elif`.
* `else` : Optionnel. Si aucune des conditions `if` ou `elif` précédentes n'a été évaluée à `True`, le bloc de code associé à `else` est exécuté comme un recours par défaut.
Un seul de ces blocs s'exécutera dans une seule chaîne `if-elif-else`. Une fois qu'une condition est remplie et que son bloc est exécuté, le programme saute généralement le reste de la chaîne.

**Expressions Booléennes :**
Le cœur de toute condition est une **expression booléenne** – une expression qui évalue à `True` ou `False`. Ces expressions sont généralement formées à l'aide :
* **Opérateurs de comparaison :** `==` (égal à), `!=` (différent de), `<` (inférieur à), `>` (supérieur à), `<=` (inférieur ou égal à), `>=` (supérieur ou égal à).
* **Opérateurs logiques :**
    * `and` : Retourne `True` si *toutes* les conditions sont `True`.
    * `or` : Retourne `True` si *au moins une* condition est `True`.
    * `not` : Inverse la valeur booléenne.
* **Opérateurs d'appartenance (`in`) :** Vérifient si une valeur est présente dans une séquence (ex: `element in ma_liste`).

**Indentation :** Python utilise l'indentation (espacement au début de la ligne) pour définir les blocs de code associés aux instructions `if`, `elif` et `else`. Une indentation cohérente est vitale pour la lisibilité et la correction.

**Conditions imbriquées :** Les conditions peuvent être **imbriquées**, c'est-à-dire qu'une instruction `if` peut contenir une autre instruction `if` dans son bloc. Cela permet des processus de prise de décision plus complexes.

**Opérateur Ternaire (Expressions Conditionnelles) :** Pour les instructions `if-else` simples sur une seule ligne (ex: `statut = "Majeur" if age >= 18 else "Mineur"`).
""",
            code_example="""# Python Code Exemple: Conditions

# 1. Structure if-elif-else de base
score = 75

if score >= 90:
    note = "A"
elif score >= 80:
    note = "B"
elif score >= 70:
    note = "C"
elif score >= 60:
    note = "D"
else:
    note = "F"

print(f"Avec un score de {score}, votre note est: {note}")

# 2. Utilisation des opérateurs logiques (`and`, `or`, `not`)
age = 25
a_permis = True
est_fatigue = False

if age >= 18 and a_permis:
    print("Vous êtes assez âgé et avez un permis pour conduire.")
elif age < 18:
    print("Vous êtes trop jeune pour conduire.")
else:
    print("Vous avez besoin d'un permis pour conduire.")

if not est_fatigue:
    print("Vous êtes plein d'énergie !")
else:
    print("Vous devriez vous reposer.")

# 3. Opérateur Ternaire (Expression Conditionnelle)
statut = "Adulte" if age >= 18 else "Mineur"
print(f"En fonction de l'âge {age}, vous êtes un {statut}.")

# 4. Vérification d'appartenance (`in`)
fruit = "pomme"
panier_de_fruits = ["banane", "orange", "pomme"]

if fruit in panier_de_fruits:
    print(f"Oui, {fruit} est dans le panier.")
else:
    print(f"Non, {fruit} n'est pas dans le panier.")

# 5. Conditions imbriquées
role_utilisateur = "admin"
niveau_acces = "Complet"

if role_utilisateur == "admin":
    print("Privilèges d'administrateur accordés.")
    if niveau_acces == "Complet":
        print("Vous avez un contrôle administratif complet.")
    else:
        print("Accès administrateur limité.")
else:
    print("Privilèges d'utilisateur standard.")
"""
        )

        # --- Contenu pour l'onglet "Boucles" ---
        self.create_concept_tab(
            tab_frame=self.tab_view.tab("Boucles"),
            title="Boucles : Répéter des Actions",
            explanation="""Imaginez que vous avez une liste de 100 noms de clients et que vous devez envoyer un e-mail personnalisé à chacun. Écririez-vous le code "envoyer e-mail" 100 fois ? Absolument pas ! C'est là que les **boucles** entrent en jeu.

Une boucle est une instruction de contrôle de flux qui permet à un bloc de code d'être exécuté à plusieurs reprises jusqu'à ce qu'une certaine condition soit remplie ou pour chaque élément d'une collection. Les boucles sont fondamentales pour automatiser les tâches répétitives, traiter des collections de données et itérer à travers des séquences.

**Pourquoi sont-elles importantes ?**
Les boucles sont indispensables pour créer des programmes efficaces et concis, permettant :
1.  **Automatisation :** Effectuer des actions répétitives sans réécrire le même code (ex: traiter toutes les lignes d'un fichier, envoyer plusieurs messages).
2.  **Traitement des données :** Itérer sur des collections de données (listes, chaînes de caractères, etc.) pour effectuer des opérations sur chaque élément (ex: calculer la somme des nombres dans une liste, trouver un élément spécifique).
3.  **Itération :** Parcourir des séquences de manière structurée (ex: compter de 1 à 10, traverser une structure d'arbre).
4.  **Conciseness :** Réduire la quantité de code nécessaire, rendant les programmes plus courts, plus lisibles et moins sujets aux erreurs.
5.  **Comportement dynamique :** Permettre aux programmes de s'adapter à des données de taille inconnue (ex: lire des données d'un capteur jusqu'à ce qu'il n'y ait plus de données).

**Types de Boucles :**
* **Boucle `for` :** Utilisée lorsque vous connaissez (ou pouvez déterminer) le nombre d'itérations à l'avance, ou lorsque vous souhaitez itérer sur chaque élément d'une collection. En Python, elle est souvent utilisée pour parcourir des listes, des tuples, des chaînes de caractères, ou des plages de nombres (`range()`).
* **Boucle `while` :** Exécute un bloc de code **tant qu'une condition spécifiée reste `True`**. Elle est utilisée lorsque vous ne savez pas à l'avance combien de fois la boucle doit s'exécuter ; elle continue jusqu'à ce qu'un certain état soit atteint. Attention aux **boucles infinies** si la condition ne devient jamais `False`.

**Instructions de Contrôle de Boucle :**
* `break` : Termine immédiatement la boucle en cours, et l'exécution se poursuit avec l'instruction suivant la boucle. Utile pour sortir d'une boucle prématurément.
* `continue` : Saute le reste de l'itération actuelle de la boucle et passe à l'itération suivante. Utile pour ignorer certains éléments ou conditions.
* `else` (avec `for`/`while`) : Clause optionnelle associée à une boucle `for` ou `while` qui s'exécute uniquement si la boucle se termine normalement (c'est-à-dire sans rencontrer d'instruction `break`).

**Boucles imbriquées :** Les boucles peuvent être **imbriquées**, ce qui signifie qu'une boucle peut être placée à l'intérieur d'une autre. La boucle intérieure effectue toutes ses itérations pour *chaque* itération de la boucle extérieure.
""",
            code_example="""# Python Code Exemple: Boucles

# 1. Boucle For: Itérer sur une liste
fruits = ["pomme", "banane", "cerise"]
print("Itération sur les fruits:")
for fruit in fruits:
    print(fruit)

# 2. Boucle For: Utilisation de range() pour un nombre fixe d'itérations
print("\\nComptage de 0 à 4:")
for i in range(5): # Génère des nombres de 0 jusqu'à (mais non compris) 5
    print(i)

# 3. Boucle While: Boucler jusqu'à ce qu'une condition soit remplie
compteur = 0
print("\\nCompteur de boucle While:")
while compteur < 3:
    print(compteur)
    compteur += 1 # Important: incrémenter pour éviter une boucle infinie

# 4. Boucle avec `break`
print("\\nBoucle avec break (s'arrête à 3):")
for i in range(10):
    if i == 3:
        break
    print(i)

# 5. Boucle avec `continue`
print("\\nBoucle avec continue (saute 3):")
for i in range(5):
    if i == 3:
        continue
    print(i)

# 6. Boucle For avec clause `else`
print("\\nBoucle For avec else (exécuté si pas de break):")
for i in range(2):
    print(f"Boucle: {i}")
else:
    print("Boucle terminée avec succès !")

# 7. Boucles imbriquées (pour une structure 2D comme un tableau)
print("\\nBoucles imbriquées (grille 2x3):")
for ligne in range(2):
    for colonne in range(3):
        print(f"({ligne}, {colonne})", end=" ") # end=" " garde la sortie sur la même ligne
    print() # Nouvelle ligne après chaque ligne (row)
"""
        )

        # --- Contenu pour l'onglet "Exceptions" ---
        self.create_concept_tab(
            tab_frame=self.tab_view.tab("Exceptions"),
            title="Exceptions : Gérer l'Imprévu",
            explanation="""Imaginez que vous suivez un ensemble d'instructions précises (votre programme), et soudain, vous rencontrez quelque chose de complètement inattendu – comme essayer de diviser par zéro, d'ouvrir un fichier qui n'existe pas, ou de recevoir du texte alors que vous attendiez un nombre. Si votre programme s'arrête brusquement avec un message d'erreur, ce n'est pas très convivial.

Les **exceptions** sont un moyen structuré pour les programmes de signaler qu'un événement inhabituel ou une erreur s'est produit pendant l'exécution. Au lieu de planter, le programme "lève" ou "déclenche" une exception. Cette exception est un objet qui contient des informations sur l'erreur. Votre programme peut alors "attraper" ou "gérer" cette exception, ce qui lui permet de répondre gracieusement au problème plutôt que de se terminer de manière inattendue.

**Pourquoi sont-elles importantes ?**
Une gestion efficace des exceptions est cruciale pour construire des logiciels robustes, fiables et conviviaux. Elle permet :
1.  **Récupération gracieuse des erreurs :** Au lieu de planter, le programme peut informer l'utilisateur, enregistrer l'erreur, tenter de résoudre le problème ou continuer dans un état dégradé mais fonctionnel.
2.  **Robustesse :** Les programmes deviennent plus résilients aux circonstances imprévues ou aux entrées non valides.
3.  **Séparation des préoccupations :** La logique de gestion des erreurs peut être séparée de la logique métier principale, ce qui rend le code plus propre et plus facile à lire.
4.  **Expérience utilisateur :** Fournit des retours significatifs aux utilisateurs lorsque les choses tournent mal, plutôt que des messages d'erreur système cryptiques.
5.  **Débogage :** Les exceptions fournissent des informations précieuses (comme une trace de pile) qui aident les développeurs à localiser où et pourquoi une erreur s'est produite.

**Le Mécanisme `try-except-finally` :**
* `try` : Le bloc de code qui pourrait potentiellement lever une exception. Le programme tente d'exécuter ce code normalement.
* `except` : Si une exception se produit dans le bloc `try`, le flux d'exécution normal est interrompu et le programme passe au bloc `except` approprié. Vous pouvez définir plusieurs blocs `except` pour gérer spécifiquement différents types d'exceptions. Le bloc `except` prend souvent un argument (l'objet exception lui-même) qui contient des détails sur l'erreur.
* `else` (avec `try-except`) : Un bloc facultatif qui s'exécute *uniquement si aucune exception* n'a été levée dans le bloc `try`.
* `finally` : Un bloc facultatif mais très utile. Le code à l'intérieur du bloc `finally` s'exécutera **toujours**, qu'une exception se soit produite ou non, qu'elle ait été gérée ou non. Il est idéal pour les opérations de nettoyage (comme la fermeture de fichiers ou la libération de ressources).

**Types d'Exceptions :**
Python a une hiérarchie de types d'exceptions intégrés pour les erreurs courantes :
* `SyntaxError` : Erreurs de grammaire du langage (détectées avant l'exécution).
* **Erreurs d'exécution (Exceptions) :** Erreurs qui se produisent pendant l'exécution du programme.
    * `ZeroDivisionError` : Tentative de division par zéro.
    * `IndexError` : Accès à un élément hors limites d'une liste ou d'un tableau.
    * `KeyError` : Accès à une clé inexistante dans un dictionnaire.
    * `TypeError` : Opération sur un type inapproprié (ex: additionner un nombre et une chaîne).
    * `ValueError` : Valeur correcte mais inappropriée (ex: `int("abc")`).
    * `FileNotFoundError` : Fichier introuvable.
    * `PermissionError` : Problèmes de droits d'accès.

**Lever des Exceptions (`raise`) :**
Vous pouvez aussi **lever** vos propres exceptions en utilisant le mot-clé `raise`. C'est utile lorsque vous détectez une condition d'erreur dans votre propre code qui doit être signalée à la partie appelante du programme.
""",
            code_example="""# Python Code Exemple: Exceptions

# 1. Gestion de ZeroDivisionError
print("--- Exemple de Division ---")
try:
    numerateur = 10
    denominateur = 0
    resultat = numerateur / denominateur
    print(f"Résultat: {resultat}")
except ZeroDivisionError:
    print("Erreur: Impossible de diviser par zéro !")
print("Tentative de division terminée.")

# 2. Gestion de ValueError (ex: conversion de chaîne invalide en entier)
print("\\n--- Exemple de Conversion d'Entrée ---")
entree_utilisateur = "abc"
try:
    nombre = int(entree_utilisateur)
    print(f"Nombre converti: {nombre}")
except ValueError:
    print(f"Erreur: '{entree_utilisateur}' n'est pas un nombre valide.")
print("Input conversion attempt complete.") # Correction de faute de frappe, doit être en français
print("Tentative de conversion d'entrée terminée.")


# 3. Gestion de plusieurs exceptions spécifiques et une exception générale
print("\\n--- Exemple d'Opérations de Fichier (simulé) ---")
# Simule une fonction qui pourrait échouer
def lire_fichier_securise(nom_fichier):
    try:
        if nom_fichier == "fichier_inexistant.txt":
            raise FileNotFoundError(f"Fichier '{nom_fichier}' introuvable.")
        elif nom_fichier == "acces_refuse.txt":
            raise PermissionError(f"Permission refusée pour accéder à '{nom_fichier}'.")
        else:
            print(f"Lecture réussie de '{nom_fichier}'. (Simulé)")
            return "Contenu du Fichier"
    except FileNotFoundError as e:
        print(f"Erreur Spécifique: {e}. Veuillez vérifier le chemin du fichier.")
    except PermissionError as e:
        print(f"Erreur Spécifique: {e}. Vérifiez les permissions du fichier.")
    except Exception as e: # Capture toute autre exception inattendue
        print(f"Une erreur inattendue s'est produite: {e}")
    finally:
        print(f"Nettoyage pour '{nom_fichier}' effectué. (Simulé)") # S'exécute toujours

lire_fichier_securise("fichier_inexistant.txt")
lire_fichier_securise("acces_refuse.txt")
lire_fichier_securise("mon_document.txt")

# 4. Utilisation de `else` avec try-except
print("\\n--- Exemple Try-Except-Else ---")
def diviser_securise(a, b):
    try:
        resultat = a / b
    except ZeroDivisionError:
        print("Impossible de diviser par zéro.")
    else: # S'exécute uniquement si aucune exception dans le bloc try
        print(f"Division réussie: {resultat}")
    finally:
        print("Tentative de division conclue.")

diviser_securise(10, 2)
diviser_securise(10, 0)

# 5. Lever une exception personnalisée
print("\\n--- Exemple d'Exception Personnalisée ---")
class AgeInvalideErreur(Exception):
    \"\"\"Exception personnalisée pour les valeurs d'âge invalides.\"\"\"
    pass

def definir_age_utilisateur(age):
    if not isinstance(age, int):
        raise TypeError("L'âge doit être un entier.")
    if not (0 < age < 120): # Âge entre 1 et 119
        raise AgeInvalideErreur("L'âge doit être entre 1 et 119 ans.")
    print(f"Âge défini à: {age}")

try:
    definir_age_utilisateur(30)
    definir_age_utilisateur(-5) # Ceci lèvera AgeInvalideErreur
except AgeInvalideErreur as e:
    print(f"Erreur personnalisée interceptée: {e}")
except TypeError as e:
    print(f"Erreur de type interceptée: {e}")

try:
    definir_age_utilisateur("vingt") # Ceci lèvera TypeError
except AgeInvalideErreur as e:
    print(f"Erreur personnalisée interceptée: {e}")
except TypeError as e:
    print(f"Erreur de type interceptée: {e}")
"""
        )

        # --- Contenu pour l'onglet "Classes" ---
        self.create_concept_tab(
            tab_frame=self.tab_view.tab("Classes"),
            title="Classes : Les Modèles pour Objets (POO)",
            explanation="""Imaginez que vous êtes un architecte qui conçoit des maisons. Vous ne construisez pas chaque maison à partir de zéro sans plan. Au lieu de cela, vous créez un **plan détaillé** qui spécifie le nombre de pièces, l'aménagement, les matériaux et la structure générale. Une fois que vous avez ce plan, vous pouvez construire de nombreuses maisons basées sur celui-ci, chacune unique (couleur différente, jardin différent) mais adhérant au même concept fondamental.

En programmation, une **classe** est ce plan. C'est un modèle ou une définition pour créer des **objets**. Un **objet** est une instance d'une classe – une réalisation concrète de ce plan. Les classes vous permettent de modéliser des entités du monde réel ou des concepts abstraits dans votre code, en regroupant des données et les actions qui peuvent être effectuées sur ces données. Ce paradigme est connu sous le nom de **Programmation Orientée Objet (POO)**.

**Pourquoi sont-elles importantes ?**
Les classes et la POO sont des outils puissants pour le développement de logiciels, offrant des avantages significatifs :
1.  **Modularité :** Elles regroupent les données (attributs) et les comportements (méthodes) liés en une seule unité cohérente. Cela rend le code plus facile à comprendre, à gérer et à déboguer.
2.  **Réutilisabilité :** Une fois qu'une classe est définie, vous pouvez créer de nombreux objets à partir d'elle, chacun avec son propre état mais partageant le même comportement sous-jacent.
3.  **Encapsulation :** Les classes vous permettent de "regrouper" les données et les méthodes qui opèrent sur ces données, en cachant les détails d'implémentation interne au monde extérieur. Cela protège l'intégrité des données et simplifie l'interface pour d'autres parties du programme.
4.  **Abstraction :** Elles vous permettent de définir des systèmes complexes en termes de concepts plus simples et de plus haut niveau. Vous interagissez avec les objets via leur interface définie (méthodes) sans avoir besoin de connaître leurs complexités internes.
5.  **Héritage :** Les classes peuvent former des hiérarchies où une classe "enfant" (sous-classe) peut hériter des propriétés et des comportements d'une classe "parente" (super-classe). Cela favorise la réutilisation du code et modélise les relations "est-un" (ex: un `Chien` "est un" type d'`Animal`).
6.  **Polymorphisme :** Permet que des objets de classes différentes soient traités comme des objets d'un type commun. Cela signifie qu'un seul appel de méthode peut se comporter différemment selon le type réel de l'objet sur lequel il est invoqué.

**Anatomie d'une Classe :**
* **Mot-clé `class` :** Déclare une nouvelle classe, suivie de son nom (généralement en `CamelCase`).
* **Attributs :** Variables qui appartiennent à la classe.
    * **Attributs d'instance :** Spécifiques à chaque objet (ex: le `nom` d'un objet `Chien` donné).
    * **Attributs de classe :** Partagés par tous les objets de cette classe (ex: l'`espèce` pour tous les objets `Chien`).
* **`__init__` (Constructeur) :** Une méthode spéciale appelée automatiquement lors de la création d'un nouvel objet (instanciation de la classe). Son but est d'initialiser les attributs de l'objet avec des valeurs de départ.
* **`self` :** Une convention (premier paramètre dans les méthodes d'instance) qui fait référence à l'instance de l'objet lui-même, permettant aux méthodes d'accéder et de modifier les propres attributs de *cet* objet.
* **Méthodes :** Fonctions définies à l'intérieur d'une classe. Elles représentent les actions ou les comportements que les objets de cette classe peuvent effectuer. Les méthodes prennent toujours `self` comme premier paramètre.
""",
            code_example="""# Python Code Exemple: Classes

# 1. Définition de Classe de Base
class Chien:
    # Attribut de classe (partagé par toutes les instances)
    espece = "Canis familiaris"

    # Méthode constructeur: appelée lors de la création d'un nouvel objet Chien
    def __init__(self, nom, race, age):
        # Attributs d'instance (uniques à chaque objet Chien)
        self.nom = nom
        self.race = race
        self.age = age
        self.a_faim = True # État par défaut

    # Méthode d'instance: opère sur les données de l'objet
    def aboyer(self):
        return f"{self.nom} dit Ouaf !"

    def manger(self):
        if self.a_faim:
            self.a_faim = False
            return f"{self.nom} n'a plus faim !"
        else:
            return f"{self.nom} n'a pas faim."

    def obtenir_infos(self):
        return f"{self.nom} est un(e) {self.age}-year-old {self.race} ({Chien.espece})." # Correction: age en français

# 2. Création d'Objets (Instances) de la classe Chien
my_dog = Chien("Buddy", "Golden Retriever", 5)
your_dog = Chien("Lucy", "Beagle", 2)

# 3. Accès aux Attributs et Appel des Méthodes
print(my_dog.obtenir_infos())
print(my_dog.aboyer())
print(my_dog.manger())
print(my_dog.manger()) # Essai de manger à nouveau quand pas faim

print("\\n" + your_dog.obtenir_infos())
print(your_dog.aboyer())

# 4. Accès à l'attribut de classe
print(f"Tous les chiens sont de l'espèce: {Chien.espece}")

# 5. Exemple d'Héritage
class Chiot(Chien): # Chiot hérite de Chien
    def __init__(self, nom, race, age, jouet_special):
        # Appelle le constructeur de la classe parente (Chien)
        super().__init__(nom, race, age)
        self.jouet_special = jouet_special

    def jouer(self):
        return f"{self.nom} adore jouer avec son {self.jouet_special}!"

    # Surcharge de méthode: Puppy a son propre son d'aboiement
    def aboyer(self):
        return f"{self.nom} dit Ouaf ouaf!"

petit_chiot = Chiot("Max", "Teckel", 0.5, "balle couinante")
print("\\n" + petit_chiot.obtenir_infos())
print(petit_chiot.aboyer()) # Uses Puppy's bark
print(petit_chiot.jouer())
print(petit_chiot.manger())
"""
        )

        # --- Contenu pour l'onglet "Combinaison & Astuces" ---
        self.create_combination_tab(
            tab_frame=self.tab_view.tab("Combinaison & Astuces")
        )

    def create_concept_tab(self, tab_frame, title, explanation, code_example):
        """
        Crée et peuple un onglet pour un concept donné avec explication, code et sortie.
        """
        # --- Section Explication ---
        explanation_frame = ctk.CTkFrame(tab_frame)
        explanation_frame.pack(side="top", fill="x", padx=10, pady=5)

        title_label = ctk.CTkLabel(explanation_frame, text=title, font=ctk.CTkFont(size=22, weight="bold"))
        title_label.pack(pady=(5, 5), padx=10, anchor="w")

        explanation_textbox = ctk.CTkTextbox(explanation_frame, wrap="word", height=250, font=("TkDefaultFont", 13))
        explanation_textbox.insert("0.0", explanation)
        explanation_textbox.configure(state="disabled") # Rendre le texte non modifiable
        explanation_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # --- Section Code Exemple ---
        code_frame = ctk.CTkFrame(tab_frame)
        code_frame.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        code_label = ctk.CTkLabel(code_frame, text="Exemple de Code Python :", font=ctk.CTkFont(size=16, weight="bold"), anchor="w")
        code_label.pack(pady=(5, 0), padx=10, anchor="w")

        code_textbox = ctk.CTkTextbox(code_frame, wrap="none", height=200, font=("Consolas", 12))
        code_textbox.insert("0.0", code_example)
        code_textbox.configure(state="disabled")
        code_textbox.pack(fill="x", padx=10, pady=(5, 5))

        # --- Bouton Exécuter ---
        execute_button = ctk.CTkButton(code_frame, text="Exécuter l'Exemple", command=lambda: self.run_code_example(code_example, tab_frame))
        execute_button.pack(pady=(5, 10), padx=10, anchor="e")

        # --- Section Résultat de l'Exécution ---
        output_frame = ctk.CTkFrame(tab_frame)
        output_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=5)

        output_label = ctk.CTkLabel(output_frame, text="Résultat de l'Exécution :", font=ctk.CTkFont(size=16, weight="bold"), anchor="w")
        output_label.pack(pady=(5, 0), padx=10, anchor="w")

        output_textbox = ctk.CTkTextbox(output_frame, wrap="word", height=150, font=("Consolas", 12))
        output_textbox.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        self.output_textboxes[tab_frame] = output_textbox # Stocker pour mise à jour

    def create_combination_tab(self, tab_frame):
        """
        Crée et peuple l'onglet "Combinaison & Astuces".
        """
        title_label = ctk.CTkLabel(tab_frame, text="Combinaison des Concepts : L'Art de la Programmation Python", font=ctk.CTkFont(size=22, weight="bold"))
        title_label.pack(pady=(10, 5), padx=10, anchor="w")

        # Section Explication Générale
        explanation_general_frame = ctk.CTkFrame(tab_frame)
        explanation_general_frame.pack(fill="x", padx=10, pady=5)
        explanation_general_textbox = ctk.CTkTextbox(explanation_general_frame, wrap="word", height=150, font=("TkDefaultFont", 13))
        explanation_general_textbox.insert("0.0", """Comprendre les concepts de programmation individuels (variables, fonctions, conditions, boucles, exceptions, classes) est essentiel, mais le véritable pouvoir de la programmation émerge lorsque vous apprenez à **combiner et entrelacer ces concepts** pour créer des applications sophistiquées, robustes et efficaces. C'est là que la programmation passe de la simple connaissance de la syntaxe à la véritable conception de solutions.

Pensez-y comme à la construction avec des LEGO. Chaque type de brique (variables, fonctions, etc.) a son propre but, mais les structures les plus impressionnantes proviennent de la connexion réfléchie de différents types de briques de manière logique.

Voici quelques stratégies et exemples concrets.""")
        explanation_general_textbox.configure(state="disabled")
        explanation_general_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # --- Exemple 1 : Système de Gestion des Utilisateurs ---
        self.add_combination_example(
            tab_frame,
            "Exemple 1: Système de Gestion des Utilisateurs (Classes, Fonctions, Conditions, Boucles)",
            """Ce système simple gère les utilisateurs via une classe `UserManager`. Il utilise une **liste (variable)** pour stocker les objets `User`. Des **méthodes (fonctions)** sont employées pour ajouter, supprimer et afficher les utilisateurs. À l'intérieur de ces méthodes, des **boucles** itèrent sur la liste des utilisateurs et des **conditions** sont utilisées pour la logique (par exemple, vérifier si un utilisateur existe déjà).""",
            """# Python Code Exemple: Système de Gestion des Utilisateurs (Combiné)

class Utilisateur:
    def __init__(self, nom_utilisateur, email):
        self.nom_utilisateur = nom_utilisateur
        self.email = email

    def __str__(self): # Représentation textuelle de l'objet
        return f"Utilisateur(Nom: {self.nom_utilisateur}, Email: {self.email})"

class GestionnaireUtilisateurs:
    def __init__(self):
        self.utilisateurs = [] # Variable de liste pour stocker les objets Utilisateur

    def ajouter_utilisateur(self, nom_utilisateur, email):
        # Condition: Vérifier si l'utilisateur existe déjà (en utilisant une boucle)
        for utilisateur in self.utilisateurs:
            if utilisateur.nom_utilisateur == nom_utilisateur:
                print(f"Erreur: L'utilisateur '{nom_utilisateur}' existe déjà.")
                return False
        nouvel_utilisateur = Utilisateur(nom_utilisateur, email)
        self.utilisateurs.append(nouvel_utilisateur)
        print(f"Utilisateur '{nom_utilisateur}' ajouté avec succès.")
        return True

    def supprimer_utilisateur(self, nom_utilisateur):
        utilisateur_trouve = False
        # Boucle: Itérer et supprimer l'utilisateur si trouvé
        for utilisateur in self.utilisateurs:
            if utilisateur.nom_utilisateur == nom_utilisateur:
                self.utilisateurs.remove(utilisateur)
                utilisateur_trouve = True
                print(f"Utilisateur '{nom_utilisateur}' supprimé.")
                break # Sortir de la boucle une fois trouvé
        if not utilisateur_trouve: # Condition: Si non trouvé après la boucle
            print(f"Erreur: L'utilisateur '{nom_utilisateur}' n'a pas été trouvé.")
        return utilisateur_trouve

    def afficher_utilisateurs(self):
        print("\\n--- Utilisateurs Actuels ---")
        if not self.utilisateurs: # Condition: Vérifier si la liste est vide
            print("Aucun utilisateur enregistré.")
            return

        # Boucle: Itérer et afficher chaque utilisateur
        for i, utilisateur in enumerate(self.utilisateurs):
            print(f"{i+1}. {utilisateur.nom_utilisateur} ({utilisateur.email})")
        print("----------------------------")

# --- Utilisation du GestionnaireUtilisateurs ---
manager = GestionnaireUtilisateurs()

manager.ajouter_utilisateur("alice", "alice@example.com")
manager.ajouter_utilisateur("bob", "bob@example.com")
manager.ajouter_utilisateur("alice", "alice_new@example.com") # Affichera une erreur (doublon)

manager.afficher_utilisateurs()

manager.supprimer_utilisateur("bob")
manager.supprimer_utilisateur("charlie") # Affichera une erreur (non trouvé)

manager.afficher_utilisateurs()

manager.ajouter_utilisateur("david", "david@example.com")
manager.afficher_utilisateurs()
"""
        )

        # --- Exemple 2 : Calculatrice Sécurisée avec Gestion d'Exceptions ---
        self.add_combination_example(
            tab_frame,
            "Exemple 2: Calculatrice Sécurisée (Classes, Fonctions, Exceptions, Conditions)",
            """Cet exemple présente une classe `Calculatrice` avec des méthodes qui effectuent des opérations. Elle utilise abondamment la **gestion d'exceptions** (`try-except`) pour gérer gracieusement les entrées ou opérations invalides (comme la division par zéro). Les **fonctions/méthodes** prennent des entrées (**variables**) et retournent des résultats. Des **conditions** valident les entrées avant les opérations.
""",
            """# Python Code Exemple: Calculatrice Sécurisée (Combiné)

class Calculatrice:
    def additionner(self, a, b):
        return a + b

    def soustraire(self, a, b):
        return a - b

    def multiplier(self, a, b):
        return a * b

    def diviser(self, a, b):
        # Condition & Gestion d'Exception pour la division par zéro
        if b == 0:
            raise ValueError("Impossible de diviser par zéro !")
        return a / b

    def obtenir_entree_numerique(self, invite):
        # Boucle pour une entrée valide, Gestion d'Exception pour la conversion
        while True:
            entree_str = input(invite)
            try:
                # Essayer de convertir en flottant (flexible pour les entiers aussi)
                nombre = float(entree_str)
                return nombre
            except ValueError:
                print("Entrée invalide. Veuillez saisir un nombre valide.")

# --- Utilisation de la Calculatrice Sécurisée ---
calc = Calculatrice()

print("\\n--- Opérations de la Calculatrice ---")

# Addition valide
num1 = calc.obtenir_entree_numerique("Saisissez le premier nombre pour l'addition: ") # Ex: 10
num2 = calc.obtenir_entree_numerique("Saisissez le second nombre pour l'addition: ") # Ex: 5
print(f"Résultat de l'addition: {calc.additionner(num1, num2)}")

# Division avec erreur potentielle
div_num = calc.obtenir_entree_numerique("Saisissez le numérateur pour la division: ") # Ex: 20
div_den = calc.obtenir_entree_numerique("Saisissez le dénominateur pour la division (essayez 0 ou 'abc'): ") # Ex: 0 ou "abc"
try:
    div_resultat = calc.diviser(div_num, div_den)
    print(f"Résultat de la division: {div_resultat}")
except ValueError as e:
    print(f"Erreur pendant la division: {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite: {e}")

# Multiplication
mul_num1 = calc.obtenir_entree_numerique("Saisissez le premier nombre pour la multiplication: ") # Ex: 7
mul_num2 = calc.obtenir_entree_numerique("Saisissez le second nombre pour la multiplication: ") # Ex: 8
print(f"Résultat de la multiplication: {calc.multiplier(mul_num1, mul_num2)}")
"""
        )

        # --- Section Astuces ---
        tips_frame = ctk.CTkFrame(tab_frame)
        tips_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tips_label = ctk.CTkLabel(tips_frame, text="Astuces (Tips) pour une Utilisation Combinée Efficace :", font=ctk.CTkFont(size=18, weight="bold"), anchor="w")
        tips_label.pack(pady=(5, 0), padx=10, anchor="w")

        tips_text = """
1.  **Décomposition (Diviser les Problèmes) :**
    * Décomposez les problèmes complexes en sous-problèmes plus petits et gérables. Chaque sous-problème correspond souvent à une **fonction** ou une **méthode** au sein d'une **classe**.
    * *Exemple :* Au lieu d'une fonction géante, créez `lire_donnees()`, `traiter_donnees()`, `enregistrer_resultats()`.

2.  **Encapsulation & Abstraction :**
    * Utilisez les **classes** pour regrouper les **attributs (variables)** et les **méthodes (fonctions)** qui opèrent sur ces attributs. Cachez la complexité interne.
    * *Exemple :* Une classe `Voiture` encapsule la `vitesse` (attribut) et `accelerer()` (méthode). Vous appelez simplement `voiture.accelerer()`, sans avoir à connaître les rouages internes du moteur.

3.  **Répétition et Prise de Décision Contrôlées :**
    * Utilisez des **boucles** pour itérer sur des collections (variables comme les listes/dictionnaires). À l'intérieur de la boucle, utilisez des **conditions** pour décider quelle action entreprendre pour chaque élément, en appelant potentiellement une **fonction** pour des actions spécifiques.
    * *Exemple :* `for article in panier_achat: if article.est_fragile: gerer_article_fragile(article)`.

4.  **Robustesse par la Gestion des Exceptions :**
    * Enveloppez les sections de code qui pourraient échouer (ex: entrée utilisateur, I/O de fichiers, requêtes réseau) dans des blocs `try-except`.
    * *Exemple :* `try: age_utilisateur = int(input()); except ValueError: print("Numéro invalide!")`.
    * **Astuce :** N'utilisez pas les exceptions pour le flux de contrôle normal. Elles sont réservées aux événements *exceptionnels*. Pour les variations attendues, utilisez `if-else`.

5.  **Gestion de l'État :**
    * Les **variables** stockent l'état du programme. Lorsqu'elles sont encapsulées dans des **classes**, elles deviennent des **attributs** d'objets, permettant à chaque objet de maintenir son propre état unique.
    * Les **fonctions/méthodes** sont les moyens sûrs de modifier ou d'accéder à cet état, souvent avec des **conditions** pour la validation.
    * **Astuce :** Minimisez les variables globales. Préférez passer les données comme paramètres de fonction ou les stocker comme attributs d'objet.

6.  **Lisibilité et Maintenabilité du Code :**
    * Utilisez des **noms significatifs** pour les variables, fonctions et classes.
    * Ajoutez des **commentaires** et des **docstrings** pour expliquer la logique complexe ou les choix de conception.
    * Maintenez une **indentation cohérente**.
    * **Astuce :** Si une fonction ou une méthode devient trop longue ou fait trop de choses, envisagez de la refactoriser en unités plus petites et plus ciblées.

En appliquant ces stratégies, vous écrirez des programmes Python plus organisés, flexibles et puissants !"""
        tips_textbox = ctk.CTkTextbox(tips_frame, wrap="word", height=400, font=("TkDefaultFont", 13))
        tips_textbox.insert("0.0", tips_text)
        tips_textbox.configure(state="disabled")
        tips_textbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))


    def add_combination_example(self, parent_frame, title, explanation, code_example):
        """
        Ajoute un bloc d'exemple de combinaison à l'onglet "Combinaison & Astuces".
        """
        example_frame = ctk.CTkFrame(parent_frame)
        example_frame.pack(fill="x", padx=10, pady=5)

        example_title_label = ctk.CTkLabel(example_frame, text=title, font=ctk.CTkFont(size=18, weight="bold"))
        example_title_label.pack(pady=(5, 5), padx=10, anchor="w")

        explanation_textbox = ctk.CTkTextbox(example_frame, wrap="word", height=80, font=("TkDefaultFont", 13))
        explanation_textbox.insert("0.0", explanation)
        explanation_textbox.configure(state="disabled")
        explanation_textbox.pack(fill="x", padx=10, pady=(0, 5))

        code_label = ctk.CTkLabel(example_frame, text="Exemple de Code :", font=ctk.CTkFont(size=14, weight="bold"), anchor="w")
        code_label.pack(pady=(5, 0), padx=10, anchor="w")

        code_textbox = ctk.CTkTextbox(example_frame, wrap="none", height=150, font=("Consolas", 11))
        code_textbox.insert("0.0", code_example)
        code_textbox.configure(state="disabled")
        code_textbox.pack(fill="x", padx=10, pady=(5, 5))

        execute_button = ctk.CTkButton(example_frame, text="Exécuter l'Exemple", command=lambda: self.run_code_example(code_example, example_frame))
        execute_button.pack(pady=(5, 10), padx=10, anchor="e")

        output_label = ctk.CTkLabel(example_frame, text="Résultat de l'Exécution :", font=ctk.CTkFont(size=14, weight="bold"), anchor="w")
        output_label.pack(pady=(5, 0), padx=10, anchor="w")

        output_textbox = ctk.CTkTextbox(example_frame, wrap="word", height=100, font=("Consolas", 11))
        output_textbox.pack(fill="both", expand=True, padx=10, pady=(5, 10))
        self.output_textboxes[example_frame] = output_textbox


    def run_code_example(self, code_str, parent_frame):
        """Exécute la chaîne de code Python et affiche la sortie dans le textbox approprié."""
        output_textbox = self.output_textboxes.get(parent_frame)
        if not output_textbox:
            print("Erreur: Le champ de sortie n'a pas été trouvé pour ce cadre.")
            return

        # Rediriger stdout pour capturer la sortie print()
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output

        output_textbox.configure(state="normal")
        output_textbox.delete("0.0", "end") # Effacer le contenu précédent

        try:
            # Pour simuler input() dans les exemples, on peut le remplacer
            # ou noter que les exemples qui attendent input() ne fonctionneront
            # pas de manière interactive ici. Les exemples fournis sont conçus
            # pour être principalement des prints ou des opérations internes.
            # Pour la calculatrice, on donne des inputs simulés.
            if "calc.obtenir_entree_numerique" in code_str: # Vérifier si c'est l'exemple de la calculatrice
                # Simuler les entrées pour la démo de la calculatrice
                simulated_inputs = iter([
                    "10", "5",  # Addition
                    "20", "0",  # Division par zéro
                    "7", "8"   # Multiplication
                ])
                def mock_input(prompt):
                    val = next(simulated_inputs)
                    sys.stdout.write(f"{prompt}{val}\\n") # Afficher la "saisie" simulée
                    return val
                original_input = __builtins__.input
                __builtins__.input = mock_input
                exec(code_str, globals(), locals())
                __builtins__.input = original_input # Restaurer input()
            else:
                exec(code_str, globals(), locals())
        except Exception as e:
            output_textbox.insert("end", f"Une erreur s'est produite lors de l'exécution:\n{e}\n")
        finally:
            sys.stdout = old_stdout # Restaurer stdout
            captured_output = redirected_output.getvalue()
            output_textbox.insert("end", captured_output)
            output_textbox.configure(state="disabled")

# --- Lancement de l'application ---
if __name__ == "__main__":
    app = PythonConceptExplorer()
    app.mainloop()