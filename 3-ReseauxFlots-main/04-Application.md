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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5b0cd70a77eaeceebd5b96f80cd71d58", "grade": false, "grade_id": "cell-1d52bcff7a53e531", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Des livraisons

3 usines données produisent des ours en peluche : 

 * $A_1$ en produit 300 par semaines
 * $A_2$ en produit 500
 * $A_3$ en produit 100
 
5 grands magasins font une commande pour la semaine prochaine :

 * $B_1$ commande 100 ours
 * $B_2$ commande 50
 * $B_3$ commande 80
 * $B_4$ commande 300
 * $B_5$ commande 200
 
La logistiques fait que chaque usine ne peut livrer que dans un certain sous-ensemble de magasins :

 * $A_1$ peut livrer $B_1$ et $B_3$
 * $A_2$ peut livrer $B_2$ et $B_4$
 * $A_3$ peut livrer $B_3$, $B_4$, et $B_5$.
 
Utiliser l'algorithme de Ford-Fulkerson pour déterminer si l'entreprise d'ours en peluche peut assurer sa commande.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 7175eec23ffd1ca5a243dfb5dc6da143
  grade: false
  grade_id: cell-31061d257bac5b9d
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from network import Network
from flow import Flow
from ford_fulkerson import maximal_flow
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 1a71619cf73f86af3ce57814e4a52059
  grade: false
  grade_id: cell-5e4d1b93a0a5b0c3
  locked: false
  schema_version: 3
  solution: true
  task: false
---
N = Network(
    edges = [('S', 'A1', 300), ('S', 'A2', 500), ('S', 'A3', 100), 
             ('A1', 'B1', 300), ('A1', 'B3', 300), 
             ('A2', 'B2', 500), ('A2', 'B4', 500), 
             ('A3', 'B3', 100), ('A3', 'B4', 100), ('A3', 'B5', 100), 
             ('B1', 'T', 100), ('B2', 'T', 50), ('B3', 'T', 80), ('B4', 'T', 300), ('B5', 'T', 200)], 
    nodes = ['S', 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'B4', 'B5', 'T']
)

F = maximal_flow(N, 'S', 'T')
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c0675894d76b20412c9345df17151188
  grade: true
  grade_id: cell-9b5d32fa91cacf26
  locked: true
  points: 3
  schema_version: 3
  solution: false
  task: false
---
import hashlib
assert hashlib.md5(bytes(F.global_value())).hexdigest() == '67f022b63ce6ae0602b1c26761f4f7ee'
```

```{code-cell} ipython3
F.flows()
```

```{code-cell} ipython3

```
