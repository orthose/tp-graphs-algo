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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "7353387e4e7a4be9f28262b6dc796ef2", "grade": false, "grade_id": "cell-1d836c2f9268f0e1", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Rapport de TP

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "335cf30a3f0c73c7f1b839bca0ce7d99", "grade": true, "grade_id": "cell-892ec4c17e615b9b", "locked": false, "points": 2, "schema_version": 3, "solution": true, "task": false}}

Dans ce TP j'ai appris ce qu'est un flot sur un réseau. J'ai également implémenté l'algorithme de Ford-Fulkerson afin de déterminer le flot maximal.

Je rencontre quelques difficultés sur la fin du TP pour la partie VelosChallenge. J'attends de l'aide via e-campus pour voir si ce ne serait pas dû à une mauvaise compréhension de l'énoncé ou bien si c'est un bogue d'implémentation de ma part.

J'ai beaucoup aimé impléménté l'algorithme de Ford-Fulkerson qui au final est assez simple. Par contre mon implémentation fonctionnelle prend le risque de planter par débordement de pile comme je fais de la récursion non-terminale.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "a93912d16e8611171d15164656e04157", "grade": false, "grade_id": "cell-f00c118da0fb33b6", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Qualité du code

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "21a0235278409ed36aab11b28f06e923", "grade": false, "grade_id": "cell-5d42db0fdaf62572", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vérification de syntaxe et de style:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 45348ea9ff7f83843c019269d821adc2
  grade: true
  grade_id: cell-e5e7a8b97e5fb0fe
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
from utils import code_checker
code_checker("flake8")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "be450f5b2921b1a6f4491493d4c33fbf", "grade": false, "grade_id": "cell-c45ae33a6e876c00", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vérification statique de types:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b2beb36f737be90539ba0206a8d3e94a
  grade: true
  grade_id: cell-c9f65f41df4f145b
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
code_checker("mypy .")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2607746ae9fd58ab25ac85f9a1b0ef57", "grade": false, "grade_id": "cell-dc7cfd25d520b9d7", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Tests unitaires:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 58c0c6668afc1a433a61fec55a5e247b
  grade: true
  grade_id: cell-6fb4d07f94265690
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
code_checker("pytest --junit-xml=feedback/pytest.xml")
```

```{code-cell} ipython3

```
