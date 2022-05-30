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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "61312f6bc1f8af5b6c5d0f1aa84cf205", "grade": false, "grade_id": "cell-8b116a662ca39c34", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Problème 2: [Rush Hour](http://www.thinkfun.com/products/rush-hour/)

La voiture rouge est coincée dans un embouteillage; comment déplacer les véhicules pour la faire sortir?
Ci-dessous le défi 1.
<center>

<img src="media/rush_hour.gif" width="30%">

</center>

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "dd86af124d161966e5d603450c9023fa", "grade": false, "grade_id": "cell-0ae0519f05fd16cf", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Quel rapport avec les parcours de graphes? Saurez-vous faire résoudre par l'ordinateur le défi 40 en un nombre minimum du coups?

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "fdccfc6d88cc1cf2f33c9c504a50e993", "grade": false, "grade_id": "cell-b58143ef6a52abc7", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Dans cette feuille, vous découvrirez le modèle et deux mini applications interactives pour le jeu RushHour qui vous sont fournis. Il ne restera «plus qu'à» implanter l'«Intelligence Artificielle» pour résoudre le jeu.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "dd6d1a7d539f86f939d8e01062d2b173", "grade": false, "grade_id": "cell-e95fbc428f5dc7f7", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Un modèle pour RushHour

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "02e58cbb8a11a7abecf9c2a5ec3a4395", "grade": false, "grade_id": "cell-c46ec613d70afce3", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Quelques exemple d'utilisation programmatique

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 319cb7837eac7044bd0f3a79f593ca5c
  grade: false
  grade_id: cell-092550ae4c9bb258
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from rush_hour import Plateau
```

```{code-cell} ipython3
plateau = Plateau(['A2R00','X2R21','C2R44','R3R52','O3D05','P3D10','Q3D13','B2D40']); plateau
```

```{code-cell} ipython3
plateau.recule("Q")
```

```{code-cell} ipython3
plateau.est_gagnant()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "0f47a25d5a1c1d31107a8f98efe4bd50", "grade": false, "grade_id": "cell-147551e49db8aa71", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Chargement du 40ème défi de RushHour (voir les fichiers dans <a href="RushHourDefis/">RushHourDefis/</a>):

```{code-cell} ipython3
Plateau(40)
```

```{code-cell} ipython3
p = Plateau(40)
d = p.voisins()
d['PU1'].voisins()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3853d37844247ef9bc2a7c8a10eefab7", "grade": false, "grade_id": "cell-5b6cd6d6f9b71716", "locked": true, "schema_version": 3, "solution": false, "task": false}}

### Un exemple d'interface utilisateur minimale

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: a4423dba29b42ee0c9edf432ff5ce134
  grade: false
  grade_id: cell-925594bf10241f01
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from ipywidgets import interact_manual
from rush_hour import Plateau
plateau = Plateau(['A2R00','X2R21','C2R44','R3R52','O3D05','P3D10','Q3D13','B2D40']); plateau
@interact_manual
def step(voiture=plateau.voitures.keys(), distance=[0,-1,1]):
    global plateau
    plateau2 = plateau.avance(voiture, distance)
    if plateau2:
        plateau = plateau2
    return plateau
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c37f849df45a599d3724eadc1cd872e3", "grade": false, "grade_id": "cell-e658e589337e3977", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Une application graphique basée sur les widgets de Jupyter

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 67f816654091fea456827676c27ba6e3
  grade: false
  grade_id: cell-a493f5ab9537f103
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from rush_hour_application import RushHourApplication
A = RushHourApplication()
A
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "f76e325e5dd473d0bcfc5ce9c3e7a6c0", "grade": false, "grade_id": "cell-3b27d02803493741", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## À vous de jouer!

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "dfebca0629ee1f735ad6d0acc6e8496d", "grade": false, "grade_id": "cell-0ea3514426195c6e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Implantez la méthode `solution` dans la class <a href="rush_hour.py">RushHour</a> pour déterminer une séquence minimale de coup permettant de résoudre un défi, puis utilisez la ci-dessous pour résoudre le défi 40 de Rush Hour.

**Indication**: considérez le graphe dont les sommets sont les états possibles du plateau et les arêtes les déplacements de voiture!

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: c1f7852bda69f01c6cba316de822ebe0
  grade: false
  grade_id: cell-0fac0ad8915bba3b
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from rush_hour import RushHour
solution = RushHour.solution(40)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: b7f2d6e940b46765dc0c5f10dc23f2aa
  grade: true
  grade_id: cell-38c9c48e258b9fd9
  locked: true
  points: 4
  schema_version: 3
  solution: false
  task: false
---
assert RushHour.est_solution(40, solution)
```

```{code-cell} ipython3
len(solution)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "1840212add1e2558b0da1b0aa57b150a", "grade": false, "grade_id": "cell-6d62883f6aa408c3", "locked": true, "points": 2, "schema_version": 3, "solution": false, "task": true}}

Pour évaluer la qualité du code:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: cc7f53fdba346df780cd10ed3c6de577
  grade: true
  grade_id: cell-608b04e180a64d9a
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
from utils import code_checker, show_source
code_checker("flake8 rush_hour.py")
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 9c9385c0d540f399c8b71f784a58cffe
  grade: true
  grade_id: cell-d8c10c2c6e3df6ed
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
code_checker("pytest rush_hour.py")
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 3b44db233dc30d4826dd2d8ecd3101e8
  grade: false
  grade_id: cell-a6971cf2d62ca9af
  locked: true
  schema_version: 3
  solution: false
  task: false
---
from utils import show_source
show_source(RushHour.solution)
```

```{code-cell} ipython3

```
