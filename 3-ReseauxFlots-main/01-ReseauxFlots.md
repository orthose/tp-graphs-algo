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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "6a4348a74ac003194e0b90b0c165dc45", "grade": false, "grade_id": "cell-11990c9b55cde004", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

# Réseaux et flots dans les réseaux

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ff503e952b145d0c5c6f6528577a839c", "grade": false, "grade_id": "cell-333e0f3433b66d69", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

## Réseaux

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ee550adec005806d9f092f45f8130f0f", "grade": false, "grade_id": "cell-333e0f3433b66d70", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "-"}}

### Définition


On appelle *réseau* un graphe orienté, sans boucles (arêtes d'un noeud vers lui-même) ni arêtes multiples, dont les arêtes sont étiquetées par des nombres positifs. Par exemple, le graphe suivant est un réseau.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 72b8658a99fe8ae85bab1d39e267039f
  grade: false
  grade_id: cell-e3af0453eaba2473
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
from network import examples
examples.example1().show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3797eac72464f172e07ba6808c7d4d54", "grade": false, "grade_id": "cell-f2620759bdad4c94", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "subslide"}}

### Implantation

En terme d'implantation, un réseau est donc simplement un graphe. On a simplement rajouté une petite surcouche à la classe Graph de networkx pour une utilisation plus commode. La fonction `Network` est implantée dans le fichier `network.py`. Elle est basée sur les graphes de `newtorkx.graph` et ne dépend donc pas de l'implantation que vous avez réalisée dans les premières sections du cours.
Quelques exemples d'utilisation :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 1ee431b38f58ab254291a4b7304ec1d1
  grade: false
  grade_id: cell-86edca38999d3d7e
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
from network import Network
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c2cb976b48d9e001f26820c62cd31f74
  grade: false
  grade_id: cell-c09f7d339b609c20
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# on construit le réseau à partir d'une liste arêtes et de noeuds
# voici un réseau avec une seule arête
N = Network(edges = [(1,2,1)], nodes = [1,2])
N.show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 0b2dcb30c55d6a17aba94752f70dc35f
  grade: false
  grade_id: cell-c3714e429f9a00ae
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
# on peut modifier la capacité de l'arête
N.set_edge_capacity(1,2,2)
N.show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: afd430773dc7ea165befda7f0b8c4f4b
  grade: false
  grade_id: cell-369568754deff319
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
N.capacity(1,2)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b0089d3b5a984ad032136ed3617312ae
  grade: false
  grade_id: cell-5ae0522b67b33b88
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
list(N.predecessors(2))
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b45daa5e629362c51ec3afe8e85e1810
  grade: false
  grade_id: cell-854eddc57e07add2
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
list(N.successors(1))
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5190551f2047a43189b10d010c02abee", "grade": false, "grade_id": "cell-d3689ec78d56aeda", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Créer un réseau $N$ contentant 3 noeuds $0,1,2$ avec une arête $(0,1)$ de capacité 1 et une arête $(2,1)$  de capacité 2.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 0e96bc0152d07619e916d74ac167b8e0
  grade: true
  grade_id: cell-62fb331a405da5dd
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
N = Network(edges = [(0,1,1),(2,1,2)], nodes = [0,1,2])
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 2391f046e3c5d0ec007d17cd4b8abacf
  grade: true
  grade_id: cell-8290e66547ba7300
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert set(N.nodes()) == {0,1,2}
assert N.capacity(0,1) == 1
assert N.capacity(2,1) == 2
assert N.capacity(0,2) == 0
assert N.capacity(1,0) == 0
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "bb83ab12a4121fd4ededf8833a12d95a", "grade": false, "grade_id": "cell-d93b1073c69b8459", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

## Flots

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3c771339eb38a7f46d55f58912dca75e", "grade": false, "grade_id": "cell-d93b1073c69b8460", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "-"}}

### Définition

Un *flot* sur un réseau $r$ entre deux sommets $s$ et $t$ est une fonction $f$ qui associe un nombre à chaque arête de $r$ tel que:

 * $f(v1,v2)$ est toujours inférieur ou égal à la capacité de l'arête $(v1,v2)$ dans $r$;
 * pour tout sommet $a$ différent de $s$ et $t$, le *flot entrant* en $a$ est égal au *flot sortant* de $a$:
   $$ \sum_{v_1\rightarrow a} f(v_1,a) \qquad = \qquad \sum_{a\rightarrow v_2} f(a,v_2)\,,$$
   où les sommes ci-dessus portent respectivement sur les voisins entrants $v_1$ et les voisins sortants $v_2$ de $a$.
 
Pour reprendre l'analogie précédente : si on imagine que le réseau est un ensemble de tuyaux de différentes tailles, le flot est une façon de faire "couler" des éléments entrant en $s$ vers le sommet $t$. En chaque point, le nombre d'éléments qui arrivent est égal au nombre d'éléments qui sort.

Voilà par exemple un flot sur le réseau donné en exemple précédemment (avec $s = 0$ et $t = 6$).

Sur chaque arête, le premier nombre est la capacité tandis que le second nombre est le flot à travers l'arête.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 9df357f54e33204a96a10cc40a718f8a
  grade: false
  grade_id: cell-45dcccd4cd0d465a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from flow_examples import flow_examples
flow_examples.example1().show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "8164782e4b5c0f882aa1341ac586f8a4", "grade": false, "grade_id": "cell-7ed4578b9e74a57e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vous pouvez vérifier que le second nombre est toujours inférieur ou égal à la capacité de l'arête et que pour chaque point en dehors de 0 et 6, le flot entrant est égal au flot sortant. Par exemple, sur le sommet $2$, on a en flot entrant $1+1$ et en flot sortant $1+1$, sur le sommet 5, on a en flot entrant $2$ et en flot sortant $1+1$.

Le sommet de départ est appelé la *source* et le sommet d'arrivée la *cible*. Le flux net entrant sur la source est égal au flux net sortant de la cible, c'est ce qu'on appelle la *valeur globale* du flot. Dans l'exemple, la valeur globale est de $0+2+1-1 = 2$ (flux entrant sur la source) qui est bien égale à $1+3-2 = 2$ (flux sortant de la cible).

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "b2ea10d58fa8c7ba394eca51a61ef8fd", "grade": false, "grade_id": "cell-5c8dcd9d3de0fae6", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "subslide"}}

