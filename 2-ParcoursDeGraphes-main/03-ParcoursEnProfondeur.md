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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "a4fb7dbd00101f46e7d957b519779f48", "grade": false, "grade_id": "cell-916f6e1be3f587ad", "locked": true, "points": 3, "schema_version": 3, "solution": false, "task": true}, "slideshow": {"slide_type": "subslide"}}

# [Parcours en profondeur](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur)

Dans cette feuille, nous étudions ce qu'il advient lorsque l'on
remplace la file `todo` de notre algorithme de parcours en largeur par
une pile.

Implantez l'algorithme de parcours en profondeur par une fonction
récursive comme sur la page wikipedia, et comparez les résultats des
deux algorithmes sur quelques exemples bien choisis.

+++

## Algorithmes

```{code-cell} ipython3
from graph import Graph, Node
from typing import Set
```

```{code-cell} ipython3
def parcours_en_largeur(G: Graph, u: Node) -> Set[Node]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = {u} # L'ensemble des sommets déjà rencontrés
    todo   = [u] # L'ensemble des sommets déjà rencontrés, mais pas encore traités
    
    while todo:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans dans `marked`
        v = todo.pop(0)
        for w in G.neighbors(v):
            if w not in marked:
                marked.add(w)
                todo.append(w)
    return marked
```

```{code-cell} ipython3
# Version récursive
def parcours_en_profondeur(G: Graph, u: Node) -> Set[Node]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = set() # L'ensemble des sommets déjà rencontrés
    
    # Fonction récursive qui empile les appels pour remplacer `todo`
    def explorer(v: Node) -> None:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` alors tous les voisins de `v` le seront
        # à la fin de la fonction explorer
        marked.add(v)
        for w in G.neighbors(v):
            if w not in marked:
                explorer(w)
    
    explorer(u)
    
    return marked
```

```{code-cell} ipython3
# Version avec pile
def parcours_en_profondeur(G: Graph, u: Node) -> Set[Node]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = {u} # L'ensemble des sommets déjà rencontrés
    todo   = [u] # L'ensemble des sommets déjà rencontrés, mais pas encore traités
    
    while todo:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans dans `marked`
        
        # On prend le sommet `v` de la pile et on le dépile
        v = todo.pop()
        # On ajoute directement `v` aux sommets visités
        marked.add(v)
        # On empile les voisins `w` de `v`
        for w in G.neighbors(v):
            if w not in marked:
                todo.append(w)
        
    return marked
```

## Tests unitaires
On teste que le parcours en largeur et le parcours en profondeur sont identiques à l'aide de tests unitaires.

```{code-cell} ipython3
from graph import Graph, examples
```

```{code-cell} ipython3
C3 = examples.C3()
C3.edges()
```

```{code-cell} ipython3
expected = {0, 1, 2}
assert parcours_en_largeur(C3, 0) == expected
assert parcours_en_profondeur(C3, 0) == expected
```

```{code-cell} ipython3
T3 = examples.T3()
T3.edges()
```

```{code-cell} ipython3
expected = {0, 1, 2}
assert parcours_en_largeur(C3, 0) == expected
assert parcours_en_profondeur(C3, 0) == expected
```

```{code-cell} ipython3
G = examples.parcours_directed()
G.edges()
```

```{code-cell} ipython3
expected = {'H', 'F', 'G'}
assert parcours_en_largeur(G, "H") == expected
assert parcours_en_profondeur(G, "H") == expected
```

```{code-cell} ipython3
expected = {'A', 'B', 'G', 'F', 'C', 'H', 'D'}
assert parcours_en_largeur(G, "A") == expected
assert parcours_en_profondeur(G, "A") == expected
```

## Visualisation

```{code-cell} ipython3
import copy

# Version avec récursion
def parcours_visualisation(G: Graph, u: Node) -> Set[Node]:
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = set() # L'ensemble des sommets déjà rencontrés
    
    player.player.reset(copy.deepcopy(locals()))
    
    # Fonction récursive qui empile les appels pour remplacer `todo`
    def explorer(v: Node) -> None:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` alors tous les voisins de `v` le seront
        # à la fin de la fonction explorer
        marked.add(v)
        # Observation des variables locales
        player.set_value(copy.deepcopy(locals()))
        for w in G.neighbors(v):
            if w not in marked:
                explorer(w)
    
    explorer(u)
    # Observation des variables locales
    player.set_value(copy.deepcopy(locals()))
    
    return marked
```

```{code-cell} ipython3
import graph_algorithm_player
variables = [{'name': 'G',      'type': 'graph' },
             {'name': 'marked', 'type': 'nodes', 'color': 'green',  'display': True},
             {'name': 'v',      'type': 'node',  'color': 'yellow', 'display': True}]
player = graph_algorithm_player.GraphAlgorithmPlayer(variables=variables)
player
```

```{code-cell} ipython3
parcours_visualisation(G, "A")
```

```{code-cell} ipython3
# Version avec pile
def parcours_visualisation(G, u):
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = {u} # L'ensemble des sommets déjà rencontrés
    todo   = [u] # L'ensemble des sommets déjà rencontrés, mais pas encore traités
    
    player.player.reset(copy.deepcopy(locals()))
    
    while todo:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans dans `marked`
        v = todo.pop()
        marked.add(v)
        for w in G.neighbors(v):
            if w not in marked:
                todo.append(w)
        player.set_value(copy.deepcopy(locals()))
    player.set_value(copy.deepcopy(locals()))
        
    return marked
```

```{code-cell} ipython3
import graph_algorithm_player
variables = [{'name': 'G',      'type': 'graph' },
             {'name': 'marked', 'type': 'nodes', 'color': 'green',  'display': True},
             {'name': 'todo', 'type': 'node', 'display':True},
             {'name': 'v',      'type': 'node',  'color': 'yellow', 'display': True}]
player = graph_algorithm_player.GraphAlgorithmPlayer(variables=variables)
player
```

```{code-cell} ipython3
parcours_visualisation(G, "A")
```

## Conclusion

Le parcours en profondeur donne le même résultat que le parcours en largeur. Simplement, les sommets sont parcourus dans un ordre différent. Le parcours en profondeur va découvrir tous les chemins possibles en s'arrêtant à chaque fois qu'il arrive sur un puits.

```{code-cell} ipython3

```
