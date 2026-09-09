# Guide utilisateur

## 1. Fonctionnement

La macro(Slide::) permet de convertir un fichier Markdown (`.md`) en fichier HTML (`.html`).

Chaque diapositive doit être séparée avec :


Slide::


Exemple :

blablabla
Slide::

# Titre

Texte de la diapositive.

Slide::

# Deuxième diapositive

Autre contenu.


## 2. Utilisation

Le fichier Markdown et le programme Python doivent être dans le même dossier.

À la fin du programme python, modifier :


convertir_diapositive("TEST1.md", "TESTHTML.html")
pour les fichier que vous allé utiliser 


Le premier fichier est le **fichier Markdown à convertir** et le deuxième est le **fichier HTML créé**.

Ensuite, exécuter le programme : **fonction diapo.py**

Le fichier HTML sera automatiquement créé.

## 3. Mise en forme

La macro supporte les principales fonctionnalités Markdown, comme :

* Les titres
* Le texte en gras
* Le texte en italique
* Les listes
* Les images

L'apparence des diapositives peut être modifiée dans la partie CSS du programme, notamment la couleur, la largeur et la hauteur.
