Intégration Markdown → HTML — Résumé des fonctionnalités

But : Convertir un fichier Markdown en présentation HTML avec diapositives, en ajoutant plusieurs fonctionnalités personnalisées (couleurs, checklist, table des matières, arbre de fichiers, texte centré).

Fonctions par personne
Antoine — ajouter_style
Applique une couleur de texte et/ou de fond à un passage de texte via la syntaxe {{couleur|texte}}.
Amé — checklistMD
Transforme les lignes commençant par /// en cases à cocher HTML (<input type="checkbox">).
Bruno — convertir_diapositive
Découpe le texte en diapositives (Slide::), convertit chacune en HTML, applique les couleurs, et génère le fichier HTML final avec le CSS.
Jay — CenterText
Remplace des paires de () par des balises <div align="center"> pour centrer le contenu entre elles.
Nico — creer_table_matiere
Détecte le marqueur **contenu:** et le remplace par une table des matières générée automatiquement à partir des titres Markdown (## à ######).
Zach — build_tree, build_html, render_tree_block
Explore un dossier jusqu'à une certaine profondeur, construit une structure de données représentant l'arborescence des fichiers, puis la convertit en HTML sous forme de liste imbriquée.
