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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "32b6ceb37ad7029be02873082375729e", "grade": false, "grade_id": "cell-0fb472606b0a09e0", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

# Introduction aux graphes et leurs structures de données

## Graphes: quelques définitions

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "687cd2409d7981fada7f641b2050e6dc", "grade": false, "grade_id": "cell-12e390568ebd39f4", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Qu'y a t'il de commun entre tous nos problèmes?
<!--TODO: figure!-->

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "dc70612489f06acbb835bdc33e4500e5", "grade": false, "grade_id": "cell-aad7f3cc33bd85bf", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Dans chacun d'entre eux, la résolution se ramènera à étudier comment certains objets sont reliés entre eux.
Autrement dit, le problème va pouvoir être **modélisé à l'aide d'un graphe**.


Informellement: un **graphe** est la donnée d'un ensemble de **sommets** reliés par des **arêtes**.
Voilà un exemple avec neuf sommets. Les sommets 0 et 2 y sont reliés entre eux. Mais pas 0 et 6:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: af9b741dae89f531e6ff3908862a74eb
  grade: false
  grade_id: cell-12f9b9189e24d940
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from graph_networkx import Graph
G = Graph(nodes=[1, 2, 3, 4, 5],
          edges=[ (1,2), (1,3), (2,4), (3,4), (4,5) ])
G.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "7382df9ae7b0cd440ae77418decd3031", "grade": false, "grade_id": "cell-83378f7cd81fe8a0", "locked": true, "schema_version": 3, "solution": false, "task": false}}

La définition formelle la plus simple est la suivante:

Un **graphe** est une paire $G:=(V,A)$ où $V$ est un ensemble et $A$ et un ensemble de paires $\{v_1,v_2\}$ d'éléments de $V$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "212c2ed7bf05f06dfb861fc1252c2163", "grade": false, "grade_id": "cell-cf0ad994eb573d6a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Dans notre exemple, $G=(V,A)$, où $V = \{1,2,3,4,5\}$ et $A = \{\{1,2\}, \{1,3\}, \{2,4\}, \{3,4\}, \{4,5\}, \{5,6\}\}$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "109988685be5af30bffd09b45a7dc1c3", "grade": false, "grade_id": "cell-13c78db3c53e0610", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Remarque: dans la définition donnée, une arête est un ensemble à deux éléments:
- le graphe n'est **pas orienté**: si $s$ est relié à $t$ alors $t$ est relié à $s$;
- il n'y a pas de **boucle**, c'est à dire une arête reliant un sommet à lui-même;
- ni d'**arête multiple**, c'est-à-dire plusieurs arêtes reliant les mêmes sommets;

On parle de **graphe simple**.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "1cf7f96c3108e81a42fd1ebc0f606377", "grade": false, "grade_id": "cell-bbf5fbc038ac698d", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

## Graphes: Variantes

Le plus souvent, cette information de base est enrichie d'informations supplémentaires: étiquettes sur les sommets, valuations sur les arêtes, orientation des arêtes, ...

On remplace la paire $\{v_1,v_2\}$ par un couple $(v_1,v_2)$:
- On a en plus: orientation, boucle...

On ajoute un nombre à la paire $(v_1, v_2, c)$:
- On a en plus: arête multiple, coût, capacité ...

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "1292fd2118a70f46f50976d1ce7a170e", "grade": false, "grade_id": "cell-35c397cbf4956ace", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

## Quelques structures de données pour les graphes

Pour étudier un graphe à l'aide d'un ordinateur, il va falloir le représenter, c'est-à-dire choisir une structure de données. Comme le champ d'application des graphes et large, il y a beaucoup d'algorithmes différents, avec des besoins différents en terme de performance des opérations élémentaires. Tel algorithme va demander d'avoir un accès très performant aux voisins d'un sommet; tel autre parcourir les arêtes, etc. De ce fait, il existe de nombreuses structures de données possibles que nous allons explorer maintenant.

On s'intéressera dans cette séance aux **graphes orientés** où chaque arête aura une capacité `c` qui sera un nombre.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ace6e9e9d645a7f83ca0ae50a7b910ad", "grade": false, "grade_id": "cell-e65e3529dbc8309a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Liste d'arêtes

