import mistletoe
import re
from pathlib import Path
from textwrap import dedent
from mistletoe.block_token import Heading


# Raccourci utilisé pour déclencher le style personnalisé dans le markdown
SHORTCUT = "!!"
# Fichier markdown source à lire
FILE = "MD_integration.md"
# Fichier HTML de sortie généré
OUTPUT_FILE = "HTML_integration.html"

# Antoine
def ajouter_style(match):
    # Récupère le groupe correspondant au style (ex: couleur texte / fond)
    style = match.group(1)
    # Récupère le texte auquel le style doit être appliqué
    texte = match.group(2)

    # Initialisation des couleurs (texte et fond) à vide par défaut
    couleur_texte = ""
    couleur_fond = ""

    # Cas où le style définit à la fois une couleur de texte et une couleur de fond
    # Format attendu : "couleur_texte,=couleur_fond"
    if ",=" in style:
        couleur_texte, couleur_fond = style.split(",=", 1)

    # Cas où seule une couleur de fond est définie
    # Format attendu : "=couleur_fond"
    elif style.startswith("="):
        couleur_fond = style[1:]

    # Cas où seule une couleur de texte est définie
    else:
        couleur_texte = style

    # Construction de la chaîne de style CSS inline
    style_html = ""

    # Ajoute la couleur du texte si elle est définie
    if couleur_texte:
        style_html += f"color: {couleur_texte}; "

    # Ajoute la couleur de fond si elle est définie
    if couleur_fond:
        style_html += f"background-color: {couleur_fond}; "

    # Retourne le texte enveloppé dans un span avec le style appliqué
    return f'<span style="{style_html}">{texte}</span>'

# Amé
def checklistMD(nomFichier):

    # Liste qui contiendra toutes les lignes (modifiées ou non) du fichier
    modifiedLines = []

    # Ouverture du fichier markdown en lecture
    with open(nomFichier + '.md', 'r', encoding='utf-8') as markdownFile:

        # Lecture de toutes les lignes du fichier
        readFile = markdownFile.readlines()

        for line in readFile:

            # Liste temporaire des caractères/éléments pour construire la ligne modifiée
            modifiedLine = []

            # Vérifie si la ligne est une ligne de checklist (commence par '///')
            if  line.startswith('///'):

                # Parcourt chaque caractère de la ligne après les 3 premiers caractères ('///')
                for letter in line[3:]:
                    modifiedLine.append(letter)

                # Insère la balise HTML de la checkbox et le label au début de la ligne
                modifiedLine.insert(0, '<input type="checkbox"> <label>')

                # Si la ligne se termine par un saut de ligne, remplace le dernier élément
                # par la fermeture du label suivie du saut de ligne
                if line.endswith('\n'):
                    modifiedLine[-1] = '</label><br>\n'
                else:
                    # Sinon, ajoute simplement la fermeture du label à la fin
                    modifiedLine.append('</label><br>\n')

                # Cette ligne doit être ici
                # Reconstitue la ligne complète et l'ajoute à la liste des lignes modifiées
                modifiedLines.append("".join(modifiedLine))

            else:
                # Ligne normale (pas de checklist) : ajoutée telle quelle
                modifiedLines.append(line)

    # Retourne le contenu complet reconstitué sous forme de chaîne unique
    return "".join(modifiedLines)

# Bruno

