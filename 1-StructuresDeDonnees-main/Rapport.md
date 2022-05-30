---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"deletable": false, "editable": false, "nbgrader": {"checksum": "7353387e4e7a4be9f28262b6dc796ef2", "grade": false, "grade_id": "cell-1d836c2f9268f0e1", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Rapport de TP

+++ {"deletable": false, "nbgrader": {"checksum": "76a3d66531cf42624019179581056ca0", "grade": false, "grade_id": "cell-892ec4c17e615b9b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

L'objectif du rapport de TP est de donner une synthèse du travail
réalisé. Pour cette séance, cette synthèse peut-être réalisée quasi
automatiquement avec les outils de vérification de code combinés avec
ce que vous avez déjà rédigé dans la documentation des méthodes. Vous
n'avez donc que quelques mots à écrire ci-dessous.

## En quelques mots, qu'avez-vous appris?
Les différentes façons de représenter un graphe et les fonctions utiles sur les graphes.

## Quelles difficultés avez vous éventuellement rencontrées?
Trouver le meilleur compromis pour garder un code lisible mais juste.

## Qu'avez vous aimé ou moins aimé dans ce TP?
J'ai apprécié la mise en place des tests unitaires automatiques et la vérification du typage et de l'esthétique du code. Cela permet de s'assurer que le travail rendu répond bien au problème. L'environnement de travail prêt à l'emploi avec la gestion simplifiée de git (course.py) ajoute vraiment de la qualité au TP.

## Notes et commentaires libres
Finalement je n'ai pas utilisé l'attribut _node_indices dans le classe Graph.

+++ {"deletable": false, "editable": false, "nbgrader": {"checksum": "a93912d16e8611171d15164656e04157", "grade": false, "grade_id": "cell-f00c118da0fb33b6", "locked": true, "points": 4, "schema_version": 3, "solution": false, "task": true}}

## Qualité du code

+++ {"deletable": false, "editable": false, "nbgrader": {"checksum": "21a0235278409ed36aab11b28f06e923", "grade": false, "grade_id": "cell-5d42db0fdaf62572", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vérification de syntaxe et de style:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  checksum: 8689bdef79131a0abb084725accde01a
  grade: false
  grade_id: cell-e5e7a8b97e5fb0fe
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from utils import code_checker
code_checker("flake8")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"checksum": "be450f5b2921b1a6f4491493d4c33fbf", "grade": false, "grade_id": "cell-c45ae33a6e876c00", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vérification statique de types:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  checksum: 26415b10e407c1d2c910eaac1c869d4f
  grade: false
  grade_id: cell-c9f65f41df4f145b
  locked: true
  schema_version: 3
  solution: false
  task: false
---
code_checker("mypy .")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"checksum": "2607746ae9fd58ab25ac85f9a1b0ef57", "grade": false, "grade_id": "cell-dc7cfd25d520b9d7", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Tests unitaires:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  checksum: 8aadabae860b92433b57a81bec1297f6
  grade: false
  grade_id: cell-6fb4d07f94265690
  locked: true
  schema_version: 3
  solution: false
  task: false
---
code_checker("pytest --junit-xml=feedback/pytest.xml")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"checksum": "b1be9f2551f51bff30f988df8e886587", "grade": false, "grade_id": "cell-e24ca78e8b1b2c8b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Code et complexité

Cette section sera plus développée dans le TP suivant.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  checksum: 916c4a1558dbd118b9ef995f5ee7591e
  grade: false
  grade_id: cell-1c9b3a5e0d64360c
  locked: true
  schema_version: 3
  solution: false
  task: false
---
import inspect
from graph import Graph
```

+++ {"deletable": false, "editable": false, "nbgrader": {"checksum": "fadab08dff7dda8bdd27775ec9c8b6ae", "grade": false, "grade_id": "cell-69687d1f6ff2d2cf", "locked": true, "points": 2, "schema_version": 3, "solution": false, "task": true}}

Code et complexité de `number_of_edges`:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  checksum: bde37976a7cd399338d613669a6eb6e0
  grade: false
  grade_id: cell-7f9eaeca83d5712d
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from utils import show_source
show_source(Graph.number_of_edges)
```

```{code-cell} ipython3

```
