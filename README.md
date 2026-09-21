# README — Intégration Markdown → HTML

## But du projet
Intégrer plusieurs fonctionnalités développées séparément par l'équipe pour convertir un fichier Markdown en un document HTML complet et enrichi : diapositives, couleurs, checklist, table des matières automatique, arbre de fichiers, et texte centré.

## Équipe et fonctionnalités intégrées

| Personne | Fonction(s) | Description |
|---|---|---|
| **Antoine** | `ajouter_style` | Applique une couleur de texte et/ou de fond via `{{couleur\|texte}}` |
| **Amé** | `checklistMD` | Transforme les lignes `///` en cases à cocher HTML |
| **Bruno** | `convertir_diapositive` | Découpe le texte en diapositives (`Slide::`), les convertit en HTML et écrit le fichier final |
| **Jay** | `CenterText` | Centre le contenu entre deux `()` avec `<div align="center">` |
| **Nico** | `creer_table_matiere` | Remplace `**contenu:**` par une table des matières générée depuis les titres Markdown |
| **Zach** | `build_tree`, `build_html`, `render_tree_block`,(`!!`)| Génère un arbre de fichiers HTML à partir d'un dossier |

## Fichiers
- `MD_integration.md` — Fichier Markdown source
- `HTML_integration.html` — Fichier HTML généré en sortie

## Pipeline d'intégration
La fonction `generer_html_depuis_markdown` exécute toutes les fonctionnalités dans l'ordre suivant :

1. Lecture du fichier Markdown source
2. Génération de la table des matières (Nico)
3. Insertion des arbres de fichiers (Zach)
4. Conversion des checklists (Amé)
5. Centrage du texte (Jay)
6. Découpage en diapositives, application des couleurs et génération du HTML final (Bruno + Antoine)

## Utilisation
1. Placer le contenu Markdown dans `MD_integration.md`.
2. Exécuter `generer_html_depuis_markdown()`.
3. Le résultat est généré dans `HTML_integration.html`.

## Dépendances
- `mistletoe`
- `re` (module standard Python)
- `pathlib` (module standard Python)
