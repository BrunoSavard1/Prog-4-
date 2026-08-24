import mistletoe
import html


with open('Diapositive.md', 'r', encoding='utf-8') as contenu:
    Texte = contenu.read()

    slides = Texte.split("Slide::")
    print(slides)

resultat = ""

for slide in slides:
    rendu = mistletoe.markdown(slide)

    slide_html = '<div style="width:100vw; height:80vh;">' + rendu + '</div>'

    resultat += slide_html
    

with open('Slide.html', 'w') as fout:
    fout.write(resultat)



#### mettre la page dans une autre couleur pour voir si la séparation c vrm fais 