def convertir_diapositive(texte, fichier_html):

    # Découpe le texte en diapositives à partir du séparateur "Slide::"
    slides = texte.split("Slide::")
    # Chaîne qui accumulera le HTML final de toutes les diapositives
    resultat = ""

    # Feuille de style CSS appliquée aux diapositives et à l'arborescence de fichiers



    # Parcourt chaque diapositive extraite du texte
    for slide in slides:

        # Convertit le contenu markdown de la diapositive en HTML
        rendu = mistletoe.markdown(slide)

        # Antoine : couleurs
        # Applique le style personnalisé (couleurs) via la fonction ajouter_style
        rendu = re.sub(r"\{\{([^|]+)\|(.+?)\}\}", ajouter_style, rendu)

        # Enveloppe le rendu HTML de la diapositive dans une div avec la classe "slide"
        slide_html = '<div class="slide">' + rendu + '</div>'

        # Ajoute la diapositive au résultat final
        resultat += slide_html

    css = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <link href="style.css" rel="stylesheet"/>
    </head>
    <body>
        {resultat}
    </body>
    </html>
    """

    # Écrit le CSS et le résultat final dans le fichier HTML de sortie
    with open(fichier_html, 'w', encoding='utf-8') as fout:
        fout.write(css)


#jay
def CenterText(md_content):
    found = False  # Variable pour savoir si on est dans une zone centrée

    # Découpe le contenu markdown en une liste de lignes
    lines = md_content.splitlines('\n')

    modified_lines = []  # Garde les lignes après modification

    # Parcourt chaque ligne du contenu
    for Symbol in lines:
        Shortcut = '()'  # Recherche du motif à remplacer

        # Si le motif est trouvé et qu'on n'est pas encore dans une zone centrée
        # -> on ouvre la zone centrée
        if Symbol.find(Shortcut) != -1 and (found == False):
            Symbol = Symbol.replace(Shortcut,'<div align="center">\n',1)
            found = True  # On est maintenant dans une zone centrée

        # Si le motif est trouvé et qu'on est déjà dans une zone centrée
        # -> on ferme la zone centrée
        elif Symbol.find(Shortcut) != -1 and (found == True):
            Symbol = Symbol.replace(Shortcut,'</div>\n',1)
            found = False  # On sort de la zone centrée

        modified_lines.append(Symbol)  # Ajoute la ligne modifiée

    return '\n'.join(modified_lines)  # Retourne le texte complet


#Nico
def creer_table_matiere(texte):

    # Vérifier si le marqueur existe
    if "**contenu:**" not in texte.lower():
        print("Aucun **contenu:** détecté.")
        return texte

    print("**contenu:** détecté.")

    # Initialise la table des matières avec son titre en markdown
    tableMatieres = "## Table des matières\n\n"

    # Parser le document
    document = mistletoe.Document(texte)

    # Parcourt les éléments de premier niveau du document markdown
    for titreMarkdown in document.children:
        # Ne traite que les éléments qui sont des titres (Heading)
        if isinstance(titreMarkdown, Heading):

            # Les titres ## à ###### sont ajoutés à la table
            if titreMarkdown.level >= 2:

                # Chaîne qui accumulera le texte complet du titre
                texteTitre = ""

                # Reconstruit le texte du titre à partir de ses sous-éléments
                for partieTitre in titreMarkdown.children:
                    if hasattr(partieTitre, "content"):
                        texteTitre += partieTitre.content

                # Crée le lien d'ancre en remplaçant les espaces par des tirets
                lienTitre = texteTitre.lower().replace(" ", "-")

                # Ajouter le titre dans la table
                # L'indentation dépend du niveau du titre (##, ###, ####, etc.)
                if titreMarkdown.level == 2:
                    tableMatieres += f"- [{texteTitre}](#{lienTitre})\n"

                elif titreMarkdown.level == 3:
                    tableMatieres += f"  - [{texteTitre}](#{lienTitre})\n"

                elif titreMarkdown.level == 4:
                    tableMatieres += f"    - [{texteTitre}](#{lienTitre})\n"

                elif titreMarkdown.level == 5:
                    tableMatieres += f"      - [{texteTitre}](#{lienTitre})\n"

                elif titreMarkdown.level == 6:
                    tableMatieres += f"        - [{texteTitre}](#{lienTitre})\n"

    # Remplacer **contenu:** par la table des matières
    New_texte = texte.replace("**contenu:**", tableMatieres, 1)

    return New_texte

# Zach
def build_tree(path: str, max_depth, current_depth=1) -> dict | list | str:
    """
    Reads a folder and builds a tree consisting of all the files at a certain depth.
    """

    # S'assure que max_depth est bien un entier
    max_depth = int(max_depth)

    # Cas particulier : si le chemin correspond au motif générique, on le remplace par un chemin vide
    if path in [r'**\\**', r'**\\**'[0]]:
        path = r''

    # Convertit la chaîne de chemin en objet Path
    path = Path(path)

    # Si le chemin pointe directement vers un fichier, retourne simplement son nom
    if path.is_file():
        return path.name

    # Si on a atteint la profondeur maximale, retourne uniquement la liste des noms
    # des fichiers/dossiers à ce niveau (en ignorant les fichiers cachés)
    if current_depth == max_depth:
        return [f.name for f in path.iterdir() if not f.name.startswith('.')]

    # Dictionnaire qui représentera l'arborescence à ce niveau
    tree = {}

    # Parcourt chaque élément (fichier ou dossier) du chemin courant
    for item in path.iterdir():
        # Ignore les fichiers/dossiers cachés
        if item.name.startswith('.'):
            continue

        if item.is_dir():
            # Appel récursif pour construire l'arborescence des sous-dossiers
            tree[item.name] = build_tree(item, max_depth, current_depth + 1)
        else:
            # Pour un fichier, on stocke simplement son nom
            tree[item.name] = item.name

    return tree


def build_html(tree: dict | list | str) -> str:
    """
    Builds the html tree fragments
    """

    # Chaîne HTML accumulée qui sera retournée
    html = ''

    # Cas où l'arbre est une liste de fichiers (niveau de profondeur maximale atteint)
    if isinstance(tree, list):
        for item in tree:
            html += f'<li><span class="file">{item}</span></li>'

    # Cas où l'arbre est directement une chaîne (un seul fichier)
    elif isinstance(tree, str):
        html += f'<li><span class="file">{tree}</span></li>'

    # Cas où l'arbre est un dictionnaire (dossier contenant fichiers et/ou sous-dossiers)
    elif isinstance(tree, dict):
        for folder_name, content in tree.items():

            # Contenu = liste de fichiers -> sous-dossier avec ses fichiers
            if isinstance(content, list):
                html += f'<li><span class="folder">{folder_name}</span><ul>'
                html += build_html(content)
                html += '</ul></li>'

            # Contenu = chaîne -> simple fichier
            elif isinstance(content, str):
                html += f'<li><span class="file">{content}</span></li>'

            # Contenu = dictionnaire -> sous-dossier avec sa propre arborescence
            elif isinstance(content, dict):
                html += f'<li><span class="folder">{folder_name}</span><ul>'
                html += build_html(content)
                html += '</ul></li>'

    return html


def render_tree_block(tree_dict):
    """
    Génère uniquement le bloc conteneur de l'arbre
    """

    # Construit le fragment HTML représentant l'arborescence
    corps_arbre = build_html(tree_dict)

    # Enveloppe le tout dans une div conteneur avec une liste HTML
    return f'<div class="file-tree"><ul>{corps_arbre}</ul></div>'





#Will
# Creation d'un gabarit HTML pour le rendu final
PAGE_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
<style>
</style>
</head>
<body>
{body}
</body>
</html>
"""

