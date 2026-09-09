import mistletoe


def convertir_diapositive(fichier_md, fichier_html):
    """
    Convertit un fichier Markdown contenant des 'Slide::'
    en un fichier HTML contenant une div par diapositive.
    """

     # Ouvre le fichier Markdown en mode lecture
    with open(fichier_md, 'r', encoding='utf-8') as contenu:
         # Lit tout le contenu du fichier et le stock dans une variable
        texte = contenu.read()

    # Séparer les diapositives à chaque 'Slide::'
    slides = texte.split("Slide::")

    # CSS des diapositives, gestion de la couleur et de la taille de la diapositive
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

        # Place le contenu HTML dans une div ayant la classe "slide"
        slide_html = '<div class="slide">' + rendu + '</div>'

        # Ajoute la diapositive au résultat final
        resultat += slide_html

    # Écrire le résultat dans le fichier HTML
    with open(fichier_html, 'w', encoding='utf-8') as fout:
        # Écrit le CSS et toutes les diapositives dans le fichier HTML
        fout.write(css + resultat)

# Appelle la fonction avec le fichier Markdown en entrée
# et le fichier HTML qui sera créé en sortie
convertir_diapositive("Diapositive.md", "Slide.html")
