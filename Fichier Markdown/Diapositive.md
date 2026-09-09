# Utilisation de la macro de diapositives

Pour créer plusieurs diapositives dans un fichier Markdown, il faut utiliser le mot-clé `Slide suivi de ::`.

## Créer une nouvelle diapositive

Chaque diapositive doit commencer par :

```
la macro
```

Tout le contenu écrit après `la macro` fera partie de cette diapositive, `jusqu'a la prochaine macro.`

### Exemple

Slide::

# Première diapositive

Ceci est le contenu de ma première diapositive.

Slide::

# Deuxième diapositive

Ceci est le contenu de ma deuxième diapositive.

- Elden Ring 
- HELP

Slide::

# Troisième diapositive

**Fin de la présentation !**
```

La macro va automatiquement transformer chaque section séparée par par la macro en une diapositive HTML.

## Écrire le contenu

À l'intérieur d'une diapositive, il est possible d'utiliser la syntaxe Markdown habituelle :

```
# Titre

## Sous-titre

Texte normal.

**Texte en gras**

*Texte en italique*

- Liste
- Liste
- Liste
```

Il n'est donc pas nécessaire d'utiliser une syntaxe différente pour écrire le contenu des diapositives.

## Important

Le mot-clé doit être écrit exactement comme ceci :


Slide::


Il permet à la macro de savoir où une diapositive se termine et où la suivante commence.

La structure générale du fichier est donc :

```
macro
Contenu de la diapositive 1

macro
Contenu de la diapositive 2

macro
Contenu de la diapositive 3
```
