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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e1ca35f96e5c4f104595b0ba48fda2ea", "grade": false, "grade_id": "cell-7fa94557a9528c30", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Applications

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "57d7bfa2939260a132e6db778d0921f4", "grade": false, "grade_id": "cell-0bf805f0964bb953", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Composantes connexes
Soit $G$ un graphe non orienté. La composante connexe d'un sommet $s$ de $G$ est l'ensemble des sommets atteignables depuis $s$ en suivant un chemin dans $G$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c02bfb32f1b13a9c8f17fbf72bb42878", "grade": false, "grade_id": "cell-e6440dd43c4d8889", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice**
1. Décrire un algorithme pour calculer toutes les composantes connexes d'un graphe non orienté
2. (Bonus) Implanter cet algorithme et visualiser son exécution

+++

1. L'algorithme naïf consite simplement à itérer sur tous les sommets et à effectuer un parcours en largeur ou en profondeur sur chacun de ces sommets.

```{code-cell} ipython3
def parcours(G, u):
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = {u} # L'ensemble des sommets déjà rencontrés
    todo   = {u} # L'ensemble des sommets déjà rencontrés, mais pas encore traités
    
    while todo:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans dans `marked`
        v = todo.pop()
        for w in G.neighbors(v):
            if w not in marked:
                marked.add(w)
                todo.add(w)
    return marked
```

```{code-cell} ipython3
from typing import Dict, Set
from graph import Graph, Node, examples

def toutes_composantes_connexes(G: Graph) -> Dict[Node, Set[Node]]:
    res = dict()
    for u in G.nodes():
        res[u] = parcours(G, u)
    return res
```

```{code-cell} ipython3
G = examples.parcours_directed()
toutes_composantes_connexes(G)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2c402bc596f9c6a3c36d6e43ddaa23ab", "grade": false, "grade_id": "cell-42d362e08da6e54f", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Généralisation

**Exercice**:

1. Généraliser la fonction `parcours` de la fiche [01-ParcoursDeGraphe.ipynb](01-ParcoursDeGraphe.ipynb) pour qu'elle prenne en argument la *fonction de voisinage* du graphe plutôt que le graphe lui-même.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: b23f06ee9c484e273b3bfcafe1278273
  grade: false
  grade_id: cell-203cbf9059dad7fa
  locked: false
  schema_version: 3
  solution: true
  task: false
---
from typing import Callable, Iterable, Set
from graph import Node

def parcours_fonction(voisins: Callable[[Node], Iterable[Node]], u: Node) -> Set[Node]:
    """
    INPUT:
    - `voisins`: une fonction telle que `voisins(v)` renvoie les voisins sortants de `v`
    - 'u' - un sommet du graphe
    
    OUTPUT: l'ensemble des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = {u} # L'ensemble des sommets déjà rencontrés
    todo   = {u} # L'ensemble des sommets déjà rencontrés, mais pas encore traités
    
    while todo:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans dans `marked`
        v = todo.pop()
        # La différence est minime
        for w in voisins(v):
            if w not in marked:
                marked.add(w)
                todo.add(w)
    return marked
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "fc7b0298a761ae8837b8a00c8d265498", "grade": false, "grade_id": "cell-035bdd195a5c981c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

2. Testez votre fonction sur l'exemple suivant.  
   **Indication**: étant donné un graphe `G` tel que implanté précédément, la fonction `voisins` requise par `distance` peut être construite comme suit:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 4eb6952971d7f60f6796159b9e94bafb
  grade: false
  grade_id: cell-8c06644285f181e9
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from graph import examples
G = examples.parcours_directed()
voisins = G.neighbors
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 39c8e1a1631b46bbbab4d2018a148059
  grade: true
  grade_id: cell-c0385743a593b35c
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert parcours_fonction(voisins, 'D') == {'D', 'F', 'G', 'H'}
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "90330a5531918591dce76048c8906986", "grade": false, "grade_id": "cell-710d5a14b2c7464c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

2. Reprenez de même tous les tests de la fiche 01 avec votre nouvelle fonction

```{code-cell} ipython3
G = examples.parcours_directed()
assert parcours_fonction(G.neighbors, "A") == {'A', 'B', 'C', 'D', 'F', 'G', 'H'}
assert parcours_fonction(G.neighbors, "B") == {'B', 'C', 'D', 'F', 'G', 'H'}
```

```{code-cell} ipython3
H = examples.cours_1_G()
assert sorted(parcours_fonction(H.neighbors, 3)) == [0, 1, 2, 3, 4, 5]
```

```{code-cell} ipython3
H = examples.disconnected()
assert sorted(parcours_fonction(H.neighbors, 1)) == [1, 2, 5]
assert sorted(parcours_fonction(H.neighbors, 3)) == [3, 4]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "a6945c3deb4e4ca66369f2f53204b833", "grade": false, "grade_id": "cell-762972522930912c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Application: ensembles définis récursivement
De nombreux ensembles mathématiques sont définis en donnant quelques éléments initiaux, puis en applicant récursivement un processus permettant de produire de nouveaux éléments à partir d'éléments déjà présents. Par exemple, l'ensemble des entiers naturels est construit à partir de $0$ et de la fonction successeur $x \mapsto x+1$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "cbca65202ae74c22f9240f26e8dccf8b", "grade": false, "grade_id": "cell-2aa4625a03b106d8", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "subslide"}}

**Définition:**