Ici, on représentera un graphe par une liste de triplets `(v1,v2,c)`, chacun d'entre eux spécifiant qu'il y a une arête reliant $v_1$ à $v_2$ de capacité $c$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "0853d4c42f47c18f3178ac553fad4c52", "grade": false, "grade_id": "cell-81506dd19fb33e98", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Ci-dessous, nous donnons la structure de données `L0` d'un graphe $G_0$ avec trois sommets, $0,1,2$, et deux arêtes; la première relie $0$ à $1$ avec une capacité de $10$ et la deuxième relie $0$ à $2$ avec une capacité de $4$.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: e8fa2af84ed6e1178aa8823a012bb87a
  grade: false
  grade_id: cell-832bab094684d111
  locked: true
  schema_version: 3
  solution: false
  task: false
---
L0 = [ (0,1,10), (0,2,4) ]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "af79f346048dc54333240a5f50f26402", "grade": false, "grade_id": "cell-53261b63230bc557", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Voici la structure de donnée pour un autre graphe $G_1$:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 3ce8abb99d1d3d9d6001abc1affee57e
  grade: false
  grade_id: cell-9c8bb4f1b140e1aa
  locked: true
  schema_version: 3
  solution: false
  task: false
---
L1 = [ (1,2,1), (1,3,1), (2,4,2), (3,4,0), (4,5,3) ]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "a2286ebc5f848663cb91415c44769993", "grade": false, "grade_id": "cell-9373d1fc68e76a53", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice**
- Dessiner sur papier les graphes `G_0` et `G_1`, en mettant sur chaque arête sa capacité.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f83307675d823333744bde2144ef233f", "grade": false, "grade_id": "cell-b251ae3315043646", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Rappel: dictionnaires Python

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "64fef411e1c32fa39c9234c2c33c4a05", "grade": false, "grade_id": "cell-0964b25fb308a178", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Un *dictionnaire* en Python est une structure de donnée permettant d'associer à une valeur à une clé. Comme un dictionnnaire de français qui associe une définition à un mot, ou un annuaire qui associe un numéro de téléphone à une personne. Voici un dictionnaire qui associe la valeur `1` à la clé `"bla"`, la valeur `3` à la clé `"ble"` et la valeur `"pi"` à la clé `3.13`:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 303260ed92c64dbc3b15a57a9821a5fe
  grade: false
  grade_id: cell-3e5330e3a0b63562
  locked: true
  schema_version: 3
  solution: false
  task: false
---
t = {"bla": 1, "ble": 3, 3.14: "pi"}
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c95bed21fcd3a485563a92324c0e6f4b
  grade: false
  grade_id: cell-845e00c098b38b75
  locked: true
  schema_version: 3
  solution: false
  task: false
---
t
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5aa7d5fb3ea4ebf83c2a3e0732fbeb5f", "grade": false, "grade_id": "cell-6567db76a8c5039a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On peut accéder à une valeur à partir de sa clé avec l'opération suivante:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c691e430ac679f09317d4f50bcfa984e
  grade: false
  grade_id: cell-aa2d958877c70084
  locked: true
  schema_version: 3
  solution: false
  task: false
---
t[3.14]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2422a05fa5195107722447f15aa4cea7", "grade": false, "grade_id": "cell-cc345264b87f4a1a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On notera la similitude avec l'accès aux éléments d'un tableau. On peut voir un tableau de taille `l` comme un dictionnaire associant des valeurs à des clés entre `0` et `l-1`

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "21e003c6f4827e7cde68bc225bbe03a6", "grade": false, "grade_id": "cell-57228cfa27b007a1", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Dictionnaire des voisins

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "d847fd3bea7ea6a643b0b0b00f68cb6d", "grade": false, "grade_id": "cell-2fea9135834106e0", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Un sommet $v_2$ est un voisin sortant d'un sommet $v_1$ s'il y a une arête reliant $v_1$ à $v_2$.

On peut représenter un graphe à l'aide d'un *dictionaire des voisins* qui à chaque sommet associe la liste de ses voisins. Comme on veut représenter des capacités, la valeur associée à la clé `v1` sera un liste de paires `(v2,c)` où $v_2$ sera le voisin et `c` la capacité de l'arête reliant $v_1$ à $v_2$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ed2784944428f8926a2f0da37d6f09b9", "grade": false, "grade_id": "cell-20f20532263d1f73", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Voici le dictionnaire des voisins pour $G_0$:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a6b8d83816d9718514e8b33244951f86
  grade: false
  grade_id: cell-296573e3bba901c6
  locked: true
  schema_version: 3
  solution: false
  task: false
