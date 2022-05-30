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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c14fa6ffbe6888e2a21ff1746454ce8f", "grade": false, "grade_id": "cell-ccee3dfdd5a11682", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

# Étude d'un algorithme de parcours de graphes

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e9d9816b4f4a5eefebded09fcc1dc801", "grade": false, "grade_id": "cell-ed2d68bc54d324e9", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

## Définitions

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "996c72640d2709706ad02ad5d34b6c20", "grade": false, "grade_id": "cell-aae8364f24aec79f", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

Soit $G$ un graphe.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "51218c24c0fb7e11d7fa3371a1dd8a15", "grade": false, "grade_id": "cell-6eb93809ad94640a", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

- un *chemin* est une suite de sommets $(v_0, v_1, v_2, ...)$ tel qu'il existe une arête entre chaque paire de sommets $v_i$ et $v_{i+1}$

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "8911e275bed3f693cf525c3a27f9be96", "grade": false, "grade_id": "cell-48f1ea9573bd68a6", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

- la *distance* entre deux sommets `u` et `v` est la longueur du plus court chemin entre `u` et `v` (ou la somme des poids des arêtes).

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f2d1b8db563a8abd43d424bcee024db3", "grade": false, "grade_id": "cell-fa06e6c7cc8c3ed4", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "fragment"}}

- On suppose ici que $G$ est non orienté. La *composante connexe* d'un sommet $u$ de $G$ est l'ensemble des sommets atteignables depuis $u$ en suivant un chemin dans $G$.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4a7cadae2d36929c140856b8cba2ec0c", "grade": false, "grade_id": "cell-ac97467184074185", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

## L'algorithme

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "22f8853504757d641ee4f535c65519cf", "grade": false, "grade_id": "cell-ef9eaf0a20c498d9", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "skip"}}

L'objectif de cette feuille est d'étudier l'algorithme suivant:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 8df2789f0825b5f23560b739317d20b2
  grade: false
  grade_id: cell-73c37b70b97f28a5
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "1ac61f51f6732d9b72392248026abe44", "grade": false, "grade_id": "cell-17deab189916256c", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "subslide"}}

## Étude sur un exemple
Nous allons commencer par étudier le comportement de cet algorithme sur le graphe suivant:

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
from graph import examples
#from graph_networkx import examples
G = examples.parcours_directed()
G.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "b1ea36d98505f33eb88ba2e7ad1eda7f", "grade": false, "grade_id": "cell-f767fd72662d19e5", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "skip"}}

**Note:** Si votre classe `Graph` n'est pas au point, remplacez `graph` par `graph_networkx` ci-dessus.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2510daff28ad241fdd7b725b91bab848", "grade": false, "grade_id": "cell-2af874cc82c7b754", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Exercice**
- Copiez le graphe ci-dessus sur une feuille de papier;
- Uniquement en consultant la documentation, prédire quel devrait être le résultat de l'algorithme appliqué au graphe ci-dessus avec `u="D"`;
- Vérifiez en exécutant la fonction `parcours` ci-dessous.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 86b2b2bdfaf7629d0db682c001aef9e9
  grade: false
  grade_id: cell-c7f16a80382e4274
  locked: false
  schema_version: 3
  solution: true
  task: false
---
parcours(G, "D")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "23f08ea4d3a014533fdeca2a55540507", "grade": false, "grade_id": "cell-ac67e0e2dfff3530", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Tests

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 94b5c9cef807a4709ceb61c2b0fd87e0
  grade: false
  grade_id: cell-459565fce15f98c2
  locked: true
  schema_version: 3
  solution: false
  task: false
---
H = examples.cours_1_reseau()
assert parcours(G, "A") == {'A', 'B', 'C', 'D', 'F', 'G', 'H'}
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 8044c6c71570754ff3af4073116cd098
  grade: false
  grade_id: cell-667069433f962551
  locked: true
  schema_version: 3
  solution: false
  task: false
---
assert parcours(G, "B") == {'B', 'C', 'D', 'F', 'G', 'H'}
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ad874ad53d3a90a731b8293fda1deefb
  grade: false
  grade_id: cell-e65408844acff6a6
  locked: true
  schema_version: 3
  solution: false
  task: false
---
H = examples.cours_1_G()
assert sorted(parcours(H, 3)) == [0, 1, 2, 3, 4, 5]
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: cbe78e82f9cb0a189ee9715f443e62d8
  grade: false
  grade_id: cell-b0cdb8ca938b180d
  locked: true
  schema_version: 3
  solution: false
  task: false
