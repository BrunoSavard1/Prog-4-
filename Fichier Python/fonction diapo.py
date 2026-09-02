import mistletoe

def convertir_diapositive(fichier_md, fichier_html):
    """
    Convertit un fichier Markdown contenant des 'Slide::'
    en un fichier HTML contenant une div par diapositive.
    """

    # Lire le fichier Markdown
    with open(fichier_md, 'r', encoding='utf-8') as contenu:
        texte = contenu.read()

    # Séparer les diapositives à chaque 'Slide::'
    slides = texte.split("Slide::")

    # CSS des diapositives, gestion de la couleur de la diapositive
    css = """
    <style>
        .slide {
            background-color: rgb(200, 184, 189);
            width: 100vw;
            height: 70vh;
        }
    </style>
    """
    # Variable qui stock le contenu HTML 
    resultat = ""

    # Convertir chaque slide en HTML
    for slide in slides:
        rendu = mistletoe.markdown(slide)

        slide_html = '<div class="slide">' + rendu + '</div>'

        resultat += slide_html

    # Écrire le résultat dans le fichier HTML
    with open(fichier_html, 'w', encoding='utf-8') as fout:
        fout.write(css + resultat)

convertir_diapositive("Diapositive.md", "Slide.html")