---
DV0 = { 0: [(1,10), (2,4) ] }
```

```{code-cell} ipython3
L1
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2e8d543e98423422320499384edf5914", "grade": false, "grade_id": "cell-d20bc2c5414d6b1a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice**
Donner le dictionnaire des voisins pour $G_1$:

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 9eefbea2eff635d8e0a85e6e56a18671
  grade: false
  grade_id: cell-d662314d2272933e
  locked: false
  schema_version: 3
  solution: true
  task: false
---
DV1 = {}
for (v1, v2, c) in L1:
    if v1 not in DV1:
        DV1[v1] = [(v2, c)]
    else:
        DV1[v1].append((v2, c))
print(DV1)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "dae07125a079331354dbce610915db3c", "grade": false, "grade_id": "cell-b6d9d6f663f27355", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Note: si les sommets du graphe sont étiquetés par $0,1,\ldots$, on peut utiliser une liste au lieu d'un dictionnnaire:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 069f23728126b8e87751ffe68b89652d
  grade: false
  grade_id: cell-e8e4a3fea4afa0c3
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# Avec un tableau (graphe etiquete par 0,1,...)
DV0 = [ [(1,10), (2,4)] ]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "eb49d83822df4c57cb1a7aa3ce5ee0aa", "grade": false, "grade_id": "cell-56783b8586212b07", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

### Dictionnaire d'arêtes

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "23ef0d027d5db19afcedf62e6d33d51c", "grade": false, "grade_id": "cell-853b0c46657a7983", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Utilisons maintenant un *dictionnaire d'arêtes* pour représenter `G_1`: il associera à chaque paire `(u1,v1)` reliés par une arête la capacité de cette arrête.
Voici le dictionnaire pour $G_0$:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 273abdaaa640e189dd9202dd199f9942
  grade: false
  grade_id: cell-8b9c4f073bacba06
  locked: true
  schema_version: 3
  solution: false
  task: false
---
DA0 = { (0,1): 10,
        (0,2): 4
      }
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "7a9570eb2a2c65870b639d3d3b11905b", "grade": false, "grade_id": "cell-6bc88084fce0f9fa", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice**
Donner le dictionnaire d'arêtes pour $G_1$:

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: d32b643c1e1f8f489b046dbfb9958708
  grade: false
  grade_id: cell-98fa5972274a0bce
  locked: false
  schema_version: 3
  solution: true
  task: false
---
DA1 = {(v1, v2) : c for (v1, v2, c) in L1}
print(DA1)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4cf9878403c073f9efc256eeff8613ce", "grade": false, "grade_id": "cell-4ae02a19ea56aaa6", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Matrice d'adjacence
La matrice d'adjacence d'un graphe est un tableau (ou matrice) à deux dimensions `M` tel que `M[v1,v2]` est la capacité `c` de l'arête reliant $v_1$ à $v_2$ ou $0$ s'il n'y a pas d'arête.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d94823b244d4cb92f8f0cf2a05fac301
  grade: false
  grade_id: cell-9ab824cd1bb2aa61
  locked: true
  schema_version: 3
  solution: false
  task: false
---
M0 = [ [0, 10, 4],
       [0,  0, 0],
       [0,  0, 0]]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3ad2fa369abc744e19408373421e3e0c", "grade": false, "grade_id": "cell-33cf5a83c5bb4813", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice**
Donner la matrice des voisins pour $G_1$.

Indication: Vous rajouterez un sommet $0$.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 2a145fd7f96dbaf05f990069c56ec576
  grade: false
  grade_id: cell-9caa44fcb3382c31
  locked: false
  schema_version: 3
  solution: true
  task: false
---
M1 = [[0 for _ in range(6)] for _ in range(6)]
for (v1, v2, c) in L1:
    M1[v1][v2] = c
print(M1)
```

# Conclusion

Maintenant que vous avez manipulé des structures de données
de graphes sur des exemples, vous pouvez passer à la feuille
[02-Implantation.md](02-Implantation.md).
