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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "d41bfa52589cd39d02b7cce6e404d2fb", "grade": false, "grade_id": "cell-28d494e048f3ca33", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Plus courts chemins, avec poids: l'[algorithme de Dijkstra](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2aa560901671da92dab6758c349d72fd", "grade": false, "grade_id": "cell-2418dd5b544980bf", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

On considère le graphe suivant qui modélise un réseau routier:
<!-- By HB (Own work) [GFDL (http://www.gnu.org/copyleft/fdl.html) or CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons

<center>

<img src="media/DijkstraBis01.svg">

</center>
!-->

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a496651197da3c9bea017a280f0ef29e
  grade: false
  grade_id: cell-932285cf25ec6af1
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from graph import examples
G = examples.dijkstra()
G.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "32c631358c34369d5626ccf66282b856", "grade": false, "grade_id": "cell-541e8093bec607c5", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On souhaite calculer le plus court chemin entre deux sommets de ce graphe.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "293b24a63cda615f4243f85792234eaf", "grade": false, "grade_id": "cell-e111cf0686add8e0", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice**
1. Implantez l'algorithme de Dijskstra

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: d8489af7e478873b066773c143b6b093
  grade: false
  grade_id: cell-b31db819a71cdffd
  locked: false
  schema_version: 3
  solution: true
  task: false
---
from graph import Graph, Node, Dict
infinity = float('inf')
def dijkstra(G: Graph, e: Node) -> Dict[Node, int]:
    """
    Renvoie un dictionnaire associant à chaque sommet sa distance depuis `e`
    """
    # Initialisation
    distance = {v: infinity for v in G.nodes()} # distance de e à v
    distance[e] = 0 # distance de 0 pour aller de e à e
    todo = list(G.nodes()) # sommets à visiter
    
    while todo:
        
        # On choisit un sommet v non-visité et atteignable depuie e 
        # telle que la distance(e, v) soit minimale
        v = todo[0]
        dv = distance[v]
        for w in todo:
            dw = distance[w]
            if dv > dw:
                v = w
                dv = dw
                
        # Mise à jour des sommets à visiter    
        todo.remove(v)
                
        # Pour tous les voisins w de v on met à jour distance[w]
        for w in G.neighbors(v):
            distance[w] = min(distance[w], distance[v] + G.capacity(v, w))
            
    return distance
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "a45e96cf27882df09754131d7dbea6fc", "grade": false, "grade_id": "cell-9052d311cb4ac13d", "locked": true, "schema_version": 3, "solution": false, "task": false}}

2. Appliquez cette fonction au graphe `G` ci-dessus:

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 2e0bca3fd9fc01af654994bedd305fc9
  grade: false
  grade_id: cell-f52c1bf66d323bc2
  locked: false
  schema_version: 3
  solution: true
  task: false
---
distances = dijkstra(G, 'A')
print(distances)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "646f89cc1c5a06298411f94358d2612b", "grade": false, "grade_id": "cell-09260c8bcd80db6a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

En déduire la distance entre `A` et `J`, à mettre dans la variable `distance_AJ`:

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: c4b4ca3e455fd152e6b71f55744fd3b5
  grade: false
  grade_id: cell-1f02da44eb448e2d
  locked: false
  schema_version: 3
  solution: true
  task: false
---
distance_AJ = distances['J']
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 4cdb0c6782d42fd1c1a7ab80bb999a66
  grade: true
  grade_id: cell-4efcd06723aa15a5
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
# Vérifie votre résultat sans dévoiler la solution, par la magie des fonctions de hachage :-)
import hashlib
h = hashlib.md5(bytes(distance_AJ)).hexdigest() == '2f6064003b888e403627e493532fc751'
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ce650eb520938304735e7f74cdf5ee18
  grade: true
  grade_id: cell-0d543769776d9f6a
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
distances = dijkstra(G, "A")
assert distances["A"] == 0
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: f5a672969316dc0b04f2756192bdf43f
  grade: true
  grade_id: cell-4670834a66e9e247
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
assert sum(distances.values()) == 2774
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ec47e6b4c737c953b6dd29b52a656d49", "grade": false, "grade_id": "cell-73fa8b07519bc08b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

3. (Bonus) Adapter la fonction précédente pour qu'elle prenne deux sommets `e` et `f` et renvoie un plus court chemin entre `e` et `f`.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 7707819c72c8f3d542e9132401d38233
  grade: true
  grade_id: cell-6e6fadae5c937751
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
def dijkstra(G: Graph, e: Node, f: Node) -> Graph:
    """
    :param G: Graphe à analyser
    :param e: Sommet de départ
    :param f: Sommet d'arrivée
    :return: Plus court chemin de e à f sous forme d'un graphe
    """
    
    # Initialisation
    distance = {v: infinity for v in G.nodes()} # distance de e à v
    distance[e] = 0 # distance de 0 pour aller de e à e
    todo = list(G.nodes()) # sommets à visiter
    predecessor = dict() # sommets précécesseurs
    
    while todo:
        
        # On choisit un sommet v non-visité et atteignable depuie e 
        # telle que la distance(e, v) soit minimale
        v = todo[0]
        dv = distance[v]
        for w in todo:
            dw = distance[w]
            if dv > dw:
                v = w
                dv = dw
                
        # Mise à jour des sommets à visiter    
        todo.remove(v)
                
        # Pour tous les voisins w de v on met à jour distance[w]
        for w in G.neighbors(v):
            dvw = distance[v] + G.capacity(v, w)
            if distance[w] > dvw:
                distance[w] = distance[v] + G.capacity(v, w)
                # Le prédécesseur de w est v donc on a une arête de v à w
                predecessor[w] = v
    
    # Construction du plus court chemin
    path = Graph()
    while f != e:
        path.add_node(f)
        g = predecessor[f]
        path.add_node(g)
        path.set_edge_capacity(g, f, G.capacity(g, f))
        f = g
        
    return path