### Implantation

Pour l'implantation, nous allons considérer un flot comme un **double réseau** : le réseau de départ $r$ et un second réseau sur le même ensemble de sommets $f$ qui vérifie des propriétés particulières. 

Dans `flots.py` vous trouverez une classe partiellemment implantée.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: e2671e4a6bca09fbcab879595c36f8bf
  grade: false
  grade_id: cell-75b10e5447c07a6c
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
from flow import Flow
from network import Network
from network import examples
from flow_examples import flow_examples
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5893bba91306c9897fbea49faa7ff45a", "grade": false, "grade_id": "cell-11c2fac73886c67e", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Vous pouvez créer un flot vide à partir d'un réseau donné. 

Par exemple :

```{code-cell} ipython3
# 0 est la source, 6 la cible
# le paramètre check permet de vérifier les propriétés du flots (pas encore implanté)
F = Flow(examples.example1(), 0, 6, check = False)
```

```{code-cell} ipython3
F.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c2ac3901ac1ab251f33dabb9393d664b", "grade": false, "grade_id": "cell-3e3a1652e1279627", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Le flot contient le réseau de départ :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 244ad583e64dc39a19581376a91fc6f9
  grade: false
  grade_id: cell-4494ff1b4060dc2a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.network().show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: f70314cb9f225804cc0c65abb85deaf1
  grade: false
  grade_id: cell-45f8245c9f6279e8
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.source()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 20eef9be5e883a408ffa0d32a252e8f4
  grade: false
  grade_id: cell-7d90dbcbe2b1204f
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.target()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "943c5c7d6c901f98516ff504237d7175", "grade": false, "grade_id": "cell-d79d06e2f75694cc", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

On peut directement récupérer la capacité d'une arête.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c9635d2d5ae409b685cfbbbe67191152
  grade: false
  grade_id: cell-1e646267604acc60
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.capacity(5,6)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d2e455e12bd7cb2aa7d6e69e0e06d950
  grade: false
  grade_id: cell-0cfffce92293bb32
  locked: true
  schema_version: 3
  solution: false
  task: false
---
F.network().capacity(5,6)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "0b292f6b4911dba91ee77814c072d0d1", "grade": false, "grade_id": "cell-bb4f8fd9597d56df", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Un second réseau est stocké dans l'objet en tant que paramètre.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 39232067e037a4c4260d7d965eb4b26f
  grade: false
  grade_id: cell-a1efd69250a73703
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: '-'
---
F._flow.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ad6bd1fbcef45c2e80ebb54ec8c73e66", "grade": false, "grade_id": "cell-6ab8f4457705993e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On ne fait pas la différence entre aucune arête entre $i$ et $j$ et une arête de valeur nulle. C'est pour cela qu'ici on ne voit aucune arête: le flot est vide. Voici un deuxième exemple:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b6e7cf255aefb87158846a9897745015
  grade: false
  grade_id: cell-cf1f08bd8ffc13e0
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# le flot avec les deux réseaux superposés ainsi que la source et la cible 
flow_examples.example1().show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 145cf0b49d8e347d23499cf1376e9fcc
  grade: false
  grade_id: cell-6d95bf6e4356834d
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# le réseau sous-jacent
flow_examples.example1().network().show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ad45fda0fc74c29e740ffc727ff2837c
  grade: false
  grade_id: cell-fdf80fb5e9a7248f
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# le réseau du flot sous-jacent
flow_examples.example1()._flow.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "444fd5afd6e3b15f7e93bed818eba038", "grade": false, "grade_id": "cell-d479210b732dd818", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

La classe flow permet de directement récupérer les données du flot.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 6128c267e2192dc45dd80f4fe7340353
  grade: false
  grade_id: cell-f71b7c45d86e3e23
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
  checksum: 8a38ddbcea3aee35bffdda1d84fc8c5c
  grade: false
  grade_id: cell-d7e38b20472b6af1
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# le flot sur l'arête 0,1
F.flow(0,1)
```

