
import mistletoe
import re


# Antoine

def ajouter_style(match):

    style = match.group(1)
    texte = match.group(2)

    couleur_texte = ""
    couleur_fond = ""

    if ",=" in style:
        couleur_texte, couleur_fond = style.split(",=", 1)

    elif style.startswith("="):
        couleur_fond = style[1:]

    else:
        couleur_texte = style

    style_html = ""

    if couleur_texte:
        style_html += f"color: {couleur_texte}; "

    if couleur_fond:
        style_html += f"background-color: {couleur_fond}; "

    return f'<span style="{style_html}">{texte}</span>'


# Amé

def checklistMD(nomFichier):

    modifiedLines = []

    with open(nomFichier + '.md', 'r', encoding='utf-8') as markdownFile:

        readFile = markdownFile.readlines()

        for line in readFile:

            modifiedLine = []

            if line.startswith('///'):

                for letter in line[3:]:
                    modifiedLine.append(letter)

                modifiedLine.insert(0, '<input type="checkbox"> <label>')

                if line.endswith('\n'):
                    modifiedLine[-1] = '</label><br>\n'
                else:
                    modifiedLine.append('</label><br>\n')

                # Cette ligne doit être ici
                modifiedLines.append("".join(modifiedLine))

            else:
                modifiedLines.append(line)

    return "".join(modifiedLines)

# Bruno

def convertir_diapositive(texte, fichier_html):

    slides = texte.split("Slide::")

    css = """
    <style>
        .slide {
            background-color: rgb(200, 184, 189);
            width: 100vw;
            height: 70vh;
        }
    </style>
    """

    resultat = ""

    for slide in slides:

        rendu = mistletoe.markdown(slide)

        # Antoine : couleurs
        rendu = re.sub(r"\{\{([^|]+)\|(.+?)\}\}", ajouter_style, rendu)

        slide_html = '<div class="slide">' + rendu + '</div>'

        resultat += slide_html

    with open(fichier_html, 'w', encoding='utf-8') as fout:
        fout.write(css + resultat)


# Programme principal

texte = checklistMD("MD_integration")

convertir_diapositive(
    texte,
    "HTML_integration.html"
)