---
H = examples.disconnected()
assert sorted(parcours(H, 1)) == [1, 2, 5]
assert sorted(parcours(H, 3)) == [3, 4]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "95ddbf8666b4f4e3011330e272b39812", "grade": false, "grade_id": "cell-59f5a82baa8c62f1", "locked": true, "schema_version": 3, "solution": false, "task": false}, "slideshow": {"slide_type": "slide"}}

## Visualisation

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "65c8b2182c5a4fb8a8b9341e4014cd46", "grade": false, "grade_id": "cell-398990d2b682d2a7", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Nous allons maintenant visualiser l'exécution de notre algorithme. Pour cela, nous allons:
1. instrumenter le code en insérant des observations des variables locales aux endroits clé (comme lorsque l'on débogue avec `print`)
2. définir une visualisation de ses variables locales

Exécutez les cellules ci-dessous, jusqu'à l'appel à la fonction `parcours`, puis jouez avec la «télécommande» pour exécuter le code pas à pas, revenir en arrière, etc.

Note: il y a encore deux boggues: la marche arrière en continu ne fonctionne pas et les valeurs ne sont mises à jour que en pas à pas.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ed1b4237738970526272ef3a1f41a64d
  grade: false
  grade_id: cell-4d1d8a9f934d9313
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
import copy
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ec71843b0daa96cd818f78fac2c0097f
  grade: false
  grade_id: cell-b77ea9ac5df0a877
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
def parcours_visualisation(G, u):
    """
    INPUT:
    - 'G' - un graphe
    - 'u' - un sommet du graphe
    
    OUTPUT: la liste des sommets `v` de `G`
            tels qu'il existe un chemin de `u` à `v`
    """
    marked = {u} # L'ensemble des sommets déjà rencontrés
    todo   = {u} # L'ensemble des sommets déjà rencontrés, mais pas encore traités
    
    player.player.reset(copy.deepcopy(locals()))
    
    while todo:
        # Invariants:
        # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
        # - Si `v` est dans `marked` et pas dans `todo`
        #   alors tous les voisins de `v` sont dans dans `marked`
        v = todo.pop()
        # Observation des variables locales
        player.set_value(copy.deepcopy(locals()))
        for w in G.neighbors(v):
            
            if w not in marked:
                marked.add(w)
                todo.add(w)
                # Observation des variables locales
                player.set_value(copy.deepcopy(locals()))
        v = None
        # Observation des variables locales
        player.set_value(copy.deepcopy(locals()))
    return marked
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 412be7ce4bd89c9ead4ffced5ec12932
  grade: false
  grade_id: cell-ddf0b04bb2d33451
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
import graph_algorithm_player
variables = [{'name': 'G',      'type': 'graph' },
             {'name': 'marked', 'type': 'nodes', 'color': 'green',  'display': True},
             {'name': 'todo',   'type': 'nodes', 'color': 'red',    'display': True},
             {'name': 'v',      'type': 'node',  'color': 'yellow', 'display': True}]
player = graph_algorithm_player.GraphAlgorithmPlayer(variables=variables)
player
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ca2c268c3c60b85ad9cb6be13d9d2f17
  grade: false
  grade_id: cell-c53b8540b921c69e
  locked: true
  schema_version: 3
  solution: false
  task: false
slideshow:
  slide_type: fragment
---
parcours_visualisation(G, "A")
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "dd81e5ab696b5a001b8e808fa9f76574", "grade": false, "grade_id": "cell-13cd85307a1b10d3", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Analyse théorique et invariants

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ee3fba8d639125919a54f9ac093f5dc9", "grade": true, "grade_id": "cell-1de49020d90d7772", "locked": false, "points": 2, "schema_version": 3, "solution": true, "task": false}}

**Exercice**: Complexité

Majorer la complexité de l'algorithme. Pour cela, choisir un *modèle de complexité*: opération(s) élémentaires et métrique(s) pour la taille des données en entrée. Puis considérer combien de fois chaque sommet est manipulé, combien de fois chaque arête est manipulée. Donner votre réponse ci-dessous, en rappellant la complexité des opérations de votre implantation de `Graph` qui sont utilisées.

On peut supposer que chaque arête est reliée avec toutes les autres. Ce serait le pire des cas. A chaque arête visitée on visite tous les voisins, mais on ne revisite pas les sommets déjà visités.

Soit `n` le nombre de sommets du graphe. On considère une opération élémentaire comme l'assignation d'une valeur à la variable `w`.

On va regarder les `n` sommets et à chaque fois on regarde les voisins ce qui est linéaire sur le nombre de sommets d'après mon implémentation de Graph.successors(). Donc je suis de l'ordre de $n^2$ soit quadratique. En réalité moins car je visite de moins en moins de sommets.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f44466e794a1d2a62d9dc7f141a26b5b", "grade": false, "grade_id": "cell-471de1d0f2917ac8", "locked": true, "schema_version": 3, "solution": false, "task": false}}

L'exercice précédent a confirmé qu'il s'agissait bien d'un algorithme: il termine en un temps fini. Il reste à démontrer qu'il est correct.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e78ac27a52498e02e075112c8ab7857e", "grade": false, "grade_id": "cell-08521a9de48faa86", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Vous avez remarqué les *invariants* marqués en commentaires dans le code. Ce sont des propriétés qui sont sensées être vérifiées à toutes les itérations de la boucle.

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "8ac75c9d36dd765cd942022d60b4df45", "grade": true, "grade_id": "cell-f7a916021445d22e", "locked": false, "points": 4, "schema_version": 3, "solution": true, "task": false}}