# Liste des propriétés CSS valides reconnues
# Pour faire un check des propriétés CSS, on peut utiliser cette liste pour valider les entrées de l'utilisateur
VALID_CSS_PROPERTIES = {
    "align-content", "align-items", "align-self", "all", "animation",
    "animation-delay", "animation-direction", "animation-duration",
    "animation-fill-mode", "animation-iteration-count", "animation-name",
    "animation-play-state", "animation-timing-function", "backdrop-filter",
    "background", "background-attachment", "background-blend-mode",
    "background-clip", "background-color", "background-image",
    "background-origin", "background-position", "background-repeat",
    "background-size", "border", "border-bottom", "border-bottom-color",
    "border-bottom-left-radius", "border-bottom-right-radius",
    "border-bottom-style", "border-bottom-width", "border-collapse",
    "border-color", "border-image", "border-left", "border-left-color",
    "border-left-style", "border-left-width", "border-radius",
    "border-right", "border-right-color", "border-right-style",
    "border-right-width", "border-spacing", "border-style", "border-top",
    "border-top-color", "border-top-left-radius", "border-top-right-radius",
    "border-top-style", "border-top-width", "border-width", "bottom",
    "box-shadow", "box-sizing", "caption-side", "caret-color", "clear",
    "clip", "clip-path", "color", "column-count", "column-gap",
    "column-rule", "column-width", "columns", "content", "cursor",
    "direction", "display", "filter", "flex", "flex-basis",
    "flex-direction", "flex-flow", "flex-grow", "flex-shrink", "flex-wrap",
    "float", "font", "font-family", "font-size", "font-style",
    "font-variant", "font-weight", "gap", "grid", "grid-area",
    "grid-column", "grid-column-end", "grid-column-start", "grid-gap",
    "grid-row", "grid-row-end", "grid-row-start", "grid-template",
    "grid-template-areas", "grid-template-columns", "grid-template-rows",
    "height", "inset", "justify-content", "justify-items", "justify-self",
    "left", "letter-spacing", "line-height", "list-style",
    "list-style-image", "list-style-position", "list-style-type", "margin",
    "margin-bottom", "margin-left", "margin-right", "margin-top",
    "max-height", "max-width", "min-height", "min-width", "object-fit",
    "object-position", "opacity", "order", "outline", "outline-color",
    "outline-offset", "outline-style", "outline-width", "overflow",
    "overflow-x", "overflow-y", "padding", "padding-bottom",
    "padding-left", "padding-right", "padding-top", "perspective",
    "pointer-events", "position", "resize", "right", "rotate", "scale",
    "table-layout", "text-align", "text-decoration", "text-indent",
    "text-overflow", "text-shadow", "text-transform", "top", "transform",
    "transform-origin", "transition", "transition-delay",
    "transition-duration", "transition-property",
    "transition-timing-function", "translate", "user-select",
    "vertical-align", "visibility", "white-space", "width", "word-break",
    "word-spacing", "word-wrap", "z-index", "src", "alt", "title"
}

