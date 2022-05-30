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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "bd99d756b40f0474676be6e6c593d4d3", "grade": false, "grade_id": "cell-f831ac926c595e4c", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

# [Parcours en largeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_largeur) et calcul de distance

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "947b25e62854e71e22de6946a4d80239", "grade": false, "grade_id": "cell-05263ea2cabe0edb", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Dans cette feuille, nous raffinons l'algorithme de parcours de graphe
vu précédemment pour calculer des *distances simples* entre sommets
d'un graphe, ne tenant pas compte des poids des arêtes. Nous suivons
la même démarche que pour notre premier algorithme: invariants, test
sur des exemples, visualisation, complexité, preuve de correction.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "23c0034b2e510f1f1a3400c99b89714c", "grade": false, "grade_id": "cell-214af97aa4f0777b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Définition** *distance simple* dans un graphe

La *distance* entre deux sommets $u$ et $v$ d'un graphe $G$ est le
plus petit entier $l$ tel qu'il existe un chemin avec $l$ arêtes
allant de $u$ à $v$. S'il n'y a pas de tel chemin, alors la distance
est $\infty$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "bfa7b695e373cb1d5d66936307ce3b26", "grade": false, "grade_id": "cell-a29ce09f98694e4c", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice**

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e9f25ef2a01d4b4c19eb7f995dae0d2f", "grade": false, "grade_id": "cell-5c625fc342cbb86c", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

1. Complétez la fonction suivante qui implante un parcours en largeur,
   en vous laissant guider par les invariants fournis:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 3753a0f4df73daed96c9bd04d7e1f749
  grade: false
  grade_id: cell-fa2ebcc093dd410e
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
from graph import Graph, Node
from typing import Dict
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: b2e6ad4af2509060a04d50ec2721292c
  grade: false
  grade_id: cell-fa2ebcc093dd410f
  locked: false
  schema_version: 3
  solution: true
  task: false
slideshow:
  slide_type: fragment
