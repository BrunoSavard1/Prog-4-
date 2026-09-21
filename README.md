Tache : Diapositive
Scrum master Antoine Bernier
Programmeur Bruno Savard

Description

Convertit un texte Markdown en une présentation HTML sous forme de diapositives, puis l'enregistre dans un fichier.

Fonctionnement
Découpe le texte en diapositives à l'aide du séparateur Slide::.
Convertit chaque diapositive de Markdown vers HTML (via mistletoe).
Enveloppe chaque diapositive dans une <div class="slide">.
Écrit le CSS (styles .slide et .file-tree) et le HTML final dans le fichier de sortie.
Utilisation
python
convertir_diapositive(texte, "sortie.html")
Paramètres
Paramètre	Type	Description
texte	str	Contenu Markdown à convertir (avec séparateurs Slide::)
fichier_html	str	Chemin du fichier HTML à créer/écraser
Sortie

Aucune valeur retournée — écrit directement le fichier HTML.
