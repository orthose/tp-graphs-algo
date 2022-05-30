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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "238a6d90febe7cbce47ac0b6607be8dd", "grade": false, "grade_id": "cell-7d6651504215e0ca", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Bibliothèque de graphes

Vous retrouverez dans <a href="graph.py">graph.py</a> le squelette de la classe
`Graph` que vous avez implanté la séance dernière. Remplacez-le par
votre implantation, puis vérifiez que tout fonctionne:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 32376a32a898fc5daf418c095603b6fa
  grade: false
  grade_id: cell-dc4476c6cd597199
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from graph import Graph, examples
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 7eaa4c147ddef1e9deae1f19740724de
  grade: true
  grade_id: cell-1dd035627b5d7b54
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
G = Graph([1,2,3], edges=[(1,2,"12"),(2,3,"23")])
```

```{code-cell} ipython3
import graph
import importlib
importlib.reload(graph)
G.edges()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 4f87e98eec3b26f5c0e005b56ef7f5a6
  grade: true
  grade_id: cell-f32bdde5da338aed
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert G.edges() == ((1, 2, '12'), (2, 1, '12'), (2, 3, '23'), (3, 2, '23'))
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d54fc39aaa557469524100c26963ad60
  grade: true
  grade_id: cell-50e1b14caae52140
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
G.show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 27e03a198c29be287e56ac7948e7af62
  grade: true
  grade_id: cell-d181f9b9b27b9a76
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
G = examples.cours_1_G()
G.edges()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 5fc062585b0f4322546e1c4fd7110a98
  grade: true
  grade_id: cell-120e2364a899a12b
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert G.number_of_nodes() == 6
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "705fb1637d5a94e9199195fa2b8dd6fc", "grade": false, "grade_id": "cell-27c1b6c455cc76fd", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Maintenant, lancez tous les tests inclus dans la documentation des fonctions:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 8dd58594ae55660bbf0d0f31e02a0f33
  grade: true
  grade_id: cell-78ca9cf736b9443b
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
from utils import code_checker
code_checker("pytest graph.py")
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 0219aae1959652b92352eba1ae316297
  grade: true
  grade_id: cell-1444090852174558
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
code_checker("flake8")
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 35bba24dad84c523d893740aee322612
  grade: true
  grade_id: cell-24b059fcc5ffdb20
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
code_checker("mypy graph.py")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "7d672101e428165cfc2bf9f3cb9af987", "grade": false, "grade_id": "cell-c10fd3d6ead480f0", "locked": true, "points": 4, "schema_version": 3, "solution": false, "task": true}}

Évaluation de l'implantation des méthodes et de la complexité

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 242b5289d771abc43f990db4797688d5
  grade: false
  grade_id: cell-6984b89d96fc0127
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from utils import show_source
show_source(Graph.successors)
show_source(Graph.predecessors)
show_source(Graph.capacity)
show_source(Graph.is_path)
```

```{code-cell} ipython3

```