---
def parcours_en_largeur(G: Graph, u: Node) -> Dict[Node, int]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: un dictionnaire associant à chaque sommet `v` accessible depuis `u` sa distance depuis `u`
    """
    distances = {u: 0} # L'ensemble des sommets déjà rencontrés
    todo      = [u]    # Une liste de sommets à traiter
    
    while todo:
        # Invariants:
        # - Si `v` est dans `distance`, alors il y a un chemin de `u` à `v`,
        #   et distance[v] contient la distance de `u` à `v`;
        # - Si `v` est dans `distance` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans `distance`
        v = todo.pop(0)
        for w in G.neighbors(v):
            if w not in distances:
                distances[w] = distances[v] + 1
                todo.append(w)
    return distances
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "cc1331bda55887175f90dc644c237d87", "grade": false, "grade_id": "cell-5deaa43c0e1f7147", "locked": true, "schema_version": 3, "solution": false, "task": false}}

2. Testez que votre fonction est correcte sur les exemples suivants.
   Si elle ne l'est pas, utilisez la question suivante pour déboguer!

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 951cbf527b66f2f1e2ef4c4dc627a817
  grade: false
  grade_id: cell-f22a5fce9c1128ba
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
  checksum: 7480702ba4ed85933fb8758081ab2ee1
  grade: false
  grade_id: cell-f22a5fce9c1128bb
  locked: true
  schema_version: 3
  solution: false
  task: false
---
C3 = examples.C3()
C3.edges()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 93935616489bffbe57b12b2d7dd6a04a
  grade: true
  grade_id: cell-e31ac5a2ec1ca694
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert parcours_en_largeur(C3, 0) == {0: 0, 1: 1, 2: 2}
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c67e08465d3ad8bd8bf9e16433708f63
  grade: false
  grade_id: cell-f22a5fce9c1128bd
  locked: true
  schema_version: 3
  solution: false
  task: false
---
T3 = examples.T3()
T3.edges()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b099bafd3e1b5c19579a359b2d30902c
  grade: true
  grade_id: cell-2a1fe26cce698ead
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert parcours_en_largeur(T3, 0) == {0: 0, 1: 1, 2: 1}
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 599bf832c16be88d6e1ac088b61f273b
  grade: false
  grade_id: cell-f61de6336f6d75cc
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from graph import examples
G = examples.parcours_directed()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 8d68f3d8d7ab81f16f43042b4251b89c
  grade: true
  grade_id: cell-8d83da87d56c871c
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert parcours_en_largeur(G, "H") == {'H': 0, 'F': 1, 'G': 2}
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 201a810f58277d5efc93b9c5a73d9e27
  grade: true
  grade_id: cell-1cefa7a59eae7cc6
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert parcours_en_largeur(G, "A") == {'A': 0, 'B': 1, 'G': 1, 'F': 1, 'C': 2, 'H': 2, 'D': 3}
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "af4b7c8f06f293aac77397ac6020a833", "grade": false, "grade_id": "cell-ae29bebcfa0eefba", "locked": true, "schema_version": 3, "solution": false, "task": false}}

3. Instrumentez votre code comme dans la feuille précédente pour visualiser son exécution

```{code-cell} ipython3
import copy
```

```{code-cell} ipython3
def parcours_visualisation(G: Graph, u: Node) -> Dict[Node, int]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: un dictionnaire associant à chaque sommet `v` accessible depuis `u` sa distance depuis `u`
    """
    distances = {u: 0} # L'ensemble des sommets déjà rencontrés
    todo      = [u]    # Une liste de sommets à traiter
    
    player.player.reset(copy.deepcopy(locals()))
    
    while todo:
        # Invariants:
        # - Si `v` est dans `distance`, alors il y a un chemin de `u` à `v`,
        #   et distance[v] contient la distance de `u` à `v`;
        # - Si `v` est dans `distance` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans `distance`
        v = todo.pop(0)
        # Observation des variables locales
        player.set_value(copy.deepcopy(locals()))
        for w in G.neighbors(v):
            if w not in distances:
                distances[w] = distances[v] + 1
                todo.append(w)
                # Observation des variables locales
                player.set_value(copy.deepcopy(locals()))
        v = None
        # Observation des variables locales
        player.set_value(copy.deepcopy(locals()))
    return distances
```

```{code-cell} ipython3
import graph_algorithm_player
variables = [{'name': 'G',      'type': 'graph' },
             {'name': 'distances', 'type': 'dict', 'color': 'green',  'display': True},
             {'name': 'todo',   'type': 'nodes', 'color': 'red',    'display': True},
             {'name': 'v',      'type': 'node',  'color': 'yellow', 'display': True}]
#player = graph_algorithm_player.GraphAlgorithmPlayer(variables=variables)
#player
```

```{code-cell} ipython3
#parcours_visualisation(G, "A")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4a54b3dff3906ba080e83120f4df2c48", "grade": false, "grade_id": "cell-c825b936675348a7", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice** Complexité

Donner une borne de complexité pour l'algorithme `parcours_en_largeur`.

Note: pour simplifier, nous avons utilisé une liste pour `todo`. Pour
avoir une bonne complexité, il faudrait utiliser une *file* (FIFO),
typiquement implantée au moyen d'une liste chaînée et non un tableau
comme dans les listes Python. Voir par exemple `queue.SimpleQueue`.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2d3be46d5a5cbd96f7ba617453e3cda7", "grade": false, "grade_id": "cell-f3846db56cd75ff8", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Bonus: chronométrez votre code sur des graphes de taille croissante
afin de tracer une courbe de complexité pratique et vérifier
empiriquement que votre code a la complexité voulue.

