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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "60b485eec4dad8f8d6ab45f4db91c896", "grade": false, "grade_id": "cell-4ee764f696c369b1", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Implantation de Ford Fulkerson

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "06053ebaeac6a36dc88bf1b67954b192", "grade": false, "grade_id": "cell-d3332ac45ccfcda3", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Recherche de chaîne augmentante

Dans le fichier `flots.py`, implantez les méthodes `find_augmenting_path` et `increase_augmenting_path`. Testez vos fonctions ci-dessous.

**N'oubliez pas de redémarrer le noyau quand vous changez les fichiers importés**

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: f7a22f631d2d6a5a00e3750019b9b0de
  grade: false
  grade_id: cell-385dafe488d81cf2
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
```

```{code-cell} ipython3
F = flow_examples.example1()
F.show()
```

```{code-cell} ipython3
F.find_augmenting_path()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 16a4ad17554976d70a9c4926e6deecb5
  grade: false
  grade_id: cell-46e58d7a49f852d9
  locked: true
  schema_version: 3
  solution: false
  task: false
---
def is_augmenting_path(F, path):
    source = path[0][0]
    if not source == F.source():
        print("Mauvaise source")
        return False
    target = path[-1][1] if path[-1][1] > 0 else path[-1][0]
    if not target == F.target():
        print("Mauvaise cible")
        return False
    for a,b,c in path:
        if c > 0:
            if not F.flow(a,b) + c == F.capacity(a,b):
                print("Mauvais potentiel sur", a,b,c)
                return False
        elif c < 0:
            if not -c == F.flow(a,b):
                print("Mauvais potentiel sur",a,b,c)
                return False
        else:
            print("Potentiel nul sur",a,b,c)
            return False
    return True
```

```{code-cell} ipython3
is_augmenting_path(F, F.find_augmenting_path())
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: e7f9f4c3b8f0d6a277688c871b97cffa
  grade: true
  grade_id: cell-f6d1497d8ef1bec7
  locked: true
  points: 3
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
F = flow_examples.example1()
assert is_augmenting_path(F, F.find_augmenting_path())
F = flow_examples.empty_flow()
assert is_augmenting_path(F, F.find_augmenting_path())
F = flow_examples.small_example()
assert is_augmenting_path(F, F.find_augmenting_path())
F = flow_examples.small_example2()
assert F.find_augmenting_path() is None
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2be9cdbe7ea6c25e95a1ef0a92fb9c87", "grade": false, "grade_id": "cell-02033b087568d879", "locked": true, "points": 2, "schema_version": 3, "solution": false, "task": true}}

Affichage du code pour correction:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a7b3aa4c88fbd30bf3a5c31651fecdf1
  grade: false
  grade_id: cell-3f6b89280458a574
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from utils import show_source
show_source(Flow.find_augmenting_path)
```

```{code-cell} ipython3
F = flow_examples.example1()
F.show()
```

```{code-cell} ipython3
F.increase_augmenting_path([(0, 2, 1), (5, 2, -1), (5, 6, 3)])
F.show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b09e34038230e420ce7990525d37b63b
  grade: true
  grade_id: cell-4966fd3fd7a57d16
  locked: true
  points: 3
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
F = flow_examples.example1()
F.increase_augmenting_path([(0, 2, 1), (5, 2, -1), (5, 6, 3)])
assert F.flow(0,2) == 2
assert F.flow(5,2) == 0
assert F.flow(5,6) == 2
F = flow_examples.empty_flow()
F.increase_augmenting_path(F.find_augmenting_path())
assert F.check_in_out()
assert F.check_capacity()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "161c6384a492b7fb6cd006356d688674", "grade": false, "grade_id": "cell-02033b087568d880", "locked": true, "points": 2, "schema_version": 3, "solution": false, "task": true}}

Affichage du code pour correction:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 41a17f4b3e74ed0926545338b2f7bc53
  grade: false
  grade_id: cell-f20413a1a656940a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from utils import show_source
show_source(Flow.increase_augmenting_path)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "0ff6a8addc60de918f2ae163249e3d4c", "grade": false, "grade_id": "cell-e40d13d14f4eb5da", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Algorithme de Ford-Fulkerson

En utilisant les méthodes précédentes, implantez l'algorithme de Ford-Fulkerson dans le fichier `ford_fulkerson.py`. 

La fonction prend en paramètre un réseau, crée le flot vide corresponant à ce réseau puis applique l'algorithme pour maximiser le flot.

Testez ci-dessous.

**N'oubliez pas de redémarrer le noyau quand vous changez les fichiers importés**

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 97ac4ec15c97f038ad9c557b586f5377
  grade: false
  grade_id: cell-b4fc73add6dcfe22
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
from network import Network
from network import examples
from ford_fulkerson import maximal_flow
```

```{code-cell} ipython3
N = examples.example1()
F = maximal_flow(N,0,6)
```

```{code-cell} ipython3
F.show()
```

```{code-cell} ipython3
F.global_value()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 27d8ccbcd3e1de87f0e5c16c475ecf24
  grade: true
  grade_id: cell-b0f19839d7c8f187
  locked: true
  points: 3
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
from network import Network
from network import examples
from ford_fulkerson import maximal_flow
F = maximal_flow(examples.example1(),0,6)
assert F.check_in_out()
assert F.check_capacity()
assert F.global_value() == 4
F = maximal_flow(examples.small_example(),0,3)
assert F.check_in_out()
assert F.check_capacity()
assert F.global_value() == 6
F = maximal_flow(examples.small_example2(),0,3)
assert F.check_in_out()
assert F.check_capacity()
assert F.global_value() == 9
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ee57ca88fd8ece9dbdc2b7fba1271354", "grade": false, "grade_id": "cell-02033b087568d867", "locked": true, "points": 2, "schema_version": 3, "solution": false, "task": true}}

Affichage du code pour correction:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 2fe459dbf4e2c4ec4c31afcfa464c384
  grade: false
  grade_id: cell-ed670857386b8df8
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from utils import show_source
show_source(maximal_flow)
```

```{code-cell} ipython3

```