def preprocess(text):
    """
    Trouve les blocs d'image @@@ et les remplace par du HTML.

    Syntaxe:

        @@@
        src: ocean.jpg
        width: 300
        height: 300
        margin-left: 50px
        margin-top: 20px
        border-radius: 10px
        @@@

    Chaque ligne est une propriété sous la forme:

        propriété: valeur
    """

    # Analyse le texte ligne par ligne
    lines = text.splitlines()
    output = []

    i = 0

    while i < len(lines):

        # Cherche le début d'un bloc @@@
        # Une fois trouvé, on cherche le prochain @@@ pour marquer la fin du bloc 
        if lines[i].strip() == "@@@":

            # Recherche le prochain @@@ qui marque la fin du bloc
            j = i + 1

            while j < len(lines) and lines[j].strip() != "@@@":
                j += 1

            # Aucun @@@ de fermeture trouvé
            if j >= len(lines):
                raise ValueError(
                    f"@@@ Invalide a la ligne {i + 1}: "
                    "@@@ de fermeture attendue."
                )

            # Dictionnaire contenant les propriétés de l'image
            properties = {}

            # Analyse chaque ligne du bloc
            for line in lines[i + 1:j]:

                # Ignore les lignes vides
                line = line.strip()

                if not line:
                    continue

                # Vérifie que la ligne contient ":"
                if ":" not in line:
                    raise ValueError(
                        f"Propriétés invalide dans le bloc @@@: {line}"
                    )

                # Sépare la propriété et sa valeur
                # On détermine la clé et la valeur en utilisant le premier ":" trouvé comme séparateur
                key, value = line.split(":", 1)

                # Nettoie les espaces
                key = key.strip()
                value = value.strip()

                if key == "alt":
                    alt_description = value
                    print("alt detected")
                    continue

                if key == "title":
                    title_description = value
                    print("title detected")
                    continue

                # Vérifie que la clé est une propriété CSS valide
                if key not in VALID_CSS_PROPERTIES:
                    raise ValueError(
                        f"Propriété CSS inconnu dans le bloc @@@ "
                        f"a la ligne {i + 1}: '{key}'"
                    )

                # Ajoute la propriété au dictionnaire
                """
                Cela ressemble a:
                {
                    "width": "300px"
                }
                """
                properties[key] = value

            # L'attribut src est obligatoire (ofc lol)
            if "src" not in properties:
                raise ValueError(
                    f"@@@ Invalide a la ligne {i + 1}: "
                    "'src' manquant."
                )

            # Récupère le chemin de l'image
            src = properties.pop("src")

            # Construction des attributs CSS
            css_properties = []

            # Transforme les propriétés en attributs CSS
            for key, value in properties.items():
                css_properties.append(f"{key}: {value}")

            # Transforme les propriétés CSS en une seule chaîne
            style = "; ".join(css_properties)

            # Génère le HTML de l'image
            html = f'<img src="{src}"'

            if style:
                html += f' style="{style};"'

            if alt_description:
                html += f' alt="{alt_description}"'

            alt_description = ""  # Reset pour pas leak
            title_description = ""  # Reset pour pas leak

            # Pour fermer la balise img, on ajoute le ">" à la fin
            html += '>'

            # Ajoute le HTML à la sortie
            output.append(html)

            # Saute tout le bloc, y compris les deux @@@
            i = j + 1

        else:
            # Ligne normale de Markdown
            output.append(lines[i])
            i += 1

    # Reconstitue le texte final
    return "\n".join(output)





