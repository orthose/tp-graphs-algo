---
jupytext:
  notebook_metadata_filter: rise
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
rise:
  auto_select: first
  autolaunch: false
  centered: false
  controls: false
  enable_chalkboard: true
  height: 100%
  margin: 0
  maxScale: 1
  minScale: 1
  scroll: true
  slideNumber: true
  start_slideshow_at: selected
  transition: none
  width: 90%
---

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "968d04f7939b662256f37926dfdd61d1", "grade": false, "grade_id": "cell-dc8a7e0d2a8ee6dc", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Algorithme De Ford-Fulkerson

L'algorithme de Ford-Fulkerson sert à calculer *le flot de valeur maximale* (ou simplement *flot maximal*) sur un réseau entre deux points donnés. C'est-à-dire la quantité maximale de «fluide» que l'on peut faire «couler» de la source vers la cible.

Le principe de base est simple : on part du flot nul (toutes les valeurs sont à 0) et on augmente le flot jusqu'à ce que ça ne soit plus possible. La question est de savoir comment «augmenter» un flot tout en conservant ses proriétés.

On présente ici une stratégie que l'on implantera ensuite sur notre classe `Flow`.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f85ae4eb75024c69984398a932490c21", "grade": false, "grade_id": "cell-5efb584a919b7fa1", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Algorithme de la chaîne augmentante

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "75ea50405c0d503a8fb90b316a712028", "grade": false, "grade_id": "cell-5efb584a919b7fa2", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Une *chaîne augmentante* est un chemin non-orienté de $s$ à $t$ (on peut prendre les arêtes dans n'importe quel sens) tel que :

 * sur les arêtes prises dans «le bon sens», la valeur du flot est strictement inférieure à la capacité de l'arête;
 * sur les arêtes prises dans «le mauvais sens», la valeur du flot est strictement supérieure à 0.
 
Par exemple, $0 - 3 -6$ est une chaîne augmentante sur l'exemple de flot suivant :
- l'arête $(0,3)$ prise dans le bon sens n'a pas atteint sa capacité maximale
- l'arête $(3,6)$ prise dans le mauvais sens a un flot strictement supérieur à 0.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: e7d1b1068c043d754fc96ec19c14c3fd
  grade: false
  grade_id: cell-ecec15119864517f
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 11183a10adfc7ffd7335b8619bce48e0
  grade: false
  grade_id: cell-799ddf40937fa6eb
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F = flow_examples.example1()
F.show(marked_edges = {(0,3), (6,3)})
```

```{code-cell} ipython3
F.global_value()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6016bd6f86b471133b444ae5a68993d7", "grade": false, "grade_id": "cell-c35ffd960146d1a4", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On regarde ensuite *le potentiel d'augmentation* $p$ pour chaque arête de la chaîne : 

 * pour une arête prise dans le bon sens, $p$ est égal à la différence entre la capacité de l'arête et la valeur du flot.
 * pour une arête prise dans le mauvais sens, $p$ est égal à la valeur du flot (la différence entre la valeur du flot et 0).

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f479c73e7a30527e9b55b686c03c8026", "grade": false, "grade_id": "cell-c35ffd960146d1a5", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On détermine $pmin$ **le potentiel minimum sur la chaîne** puis, on **augmente** le flot des arêtes dans le bon sens et on **diminue** celui des arêtes dans le mauvais sens de la valeur $pmin$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2f26bf061bbb8f6ff2c4b5b1853646e1", "grade": false, "grade_id": "cell-c35ffd960146d1a6", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Par exemple, pour notre chaîne $0 - 3 - 6$, le potentiel de $(0,3)$ est 1 et le potentiel sur $(3,6)$ est 2. Dans ce cas, on a $pmin = 1$ et on peut : augmenter le flot de $(0,3)$ pour le faire passer à 1 et diminuer le flot de $(3,6)$ pour le faire passer à 1. Le résultat est toujours un flot.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: cbad616d4353cc55b2500db914e48283
  grade: false
  grade_id: cell-7b79af85e008d48a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
pmin = 1
F.add_flow(0,3,pmin)
F.add_flow(6,3,-pmin)
F.show(marked_edges = {(0,3), (6,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 794a87aaacf4676fa63bcee565cfe31c
  grade: false
  grade_id: cell-9a7c21e49deff653
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.check_in_out()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 3933142663be10620233bf77a2d89906
  grade: false
  grade_id: cell-e997ce48e962f30b
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.check_capacity()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f009d8464e1f90c8ff1e4f371d82a8d6", "grade": false, "grade_id": "cell-56067cb510ba8d9b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Par ailleurs, on remarque que la valeur du flot a augmenté:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 90a07bc2af1271a9b6afdd8be1db3476
  grade: false
  grade_id: cell-b6608adbe10e9100
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.global_value()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f8f5431eef553aaab7ab564b64e9b939", "grade": false, "grade_id": "cell-09228752f3790add", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Peut-on trouver d'autres chaînes augmentantes ?**

```{code-cell} ipython3
F.show()
```

```{code-cell} ipython3
F.show(marked_edges = {(0,2), (5,2), (5,6)})
```

```{code-cell} ipython3
F.show(marked_edges = {(0,2), (5,2), (3,5), (6,3)})
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ed8cc3b7607c9bdafae10a178da80b76", "grade": false, "grade_id": "cell-f1050456c7e8ec46", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Comment chercher systématiquement une chaîne augmentante ?**

Il suffit d'appliquer un algorithme de parcours du graphe (en profondeur ou en largeur). Attention, cependant, le graphe est orienté mais le parcours suit les arêtes **dans les deux sens**.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "91ec5619075d85808095fd7c36e593c1", "grade": false, "grade_id": "cell-f1050456c7e8ec47", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exemple avec un parcours en profondeur**

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 46553b5c96a770059366514d59fae291
  grade: false
  grade_id: cell-883866263207dea8
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F = flow_examples.example1()
F.show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a9fee8664272fa9ef522a065f070bb7b
  grade: false
  grade_id: cell-9fdb5648d06bb34b
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,1)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 46b45753ce5c11cff954c91a13ef94d6
  grade: false
  grade_id: cell-eb056a2fd9d365fd
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: eabb8cf2df22e35c9b690e010eb8f6f9
  grade: false
  grade_id: cell-0675b561e5d02445
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2)}, marked_nodes = {2})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 9055e59b17bc124fb2ce32a132b05602
  grade: false
  grade_id: cell-a689075d2ee527a4
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (2,1)}, marked_nodes = {2})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 3ac5aaf9043669b4db44e841004abccb
  grade: false
  grade_id: cell-6c95380a56c137f4
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (2,4)}, marked_nodes = {2})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 093eb16f032a548fe9381f4c329f2e07
  grade: false
  grade_id: cell-2b8d5aaef056aeed
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (5,2)}, marked_nodes = {2})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: fff698015c594ae0f03b82e6317cabbb
  grade: false
  grade_id: cell-38e604826eaaaff2
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (5,2)}, marked_nodes = {2,5})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c25e26f4747819b71406b11ca18806e2
  grade: false
  grade_id: cell-6b0c54e27b8c374a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (5,2), (5,6)}, marked_nodes = {2,5})
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "20e1d3d24c1d94ad7e02d57cb58b1162", "grade": false, "grade_id": "cell-bc59359b1a835784", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Utiliser les chaînes augmentante pour trouver le flot maximal

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "428040e76c457f188b795ecd0938c317", "grade": false, "grade_id": "cell-92dd83371a161a8e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On part du flot nul et on augmente grâce aux chaînes augmentantes.

**Exemple :**

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 5581127636676cf1694f9cbc4d740a07
  grade: false
  grade_id: cell-d57043da1be5d63b
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
F = flow_examples.small_example()
F.show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 2ead61398dbab200d48a47ab507f750e
  grade: false
  grade_id: cell-1764264627630b54
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,1), (1,2), (2,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 124c86a657c5ad649056cad917ebdbf2
  grade: false
  grade_id: cell-bdaaf79ccf65cafa
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.add_flow(0,1,2)
F.add_flow(1,2,2)
F.add_flow(2,3,2)
F.show(marked_edges = {(0,1), (1,2), (2,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: dc3777fa2179a934cd5161f3960d9516
  grade: false
  grade_id: cell-1e2d850b049b1225
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,1), (1,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b94030d2849e718031ce9e3a4f9bb6e7
  grade: false
  grade_id: cell-b46e787fb8484c71
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.add_flow(0,1,1)
F.add_flow(1,3,1)
F.show(marked_edges = {(0,1), (1,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 33122db661baba74484c4642cf9059c2
  grade: false
  grade_id: cell-b9565052040e2d73
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (2,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 6d35508bfc650a92a0da7c5139c62798
  grade: false
  grade_id: cell-263dd4b6e8b38d09
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.add_flow(0,2,1)
F.add_flow(2,3,1)
F.show(marked_edges = {(0,2), (2,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ea485c4561b43d6aaaeaf017e2a199fe
  grade: false
  grade_id: cell-6f89d231fab3f255
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (1,2), (1,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b9ce83131f3f0e5cf4b38f11599380f0
  grade: false
  grade_id: cell-c4a4bc04b5aeab4e
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.add_flow(0,2,2)
F.add_flow(1,2,-2)
F.add_flow(1,3,2)
F.show(marked_edges = {(0,2), (1,2), (1,3)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 1e3c2bbd7766d031e5222c64ce7786b5
  grade: false
  grade_id: cell-26ebde8b41738d49
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.global_value()
```

**Est-on sûr d'avoir obtenu le flot maximal ? On aurait pu faire d'autres choix pour les chaînes augmentantes !**

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "101a8661d49ec9da4d870899d46e0846", "grade": false, "grade_id": "cell-9d7f221d23ad031e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## La coupe minimale et théorème flot-max/coupe-min

Pour un flot donné, on appelle *une coupe* un ensemble $S$ de sommets tels que

* La source du flot est dans $S$
* La cible du flot n'est pas dans $S$

On calcule la *capacité* $c$ de la coupe 

$$c(S) = \sum_{v \in S, t \notin S} c(v,t)$$

où $c(v,t)$ est la capacité de l'arête $(v,t)$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "12fe0c184facfe59a2762de32f782b1e", "grade": false, "grade_id": "cell-9d7f221d23ad031f", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exemple :**

```{code-cell} ipython3
F = flow_examples.example1()
F.show()
```

```{code-cell} ipython3
S = {0,1,2,5,3}
F.show(marked_nodes = S)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c8e34ed15f978f19585c584472d7bd84
  grade: false
  grade_id: cell-ef16900ccb9afc7a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
edges = set()
for a,b in F.network().edges():
    if a in S and b not in S:
        edges.add((a,b))
F.show(marked_nodes = S, marked_edges = edges)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 217baf32339d127213ee70d4befff895
  grade: false
  grade_id: cell-d491a9c2ae8ec178
  locked: true
  schema_version: 3
  solution: false
  task: false
---
c = sum(F.capacity(a,b) for a,b in edges)
c
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "603863f1e3b6c5c2315951f821ed7419", "grade": false, "grade_id": "cell-7d57861198f4b0be", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Pour une coupe $S$, la *valeur de flot* de la coupe est donnée par :

$$ \sum_{v \in S, t \notin S} f(v,t) - \sum_{v \notin S, t \in S} f(v,t)$$

où $f(v,t)$ est la valeur du flot sur l'arête $(v,t)$.

Par exemple :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: e2ec357693fb8d9ea6aa115a5360575a
  grade: false
  grade_id: cell-0641b32df10fd92a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
edges_out = set()
edges_in = set()
for a,b in F.network().edges():
    if a in S and b not in S:
        edges_out.add((a,b))
    if a not in S and b in S:
        edges_in.add((a,b))
edges = edges_out.union(edges_in)
F.show(marked_nodes = S, marked_edges = edges)
```

```{code-cell} ipython3
f = sum(F.flow(a,b) for a,b in edges_out) - sum(F.flow(a,b) for a,b in edges_in)
f
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "784f44e9fcbb93815b0343de5b033bf6", "grade": false, "grade_id": "cell-aec89d87bc58aea4", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Proposition : pour un flot donné, quelle que soit la coupe $S$, la valeur de flot $f(S)$ est constante et égal à la valeur globale du flot.**

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "cef6e07f2168cb41e283cc2e91d74586", "grade": false, "grade_id": "cell-4357265cc0c5b051", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**[Théorème flot-max/coupe-min](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_flot-max/coupe-min) : la capacité de la coupe minimale d'un réseau est égale à la valeur globale de son flot maximal.**

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "57e2e5bdf2ec1e7eeb19567b6f7fc820", "grade": false, "grade_id": "cell-7bccae5108633e8c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Démonstration : Soit $F$ un flot sur un réseau $N$ et $S$ une coupe de $N$. Par définition il est clair que 

$$ f(S) \leq c(S)$$

Appliquons à présent l'algorithme de Ford-Fulkerson à $N$ et soit $F$ un flot tel qu'il n'y ait plus de chaîne augmentante. Par exemple :

```{code-cell} ipython3
F = flow_examples.small_example2()
F.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "a7e30a35b97c3f7ad1607c016f1557aa", "grade": false, "grade_id": "cell-07db7323906c7150", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Cherchons une chaîne augmentante par un parcours en profondeur:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 5f9f908cee2e544737c779aeb7440c83
  grade: false
  grade_id: cell-b2ac28be644d8ec1
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,1)})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c249f426aa54051ca2874451c648aff1
  grade: false
  grade_id: cell-1f9cba48808f86b6
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,1)}, marked_nodes = {1})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 1f1243daf191b8214f887e18585339cd
  grade: false
  grade_id: cell-1a217c6dd6d75c2c
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,1),(1,2)}, marked_nodes = {1})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 9b090aa3886521aff68e68b453483a19
  grade: false
  grade_id: cell-7a354f2b266331c1
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,1), (1,3)}, marked_nodes = {1})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 079e76eab53bfb99b6322c35e2caf387
  grade: false
  grade_id: cell-80554685b25cf65b
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2)}, marked_nodes = {1})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: e1829f1908a26e8ab60e753ffbe15c14
  grade: false
  grade_id: cell-81550d99a5ca8b36
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2)}, marked_nodes = {1,2})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 841d840b20bb402a68ab27bc7dbf3cdb
  grade: false
  grade_id: cell-7b11c331a12ca3b0
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (2,3)}, marked_nodes = {1,2})
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d889d33d3b3f3cbbfcb7e6650ea2ede9
  grade: false
  grade_id: cell-93bfa9dea69182c9
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.show(marked_edges = {(0,2), (1,2)}, marked_nodes = {1,2})
```

```{code-cell} ipython3
F.show(marked_nodes = {1,2})
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c558bab5737eae667dd820d4eb27a9c4", "grade": false, "grade_id": "cell-66b2413da6cd1253", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Les sommets visités $0,1,2$ forment une coupe $S$. Et par ailleurs, on sait que :