```{code-cell} ipython3
# tous les flots sur l'ensemble des arêtes du réseau
F.flows()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "9525957f44c15096501a514f6d56889a", "grade": false, "grade_id": "cell-44e914b8f5fa277e", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

En utilisant les méthodes `predescessors` et `successors` comme ci-dessous, calculez les flots entrants et sortants sur le noeud $2$ que vous stockerez dans les variables `f_in` et `f_out`.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: eaf904f8295b84e00d9fc513feb3fb82
  grade: false
  grade_id: cell-1ba5fa38e7ddab19
  locked: true
  schema_version: 3
  solution: false
  task: false
---
list(F.network().predecessors(2))
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ac2bb953585b47f6e9b4243e94c6ea16
  grade: false
  grade_id: cell-5ccc1e19a113d03c
  locked: true
  schema_version: 3
  solution: false
  task: false
---
list(F.network().successors(2))
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 63c08d5c36cfdeea82945ff53680b146
  grade: true
  grade_id: cell-ae5d62de4fe381e8
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
f_in = sum([F.flow(x, 2) for x in F.network().predecessors(2)])
f_out = sum([F.flow(2, x) for x in F.network().successors(2)])
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c0ac18ad343d570ed226bea84d3c4530
  grade: true
  grade_id: cell-07b74e3fa059796e
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert f_in == 2
assert f_out == 2
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "121aa489b6ce3951603c7742d231fc25", "grade": false, "grade_id": "cell-a73dd6aecfb71347", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Implantez les méthodes `flow_in` et `flow_out` de la classe `Flow` du fichier `flow.py`.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3b05a0c3f9adeff58b590065e632b077", "grade": false, "grade_id": "cell-a73dd6aecfb71348", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

**Vérifier votre implantation en rédémarrant le noyau et en exécutant les cellules suivantes**

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 4d544a8036b353f26919c445cda9e153
  grade: false
  grade_id: cell-7a652aeea74d55b1
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
F = flow_examples.example1()
```