**Indication**: vous pouvez par exemple utiliser les outils
`time.time`, `%timit`, `timeit` ou
[bleachermark](https://github.com/miguelmarco/bleachermark) (note: ce
dernier n'est pas encore compatible Python 3).

```{code-cell} ipython3
import random

def random_graph(n_nodes=10, n_edges=5):
    nodes = [i for i in range(n_nodes)]
    edges = []
    for i in nodes:
        for _ in range(n_edges):
            j = random.randint(0, n_edges-1)
            if i != j:
                edges.append((i, j, 1))
    return Graph(nodes=nodes, edges=edges)
```

```{code-cell} ipython3
import time

def mesurer_parcours(graphs):
    measures = []    
    for g in graphs:
        t1 = time.time()
        parcours_en_largeur(g, 0)
        t2 = time.time()
        measures.append(t2-t1)
    return measures
```

```{code-cell} ipython3
import time
import matplotlib.pyplot as plt

max_nodes = 300

# Augmentation du nombre de sommets
graphs = []
x = [n for n in range(100, max_nodes, 100)]
for n_node in x:
    graphs.append(random_graph(n_node))
    
y = mesurer_parcours(graphs)
#plt.plot(x, y)
```

```{code-cell} ipython3
# Augmentation du nombre d'arêtes

max_edges = 200

graphs = []
x = [e for e in range(50, max_edges, 50)]
for n_edge in x:
    graphs.append(random_graph(n_nodes=500, n_edges=n_edge))
    
y = mesurer_parcours(graphs)
#plt.plot(x, y)
```

D'après les expériences réalisées ci-dessus avec des graphes générés aléatoirement la complexité temporelle évolue de manière relativement linéaire par rapport au nombre d'arêtes, et de manière plutôt quadratique par rapport au nombre de sommets.

L'algorithme de parcours en largeur utilisé ici est quasiment identique à celui du parcours de graphe de la feuille précédente. À la différence près que `todo` est une liste Python donc il y a un risque pour que l'opération `todo.pop()` soit un peu plus coûteuse que dans le cas des listes chaînées. Mais on ignore ce point et on suppose que c'est en temps constant. De plus, au lieu d'ajouter dans un ensemble `marked` les éléments observés on crée une entrée dans un dictionnaire `distances` pour indiquer la distance du sommet `w` par rapport au sommet `u` de départ. Or, l'ajout et l'accès dans un dictionnaire est supposé en temps constant de la même manière que pour l'ajout dans un ensemble. Donc cela ne change rien à la complexité qui reste en $n^2$ avec n le nombre de sommets, en gardant le même modèle de complexité que précédemment.

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f870fd88ac1ea46cf34b92b4ae6e6023", "grade": true, "grade_id": "cell-4602f238ddb35643", "locked": false, "points": 2, "schema_version": 3, "solution": true, "task": false}}

**Exercice** Preuve de correction

(a) Si `v` est dans `distances`, alors il y a un chemin de `u` à `v`, et distances\[v\] contient la distance de `u` à `v`
(b) Si `v` est dans `distances` et pas dans `todo` alors tous les voisins de `v` sont dans `distances`

À l'initialisation (a) est respecté car `distances = {u: 0}` or le chemin de `u` à `u` existe toujours et a bien une distance de 0 (aucune arête pour aller de `u` à `u`). De plus, (b) est respecté car `u` est à la fois dans `distances` et `todo`.

En fin de boucle while l'invariant (a) est respecté car il y a un chemin de `v` à `w` puisque `w` est voisin de `v` or comme `v` est dans `distances` il y a un chemin de `u` à `v` par hypothèse de récurrence, donc au total un chemin de `u` à `w`. De plus, `distances[w]` contient `distances[v] + 1` car par hypothèse de récurrence `distances[v]` contient la distance de `u` à `v`, or il y a une seule arête entre `v` et `w`. Enfin, l'invariant (b) est respecté car à chaque itération on supprime `v` de `todo` puis on visite tous les voisins `w` de `v` pour ajouter `distances[w]` aux distances connues.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "41e3521e65104239288bbab69f24f653", "grade": false, "grade_id": "cell-c1fde793cc0a2414", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Conclusion

Dans cette feuille, vous avez mené en toute autonomie l'implantation
et l'étude d'un autre parcours de graphe pour mettre en pratique tout
ce que nous avions vu dans la fiche précédente. Bravo!