**Exercice** Preuve de correction

1. Vérifiez que les invariants sont respectés à l'initialisation
2. Vérifiez que, à chaque itération de la boucle while, si les invariants sont respectés au début de l'itération, alors ils le sont encore à la fin
3. Qu'en déduisez vous par récurence?
4. Concluez en montrant que, s'il y a un chemin de `u` à `v`, alors `v` est dans `marked` à la fin de l'exécution de l'algorithme

Rappel des invariants :
(a) Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
(b) Si `v` est dans `marked` et pas dans `todo` alors tous les voisins de `v` sont dans dans `marked`


1. `marked = {u}` et `todo = {u}` donc (a) est respecté car il y a bien un chemin immédiat de `u` à `u` et (b) est respecté car `u` est à la fois dans `marked` et `todo`.

2. On prend un `v` élément de `todo` il y a un risque que (b) ne soit plus respecté. On regarde les voisins de cet élément. Si un `w` voisin n'est pas marqué il est ajouté à `marked` et `todo`. Donc à la fin de la boucle while on a (a) respecté car on a un chemin de `v` à `w` (puisqu'ils sont voisins) et par hypothèse de récurrence on a un chemin de `u` à `v` donc le chemin de `u` à `w` est valide or `w` a été ajouté à `marked`. On a également (b) respecté car l'opération `v = todo.pop()` retire l'élément `v` de `todo` et que par la suite la boucle for enregistre tous les voisins `w` de `v` dans `marked`.

3. Par récurrence, les invariants (a) et (b) sont toujours respectés en fin de parcours de graphe lorsque `todo` est vide.

4. S'il y a un chemin de `u` à `v` alors `v` est nécessairement dans `marked` à la fin de l'exécution de l'algorithme car on a l'invariant (a) qui est respecté en fin d'algorithme.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "04f85af3f7f5049e3906244e22c67247", "grade": false, "grade_id": "cell-5dbfbfd82f6bfb1a", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Conclusion

Dans cette feuille, nous avons étudié un algorithme au moyen de deux outils:
- L'instrumentation du code pour observer visuellement son exécution
- Les invariants pour démontrer la correction de l'algorithme

Nous utiliserons systématiquement ces outils dans la suite du cours.

Les invariants sont des outils très puissants pour le programmeur. Ils jouent le même rôle que les hypothèses de récurences dans les démonstrations. Ils permettent de se convaincre après coup que les programmes sont corrects. Au moins aussi important, ce sont des guides précieux sur lesquels s'appuyer au moment de la programmation elle même. En fait, bien souvent, une fois que l'on a choisis ses invariants, l'écriture du programme est quasiment imposée.

**Recommandations**:
- Écrivez vos programmes dans l'ordre suivant: documentation, tests, invariants, puis seulement code.

  C'est l'analogue exact de la démarche en mathématiques: énoncé du théorème, exemples, hypothèse de récurence, reste de la preuve.

- Dans l'exemple ci-dessus, les invariants étaient écrits dans des commentaires. Lisibles par l'homme, donc, mais inexploitable par la machine. Chaque fois que possible, exprimez vos invariants sous une forme *exécutable* tout en restant *lisible*. Cela se fait typiquement avec:

      assert ...
    
  Dans la phase de mise au point, cette forme permet de vérifier systématiquement les invariants, et d'arêter l'exécution du programme le plus tôt possible en cas de problème. Lors de la mise en production, il est possible de désactiver la vérification des asserts (option -O en Python) pour ne pas pénaliser la vitesse d'exécution.
