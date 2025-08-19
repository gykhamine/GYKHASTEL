import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class CSSSyntaxExplainer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Explorateur Ultra-Détaillé de la Syntaxe CSS")
        self.geometry("1400x900") # Encore plus grand pour le contenu riche
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Contenu détaillé de l'explication de la syntaxe CSS
        self.css_sections = {
            "Introduction": {
                "title": "Introduction Approfondie à la Syntaxe CSS : L'Art de Styliser le Web",
                "text": """
                Le **CSS** (Cascading Style Sheets, ou **Feuilles de Style en Cascade**) est bien plus qu'un simple langage de "décoration". C'est le langage fondamental qui nous permet de **séparer la structure du contenu (HTML) de sa présentation visuelle**. Cette séparation est une pierre angulaire du développement web moderne, offrant une flexibilité, une maintenabilité et une performance accrues.

                Imaginez le HTML comme le squelette d'un bâtiment (les murs, les poutres), et le CSS comme l'architecte d'intérieur qui décide des couleurs des murs, du type de mobilier, de l'éclairage, et de la disposition générale. Sans CSS, les sites web seraient des documents bruts, peu engageants et uniformes.

                **Pourquoi le CSS est-il si important ?**
                * **Contrôle Total de l'Apparence :** Du plus petit détail (taille de police d'un caractère) à la mise en page complexe (grilles responsives), le CSS offre un contrôle précis sur chaque aspect visuel.
                * **Cohérence Visuelle :** En définissant des styles dans une feuille de style centrale, vous assurez une apparence uniforme sur l'ensemble de votre site web, renforçant la marque et l'expérience utilisateur.
                * **Maintenabilité et Évolutivité :** Modifier l'apparence d'un élément sur des centaines de pages ? Une seule ligne de CSS suffit ! Cela simplifie les mises à jour et permet des refontes rapides.
                * **Performance :** En réutilisant les styles et en mettant en cache les fichiers CSS externes, le temps de chargement des pages est réduit.
                * **Accessibilité :** Le CSS permet d'adapter l'affichage pour différents appareils (smartphones, tablettes, ordinateurs) et pour les utilisateurs ayant des besoins spécifiques (ex: fort contraste, taille de texte agrandie). C'est la base du **Responsive Design**.
                * **Expérience Utilisateur (UX) :** Un design bien pensé et stylisé améliore l'engagement, la lisibilité et la navigation, rendant le site plus agréable à utiliser.

                Ce guide interactif vous emmènera à travers les méandres de la syntaxe CSS, de sa structure élémentaire à ses concepts les plus puissants comme la cascade et la spécificité, en passant par les techniques d'intégration et les bonnes pratiques qui feront de vous un styliste web accompli.
                """
            },
            "La Règle de Style": {
                "title": "La Règle de Style CSS : L'Unité Fondamentale de Stylisation",
                "text": """
                Au cœur de chaque feuille de style CSS se trouve la **règle de style** (parfois appelée "règle CSS" ou simplement "règle"). C'est l'instruction de base qui dit au navigateur *quels éléments styliser* et *comment les styliser*.

                Une règle de style est systématiquement composée de deux parties principales :

                1.  **Le Sélecteur** : La partie qui précède les accolades `{}`. Son rôle est de **cibler un ou plusieurs éléments HTML** spécifiques auxquels les styles devront être appliqués. Le sélecteur peut être très simple (ex: `p` pour tous les paragraphes) ou très complexe (ex: `div.card > h2 + p:hover::first-line`).
                2.  **Le Bloc de Déclaration** : Tout ce qui est contenu **entre les accolades `{}`**. Ce bloc renferme une ou plusieurs **déclarations de style**, chacune étant une instruction spécifique sur une propriété de l'élément ciblé.

                Voici la syntaxe générique d'une règle de style :

                ```css
                sélecteur {
                  propriété: valeur;  /* Première déclaration */
                  propriété-2: valeur-2; /* Deuxième déclaration */
                  /* ... d'autres déclarations ... */
                }
                ```

                **Zoom sur les Déclarations :**
                Chaque déclaration est une paire **`propriété: valeur;`** :
                * **`propriété`** : C'est l'aspect spécifique de l'élément que vous souhaitez modifier. Par exemple, `color` pour la couleur du texte, `font-size` pour la taille de la police, `margin` pour les marges. Le CSS propose des centaines de propriétés pour contrôler absolument tout l'aspect visuel et la disposition.
                * **`:` (Deux-points)** : Sépare la propriété de sa valeur. C'est un délimiteur obligatoire.
                * **`;` (Point-virgule)** : Termine chaque déclaration. Il est crucial d'utiliser le point-virgule pour séparer les déclarations. Bien qu'il soit techniquement facultatif pour la *dernière* déclaration d'un bloc, il est fortement recommandé de toujours l'inclure. Cela évite les erreurs si vous ajoutez de nouvelles déclarations ultérieurement et améliore la lisibilité.

                **Exemple Concret :**

                Considérons ce fragment HTML :
                ```html
                <p class="introduction">Bienvenue sur notre site.</p>
                ```

                Et la règle CSS suivante :
                ```css
                .introduction { /* Sélecteur: cible les éléments avec la classe "introduction" */
                  color: #333333; /* Déclaration 1: propriété 'color' avec la valeur '#333333' (gris foncé) */
                  font-size: 1.1em; /* Déclaration 2: propriété 'font-size' avec la valeur '1.1em' (1.1 fois la taille de police du parent) */
                  margin-bottom: 15px; /* Déclaration 3: propriété 'margin-bottom' avec la valeur '15px' */
                }
                ```
                Dans cet exemple, le texte du paragraphe `p` avec la classe `introduction` sera stylisé en gris foncé, avec une taille de police légèrement plus grande que la normale et aura une marge de 15 pixels en dessous.

                La clarté et la simplicité de cette structure (`sélecteur { propriété: valeur; }`) sont ce qui rend le CSS si puissant et relativement facile à apprendre, malgré la multitude de propriétés et de sélecteurs disponibles.
                """
            },
            "Les Sélecteurs CSS Avancés": {
                "title": "Les Sélecteurs CSS Avancés : Maîtriser le Ciblage des Éléments",
                "text": """
                Le choix du bon sélecteur est essentiel pour appliquer vos styles avec précision sans affecter des éléments non désirés. Les sélecteurs peuvent être combinés et utilisés de manière très sophistiquée.

                **1. Sélecteurs Simples :**
                * **Sélecteur de type (ou d'élément)** : `p`, `h1`, `div`, `a`. Cible toutes les instances de cette balise.
                    ```css
                    a {
                      text-decoration: none; /* Supprime le soulignement des liens par défaut */
                    }
                    ```
                * **Sélecteur de classe** : `.nom-de-classe`. Cible tous les éléments ayant cette classe. Très flexible et réutilisable. Un élément peut avoir plusieurs classes (ex: `<div class="card active large">`).
                    ```css
                    .btn-primary {
                      background-color: blue;
                      color: white;
                      padding: 10px 15px;
                    }
                    .active {
                      border: 2px solid green;
                    }
                    ```
                * **Sélecteur d'ID** : `#id-unique`. Cible l'**unique** élément ayant cet ID. À utiliser avec parcimonie pour des éléments véritablement uniques, car sa spécificité est très élevée et il est moins réutilisable que les classes.
                    ```css
                    #header-logo {
                      width: 150px;
                      height: auto;
                    }
                    ```
                * **Sélecteur universel** : `*`. Cible **tous** les éléments. Souvent utilisé pour des réinitialisations de styles de base.
                    ```css
                    * {
                      box-sizing: border-box; /* Fait en sorte que padding et border soient inclus dans la largeur/hauteur */
                    }
                    ```

                **2. Sélecteurs d'Attributs :**
                Ciblent les éléments en fonction de leurs attributs HTML.
                * `[attribut]` : Élément avec l'attribut spécifié (peu importe sa valeur).
                    ```css
                    [title] { /* Cible tous les éléments ayant un attribut 'title' */
                      border-bottom: 1px dotted gray;
                    }
                    ```
                * `[attribut="valeur"]` : Élément avec l'attribut ayant une valeur exacte.
                    ```css
                    input[type="submit"] { /* Cible les boutons de soumission */
                      background-color: green;
                    }
                    ```
                * `[attribut~="valeur"]` : L'attribut contient une liste de mots séparés par des espaces, et l'un de ces mots est la `valeur`. Utile pour les classes multiples.
                    ```css
                    a[class~="external"] { /* Cible les liens avec une classe 'external' parmi d'autres */
                      color: orange;
                    }
                    ```
                * `[attribut^="valeur"]` : L'attribut commence par la `valeur`.
                    ```css
                    a[href^="https://"] { /* Cible les liens sécurisés HTTPS */
                      font-weight: bold;
                    }
                    ```
                * `[attribut$="valeur"]` : L'attribut se termine par la `valeur`.
                    ```css
                    img[src$=".png"] { /* Cible les images PNG */
                      border: 1px dashed blue;
                    }
                    ```
                * `[attribut*="valeur"]` : L'attribut contient la `valeur` n'importe où.
                    ```css
                    [data-info*="user"] { /* Cible les éléments avec l'attribut 'data-info' contenant 'user' */
                      background-color: #e0e0ff;
                    }
                    ```

                **3. Sélecteurs de Combinateurs :**
                Ciblent les éléments en fonction de leur relation hiérarchique ou de voisinage.
                * **Sélecteur descendant (` ` - espace)** : `parent descendant`. Cible un élément qui est un descendant (enfant, petit-enfant, etc.) d'un autre. C'est le plus couramment utilisé.
                    ```css
                    nav a { /* Cible tous les liens <a> à l'intérieur d'une balise <nav> */
                      padding: 5px 10px;
                    }
                    ```
                * **Sélecteur d'enfant direct (`>`)** : `parent > enfant`. Cible un élément qui est un enfant **direct** d'un autre.
                    ```css
                    ul > li { /* Cible uniquement les <li> qui sont des enfants directs d'un <ul>, pas les <li> dans un <ul> imbriqué */
                      list-style-type: disc;
                    }
                    ```
                * **Sélecteur de frère adjacent (`+`)** : `élément1 + élément2`. Cible un `élément2` qui suit immédiatement un `élément1` et partage le même parent.
                    ```css
                    h2 + p { /* Cible le premier paragraphe qui suit immédiatement un titre <h2> */
                      margin-top: 0;
                      font-style: italic;
                    }
                    ```
                * **Sélecteur de frère général (`~`)** : `élément1 ~ élément2`. Cible tous les `élément2` qui suivent un `élément1` et partagent le même parent, sans être nécessairement adjacents.
                    ```css
                    h1 ~ p { /* Cible tous les paragraphes qui suivent un <h1>, même s'il y a d'autres éléments entre */
                      text-indent: 1.5em;
                    }
                    ```

                **4. Pseudo-classes :**
                Ciblent des éléments en fonction de leur **état actuel** ou de leur **position** dans la structure du document. Elles commencent par un seul deux-points (`:`).
                * **Pseudo-classes d'état utilisateur** :
                    * `:hover` : Quand la souris est sur l'élément.
                    * `:active` : Quand l'élément est cliqué/activé.
                    * `:focus` : Quand l'élément (input, lien) a le focus clavier.
                    * `:visited` : Pour les liens déjà visités (sécurité limite les propriétés modifiables).
                    * `:link` : Pour les liens non visités.
                    ```css
                    a:hover { color: orange; }
                    button:active { transform: translateY(1px); }
                    input:focus { border-color: blue; outline: none; }
                    ```
                * **Pseudo-classes structurelles (position dans l'arbre DOM)** :
                    * `:first-child`, `:last-child` : Le premier/dernier enfant de son parent.
                    * `:nth-child(n)`, `:nth-last-child(n)` : Le nième enfant (compte depuis le début/fin). `n` peut être un nombre, `even` (pair), `odd` (impair), ou une formule (`2n`, `3n+1`).
                    * `:only-child` : Si l'élément est le seul enfant de son parent.
                    * `:empty` : Si l'élément ne contient aucun enfant (texte ou balise).
                    * `:root` : L'élément racine du document (généralement `<html>`). Très utile pour définir des variables CSS globales.
                    ```css
                    li:first-child { font-weight: bold; }
                    tr:nth-child(odd) { background-color: #f2f2f2; } /* Lignes impaires d'un tableau */
                    p:empty { display: none; } /* Cache les paragraphes vides */
                    ```
                * **Pseudo-classes d'état des formulaires** :
                    * `:checked` : Pour les cases à cocher ou boutons radio sélectionnés.
                    * `:disabled`, `:enabled` : Pour les champs de formulaire désactivés/activés.
                    * `:required`, `:optional` : Pour les champs marqués comme requis/optionnels.
                    * `:valid`, `:invalid` : Pour les champs dont la valeur est/n'est pas valide selon leur type ou patterns.
                    ```css
                    input:checked + label { color: green; }
                    input:invalid { border-color: red; }
                    ```
                * **Pseudo-classes de négation** :
                    * `:not(sélecteur)` : Cible les éléments qui **ne correspondent pas** au sélecteur passé en argument.
                    ```css
                    button:not(.disabled) { cursor: pointer; } /* Boutons qui ne sont pas désactivés */
                    ```

                **5. Pseudo-éléments :**
                Permettent de styliser des parties spécifiques d'un élément qui ne sont pas représentées par des balises HTML réelles dans le DOM. Ils commencent par deux doubles points (`::`).
                * `::before` : Insère du contenu généré avant le contenu d'un élément.
                * `::after` : Insère du contenu généré après le contenu d'un élément.
                    Ces deux sont souvent utilisés avec la propriété `content` pour ajouter des icônes, des numérotations, ou des effets décoratifs.
                    ```css
                    a.external::after {
                      content: " ↗"; /* Ajoute une flèche après les liens externes */
                      font-size: 0.8em;
                    }
                    ```
                * `::first-line` : Cible la première ligne de texte d'un élément de bloc.
                * `::first-letter` : Cible la première lettre d'un élément de bloc.
                    ```css
                    p::first-letter {
                      font-size: 2em;
                      font-weight: bold;
                      float: left; /* Pour un effet de lettrine */
                      margin-right: 5px;
                    }
                    ```
                * `::selection` : Cible le texte que l'utilisateur a sélectionné avec la souris.
                    ```css
                    ::selection {
                      background-color: yellow;
                      color: black;
                    }
                    ```
                * `::placeholder` : Cible le texte d'espace réservé dans les champs de formulaire.
                    ```css
                    input::placeholder {
                      color: #aaa;
                      font-style: italic;
                    }
                    ```

                Maîtriser ces sélecteurs vous ouvre la porte à un ciblage extrêmement précis et efficace, réduisant la nécessité d'ajouter des classes ou des ID supplémentaires uniquement pour le style.
                """
            },
            "Propriétés et Valeurs Approfondies": {
                "title": "Propriétés et Valeurs CSS : Le Dictionnaire Visuel Complet",
                "text": """
                Chaque déclaration CSS est un duo `propriété: valeur;`. C'est là que réside la magie de la transformation visuelle. Explorons les types de propriétés et de valeurs plus en détail.

                **Catégories Majeures de Propriétés CSS :**

                1.  **Propriétés de Texte et Typographie :**
                    * `font-family` : Pile de polices (ex: `Arial, sans-serif`).
                    * `font-size` : Taille du texte (ex: `16px`, `1.2em`, `2rem`, `2vw`).
                    * `font-weight` : Graisse de la police (ex: `normal`, `bold`, `400`, `700`).
                    * `font-style` : Style de police (ex: `normal`, `italic`, `oblique`).
                    * `text-align` : Alignement horizontal (ex: `left`, `right`, `center`, `justify`).
                    * `color` : Couleur du texte.
                    * `text-decoration` : Ligne sous/sur/à travers le texte (ex: `none`, `underline`, `line-through`).
                    * `text-transform` : Casse du texte (ex: `uppercase`, `lowercase`, `capitalize`).
                    * `line-height` : Hauteur de ligne (espacement vertical entre les lignes de texte).
                    * `letter-spacing` : Espacement entre les caractères.
                    * `word-spacing` : Espacement entre les mots.
                    * `white-space` : Gestion des espaces blancs.

                2.  **Propriétés du Modèle de Boîte (Box Model) :**
                    Chaque élément HTML est traité comme une boîte rectangulaire, avec des couches de contenu, de rembourrage (padding), de bordure (border) et de marge (margin).
                    * `width`, `height` : Dimensions du contenu.
                    * `max-width`, `min-width`, `max-height`, `min-height` : Limites de dimension.
                    * `padding` : Espace entre le contenu et la bordure (interne). Peut être défini pour chaque côté (`padding-top`, `padding-right`, etc.) ou en raccourci (`padding: 10px 20px;`).
                    * `border` : Bordure de l'élément (`border: 1px solid black;`). Peut être défini pour chaque côté (`border-left`, etc.) et avec des propriétés séparées (`border-width`, `border-style`, `border-color`).
                    * `margin` : Espace entre la bordure et les éléments adjacents (externe). Peut être défini pour chaque côté (`margin-top`, etc.) ou en raccourci (`margin: 20px auto;` pour centrer horizontalement un bloc).
                    * `box-sizing` : Contrôle la façon dont `width` et `height` sont calculés (`content-box` par default, `border-box` recommandé pour un contrôle plus intuitif).

                3.  **Propriétés d'Arrière-plan (Background) :**
                    * `background-color` : Couleur de fond.
                    * `background-image` : Image de fond (ex: `url('image.png')`).
                    * `background-repeat` : Répétition de l'image (ex: `no-repeat`, `repeat-x`, `repeat-y`).
                    * `background-position` : Position de l'image de fond (ex: `center top`, `50% 50%`).
                    * `background-size` : Taille de l'image de fond (ex: `cover`, `contain`, `100% auto`).
                    * `background-attachment` : Comportement de l'image au défilement (ex: `scroll`, `fixed`, `local`).
                    * `background` (raccourci) : Permet de définir plusieurs propriétés de fond en une seule ligne.

                4.  **Propriétés de Disposition (Layout) :**
                    * `display` : Contrôle le type de boîte d'affichage d'un élément.
                        * `block` : Prend toute la largeur disponible, démarre sur une nouvelle ligne (ex: `div`, `p`, `h1`).
                        * `inline` : Prend seulement la largeur nécessaire, ne démarre pas sur une nouvelle ligne (ex: `span`, `a`, `strong`).
                        * `inline-block` : Combine les propriétés des deux (peut avoir largeur/hauteur, mais reste en ligne).
                        * `none` : L'élément est complètement retiré du flux du document (invisible et n'occupe pas d'espace).
                        * `flex` : Active Flexbox, un modèle de disposition unidimensionnel très puissant.
                        * `grid` : Active CSS Grid, un modèle de disposition bidimensionnel pour des mises en page complexes.
                    * `position` : Contrôle le positionnement d'un élément.
                        * `static` : Position par défaut (dans le flux normal du document).
                        * `relative` : Reste dans le flux normal, mais peut être décalé (`top`, `bottom`, `left`, `right`) par rapport à sa position normale.
                        * `absolute` : Sort l'élément du flux normal ; positionné par rapport à l'ancêtre positionné le plus proche.
                        * `fixed` : Sort l'élément du flux normal ; positionné par rapport à la fenêtre d'affichage (viewport), reste fixe au défilement.
                        * `sticky` : Se comporte comme `relative` jusqu'à un certain point de défilement, puis comme `fixed`.
                    * `top`, `bottom`, `left`, `right` : Utilisé avec `position` pour décaler un élément.
                    * `z-index` : Détermine l'ordre d'empilement des éléments positionnés.

                5.  **Propriétés de Flexbox (si `display: flex;`) :**
                    * `flex-direction` : Direction de l'axe principal (ex: `row`, `column`).
                    * `justify-content` : Alignement des éléments sur l'axe principal.
                    * `align-items` : Alignement des éléments sur l'axe secondaire.
                    * `flex-wrap` : Permet aux éléments de passer à la ligne.
                    * `gap` (ou `grid-gap`) : Espace entre les éléments flexibles/grille.

                6.  **Propriétés de CSS Grid (si `display: grid;`) :**
                    * `grid-template-columns`, `grid-template-rows` : Définit les colonnes/lignes de la grille.
                    * `grid-gap`, `row-gap`, `column-gap` : Espace entre les cellules de la grille.
                    * `grid-column`, `grid-row` : Positionne un élément dans la grille.

                7.  **Propriétés d'Effets Visuels :**
                    * `opacity` : Transparence de l'élément (de `0` à `1`).
                    * `box-shadow`, `text-shadow` : Ajoute des ombres.
                    * `border-radius` : Arrondit les coins des bordures.
                    * `transform` : Applique des transformations 2D/3D (ex: `scale()`, `rotate()`, `translate()`).
                    * `transition` : Anime les changements de propriétés CSS en douceur.
                    * `animation` : Anime des séquences d'états plus complexes via des `@keyframes`.

                **Types de Valeurs Détaillés :**

                * **Mots-clés** : `initial` (valeur par défaut de la propriété), `inherit` (hérite de la valeur du parent), `unset` (réinitialise à `inherit` si héritable, sinon à `initial`).
                * **Unités de Longueur** :
                    * **Absolues** : `px` (pixels), `pt` (points), `cm`, `mm`, `in` (pouces). Les pixels sont les plus courants sur le web.
                    * **Relatives** :
                        * `em` : Relatif à la taille de police de l'élément parent. (ex: `1.5em` signifie 1.5 fois la taille de police de l'élément parent).
                        * `rem` : Relatif à la taille de police de l'élément racine (`<html>`). Plus prévisible que `em`.
                        * `vw` (viewport width) : 1% de la largeur de la fenêtre d'affichage.
                        * `vh` (viewport height) : 1% de la hauteur de la fenêtre d'affichage.
                        * `vmin` / `vmax` : 1% de la dimension la plus petite/grande de la fenêtre.
                        * `%` : Pourcentages, souvent relatifs à la dimension de l'élément parent ou du conteneur.
                * **Unités d'Angle** : `deg` (degrés), `grad` (grades), `rad` (radians), `turn` (tours). Utilisées pour les rotations (ex: `transform: rotate(45deg);`).
                * **Unités de Temps** : `s` (secondes), `ms` (millisecondes). Utilisées pour les transitions et animations (ex: `transition-duration: 0.5s;`).
                * **Couleurs** :
                    * **Noms prédéfinis** : `red`, `blue`, `gold`, `aliceblue`, etc. (plus de 140 couleurs).
                    * **Hexadécimal** : `#RRGGBB` (ex: `#FF0000` pour rouge), `#RGB` (raccourci pour couleurs répétées, ex: `#F00` pour `#FF0000`).
                    * **RGB(A)** : `rgb(rouge, vert, bleu)` ou `rgba(rouge, vert, bleu, alpha)`. `alpha` est l'opacité de `0` (transparent) à `1` (opaque). Ex: `rgba(255, 0, 0, 0.5)`.
                    * **HSL(A)** : `hsl(teinte, saturation, luminosité)` ou `hsla(teinte, saturation, luminosité, alpha)`. Plus intuitif pour choisir des couleurs. Ex: `hsla(120, 100%, 50%, 0.7)` (vert vif semi-transparent).
                * **Fonctions** :
                    * `url()` : Pour les images (ex: `background-image: url('images/bg.jpg');`).
                    * `linear-gradient()`, `radial-gradient()` : Pour créer des dégradés de couleur.
                    * `calc()` : Pour effectuer des calculs mathématiques directement dans les valeurs CSS (ex: `width: calc(100% - 20px);`).
                    * `var()` : Pour utiliser des variables CSS (ex: `color: var(--primary-color);`).

                La connaissance de cette richesse de propriétés et de valeurs est essentielle pour créer des interfaces utilisateur riches et dynamiques.
                """
            },
            "La Cascade, Spécificité, Héritage et !important": {
                "title": "La Cascade, la Spécificité, l'Héritage et `!important` : Les Fondations du Rendu CSS",
                "text": """
                Ces quatre concepts sont au cœur de la façon dont le navigateur interprète et applique vos styles CSS. Les comprendre est crucial pour déboguer et maîtriser le comportement de vos feuilles de style.

                **1. La Cascade : L'Ordre d'Application des Styles**
                La cascade est le processus par lequel le navigateur combine les styles provenant de différentes sources et détermine quel style appliquer lorsqu'il y a des conflits. C'est un système de priorité basé sur l'origine et l'ordre des styles. Les sources de style sont traitées dans l'ordre suivant (du moins prioritaire au plus prioritaire, pour la même spécificité) :

                * **Feuilles de style du navigateur (User Agent Stylesheets) :** Les styles par défaut que chaque navigateur applique aux éléments HTML. Ex: les liens sont bleus et soulignés, les titres sont en gras et plus grands.
                * **Feuilles de style utilisateur (User Stylesheets) :** Styles définis par l'utilisateur final dans son navigateur. C'est rare, souvent pour des besoins d'accessibilité (ex: forcer une taille de police minimale).
                * **Feuilles de style de l'auteur (Author Stylesheets) :** **Ce sont vos styles CSS !** Ils peuvent être :
                    * **Définis en ligne (Inline Styles) :** Attribut `style=""` directement sur l'élément HTML. Ils ont une très haute priorité dans la cascade et la spécificité.
                    * **Embarqués (Embedded Styles) :** Définis dans une balise `<style>` dans la section `<head>` du document HTML.
                    * **Externes (External Styles) :** Liés via `<link rel="stylesheet" href="style.css">`. C'est la méthode recommandée.
                    * **Importés :** Via `@import` à l'intérieur d'une autre feuille de style (moins courant et déconseillé pour la performance).
                * **Importance de l'ordre :** Pour les règles de même spécificité et origine (par exemple, deux règles dans votre fichier `style.css` ciblant le même élément), la **dernière règle déclarée dans le code CSS** l'emporte.

                **2. La Spécificité : Le Poids des Sélecteurs**
                Lorsque plusieurs règles CSS ciblent le même élément et définissent la même propriété, la règle avec la **spécificité la plus élevée** l'emporte, quelle que soit sa position dans la feuille de style. La spécificité est un score calculé pour chaque sélecteur. Plus le score est élevé, plus le sélecteur est spécifique.

                Le score est calculé comme une combinaison de quatre valeurs (a, b, c, d) :
                * **`a`** : 1 si la déclaration est un **style en ligne**, 0 sinon.
                * **`b`** : Nombre d'**ID** (`#id`) dans le sélecteur.
                * **`c`** : Nombre de **classes** (`.class`), **attributs** (`[attr]`), et **pseudo-classes** (`:hover`) dans le sélecteur.
                * **`d`** : Nombre d'**éléments** (`p`), et **pseudo-éléments** (`::before`) dans le sélecteur.

                **Exemples de calcul de spécificité :**
                * `p`                           -> (0, 0, 0, 1) = 1
                * `.ma-classe`                  -> (0, 0, 1, 0) = 10
                * `#mon-id`                     -> (0, 1, 0, 0) = 100
                * `p.ma-classe`                 -> (0, 0, 1, 1) = 11
                * `div #mon-id`                 -> (0, 1, 0, 1) = 101
                * `input[type="text"]:focus`    -> (0, 0, 2, 1) = 21 (1 pour `[type="text"]`, 1 pour `:focus`, 1 pour `input`)
                * `<p style="color: blue;">`   -> (1, 0, 0, 0) = 1000

                **Règles de la spécificité :**
                * Plus le score est élevé, plus la règle est spécifique et l'emporte.
                * Si les scores sont égaux, la règle qui apparaît **en dernier** dans la feuille de style (selon l'ordre de la cascade) l'emporte.
                * Le sélecteur universel (`*`) a une spécificité de 0.
                * Les sélecteurs combinatoires (` `, `+`, `~`, `>`) n'ajoutent pas de spécificité propre, seule la spécificité des sélecteurs qu'ils combinent est comptée.

                **3. L'Héritage : La Transmission des Styles**
                Certaines propriétés CSS sont **héritables**, ce qui signifie que si vous les appliquez à un élément parent, leur valeur est automatiquement transmise (héritée) par ses éléments descendants, à moins que ces descendants ne définissent explicitement une autre valeur pour cette propriété.

                * **Propriétés couramment héritables (liées au texte et à la couleur) :** `color`, `font-family`, `font-size`, `font-weight`, `line-height`, `text-align`, `list-style`, `visibility`, `cursor`.
                * **Propriétés non héritables (liées au modèle de boîte, positionnement, etc.) :** `background-color`, `border`, `margin`, `padding`, `width`, `height`, `display`, `position`, `top`, `left`, `z-index`.

                **Exemple d'héritage :**
                ```html
                <div style="font-family: 'Open Sans', sans-serif; color: #555;">
                    <p>Ce paragraphe hérite de la police et de la couleur du div.</p>
                    <ul>
                        <li><a href="#">Ce lien hérite de la police et de la couleur.</a></li>
                    </ul>
                </div>
                ```
                Dans cet exemple, le paragraphe et le lien hériteront de la `font-family` et de la `color` du `div` parent.

                **4. Le Mot-clé `!important` : L'Exception à la Règle**
                Le mot-clé `!important` est un modificateur que vous pouvez ajouter à une déclaration CSS pour lui donner une priorité absolue. Une déclaration marquée `!important` l'emporte sur **toute autre déclaration**, quelle que soit sa spécificité ou sa position dans la cascade, sauf si une autre déclaration a également `!important` *et* provient d'une source plus prioritaire (ex: un style utilisateur `!important` l'emporte sur un style auteur `!important`).

                ```css
                .bouton-special {
                    background-color: red !important; /* Cette règle l'emportera toujours */
                    color: white;
                }
                #header .bouton-special { /* Même si ce sélecteur est plus spécifique */
                    background-color: blue; /* Cette règle sera ignorée pour background-color */
                }
                ```
                **Pourquoi `!important` est (presque) toujours une mauvaise idée :**
                * **Casse la Cascade et la Spécificité :** Il rend le code imprévisible et très difficile à déboguer, car il viole les règles normales du CSS.
                * **Maintenabilité Réduite :** Il devient extrêmement difficile de surcharger un style `!important` ultérieurement, ce qui peut vous forcer à ajouter d'autres `!important` et créer une "guerre de `!important`".
                * **Mauvaise Pratique :** Son utilisation est généralement un signe que votre architecture CSS n'est pas optimale. Il y a presque toujours une meilleure façon d'atteindre le même résultat en utilisant la spécificité et la structure du document.

                **Quand pourrait-il être utilisé (avec beaucoup de prudence) ?**
                * **Surcharger des styles de bibliothèques tierces :** Si une bibliothèque externe utilise des styles très spécifiques que vous ne pouvez pas modifier.
                * **Utilitaires de surcharge spécifiques :** Par exemple, une classe utilitaire `.`hidden { display: none !important; }` qui doit garantir de masquer un élément à tout prix.

                Comprendre ces concepts est la clé pour écrire du CSS prédictible, efficace et maintenable. N'hésitez jamais à utiliser les outils de développement de votre navigateur (inspecteur d'éléments) pour analyser la cascade et la spécificité d'un élément donné.
                """
            },
            "Les Unités CSS et Fonctions Avancées": {
                "title": "Les Unités CSS et Fonctions Avancées : Mesure, Calcul et Personnalisation",
                "text": """
                Le CSS ne se limite pas aux valeurs fixes. Il offre une multitude d'unités de mesure et de fonctions qui permettent des designs fluides, adaptatifs et dynamiques.

                **1. Unités de Mesure Approfondies :**

                * **Unités Absolues (Fixes et Immuables) :**
                    * `px` (pixels) : L'unité la plus courante. 1px = 1/96ème de pouce. La taille réelle du pixel varie en fonction de la densité de pixels de l'écran (DPI/PPI), mais en CSS, 1px est une référence abstraite. Bon pour un contrôle précis, mais moins flexible pour le responsive.
                    * `pt` (points) : 1pt = 1/72ème de pouce. Principalement pour l'impression.
                    * `cm`, `mm`, `in` (centimètres, millimètres, pouces) : Aussi pour l'impression, rarement utilisés sur le web.

                * **Unités Relatives (S'adaptent au Contexte) :**
                    Ces unités sont cruciales pour le **Responsive Design** et l'**Accessibilité**.
                    * **Relatives à la police :**
                        * `em` : **Relative à la taille de police de l'élément parent**. Si le parent a `font-size: 16px;`, alors `1em` dans l'enfant est `16px`. Si l'enfant a lui-même `font-size: 20px;`, alors `1em` dans ses propres descendants sera `20px`. Peut rendre les calculs complexes dans des hiérarchies profondes.
                            ```css
                            .parent { font-size: 16px; }
                            .enfant { font-size: 1.2em; /* 1.2 * 16px = 19.2px */ }
                            ```
                        * `rem` (root em) : **Relative à la taille de police de l'élément racine du document (`<html>`)**. C'est souvent l'unité préférée pour la taille de police pour une meilleure prévisibilité, car elle ne dépend que d'une seule valeur globale.
                            ```css
                            html { font-size: 16px; } /* Taille de base pour rem */
                            .titre { font-size: 2.5rem; /* 2.5 * 16px = 40px */ }
                            .paragraphe { font-size: 1rem; /* 1 * 16px = 16px */ }
                            ```
                    * **Relatives à la fenêtre d'affichage (Viewport) :**
                        * `vw` (viewport width) : 1% de la largeur de la fenêtre d'affichage. Ex: `width: 50vw;` = 50% de la largeur du navigateur.
                        * `vh` (viewport height) : 1% de la hauteur de la fenêtre d'affichage. Ex: `height: 100vh;` = la hauteur complète du navigateur.
                        * `vmin` : 1% de la dimension la plus petite de la fenêtre d'affichage (min(vw, vh)).
                        * `vmax` : 1% de la dimension la plus grande de la fenêtre d'affichage (max(vw, vh)).
                        Ces unités sont idéales pour des éléments qui doivent s'adapter proportionnellement à la taille de l'écran.
                    * **Pourcentages (`%`) :** Relative à la dimension de l'élément parent ou du contexte. Par exemple, `width: 50%;` signifie 50% de la largeur du parent. Le contexte exact dépend de la propriété.

                **2. Fonctions CSS Avancées :**

                * **`calc()` : Effectuer des Calculs Mathématiques**
                    Permet d'effectuer des opérations arithmétiques (`+`, `-`, `*`, `/`) pour calculer des valeurs de propriété. Très utile pour des mises en page complexes où vous avez besoin de combiner différentes unités.
                    ```css
                    .sidebar {
                        width: calc(30% - 20px); /* 30% de la largeur du parent moins 20 pixels */
                    }
                    .main-content {
                        width: calc(70% - 20px);
                        margin-left: calc(30% - 20px); /* Positionnement dynamique */
                    }
                    ```
                    Vous pouvez aussi l'utiliser pour définir des marges, des paddings, etc.

                * **`var()` : Utiliser les Variables CSS (Custom Properties)**
                    Les variables CSS (ou "propriétés personnalisées") vous permettent de définir des valeurs réutilisables dans toute votre feuille de style. Elles commencent par `--` et sont définies dans des sélecteurs (souvent `:root` pour des variables globales).
                    * **Déclaration :** `--nom-de-variable: valeur;`
                    * **Utilisation :** `var(--nom-de-variable, valeur-de-secours);`
                    ```css
                    :root { /* Déclare des variables globales sur l'élément racine */
                        --primary-color: #007bff;
                        --secondary-color: #6c757d;
                        --spacing-unit: 1rem;
                        --border-radius: 5px;
                    }

                    button {
                        background-color: var(--primary-color);
                        color: white;
                        padding: var(--spacing-unit) calc(var(--spacing-unit) * 1.5);
                        border-radius: var(--border-radius);
                    }

                    .text-muted {
                        color: var(--secondary-color, gray); /* 'gray' est une valeur de secours si --secondary-color n'est pas définie */
                    }
                    ```
                    **Avantages des variables CSS :**
                    * **Maintenabilité :** Changez une valeur à un seul endroit, et elle se met à jour partout où la variable est utilisée. Idéal pour les thèmes.
                    * **Cohérence :** Garantit que les mêmes valeurs sont utilisées pour les éléments similaires.
                    * **Dynamisme :** Peuvent être modifiées en JavaScript en temps réel pour des thèmes sombres/clairs, des tailles de police dynamiques, etc.
                    * **Lisibilité :** Les noms descriptifs rendent le code plus compréhensible.

                * **Fonctions de Couleurs (pour la manipulation) :**
                    En plus de `rgb()`, `rgba()`, `hsl()`, `hsla()`, il existe des fonctions CSS plus récentes pour manipuler les couleurs directement :
                    * `color()` : Permet de spécifier des couleurs dans différents espaces colorimétriques (ex: `color(display-p3 0.96 0.28 0.28)` pour des couleurs au-delà de sRGB).
                    * `lch()`, `lab()` : Pour des couleurs basées sur la perception humaine.
                    * `hwb()` : (Hue, Whiteness, Blackness).
                    * `color-mix()` : Mélange deux couleurs dans un espace colorimétrique donné (très puissant pour les thèmes).
                        ```css
                        /* Mélange du vert et du bleu */
                        .mixed-bg {
                            background-color: color-mix(in srgb, green 20%, blue);
                        }
                        ```
                    * `lighten()`, `darken()`, `saturate()` etc. : Ces fonctions étaient populaires dans les préprocesseurs (Sass, Less) et certaines commencent à arriver nativement en CSS.

                * **Fonctions d'Interpolation et de Clamp (Responsive Design) :**
                    * `clamp(min, preferred, max)` : Permet de définir une taille qui sera toujours entre un minimum et un maximum, mais qui s'adaptera en fonction d'une valeur préférée (souvent une unité viewport).
                        ```css
                        h1 {
                            font-size: clamp(2rem, 5vw, 4rem); /* La taille de h1 sera min 2rem, max 4rem, s'adapte avec 5vw */
                        }
                        ```
                    * `min()`, `max()` : Retourne la valeur minimum/maximum d'une liste de valeurs.
                        ```css
                        .element {
                            width: min(90%, 800px); /* La largeur sera 90% du parent, mais jamais plus de 800px */
                        }
                        ```

                La maîtrise de ces unités et fonctions avancées est ce qui distingue le CSS basique du CSS moderne, fluide et performant. Elles sont essentielles pour créer des interfaces utilisateur riches et dynamiques.
                """
            },
            "Intégration et Organisation du CSS": {
                "title": "Intégration et Organisation du CSS : Structurer Vos Styles",
                "text": """
                La manière dont vous intégrez et organisez votre CSS est aussi importante que le CSS lui-même. Une bonne structure améliore la maintenabilité, la performance et la collaboration.

                **1. Méthodes d'Intégration du CSS dans le HTML :**

                * **1.1. CSS Externe (Méthode Recommandée et la Plus Courante)**
                    * **Principe :** Les styles sont définis dans un ou plusieurs fichiers `.css` séparés.
                    * **Lien :** Utilisé via la balise `<link>` dans la section `<head>` de votre document HTML.
                    ```html
                    <!DOCTYPE html>
                    <html lang="fr">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Mon Super Site</title>
                        <link rel="stylesheet" href="styles/main.css"> <link rel="stylesheet" href="[https://cdn.example.com/libs/some-library.css](https://cdn.example.com/libs/some-library.css)"> </head>
                    <body>
                        </body>
                    </html>
                    ```
                    * **Avantages :**
                        * **Séparation des préoccupations :** Nettoie le code HTML en le laissant se concentrer sur le contenu.
                        * **Maintien facile :** Les changements de style n'affectent pas le HTML et peuvent être appliqués à plusieurs pages.
                        * **Performance :** Les navigateurs mettent en cache les fichiers CSS externes après le premier chargement, accélérant les chargements de pages suivantes.
                        * **Collaboration :** Facilite le travail en équipe (développeurs HTML, designers CSS).
                        * **Accessibilité :** Permet de changer de style via des feuilles de style alternatives ou par l'utilisateur.
                    * **Inconvénients :** Nécessite une requête HTTP supplémentaire pour chaque fichier CSS.

                * **1.2. CSS Interne (Embarqué)**
                    * **Principe :** Les styles sont définis directement dans le document HTML, à l'intérieur de la balise `<style>`.
                    * **Lien :** La balise `<style>` est généralement placée dans la section `<head>`.
                    ```html
                    <head>
                      <style>
                        /* Styles spécifiques à cette page */
                        h1 {
                          color: #0056b3;
                          border-bottom: 1px solid #0056b3;
                          padding-bottom: 10px;
                        }
                        .hero-section {
                            background-color: #e6f7ff;
                            padding: 50px;
                        }
                      </style>
                    </head>
                    ```
                    * **Avantages :**
                        * Utile pour des styles très spécifiques à une **seule page** qui ne seront pas réutilisés ailleurs.
                        * Pas de requête HTTP supplémentaire pour un fichier externe.
                        * Pratique pour des tests rapides ou des prototypes.
                    * **Inconvénients :**
                        * **Mélange contenu et présentation :** Rend le HTML moins propre.
                        * **Non réutilisable :** Si les styles sont nécessaires sur d'autres pages, il faut les copier/coller.
                        * **Pas de mise en cache :** Les styles sont rechargés à chaque visite de la page.

                * **1.3. CSS en Ligne (Inline Styles)**
                    * **Principe :** Les styles sont appliqués directement à un élément HTML spécifique via l'attribut `style`.
                    * **Lien :** Directement dans la balise d'ouverture de l'élément.
                    ```html
                    <p style="color: darkgreen; font-weight: bold; margin-top: 20px;">
                        Ce paragraphe a un style très spécifique directement ici.
                    </p>
                    <button type="button" style="background-color: #ffc107; padding: 8px 15px; border-radius: 4px;">
                        Cliquez-moi !
                    </button>
                    ```
                    * **Avantages :**
                        * Permet un contrôle ultra-spécifique sur un seul élément.
                        * Utile pour des modifications dynamiques avec JavaScript où vous manipulez directement le DOM.
                    * **Inconvénients :** **FORTEMENT DÉCONSEILLÉ POUR LA MISE EN PAGE NORMALE !**
                        * **Violent la séparation des préoccupations :** Le pire mélange du HTML et du CSS.
                        * **Maintenabilité quasi-nulle :** Impossible à gérer à grande échelle. Pour changer ce style, il faut modifier chaque instance de l'élément.
                        * **Spécificité écrasante :** Les styles en ligne ont la plus haute spécificité (1000 points), ce qui les rend extrêmement difficiles à surcharger par des règles externes ou internes. Vous seriez obligé d'utiliser `!important` ailleurs, créant un désordre stylistique.
                        * **Non réutilisable :** Chaque style est attaché à un seul élément.

                **2. Organisation des Fichiers et du Code CSS :**

                Une bonne organisation est essentielle pour les projets de toute taille.

                * **2.1. Structure de Fichiers :**
                    Pour les projets de taille moyenne à grande, un seul fichier `main.css` peut devenir ingérable. Considérez de diviser votre CSS en plusieurs fichiers, puis de les importer dans un fichier principal (ou de les lier séparément dans le HTML, mais le regroupement est souvent préféré).
                    ```
                    css/
                    ├── main.css           <-- Fichier principal qui importe les autres
                    ├── base/              <-- Styles de base
                    │   ├── _reset.css
                    │   ├── _typography.css
                    │   └── _variables.css
                    ├── components/        <-- Styles des composants réutilisables
                    │   ├── _button.css
                    │   ├── _card.css
                    │   └── _navbar.css
                    ├── layout/            <-- Styles de la mise en page générale
                    │   ├── _header.css
                    │   ├── _footer.css
                    │   └── _grid.css
                    ├── pages/             <-- Styles spécifiques à des pages
                    │   ├── _home.css
                    │   └── _contact.css
                    └── utilities/         <-- Classes utilitaires
                        └── _helpers.css
                    ```
                    Dans `main.css`, vous utiliseriez `@import` (historiquement) ou plus souvent, les regrouperiez lors de la compilation avec un préprocesseur (Sass, Less) ou un bundler (Webpack, Vite).

                * **2.2. Méthodologies CSS (pour structurer le code) :**
                    Ces approches fournissent des conventions de nommage et des architectures pour rendre votre CSS plus maintenable et scalable.
                    * **BEM (Block-Element-Modifier)** : Favorise des noms de classes très descriptifs et plats pour éviter les problèmes de spécificité.
                        * `block` : `button`, `card`, `header`
                        * `block__element` : `card__title`, `button__icon`
                        * `block--modifier` : `button--primary`, `card----disabled`
                        ```css
                        .card { /* block */ }
                        .card__title { /* element */ }
                        .card--disabled { /* modifier */ }
                        ```
                    * **SMACSS (Scalable and Modular Architecture for CSS)** : Organise le CSS en 5 catégories : Base, Layout, Modules, State, Theme.
                        * **Base:** Styles de base pour les balises HTML.
                        * **Layout:** Mise en page globale (en-tête, pied de page, colonnes).
                        * **Modules:** Composants réutilisables (boutons, formulaires).
                        * **State:** Styles liés aux états (actif, désactivé, caché).
                        * **Theme:** Styles spécifiques à un thème visuel.
                    * **ITCSS (Inverted Triangle CSS)** : Organise les règles du plus général au plus spécifique, en utilisant la spécificité pour gérer la cascade.
                        * Settings (variables)
                        * Tools (mixins, functions)
                        * Generic (reset, normalise)
                        * Elements (base HTML elements)
                        * Objects (layout objects)
                        * Components (UI components)
                        * Trumps (`!important` overrides)

                * **2.3. Conventions de Codage :**
                    * **Indentation :** Utilisez une indentation cohérente (2 ou 4 espaces).
                    * **Points-virgules :** Toujours terminer les déclarations par un point-virgule.
                    * **Noms de classes/ID :** Utilisez des noms significatifs et cohérents (ex: `kebab-case` `ma-classe-super`).
                    * **Commentaires :** Utilisez-les judicieusement pour expliquer des sections complexes, des choix de design ou des zones du code.

                Adopter ces méthodes d'intégration et d'organisation est crucial pour passer d'un simple "codeur" CSS à un architecte de styles, capable de gérer des projets web complexes et de collaborer efficacement.
                """
            },
            "Responsive Design et Media Queries": {
                "title": "Responsive Design et Media Queries : Adapter le Style à Chaque Appareil",
                "text": """
                Avec la prolifération des smartphones, tablettes, ordinateurs portables et grands écrans, il est devenu indispensable que les sites web s'adaptent et offrent une expérience utilisateur optimale sur tous ces appareils. C'est le rôle du **Responsive Web Design**, et les **Media Queries CSS** en sont le cœur battant.

                **1. Qu'est-ce que le Responsive Web Design ?**
                Le Responsive Web Design (RWD) est une approche de conception web qui vise à créer des sites qui **s'adaptent fluidement** à la taille de l'écran, à l'orientation et aux capacités de l'appareil de l'utilisateur. Au lieu de créer des versions séparées du site pour chaque appareil (par exemple, un site mobile dédié), un site responsive utilise une seule base de code HTML et CSS qui se réorganise et se restyle dynamiquement.

                **Les piliers du Responsive Design :**
                * **Grilles Fluides (Fluid Grids) :** Utilisation de pourcentages et d'unités relatives (`%`, `vw`, `em`, `rem`) pour les largeurs, les hauteurs et les marges, plutôt que des pixels fixes.
                * **Images Flexibles (Flexible Images) :** Les images s'adaptent à la taille de leur conteneur, évitant de déborder. `img { max-width: 100%; height: auto; }` est un classique.
                * **Media Queries :** Des règles CSS conditionnelles qui permettent d'appliquer des styles différents en fonction des caractéristiques de l'appareil (largeur, hauteur, résolution, orientation, etc.).

                **2. Les Media Queries CSS : La Logique Conditionnelle du Style**
                Une Media Query est une règle CSS qui ne s'applique que si certaines conditions (caractéristiques du média) sont remplies. Elle commence par `@media`.

                **Syntaxe de base :**
                ```css
                @media media_type and (feature: value) {
                  /* Règles CSS à appliquer si la condition est vraie */
                }
                ```

                * **`media_type` (Type de Média) :** Spécifie le type d'appareil cible.
                    * `all` (par défaut) : Tous les appareils.
                    * `screen` : Écrans d'ordinateur, tablettes, smartphones. (Le plus courant).
                    * `print` : Imprimantes.
                    * `speech` : Synthétiseurs vocaux (pour les lecteurs d'écran).
                    Ex: `@media screen and (...)`

                * **`feature: value` (Caractéristique du Média) :** La condition à vérifier. Les caractéristiques les plus courantes sont liées aux dimensions du viewport :
                    * `width`, `height` : Largeur/hauteur du viewport.
                    * `min-width`, `max-width` : Largeur minimale/maximale du viewport. (Très utilisées pour les **breakpoints**).
                    * `min-height`, `max-height` : Hauteur minimale/maximale du viewport.
                    * `orientation` : `portrait` ou `landscape`.
                    * `resolution` : Résolution de l'écran (ex: `min-resolution: 2dppx` pour écrans Retina).
                    * `prefers-color-scheme` : `light` ou `dark` (pour les thèmes sombres/clairs du système d'exploitation).

                **Opérateurs Logiques :**
                * `and` : Combine plusieurs conditions (toutes doivent être vraies).
                * `or` (ou `,`) : Si au moins une des conditions est vraie.
                * `not` : Inverse la condition.
                * `only` : Cache la feuille de style des navigateurs plus anciens qui ne supportent pas les Media Queries.

                **Exemples de Media Queries courantes (Breakpoints) :**

                * **Mobile First (Approche recommandée) :**
                    Commencez par concevoir et styliser pour les petits écrans d'abord, puis ajoutez des Media Queries pour les écrans plus grands. C'est plus efficace car les styles de base sont plus légers.
                    ```css
                    /* Styles par défaut pour les mobiles et petits écrans */
                    body {
                      font-size: 16px;
                    }
                    .container {
                      width: 100%;
                      padding: 15px;
                    }

                    /* Styles pour tablettes (au-dessus de 768px de large) */
                    @media screen and (min-width: 768px) {
                      body {
                        font-size: 18px;
                      }
                      .container {
                        width: 750px;
                        margin: 0 auto; /* Centrer le conteneur */
                      }
                      .column {
                          float: left;
                          width: 50%; /* Les colonnes passent de 100% à 50% sur tablette */
                      }
                    }

                    /* Styles pour ordinateurs de bureau (au-dessus de 1024px de large) */
                    @media screen and (min-width: 1024px) {
                      body {
                        font-size: 20px;
                      }
                      .container {
                        width: 960px;
                      }
                      .column {
                          width: 33.33%; /* Les colonnes passent à 33.33% sur desktop */
                      }
                    }
                    ```
                    Cette approche est très efficace car elle garantit que les petits appareils ne téléchargent et ne traitent que les styles dont ils ont besoin, et les styles supplémentaires ne sont ajoutés que pour les écrans plus grands.

                * **Desktop First (Moins courant, mais possible) :**
                    Concevez pour les grands écrans d'abord, puis utilisez `max-width` pour adapter aux plus petits écrans.
                    ```css
                    /* Styles par défaut pour ordinateurs de bureau */
                    .header {
                        height: 100px;
                    }

                    /* Styles pour écrans de moins de 768px de large (tablettes et mobiles) */
                    @media screen and (max-width: 767px) {
                      .header {
                          height: 60px; /* Réduire la hauteur du header sur les petits écrans */
                      }
                    }
                    ```

                **3. Balise `meta viewport` : Indispensable pour le Responsive Design**
                Pour que les Media Queries fonctionnent correctement sur les appareils mobiles, vous devez toujours inclure la balise `meta viewport` dans la section `<head>` de votre HTML :
                ```html
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                ```
                * `width=device-width` : Indique au navigateur de définir la largeur du viewport à la largeur réelle de l'appareil (en pixels CSS), plutôt que la largeur par défaut des navigateurs mobiles (souvent 980px).
                * `initial-scale=1.0` : Définit le niveau de zoom initial lorsque la page est chargée pour la première fois.

                Sans cette balise, les appareils mobiles rendront votre page comme s'il s'agissait d'un grand écran, puis la réduiront, ce qui rendra les Media Queries inefficaces.

                **4. Cas d'utilisation Avancés des Media Queries :**
                * **Orientation :**
                    ```css
                    @media screen and (orientation: landscape) { /* Styles pour le mode paysage */
                      .image-gallery {
                        grid-template-columns: repeat(4, 1fr);
                      }
                    }
                    ```
                * **Préférences de l'utilisateur (Dark Mode) :**
                    ```css
                    @media (prefers-color-scheme: dark) {
                      body {
                        background-color: #333;
                        color: #eee;
                      }
                      a {
                        color: #88f;
                      }
                    }
                    ```
                * **Résolution :**
                    ```css
                    /* Styles pour écrans haute résolution (Retina) */
                    @media screen and (min-resolution: 192dpi),
                           screen and (min-resolution: 2dppx),
                           screen and (min-width: 1200px) and (-webkit-min-device-pixel-ratio: 2) {
                        .logo {
                            background-image: url('logo@2x.png'); /* Charger une image de meilleure qualité */
                            background-size: contain;
                        }
                    }
                    ```
                * **Accessibilité (Réduction du mouvement) :**
                    ```css
                    @media (prefers-reduced-motion: reduce) {
                      * {
                        transition: none !important; /* Désactiver toutes les transitions et animations */
                        animation: none !important;
                      }
                    }
                    ```

                Le Responsive Design et les Media Queries sont devenus des compétences indispensables pour tout développeur web moderne, permettant de créer des expériences utilisateur flexibles et accessibles sur l'écosystème numérique varié d'aujourd'hui.
                """
            },
            "Les Préprocesseurs CSS (Concepts)": {
                "title": "Les Préprocesseurs CSS : Extension de la Puissance du CSS",
                "text": """
                Les **préprocesseurs CSS** sont des langages de script qui étendent les capacités du CSS standard. Ils vous permettent d'utiliser des fonctionnalités qui ne sont pas disponibles nativement en CSS pur (comme les variables complexes, les fonctions, les imbrications, les mixins, les opérations mathématiques, etc.) et de compiler ce code en CSS standard que le navigateur peut comprendre.

                **Comment ça marche ?**
                Vous écrivez votre code dans un préprocesseur (par exemple, un fichier `.scss`, `.less` ou `.styl`). Un "compilateur" (un programme ou un outil de build comme Webpack, Vite, Gulp) lit ce code, le traite et génère un fichier CSS standard (`.css`) que vous liez ensuite à votre HTML.

                **Les préprocesseurs les plus populaires :**
                1.  **Sass (Syntactically Awesome Style Sheets)** : Le plus populaire et le plus riche en fonctionnalités. Il a deux syntaxes :
                    * **SCSS (Sassy CSS)** : La syntaxe la plus utilisée, car elle est compatible avec le CSS normal (c'est du CSS avec des fonctionnalités Sass en plus). Fichiers en `.scss`.
                    * **Sass (syntaxe originale)** : Utilise des indentations au lieu d'accolades et de points-virgules. Moins courant. Fichiers en `.sass`.
                2.  **Less (Leaner CSS)** : Moins de fonctionnalités que Sass, mais souvent plus simple à prendre en main pour les débutants. Fichiers en `.less`.
                3.  **Stylus** : Très flexible au niveau de la syntaxe (peut ressembler à Sass, Less, ou CSS pur). Fichiers en `.styl`.

                **Fonctionnalités Clés Offertes par les Préprocesseurs :**

                1.  **Variables :**
                    Permettent de stocker des valeurs (couleurs, tailles, polices) dans des variables réutilisables. Similaires aux variables CSS natives (`--var`), mais avec plus de flexibilité (opérations).
                    ```scss
                    // Sass (SCSS)
                    $primary-color: #007bff;
                    $font-stack: 'Helvetica Neue', Helvetica, Arial, sans-serif;

                    body {
                      font-family: $font-stack;
                      color: $primary-color;
                    }

                    button {
                      background-color: $primary-color;
                      border: 1px solid $primary-color;
                    }
                    ```
                    **Avantage :** Mises à jour globales faciles, cohérence du design.

                2.  **Imbrication (Nesting) :**
                    Permet d'imbriquer les sélecteurs CSS les uns dans les autres, reflétant la structure HTML. Rend le code plus propre et plus facile à lire pour les hiérarchies complexes.
                    ```scss
                    // Sass (SCSS)
                    .navbar {
                      background-color: #333;
                      padding: 10px;

                      ul { // Imbriqué dans .navbar
                        list-style: none;
                        margin: 0;
                        padding: 0;

                        li { // Imbriqué dans ul
                          display: inline-block;

                          a { // Imbriqué dans li
                            color: white;
                            text-decoration: none;
                            padding: 8px 15px;

                            &:hover { // Le '&' référence le sélecteur parent (ici 'a')
                              background-color: #555;
                            }
                          }
                        }
                      }
                    }
                    ```
                    **Compile en :**
                    ```css
                    .navbar { /* ... */ }
                    .navbar ul { /* ... */ }
                    .navbar ul li { /* ... */ }
                    .navbar ul li a { /* ... */ }
                    .navbar ul li a:hover { /* ... */ }
                    ```
                    **Avantage :** Code plus concis, meilleure correspondance avec la structure HTML.

                3.  **Mixins :**
                    Des blocs de code CSS réutilisables qui peuvent accepter des arguments. Idéal pour des groupes de propriétés souvent répétées ou pour gérer les préfixes vendeurs.
                    ```scss
                    // Sass (SCSS)
                    @mixin border-radius($radius) {
                      -webkit-border-radius: $radius;
                      -moz-border-radius: $radius;
                      border-radius: $radius;
                    }

                    .button {
                      @include border-radius(5px);
                      background-color: blue;
                    }

                    .card {
                      @include border-radius(10px);
                      box-shadow: 2px 2px 5px gray;
                    }
                    ```
                    **Avantage :** Réduction de la duplication de code (DRY - Don't Repeat Yourself), gestion des préfixes, code plus modulaire.

                4.  **Fonctions :**
                    Permettent d'effectuer des opérations complexes et de retourner des valeurs. Sass a de nombreuses fonctions intégrées (couleurs, nombres, chaînes de caractères) et vous pouvez en créer de nouvelles.
                    ```scss
                    // Sass (SCSS)
                    $base-font-size: 16px;

                    @function rem($pixels) {
                      @return ($pixels / $base-font-size) * 1rem;
                    }

                    .title {
                      font-size: rem(32px); // Utilise la fonction rem pour convertir pixels en rem
                    }
                    .text {
                      font-size: rem(18px);
                    }
                    ```
                    **Avantage :** Logique avancée, conversion d'unités, manipulation de couleurs.

                5.  **Partials et Importations :**
                    Permettent de diviser votre code CSS en plusieurs petits fichiers logiques (partials, commençant par `_`, ex: `_variables.scss`), puis de les importer dans un fichier principal. Le compilateur les fusionne en un seul fichier CSS.
                    ```scss
                    // style.scss
                    @import 'base/variables';
                    @import 'components/button';
                    @import 'layout/header';

                    /* Autres styles */
                    ```
                    **Avantage :** Meilleure organisation, maintenabilité, modularité.

                6.  **Héritage (`@extend`) :**
                    Permet à un sélecteur d'hériter de tous les styles d'un autre sélecteur, sans duplication de code dans le CSS compilé.
                    ```scss
                    // Sass (SCSS)
                    .message {
                      border: 1px solid gray;
                      padding: 10px;
                      margin-bottom: 10px;
                    }

                    .message--success {
                      @extend .message;
                      border-color: green;
                      background-color: lightgreen;
                    }
                    ```
                    **Compile en :**
                    ```css
                    .message, .message--success {
                      border: 1px solid gray;
                      padding: 10px;
                      margin-bottom: 10px;
                    }

                    .message--success {
                      border-color: green;
                      background-color: lightgreen;
                    }
                    ```
                    **Avantage :** Réduction de la duplication de code et du poids du fichier CSS.

                **Inconvénients des Préprocesseurs :**
                * **Nécessite un processus de compilation :** Ajoute une étape au workflow de développement.
                * **Courbe d'apprentissage :** Il faut apprendre la syntaxe et les fonctionnalités du préprocesseur.
                * **Dépendance à un outil :** Si l'outil est mis à jour ou abandonné, cela peut impacter le projet.

                Avec l'évolution rapide du CSS natif (variables CSS, `clamp()`, `min()`, `max()`, `@layer`, `container-queries`), certaines des fonctionnalités des préprocesseurs deviennent disponibles directement dans le navigateur. Cependant, les préprocesseurs restent extrêmement utiles pour des fonctionnalités comme les mixins complexes, l'héritage d'extensions, et une organisation de fichiers avancée. Ils restent un outil puissant dans l'arsenal du développeur front-end.
                """
            },
            "Outils et Bonnes Pratiques Complémentaires": {
                "title": "Outils et Bonnes Pratiques Complémentaires pour un CSS Robuste",
                "text": """
                Au-delà de la syntaxe pure, l'efficacité de votre CSS dépend aussi des outils que vous utilisez et des méthodologies que vous adoptez.

                **1. Outils Essentiels pour le Développement CSS :**

                * **Inspecteur de Navigateur (Developer Tools) :**
                    * **Fonctionnalité :** L'outil le plus indispensable. Permet d'inspecter les styles appliqués à chaque élément, de comprendre la cascade et la spécificité (onglet "Styles" ou "Computed"), de modifier les styles en direct pour tester des changements, et de simuler différentes tailles d'écran (mode "Responsive Design").
                    * **Comment y accéder :** Clic droit > "Inspecter" ou "Inspecter l'élément" (sur Chrome/Firefox/Edge).
                * **Préprocesseurs (Sass, Less, Stylus) :**
                    * **Rôle :** Comme détaillé précédemment, ils étendent le CSS avec des variables, imbrications, mixins, fonctions, etc. Nécessitent un compilateur.
                    * **Utilisation :** Intégrés dans les environnements de développement modernes (npm scripts, Webpack, Vite, Gulp, Grunt).
                * **PostCSS :**
                    * **Rôle :** Un outil qui transforme le CSS après qu'il ait été écrit ou compilé. Il fonctionne avec des "plugins".
                    * **Exemples de plugins :**
                        * **Autoprefixer :** Ajoute automatiquement les préfixes vendeurs (`-webkit-`, `-moz-`, etc.) nécessaires pour la compatibilité avec les anciens navigateurs.
                        * **CSSNano :** Minifie votre CSS (réduit la taille des fichiers).
                        * **CSS Modules / PostCSS Nesting :** Permet d'utiliser l'imbrication ou de scope le CSS.
                    * **Avantage :** Plus flexible et modulaire qu'un préprocesseur tout-en-un, permet d'ajouter des fonctionnalités futuristes au CSS d'aujourd'hui.
                * **Linters et Formatters (ESLint, Stylelint, Prettier) :**
                    * **Rôle :** Assurent la cohérence du code, détectent les erreurs potentielles et formatent le code automatiquement selon des règles prédéfinies.
                    * **Avantage :** Améliore la qualité du code, facilite la collaboration, automatise le respect des conventions.
                * **Systèmes de Design (Design Systems) et Bibliothèques de Composants (ex: Bootstrap, Tailwind CSS, Material-UI) :**
                    * **Rôle :** Fournissent un ensemble de composants UI pré-stylisés et de directives de design pour construire des interfaces rapidement et de manière cohérente.
                    * **Avantage :** Gain de temps, cohérence du design, meilleures pratiques intégrées.
                * **CSS-in-JS (React, Vue, Angular) :**
                    * **Rôle :** Permet d'écrire du CSS directement dans le JavaScript/TypeScript de vos composants.
                    * **Exemples :** Styled Components, Emotion.
                    * **Avantage :** Styles scopés au composant, meilleure expérience développeur pour les applications basées sur les composants.

                **2. Bonnes Pratiques Complémentaires pour un CSS Robuste et Maintenable :**

                * **Approche Mobile-First :**
                    * **Principe :** Concevez et codez d'abord pour les plus petits écrans, puis utilisez les Media Queries (`min-width`) pour ajouter des styles spécifiques aux écrans plus grands.
                    * **Avantage :** Optimise la performance pour les appareils mobiles, force une réflexion sur le contenu essentiel, simplifie le code de base.
                * **Composants Réutilisables :**
                    * **Principe :** Pensez votre UI en termes de composants autonomes (boutons, cartes, navigations). Chaque composant devrait avoir son propre style et être indépendant.
                    * **Avantage :** Réduction de la duplication de code, maintenance plus facile, clarté.
                * **Éviter la Spécificité Excessif :**
                    * **Principe :** Préférez les sélecteurs de classe simples. Évitez d'enchaîner trop de sélecteurs ou d'utiliser des ID trop souvent pour le style.
                    * **Avantage :** Facilite la surcharge des styles, rend le code plus flexible et moins sujet aux conflits.
                * **Variables CSS (Custom Properties) :**
                    * **Principe :** Utilisez-les pour toutes les valeurs récurrentes (couleurs, espacements, typographie).
                    * **Avantage :** Centralisation des valeurs, thèmes faciles à implémenter, débogage simplifié.
                * **Modularisation :**
                    * **Principe :** Divisez votre feuille de style en fichiers plus petits et logiques (voir section "Organisation").
                    * **Avantage :** Maintien facilité, meilleure collaboration, organisation claire du projet.
                * **Documentation du Code :**
                    * **Principe :** Commentez les sections complexes, les justifications de design, les hacks spécifiques.
                    * **Avantage :** Permet aux autres (et à vous-même plus tard) de comprendre rapidement l'intention derrière le code.
                * **Tests de Régression Visuelle :**
                    * **Principe :** Utilisez des outils (ex: Percy, Chromatic) pour détecter automatiquement les régressions visuelles (changements inattendus d'apparence) lors des modifications de code.
                    * **Avantage :** S'assurer que les changements de style n'ont pas d'effets secondaires indésirables sur d'autres parties du site.
                * **Performance CSS :**
                    * **Minification/Compression :** Réduisez la taille de vos fichiers CSS avant la production.
                    * **Éviter les styles bloquants :** Chargez les CSS critiques en premier et différez le chargement des CSS non-critiques (avec `media="print"` ou `preload`).
                    * **Optimisation des sélecteurs :** Les sélecteurs simples sont plus rapides à analyser par le navigateur.

                Le monde du CSS est vaste et en constante évolution. En combinant une solide compréhension de la syntaxe avec l'utilisation judicieuse des outils et l'adoption de bonnes pratiques, vous serez bien équipé pour créer des interfaces web exceptionnelles, performantes et maintenables.
                """
            },
            "Flexbox (Disposition Flexible)": {
                "title": "Flexbox : Le Contrôle Unidimensionnel de la Disposition",
                "text": """
                **Flexbox** est un module de disposition CSS unidimensionnel, conçu pour distribuer l'espace entre les éléments d'une interface et les aligner, même si leur taille est inconnue ou dynamique. Il est parfait pour créer des barres de navigation, des galeries d'images, ou aligner des éléments dans un conteneur.

                * **Conteneur Flex (Flex Container):** L'élément parent auquel vous appliquez `display: flex;` ou `display: inline-flex;`. C'est lui qui devient un conteneur flexible.
                * **Élément Flex (Flex Item):** Les enfants directs du conteneur flex. Ce sont ces éléments qui sont arrangés par Flexbox.

                **Propriétés clés pour le Conteneur Flex:**

                * `display: flex;` ou `display: inline-flex;` : Transforme l'élément en conteneur flex.
                * `flex-direction`: Définit la direction de l'axe principal (où les éléments sont placés).
                    * `row` (par défaut): De gauche à droite.
                    * `column`: De haut en bas.
                    * `row-reverse`, `column-reverse`.
                * `justify-content`: Aligne les éléments le long de l'axe principal.
                    * `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`.
                * `align-items`: Aligne les éléments le long de l'axe secondaire (perpendiculaire à l'axe principal).
                    * `flex-start`, `flex-end`, `center`, `baseline`, `stretch`.
                * `flex-wrap`: Gère le passage à la ligne des éléments si l'espace est insuffisant.
                    * `nowrap` (par défaut): Pas de retour à la ligne.
                    * `wrap`: Retour à la ligne.
                    * `wrap-reverse`.
                * `gap` (ou `column-gap`, `row-gap`): Crée de l'espace entre les éléments flex (équivalent au `grid-gap` de Grid).

                **Propriétés clés pour les Éléments Flex:**

                * `flex-grow`: Spécifie la capacité d'un élément à grandir pour occuper l'espace disponible.
                * `flex-shrink`: Spécifie la capacité d'un élément à rétrécir pour éviter les débordements.
                * `flex-basis`: Définit la taille initiale d'un élément avant que l'espace disponible ne soit distribué.
                * `flex` (raccourci): Combine `flex-grow`, `flex-shrink`, `flex-basis`.
                * `order`: Change l'ordre visuel des éléments, indépendamment de leur ordre dans le HTML.

                **Exemple simple:**
                ```css
                .container {
                  display: flex; /* Active Flexbox */
                  flex-direction: row; /* Les éléments s'alignent horizontalement */
                  justify-content: space-around; /* Espace uniformément entre et autour des éléments */
                  align-items: center; /* Centre les éléments verticalement */
                  height: 100px;
                  border: 1px solid #ccc;
                }

                .item {
                  padding: 10px;
                  background-color: lightblue;
                  margin: 5px;
                }
                ```
                """
            },
            "CSS Grid Layout (Grille)": {
                "title": "CSS Grid Layout : La Disposition Bidimensionnelle Avancée",
                "text": """
                **CSS Grid Layout** est un module de disposition CSS bidimensionnel, conçu pour gérer la mise en page des lignes et des colonnes simultanément. Il est idéal pour des mises en page entières de pages web ou des sections complexes, là où Flexbox excelle dans les composants individuels.

                * **Conteneur de Grille (Grid Container):** L'élément parent auquel vous appliquez `display: grid;` ou `display: inline-grid;`.
                * **Élément de Grille (Grid Item):** Les enfants directs du conteneur de grille.

                **Propriétés clés pour le Conteneur de Grille:**

                * `display: grid;` ou `display: inline-grid;` : Transforme l'élément en conteneur de grille.
                * `grid-template-columns`: Définit les colonnes de la grille (tailles et nombre).
                    * `grid-template-columns: 1fr 2fr 1fr;` (3 colonnes, la deuxième deux fois plus large).
                    * `grid-template-columns: repeat(3, 1fr);` (3 colonnes égales).
                    * `grid-template-columns: 100px auto 1fr;`
                * `grid-template-rows`: Définit les lignes de la grille.
                * `grid-gap`, `row-gap`, `column-gap`: Espace entre les cellules de la grille.
                * `justify-items`, `align-items`: Aligne le *contenu* des cellules de la grille.
                * `justify-content`, `align-content`: Aligne la *grille entière* dans le conteneur si elle n'occupe pas tout l'espace.

                **Propriétés clés pour les Éléments de Grille:**

                * `grid-column-start`, `grid-column-end`: Définissent où un élément commence et finit sur les lignes de colonne.
                * `grid-row-start`, `grid-row-end`: Définissent où un élément commence et finit sur les lignes de ligne.
                * `grid-column` (raccourci): `grid-column: 1 / span 2;` (commence à la ligne 1, s'étend sur 2 colonnes).
                * `grid-row` (raccourci).
                * `grid-area`: Nomme une zone de la grille et positionne un élément par ce nom.

                **Exemple simple:**
                ```css
                .grid-container {
                  display: grid;
                  grid-template-columns: 1fr 2fr 1fr; /* Trois colonnes: étroite, large, étroite */
                  grid-template-rows: auto 100px; /* Deux lignes: hauteur automatique, puis 100px */
                  gap: 20px; /* Espace de 20px entre les cellules */
                  border: 1px solid #ccc;
                  padding: 10px;
                }

                .grid-item {
                  background-color: lightcoral;
                  padding: 15px;
                  text-align: center;
                }

                .header {
                  grid-column: 1 / span 3; /* L'en-tête s'étend sur les 3 colonnes */
                  background-color: lightgreen;
                }

                .sidebar {
                  grid-row: 2;
                  background-color: lightblue;
                }
                ```
                """
            },
            "Modèle de Boîte (Box Model) Détaillé": {
                "title": "Modèle de Boîte CSS : Comprendre la Structure de Chaque Élément",
                "text": """
                Le **modèle de boîte CSS** décrit comment chaque élément HTML est rendu comme une boîte rectangulaire, englobant son contenu, son rembourrage (padding), sa bordure (border) et sa marge (margin).

                ```
                +-----------------------------------+
                |              Margin               |  (Espace EXTERNE autour de l'élément)
                |  +-----------------------------+  |
                |  |           Border            |  |  (Ligne de contour de l'élément)
                |  |  +-----------------------+  |  |
                |  |  |        Padding        |  |  |  (Espace INTERNE entre la bordure et le contenu)
                |  |  |  +-----------------+  |  |  |
                |  |  |  |     Content     |  |  |  |  (Contenu réel de l'élément: texte, image, etc.)
                |  |  |  +-----------------+  |  |  |
                |  |  |                       |  |  |
                |  |  +-----------------------+  |  |
                |  |                             |  |
                |  +-----------------------------+  |
                |                                   |
                +-----------------------------------+
                ```

                * **`content`:** Le contenu réel de l'élément (texte, images, autres éléments HTML). Ses dimensions sont définies par `width` et `height`.
                * **`padding`:** L'espace transparent entre le contenu et la bordure. Il est interne à la boîte et prend la couleur de fond de l'élément.
                    * `padding: 10px;` (tous les côtés)
                    * `padding: 10px 20px;` (haut/bas 10px, gauche/droite 20px)
                    * `padding: 10px 20px 30px 40px;` (haut, droite, bas, gauche)
                    * `padding-top`, `padding-right`, `padding-bottom`, `padding-left`.
                * **`border`:** La ligne qui entoure le padding et le contenu. Elle a une `width`, un `style` et une `color`.
                    * `border: 1px solid black;`
                    * `border-width`, `border-style`, `border-color`.
                    * `border-radius`: Pour arrondir les coins.
                * **`margin`:** L'espace transparent à l'extérieur de la bordure, créant une séparation avec les éléments voisins. Les marges verticales peuvent se "fusionner" (margin collapsing).
                    * `margin: 20px;` (tous les côtés)
                    * `margin: 0 auto;` (haut/bas 0, centré horizontalement pour les éléments de type `block` avec une largeur définie).
                    * `margin-top`, `margin-right`, `margin-bottom`, `margin-left`.

                **`box-sizing` (Propriété cruciale):**
                Cette propriété modifie la façon dont la largeur (`width`) et la hauteur (`height`) d'un élément sont calculées.
                * `content-box` (par défaut): `width` et `height` ne s'appliquent qu'au **contenu**. Padding et border sont *ajoutés* à cette taille.
                    * Ex: `width: 100px; padding: 10px; border: 1px;` => Largeur réelle = `100 + 10*2 (padding) + 1*2 (border) = 122px`.
                * `border-box`: `width` et `height` incluent le **padding et la bordure**. Le contenu se réduit pour compenser. **C'est le mode préféré et recommandé** pour un contrôle de mise en page plus intuitif.
                    * Ex: `width: 100px; padding: 10px; border: 1px; box-sizing: border-box;` => Largeur réelle = `100px`. Le contenu aura une largeur de `100 - 20 (padding) - 2 (border) = 78px`.

                Souvent, on utilise un "reset" pour appliquer `box-sizing: border-box;` à tous les éléments:
                ```css
                html {
                  box-sizing: border-box;
                }
                *, *::before, *::after {
                  box-sizing: inherit;
                }
                ```
                """
            },
            "Positionnement CSS": {
                "title": "Positionnement CSS : Contrôler l'Emplacement des Éléments",
                "text": """
                La propriété `position` permet de contrôler précisément l'emplacement d'un élément sur la page.

                * **`static` (par défaut):** L'élément est dans le flux normal du document. Les propriétés `top`, `right`, `bottom`, `left` n'ont aucun effet.
                * **`relative`:** L'élément reste dans le flux normal, mais vous pouvez le décaler de sa position normale en utilisant `top`, `right`, `bottom`, `left`.
                    * Utile pour positionner des enfants `absolute` par rapport à lui (le parent `relative` devient le contexte de positionnement).
                * **`absolute`:** L'élément est complètement retiré du flux normal du document. Sa position est déterminée par les propriétés `top`, `right`, `bottom`, `left` **par rapport à l'ancêtre positionné le plus proche** (un parent avec `position: relative`, `absolute`, `fixed`, ou `sticky`). S'il n'y a pas d'ancêtre positionné, il se positionne par rapport au `<body>`.
                    * Idéal pour les menus déroulants, les info-bulles, les modales.
                * **`fixed`:** L'élément est retiré du flux normal et positionné par rapport à la **fenêtre d'affichage (viewport)**. Il reste fixe même lorsque la page défile.
                    * Utile pour les en-têtes ou pieds de page qui doivent rester visibles.
                * **`sticky`:** Un hybride de `relative` et `fixed`. Il se comporte comme `relative` jusqu'à ce que l'utilisateur le fasse défiler au-delà d'un certain seuil (défini par `top`, `right`, `bottom`, `left`), puis il devient `fixed` jusqu'à ce que son parent disparaisse du viewport.
                    * Parfait pour les barres de navigation qui deviennent "collantes" après un certain défilement.

                **Propriété `z-index`:**
                Utilisée avec les éléments positionnés (`relative`, `absolute`, `fixed`, `sticky`), `z-index` contrôle l'ordre d'empilement des éléments sur l'axe Z (profondeur). Un élément avec un `z-index` plus élevé apparaît au-dessus des éléments avec un `z-index` plus bas.
                """
            },
            "Pseudo-classes et Pseudo-éléments Avancés": {
                "title": "Pseudo-classes et Pseudo-éléments Avancés : Cibler des États et des Parties Spécifiques",
                "text": """
                Nous avons vu les bases, mais voici quelques exemples plus élaborés de pseudo-classes et pseudo-éléments :

                **Pseudo-classes (`:`):**

                * `:nth-of-type(n)` / `:nth-last-of-type(n)`: Similaire à `nth-child`, mais compte parmi les frères de *même type d'élément*.
                    ```css
                    p:nth-of-type(2) { /* Cible le deuxième paragraphe dans son parent, même s'il y a d'autres éléments avant */
                      color: purple;
                    }
                    ```
                * `:target`: Cible l'élément dont l'ID correspond au fragment d'URL (ex: `http://example.com/#section1`).
                    ```css
                    #section1:target {
                      background-color: yellow;
                    }
                    ```
                * `:focus-within`: Cible un élément parent si lui-même ou l'un de ses descendants a le focus. Utile pour styliser des conteneurs de formulaire.
                    ```css
                    .form-group:focus-within {
                      border-color: blue;
                      box-shadow: 0 0 5px rgba(0,0,255,0.3);
                    }
                    ```
                * `:read-only`, `:read-write`: Pour les champs de formulaire en lecture seule ou modifiables.

                **Pseudo-éléments (`::`):**

                * `::first-letter` / `::first-line`: Pour styliser la première lettre ou la première ligne d'un bloc de texte.
                    ```css
                    p::first-letter {
                      font-size: 2em;
                      font-weight: bold;
                      color: #333;
                    }
                    ```
                * `::selection`: Pour styliser le texte sélectionné par l'utilisateur.
                    ```css
                    ::selection {
                      background: #ffcc00;
                      color: #000;
                    }
                    ```
                * `::marker`: Permet de styliser les puces ou numéros des listes (`<li>`).
                    ```css
                    li::marker {
                      color: red;
                      font-size: 1.2em;
                    }
                    ```
                """
            },
            "Variables CSS (Custom Properties)": {
                "title": "Variables CSS (Custom Properties) : La Personnalisation Avancée",
                "text": """
                Les **variables CSS** (ou propriétés personnalisées) sont des entités définies par l'auteur qui contiennent des valeurs réutilisables dans un document. Elles sont déclarées avec un préfixe `--` et accédées avec la fonction `var()`.

                * **Déclaration:** Définissez les variables à l'intérieur de n'importe quel sélecteur. Souvent, elles sont définies sur le pseudo-classe `:root` pour être accessibles globalement.
                    ```css
                    :root {
                      --main-color: #007bff;
                      --secondary-color: #6c757d;
                      --font-family-body: 'Arial', sans-serif;
                      --spacing-unit: 1rem;
                    }
                    ```
                * **Utilisation:** Utilisez la fonction `var()` pour récupérer la valeur d'une variable. Vous pouvez aussi définir une valeur de secours si la variable n'est pas trouvée.
                    ```css
                    body {
                      font-family: var(--font-family-body);
                      color: var(--main-color);
                    }

                    .card {
                      padding: var(--spacing-unit);
                      border: 1px solid var(--secondary-color, lightgray); /* lightgray est la valeur de secours */
                    }
                    ```
                * **Avantages:**
                    * **Maintenabilité:** Changez une valeur à un seul endroit, elle se met à jour partout.
                    * **Thèmes:** Facilite la création de thèmes (clair/sombre, différentes marques) en changeant simplement quelques variables.
                    * **Dynamisme:** Les variables CSS peuvent être modifiées via JavaScript, ce qui ouvre la porte à des interactions et des thèmes dynamiques.
                    * **Lisibilité:** Le code est plus clair grâce à des noms significatifs.
                """
            },
            "Transitions et Animations CSS": {
                "title": "Transitions et Animations CSS : Ajouter du Mouvement et de l'Interactivité",
                "text": """
                Ces modules permettent de créer des effets visuels fluides et dynamiques sans JavaScript.

                **Transitions (`transition`):**
                Permettent de modifier en douceur l'état d'une propriété CSS sur une période donnée. Elles s'activent lorsqu'une propriété change de valeur (ex: au survol `:hover`).

                * `transition-property`: La propriété CSS à animer (ex: `color`, `background-color`, `transform`, `all`).
                * `transition-duration`: La durée de la transition (ex: `0.3s`, `500ms`).
                * `transition-timing-function`: La courbe d'accélération/décélération (ex: `ease`, `linear`, `ease-in-out`, `cubic-bezier()`).
                * `transition-delay`: Un délai avant que la transition ne commence.
                * `transition` (raccourci): `transition: [property] [duration] [timing-function] [delay];`

                **Exemple:**
                ```css
                button {
                  background-color: blue;
                  color: white;
                  padding: 10px 20px;
                  transition: background-color 0.3s ease-in-out, transform 0.2s ease-out; /* Deux transitions séparées */
                }

                button:hover {
                  background-color: darkblue;
                  transform: translateY(-2px); /* Déplace légèrement le bouton vers le haut */
                }
                ```

                **Animations (`animation` et `@keyframes`):**
                Permettent de créer des séquences d'animation plus complexes avec plusieurs étapes (keyframes). Elles peuvent se jouer automatiquement et se répéter.

                * `@keyframes`: Règle CSS qui définit les étapes d'une animation.
                    ```css
                    @keyframes slideIn {
                      from {
                        transform: translateX(-100%);
                        opacity: 0;
                      }
                      to {
                        transform: translateX(0);
                        opacity: 1;
                      }
                    }
                    ```
                * `animation-name`: Nom de l'animation (`slideIn` ci-dessus).
                * `animation-duration`: Durée de l'animation.
                * `animation-timing-function`: Courbe de vitesse.
                * `animation-delay`: Délai avant le début.
                * `animation-iteration-count`: Nombre de répétitions (`infinite` pour une boucle).
                * `animation-direction`: Sens de l'animation (`normal`, `reverse`, `alternate`).
                * `animation-fill-mode`: Styles appliqués avant/après l'animation (`forwards`, `backwards`, `both`).
                * `animation` (raccourci): `animation: [name] [duration] [timing-function] [delay] [iteration-count] [direction] [fill-mode];`

                **Exemple:**
                ```css
                .box {
                  width: 100px;
                  height: 100px;
                  background-color: red;
                  animation: pulse 2s infinite alternate; /* Anime 'pulse', 2s, infini, alterne direction */
                }

                @keyframes pulse {
                  0% {
                    transform: scale(1);
                    background-color: red;
                  }
                  50% {
                    transform: scale(1.1);
                    background-color: orange;
                  }
                  100% {
                    transform: scale(1);
                    background-color: red;
                  }
                }
                ```
                """
            },
            "Unités Viewport (vw, vh, vmin, vmax)": {
                "title": "Unités Viewport : S'Adapter Dynamiquement à la Fenêtre d'Affichage",
                "text": """
                Ces unités sont relatives à la taille de la fenêtre d'affichage (viewport) du navigateur. Elles sont essentielles pour créer des designs fluides et véritablement responsives.

                * `vw` (viewport width): 1% de la **largeur** de la fenêtre d'affichage.
                * `vh` (viewport height): 1% de la **hauteur** de la fenêtre d'affichage.
                * `vmin`: 1% de la **plus petite** dimension de la fenêtre d'affichage (largeur ou hauteur). Utile pour s'assurer qu'un élément reste toujours visible.
                * `vmax`: 1% de la **plus grande** dimension de la fenêtre d'affichage (largeur ou hauteur).

                **Exemples:**
                ```css
                h1 {
                  font-size: 5vw; /* La taille du titre s'adaptera proportionnellement à la largeur de l'écran */
                }

                .hero-section {
                  height: 80vh; /* La section prendra 80% de la hauteur du viewport */
                  min-height: 400px; /* Mais jamais moins de 400px */
                }

                .square {
                  width: 50vmin; /* Le carré aura une taille de 50% de la plus petite dimension du viewport (largeur ou hauteur) */
                  height: 50vmin;
                }
                ```
                """
            },
            "Le Concept de BFC (Block Formatting Context)": {
                "title": "Le Concept de BFC : Comprendre les Contextes de Formatage de Blocs",
                "text": """
                Un **Block Formatting Context (BFC)** est un environnement de rendu en CSS où le positionnement des boîtes (éléments) est basé sur le modèle de boîte. Un BFC est créé par certaines propriétés CSS et il a des règles spécifiques sur la façon dont les éléments à l'intérieur se comportent.

                **Quand un BFC est-il créé ?**
                Un BFC est créé par :
                * L'élément racine (`<html>`).
                * `float` (n'importe quelle valeur sauf `none`).
                * `position` (`absolute` ou `fixed`).
                * `display`: `inline-block`, `table-cell`, `table-caption`, `flex`, `grid`.
                * `overflow` (n'importe quelle valeur sauf `visible`).
                * `column-count` ou `column-width`.
                * `contain: layout`, `content`, ou `strict`.

                **Pourquoi est-ce important ?**
                Les BFC sont utiles pour résoudre certains problèmes de mise en page:
                1.  **Prévenir l'effondrement des marges (Margin Collapsing):** Les marges verticales de deux blocs adjacents peuvent se fusionner. Un BFC peut empêcher cela.
                2.  **Contenir les flottants (Floats):** Si un parent contient des éléments flottants, sa hauteur peut s'effondrer. Créer un BFC sur le parent (par ex., avec `overflow: hidden;`) le forcera à contenir ses flottants.
                3.  **Empêcher le chevauchement avec des flottants:** Un élément dans un BFC ne chevauchera jamais un élément flottant. Il se mettra à côté.

                **Exemple pour contenir des flottants:**
                ```html
                <div class="container">
                  <div class="float-box">Float</div>
                  <p>Ceci est un paragraphe.</p>
                </div>
                ```
                ```css
                .float-box {
                  float: left;
                  width: 100px;
                  height: 100px;
                  background-color: lightblue;
                }

                .container {
                  /* Sans overflow: hidden;, le conteneur n'engloberait pas float-box et p chevaucherait */
                  overflow: hidden; /* Crée un nouveau BFC, forçant le conteneur à englober le flottant */
                  background-color: #eee;
                  padding: 10px;
                }
                ```
                """
            },
            "CSS Reset et Normalize.css": {
                "title": "CSS Reset et Normalize.css : Harmoniser les Styles du Navigateur",
                "text": """
                Les navigateurs appliquent par défaut leurs propres styles aux éléments HTML (ex: les titres sont gras, les liens sont bleus et soulignés). Ces styles par défaut varient d'un navigateur à l'autre, ce qui peut entraîner des incohérences visuelles.

                * **CSS Reset:**
                    * **Principe:** Remet à zéro tous les styles par défaut des navigateurs. L'idée est de partir d'une feuille vierge et de construire tous les styles à partir de zéro.
                    * **Exemple (partiel):**
                        ```css
                        * {
                          margin: 0;
                          padding: 0;
                          border: 0;
                          font-size: 100%;
                          font: inherit;
                          vertical-align: baseline;
                          box-sizing: border-box; /* Très courant dans les resets modernes */
                        }
                        /* D'autres règles pour HTML5 display-role reset pour les navigateurs plus anciens */
                        article, aside, details, figcaption, figure,
                        footer, header, hgroup, menu, nav, section {
                          display: block;
                        }
                        body {
                          line-height: 1;
                        }
                        ol, ul {
                          list-style: none;
                        }
                        table {
                          border-collapse: collapse;
                          border-spacing: 0;
                        }
                        ```
                    * **Avantages:** Contrôle total sur les styles, élimine les incohérences.
                    * **Inconvénients:** Peut nécessiter plus de code CSS car tout doit être stylisé.

                * **Normalize.css:**
                    * **Principe:** Au lieu de tout remettre à zéro, Normalize.css corrige les incohérences entre les navigateurs tout en conservant les styles par défaut *utiles* du navigateur (ex: la taille de police par défaut des titres est conservée). Il vise à rendre les styles par défaut cohérents.
                    * **Avantages:** Plus léger qu'un reset complet, préserve les styles par défaut sémantiques qui peuvent être utiles.
                    * **Inconvénients:** Moins de contrôle total que le reset, peut encore nécessiter quelques ajustements personnels.

                **Quand choisir ?**
                * Utilisez un **Reset CSS** si vous voulez avoir un contrôle absolu sur chaque pixel de votre design et que vous êtes prêt à styliser chaque élément de base.
                * Utilisez **Normalize.css** si vous préférez une approche plus douce qui corrige simplement les incohérences, tout en laissant les styles sémantiques par défaut des navigateurs intacts. C'est le choix le plus courant aujourd'hui.
                * Beaucoup de frameworks CSS (comme Bootstrap) ou de starters de projets incluent déjà leur propre forme de normalisation ou de reset intégré.
                """
            },
        }

        # Sidebar Frame - Maintenant un CTkScrollableFrame
        self.sidebar_frame = ctk.CTkScrollableFrame(self, width=320, corner_radius=0) # Remplacé par CTkScrollableFrame
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # Pas besoin de grid_rowconfigure ici, CTkScrollableFrame gère le scroll de ses enfants

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Syntaxe CSS", font=ctk.CTkFont(size=28, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20, sticky="ew") # Ajout de sticky="ew" pour centrer le texte

        # Buttons for each section
        self.section_buttons = []
        for i, section_name in enumerate(self.css_sections.keys()):
            button = ctk.CTkButton(self.sidebar_frame, text=section_name,
                                   command=lambda name=section_name: self.show_section(name),
                                   fg_color=("gray70", "gray25"),
                                   hover_color=("gray60", "gray35"),
                                   anchor="w", # Align text to the left
                                   height=40, # Plus de hauteur pour les boutons
                                   font=ctk.CTkFont(size=16)) # Police des boutons
            button.grid(row=i + 1, column=0, padx=20, pady=8, sticky="ew") # Plus de padding
            self.section_buttons.append(button)

        # Main content Frame
        self.main_content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_content_frame.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
        self.main_content_frame.grid_columnconfigure(0, weight=1)
        self.main_content_frame.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self.main_content_frame, text="", font=ctk.CTkFont(size=32, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 30), sticky="ew")

        self.text_area = ctk.CTkTextbox(self.main_content_frame, wrap="word", width=950, height=750, font=("Segoe UI", 16),
                                        activate_scrollbars=True)
        self.text_area.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.text_area.configure(state="disabled")

        # Initial display
        self.show_section("Introduction")

    def show_section(self, section_name):
        section_data = self.css_sections.get(section_name)
        if section_data:
            self.title_label.configure(text=section_data["title"])
            self.text_area.configure(state="normal")
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", section_data["text"])
            self.text_area.configure(state="disabled")
            self.text_area.see("1.0") # Scroll to top

            # Highlight the active button
            for btn in self.section_buttons:
                if btn.cget("text") == section_name:
                    btn.configure(fg_color=("gray60", "gray40"))
                else:
                    btn.configure(fg_color=("gray70", "gray25"))

if __name__ == "__main__":
    app = CSSSyntaxExplainer()
    app.mainloop()