Soit $E$ un ensemble, $R\subset E$ un sous ensemble fini, et $f$ une fonction associant à chaque élément de $E$ un sous-ensemble fini de $E$. L'ensemble $f$ défini récursivement par $R$ et $f$ est le plus petit sous-ensemble de $E$ contenant $R$ et *stable* par $f$: si $e\in F$ alors $f(e)\subset F$.

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5472bd08bf929ef92ffb952552f07562", "grade": true, "grade_id": "cell-d00c1b613f9e6da2", "locked": false, "points": 4, "schema_version": 3, "solution": true, "task": false}, "slideshow": {"slide_type": "subslide"}}

**Exercice**

Décrire les ensembles définis récursivement obtenus dans chacun des cas suivants:
- $E=\mathbb N$, $R=\{1\}$, $f(e) = \{ e + 2 \}$
  L'ensemble des nombres entiers impairs.
  
- $E=\mathbb N$, $R=\{1\}$, $f(e) = \{ 2e, e+3 \}$
  L'ensemble nombres qui ne sont pas multiples de 3.
  $\{1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, ...\}$

- $E$: listes, $R=\{()\}$, $f(u)$: rajouter $0$ ou $1$ à la fin du $u$
  L'ensemble des nombres binaires
  $\{(), (0), (1), (00), (10), (01), (11), ...\}$

- $E$: listes, $R=\{(1,2,3,2,1)\}$, $f(u)$: supprimer la première ou dernière lettre de $u$
  $\{(1,2,3,2,1), (1,2,3,2), (2,3,2,1), (2,3,2), ()\}$

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c5b1ed41608ab4f65a516468bb0de780", "grade": false, "grade_id": "cell-87e84eed2d08ea7e", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "subslide"}}

**Exercice**

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6d60ce38c045b0e89a94564e7d71ac90", "grade": false, "grade_id": "cell-08700a3e88cf3428", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Soit $C_n$ l'ensemble récursivement défini par:
- $R=\{ (\underbrace{1,1,\cdots,1}_n)\}$
- $f$ qui a une liste associe toute les listes obtenues en regroupant et sommant deux entrées consécutives<br>
Par exemple, $f((2,3,1,1)) = \{(5,1,1), (2,4,1), (2,3,2)\}$

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "9a96022c9f2dfc2eb176015fee285b16", "grade": true, "grade_id": "cell-55b16a3d76390cbb", "locked": false, "points": 4, "schema_version": 3, "solution": true, "task": false}}

- Calculer à la main les **quatres** éléments de $C_3$, sans oublier $(3)$!
- Calculer avec la machine tous les éléments de $C_6$.
- Combien y en a t'il?

- Même chose pour $C_1,C_2,C_3,C_4,C_5$.
- Que conjecturez vous?
- Pouvez vous le prouver?

$C_3 = \{(1,1,1),(2,1),(1,2),(3)\}$

```{code-cell} ipython3
def calculer_cn(n):
    assert n >= 1
    
    def toutes_sommes(t):
        """
        :param t: n-uplet non-vide
        :return: ensemble des n-uplets des sommes consécutives
        """
        assert len(t) > 0
        
        if len(t) == 1:
            return t
        
        res = set()
        i = 0
        while i < len(t) - 1:
            # Pas terrible d'utiliser des slices mais je ne trouve pas mieux
            res.add((() if i == 0 else t[0:i]) + (t[i] + t[i + 1],) + (() if i == len(t) - 2 else t[i+2:]))
            i += 1
        return res
    
    res = set([tuple([1 for _ in range(n)])])
    for i in range(n, 1, -1):
        for t in res:
            if len(t) == i:
                # L'union peut être coûteux
                res = res.union(toutes_sommes(t))
    return res
```

```{code-cell} ipython3
assert calculer_cn(1) == {(1,)}
assert calculer_cn(2) == {(1,1), (2,)}
assert calculer_cn(3) == {(1,1,1), (2,1), (1,2), (3,)}
assert calculer_cn(4) == {(1,1,1,1), (2,1,1), (1,2,1), (1,1,2), (3,1), (2,2), (1,3), (4,)}
```

```{code-cell} ipython3
len(calculer_cn(5))
```

```{code-cell} ipython3
len(calculer_cn(6))
```

On peut conjecturer qu'il y a $2^{n-1}$ éléments dans $C_n$.

De manière informelle, il est normal d'arriver à une puissance de ce genre car on travaille en fait avec un arbre. C'est un arbre qui au départ de la racine à $n - 1$ branches, puis à l'étage en-dessous chaque fils à $n - 2$ branches, jusqu'à  arriver à 1 branche par fils. Il se trouve que on arrive à l'équivalent d'un arbre binaire d'après la conjecture. Mais il est difficile de savoir quels n-uplets vont être répétés lors du déroulement, donc éliminés du comptage.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3cae93e9b4d8f17083111e89058f309f", "grade": false, "grade_id": "cell-c619ca94679e9fbb", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice** (bonus)
Une *permutation* est une liste d'entiers telle que, si $n$ est sa longueur, alors tous les entiers de $1$ à $n$ apparaissent exactement une fois. Décrire l'ensemble des permutations comme un ensemble énuméré. Utiliser cela pour lister toutes les permutations de longueur $n\leq 6$

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 89063f64eacfefe6cbaa35413bbc1aab
  grade: true
  grade_id: cell-e75b5213a8b5e829
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
def permutation(n):
    assert n >= 0
    if n == 0:
        return []
    elif n == 1:
        return [(n,)]
    else:
        res = []
        for x in permutation(n - 1):
            # On insère (n,) entre tous les nombres pour chaque tuple
            for i in range(n):
                res.append(x[:i] + (n,) + x[i:])
        return res
```

```{code-cell} ipython3
permutation(6)
```

```{code-cell} ipython3

```
