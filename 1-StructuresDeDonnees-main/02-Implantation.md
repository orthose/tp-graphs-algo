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

# Implantation

+++

## Rappels et exemples Python sur les dictionnaires et compréhensions

Suivez le tutoriel suivant: http://doc.sagemath.org/html/en/thematic_tutorials/tutorial-comprehensions.html

Puis analysez les exemples suivants:

```{code-cell} ipython3
l = [3,2,1,0]
[ i**2    for i in l ]
```

```{code-cell} ipython3
l = ["a", "z", "b"]
d = {l[i] : i for i in range(len(l))}
```

```{code-cell} ipython3
for v in d.keys():
    print(v)
```

```{code-cell} ipython3
[(v, 1) for v in l]
```

## Conversions

+++

**Exercice:**

Choisissez une des structure de données de graphes que l'on a vues
(liste d'arêtes, dictionnaire des voisins, dictionnaire d'arêtes,
matrice d'adjacence).

Implantez des fonctions Python `from_matrix`, `from_edges`,
`from_neighbor_dict`, `from_edge_dict`. Par exemple, la fonction
`from_matrix` prendra un graphe représenté par une matrice d'adjacence
et renverra le même graphe dans la structure de donnée que vous avez
choisi.

Testez ces fonctions sur les exemples de la fiche précédente.

```{code-cell} ipython3
from typing import Dict, List, Tuple
```

```{code-cell} ipython3
# Je choisis la liste d'arêtes comme structure de sortie
def from_matrix(g:List[List[int]]) -> List[Tuple[int, int, int]]:
    assert len(g) > 0 and len(g[0]) > 0
    return [(i, j, g[i][j]) for i in range(len(g)) for j in range(len(g[0])) if g[i][j] != 0]
```

```{code-cell} ipython3
def from_neighbor_dict(g:Dict[int, Tuple[int, int]]) -> List[Tuple[int, int, int]]:
    return [(v1, v2, c) for v1 in g for (v2, c) in g[v1]]
```

```{code-cell} ipython3
def from_edge_dict(g:Dict[Tuple[int, int], int]) -> List[Tuple[int, int, int]]:
    return [(v1, v2, g[(v1, v2)]) for (v1, v2) in g]
```

```{code-cell} ipython3
L = [ (1,2,1), (1,3,1), (2,4,2), (3,4,0), (4,5,3) ]

g = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3], [0, 0, 0, 0, 0, 0]]
for x in from_matrix(g):
    assert x in L

g = {1: [(2, 1), (3, 1)], 2: [(4, 2)], 3: [(4, 0)], 4: [(5, 3)]}
assert from_neighbor_dict(g) == L

g = {(1, 2): 1, (1, 3): 1, (2, 4): 2, (3, 4): 0, (4, 5): 3}
assert from_edge_dict(g) == L 
```

## Une classe graphe

+++

Le fichier <a href="graph.py">graph.py</a> contient un squelette de classe pour
représenter des graphes. Votre mission pour la prochaine séance est de
compléter les méthodes non implantées. Le [rapport](Rapport.md)
contient des vérifications automatiques pour votre code. Utilisez le
au fur et à mesure pour suivre votre avancement et complétez le.
