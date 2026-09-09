
Scrum master Antoine Bernier
Programmeur Bruno Savard

# Macro Markdown vers HTML

Cette macro permet de convertir un fichier **Markdown (`.md`)** en fichier **HTML (`.html`)** contenant plusieurs diapositives.

## Installation

La bibliothèque `mistletoe` est nécessaire :


pip install mistletoe


## Utilisation

Chaque diapositive doit être séparée avec :

text
Slide::


Exemple :

Bonjours blablabla
Slide::

# Première diapositive

Mon contenu.

Slide::

# Deuxième diapositive

Autre contenu.


Pour choisir les fichiers utilisés, modifier la dernière ligne du programme :


convertir_diapositive("TEST1.md", "TESTHTML.html")


Le premier fichier est le fichier Markdown à lire et le deuxième est le fichier HTML qui sera créé.

## Exécution

Lancer le programme avec :


python fonction diapo.py


Le fichier HTML sera ensuite créé automatiquement.

## Fonctionnalités

La macro permet notamment d'utiliser :

* Les titres
* Le gras et l'italique
* Les listes
* Les images
* Plusieurs diapositives dans un même fichier

La couleur et la taille des diapositives peuvent être modifiées directement dans le CSS du programme.