```

```{code-cell} ipython3
dijkstra(G, 'A', 'J').edges()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6378da0514a1e3a4a7fd6ef6ac7b079a", "grade": false, "grade_id": "cell-bc2add573b4d29c0", "locked": true, "schema_version": 3, "solution": false, "task": false}}

4. (Bonus) Instrumentez votre fonction pour en visualiser l'exécution.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: e17102cb766d7f7c3e2a7bad5e5d07c0
  grade: true
  grade_id: cell-06c0e69a490a9644
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
import copy

def dijkstra_visualisation(G: Graph, e: Node) -> Dict[Node, int]:
    """
    Renvoie un dictionnaire associant à chaque sommet sa distance depuis `e`
    """
    # Initialisation
    distance = {v: infinity for v in G.nodes()} # distance de e à v
    distance[e] = 0 # distance de 0 pour aller de e à e
    todo = list(G.nodes()) # sommets à visiter
    
    player.set_value(copy.deepcopy(locals()))
    
    while todo:
        
        # On choisit un sommet v non-visité et atteignable depuie e 
        # telle que la distance(e, v) soit minimale
        v = todo[0]
        dv = distance[v]
        for w in todo:
            dw = distance[w]
            if dv > dw:
                v = w
                dv = dw
                
        # Mise à jour des sommets à visiter    
        todo.remove(v)
        
        player.set_value(copy.deepcopy(locals()))
                
        # Pour tous les voisins w de v on met à jour distance[w]
        for w in G.neighbors(v):
            distance[w] = min(distance[w], distance[v] + G.capacity(v, w))
            
    return distance
```

```{code-cell} ipython3
import graph_algorithm_player
variables = [{'name': 'G',      'type': 'graph' },
             {'name': 'distance', 'type': 'dict', 'color': 'green',  'display': True},
             {'name': 'todo',   'type': 'nodes', 'color': 'red',    'display': True},
             {'name': 'v',      'type': 'node',  'color': 'yellow', 'display': True}]
            
player = graph_algorithm_player.GraphAlgorithmPlayer(variables=variables)
player
```

```{code-cell} ipython3
dijkstra_visualisation(G, 'A')
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6508f3d1b1c6a16d213875d14b85868b", "grade": false, "grade_id": "cell-712564125b629eea", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Problème 1: Le chemin le plus rapide en métro de Montgallet à Billancourt ?
<center>

<img src="media/metro-paris.gif" width="50%">

</center>

1. Le fichier <a href="metro_complet.txt">metro_complet.txt</a> contient la description d'un graphe modélisant le métro de Paris. Consultez son contenu pour en comprendre le format.
2. Écrire une fonction qui lit le fichier et renvoie le graphe qu'il contient sous la forme d'un objet de type `Graph`.
3. Utilisez la fonction `dijkstra` pour calculer un plus court chemin de Montgallet à Billancourt!

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 665120a2ba92bf201f11ba072aba38a9
  grade: true
  grade_id: cell-7e01ead24612c65d
  locked: false
  points: 3
  schema_version: 3
  solution: true
  task: false
---
import re

def parser_metro(file:str="./metro_complet.txt") -> Graph:
    with open("./metro_complet.txt", 'r') as f:
        data = f.read().strip().split('\n') 
    i = data.index("noms sommets")
    j = data.index("coord sommets")
    k = data.index("arcs values")
    
    # Je pense que la table coord sommets ne sert à rien
    table_names = data[i+1:j]
    table_arcs = data[k+1:-1]
    nodes = dict()
    edges = list()
    
    for l in table_names:
        m = re.match(r"(\d{4}) (.+)", l)
        station = m.group(1)
        name = m.group(2)
        nodes[int(station)] = name
        
    for l in table_arcs:
        m = re.match(r"(\d+) (\d+) (\d+)", l)
        station1 = nodes[int(m.group(1))]
        station2 = nodes[int(m.group(2))]
        distance = m.group(3)
        edges.append((station1, station2, int(distance)))
    
    return Graph(nodes=nodes.values(), edges=edges)
```

```{code-cell} ipython3
G = parser_metro()
trajet = dijkstra(G, 'Montgallet', 'Billancourt')
trajet.edges()
```

```{code-cell} ipython3
trajet.show()
```

```{code-cell} ipython3

```