```{code-cell} ipython3
F.flow_in(1)
```

```{code-cell} ipython3
F.flow_out(1)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 31eb4f6ecc280daaae552a6838a96db6
  grade: true
  grade_id: cell-be2ccc0980963315
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert F.flow_in(1) == 2
assert F.flow_out(1) == 2
assert F.flow_out(0) == 2
assert F.flow_in(6) == 4
assert F.flow_out(6) == 2
assert F.flow_in(4) == 3
assert F.flow_out(4) == 3
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 3894cf39ff8176c8e36c82881c77c92f
  grade: false
  grade_id: cell-079b233c47effa15
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# affichage de la source pour correction
import inspect
print(inspect.getsource(Flow.flow_in))
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c468f4222bac70d9ff393a9fbcf7a6af
  grade: false
  grade_id: cell-c35eb7e521acd9d9
  locked: true
  schema_version: 3
  solution: false
  task: false
---
print(inspect.getsource(Flow.flow_out))
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "da6154165f736af7e3f351b2afa7aed5", "grade": false, "grade_id": "cell-c2d2ff7147a12083", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Implantez la méthode `global_value` et vérifiez ci-dessous.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 82469e716c4f9f5478486ec67caad0e1
  grade: false
  grade_id: cell-7b0231611e265546
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
F = flow_examples.example1()
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
  checksum: 781df3390199a886bd69a7e0258df30b
  grade: true
  grade_id: cell-95363eca0cc8f1d7
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert F.global_value() == 2
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: da8bdd06fe384360ac1004ee77508639
  grade: false
  grade_id: cell-6ad27e4748ecafc5
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# affichage de la source pour correction
import inspect
print(inspect.getsource(Flow.global_value))
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "fc7864481998aad11ebaa74b91377892", "grade": false, "grade_id": "cell-89abef27d8fa0f03", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Implantez les méthodes `check_capacity` et `check_in_out` et vérifier ci-dessous.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 1d0a4f4dd51d513114bb696a6f3202e3
  grade: false
  grade_id: cell-2fc634a0eb23b77a
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from flow import Flow
from flow_examples import flow_examples
F = flow_examples.example1()
```

```{code-cell} ipython3
F.check_capacity() 
```

```{code-cell} ipython3
F.check_in_out()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d1f0f0706855fe5eb1b3acfa58c619be
  grade: true
  grade_id: cell-5c80baaccdc8fe8d
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert flow_examples.example1().check_capacity()
assert flow_examples.example1().check_in_out()
assert not flow_examples.wrong_capacity().check_capacity()
assert not flow_examples.wrong_in_out().check_in_out()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 1fa21f402ec82aa5ba5a267bba05ca89
  grade: false
  grade_id: cell-0a9b5a2519def22c
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# affichage de la source pour correction
import inspect
print(inspect.getsource(Flow.check_capacity))
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: df089a84bd4effe05d55ba2bc64e5d26
  grade: false
  grade_id: cell-7863e4502a173951
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# affichage de la source pour correction
import inspect
print(inspect.getsource(Flow.check_in_out))
```

+++ {"slideshow": {"slide_type": "slide"}}

Vous voici arrivés à la fin de cette feuille d'introduction aux réseaux et aux flots.
Dans la feuille suivante, vous découvrirez un des algorithmes fondamentaux pour calculer
des flots.