def generer_html_depuis_markdown():
    """
    Fonction principale qui exécute tout le pipeline de conversion :
    lecture du fichier markdown, application de toutes les transformations
    (table des matières, arbre de fichiers, checklist, texte centré),
    puis génération du fichier HTML final.
    """

    # Lecture du fichier Markdown
    # Ouvre le fichier source(.md) (FILE) en lecture et récupère tout son contenu
    with open(FILE, "r", encoding="utf-8") as fichier:
        texte = fichier.read()

    # Nico : table des matières
    # Cherche le marqueur "**contenu:**" dans le texte et le remplace par
    # une table des matières générée à partir des titres markdown (## à ######)
    texte = creer_table_matiere(texte)

    

    # Zach : arbre de fichiers
    # Découpe le texte en lignes (en conservant les sauts de ligne)
    lignes = texte.splitlines(keepends=True)
    lignesModifiees = []

    # Parcourt chaque ligne du texte
    for ligne in lignes:
        # Si la ligne commence par le raccourci défini (SHORTCUT, ex: "!!")
        # c'est une demande de génération d'arbre de fichiers
        if ligne.startswith(SHORTCUT):
            # Extrait les paramètres après le raccourci (ex: chemin et profondeur)
            parameters = ligne[len(SHORTCUT):].strip().split(' ')
            # Le premier paramètre est le chemin du dossier à explorer
            path = parameters[0]

            # Tente de récupérer la profondeur maximale en 2e paramètre
            # Si absent ou invalide, utilise une profondeur par défaut de 1
            try:
                depth = int(parameters[1])
            except (IndexError, ValueError):
                depth = 1

            # Construit la structure de données de l'arborescence (dict/list/str)
            tree_data = build_tree(path, depth)
            # Convertit cette structure en bloc HTML (div + liste)
            html_tree = render_tree_block(tree_data)

            # Remplace la ligne du raccourci par le HTML généré
            lignesModifiees.append(html_tree + "\n")

        else:
            # Ligne normale : conservée telle quelle
            lignesModifiees.append(ligne)

    # Reconstitue le texte complet avec les arbres de fichiers insérés
    texte = "".join(lignesModifiees)

    # Amé : checklist
    # Découpe à nouveau le texte (mis à jour) en lignes
    lignes = texte.splitlines(keepends=True)
    lignesModifiees = []

    # Parcourt chaque ligne du texte
    for ligne in lignes:
        # Si la ligne commence par "///" -> c'est un élément de checklist
        if ligne.startswith("///"):
            # Récupère le texte de la checklist (après "///", sans espaces superflus)
            texteChecklist = ligne[3:].strip()
            # Remplace la ligne par une checkbox HTML avec son label
            lignesModifiees.append(
                '<input type="checkbox"> <label>' +
                texteChecklist +
                '</label><br>\n'
            )
        else:
            # Ligne normale : conservée telle quelle
            lignesModifiees.append(ligne)

    # Reconstitue le texte complet avec les checklists converties en HTML
    texte = "".join(lignesModifiees)

    # Jay : texte centré
    # Recherche les paires de "()" dans le texte pour ouvrir/fermer
    # des blocs <div align="center"> autour du contenu concerné
    texte = CenterText(texte)

    # Will : image

    texte = preprocess(texte)

    # Création du HTML final
    # Découpe le texte en diapositives ("Slide::"), convertit chacune en HTML,
    # applique les styles de couleur (Antoine), puis écrit le résultat
    # (CSS + diapositives) dans le fichier de sortie OUTPUT_FILE
    convertir_diapositive(texte, OUTPUT_FILE)

generer_html_depuis_markdown()