* toutes les arêtes sortantes de la coupe sont à capacité maximale 
* toutes les arêtes entrantes dans la coupe sont à 0

(sinon, on aurait pu continuer l'exploration pour chercher une chaîne augmentante) donc:

$$c(S) = f(S)$$

+++

Toutes les arêtes entrantes dans la coupe sont à 0 = Les arêtes qui entrent dans la coupe (aucune dans cet exemple) ont un flot de 0.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4558de617914cf78a07c021e96fc0d4e", "grade": false, "grade_id": "cell-eb8f9d689ae53c40", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Maintenant, on met ces éléments ensemble :
    
1. La valeur globale d'un flot $F$ sur un réseau $N$ est égale à $f(S)$ quelle que soit la coupe $S$ de $N$.
1. Quelque soit le flot $F$ sur $N$ et quelle que soit la coupe $S$ de $N$, on a $f(S) \leq c(S)$
1. Il existe un flot $F_m$ et une coupe $S_m$ tel que $f(S_m) = c(S_m)$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "961394c5f0e3f4cfab2f094a25db54ae", "grade": false, "grade_id": "cell-d30d247b7e9b909d", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Les points 1 et 2, nous indiquent que **le flot maximal** est de valeur plus petite ou égale à la **couple minimale** car tout flot est de valeur plus petite que toute coupe.

Soit $F_{max}$ la valeur du flot maximal, et $C_{min}$ la valeur de la coupe minimale, avec le point 3, on a

$$ F_{max} \geq f(S_m) = c(S_m) \geq C_{min}$$

Le flot maximal est à la fois plus petit ou égal et plus grand ou égal à la coupe minimale : on a donc nécessairement

$$ F_{max} = f(S_m) = c(S_m) = C_{min}$$

+++

## Mise en perspective

+++

Les problèmes de flots dans les réseaux sont un cas particulier des problèmes [d'optimisation linéaire](https://fr.wikipedia.org/wiki/Optimisation_lin%C3%A9aire) (recherche d'une solution optimal d'un systèmes d'**inéquations linéaires**). L'algorithme de Ford-Fulkerson est une spécialisation de l'algorithme du simplexe. Le théorème flot-max coupe min est une spécialisation du théorème du dualité de la programmation linéaire.

Mais alors, pourquoi s'intéresser aux problèmes de flots, alors qu'une théorie plus générale existe?

D'abord parce que c'est une gamme de problèmes importante en pratique. Ensuite parce que les algorithmes se spécialisent bien. Et enfin parce que les problèmes de flots ont des propriétés particulières (théorème d'intégralité) qui permettent d'encoder de nombreux problèmes combinatoires (par exemple: recherche d'un couplage dans un graphe biparti) comme problème de flot pour les résoudre. Cela permet d'en déduire de nombreux théorèmes de type min-max en combinatoire.

Tout cela est le sujet de la **combinatoire polyhédrale**.

+++

## Conclusion

+++

Après cette description théorique de l'algorithme de Ford-Fulkerson, il est temps de passer à son implantation!
