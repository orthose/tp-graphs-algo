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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "2c4687f232d08cdb92e40b3ca2f4ec09", "grade": false, "grade_id": "cell-340372ef6a82d730", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Prise en main de l'environnement de travail

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "62f546479e635041c76d857ce83a0f5f", "grade": false, "grade_id": "cell-340372ef6a82d731", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Suivez les
[instructions](http://nicolas.thiery.name/Enseignement/M1-ISD-AlgorithmiqueAvancee/ComputerLab/README.html#telechargement-et-depot-des-tps)
pour accéder à l'environnement de travail et téléchargez le TP.

Puis ouvrez cette première feuille Jupyter `00-PriseEnMain`.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "092c8fea17dcae538d5fd08e5b1279cf", "grade": false, "grade_id": "cell-340372ef6a82d732", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Prise en main de Jupyter

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "bc952e623023ddacabfe33a50951dce2", "grade": false, "grade_id": "cell-340372ef6a82d733", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Cette feuille est dédiée à la prise en main des feuilles de travail
Jupyter (que la plupart d'entre vous connaisse), ainsi que du
mécanisme de correction semi-automatique que nous utiliserons dans ce
cours.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "8f59c24d0dfaef323ad0adec34baa9b4", "grade": false, "grade_id": "cell-4911a792a82448d7", "locked": true, "schema_version": 3, "solution": false}}

Une analyse de donnée prend la forme d'un document narratif expliquant
les objectifs, hypothèses et étapes de l'analyse: quelles sont les
données, qu'est-ce que l'on souhaite calculer, pourquoi, comment,
quels sont les résultats et quelles conclusions on en tire. Ce
document est typiquement écrit en anglais pour qu'il puisse être
partagé avec le plus grand nombre.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "8d0354605c5a45af1b45f9f35f0880d4", "grade": false, "grade_id": "cell-49874ed5d0338eec", "locked": true, "schema_version": 3, "solution": false}}

Depuis quelques années, les feuilles de travail (notebook) Jupyter
sont un des moyens prisés pour rédiger de telles analyses de données
et mener les calculs sous-jacents. Il s'agit en effet de documents
permettant de mêler narration, interaction, calcul, visualisation et
programmation.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "d15693d9efa63fa1acc33a146c03c9c6", "grade": false, "grade_id": "cell-49874ed5d0338eed", "locked": true, "schema_version": 3, "solution": false}}

Le document que vous êtes en train de lire est une feuille Jupyter. On
peut y mettre des calculs comme ci-dessous. Pour exécuter le calcul,
cliquez dans la *cellule* ci-dessous et tapez Shift-Enter:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d4fc1b7754a0b4f373967b4653c39d7b
  grade: false
  grade_id: cell-02a086c93b3ab3f2
  locked: true
  schema_version: 3
  solution: false
---
1 + 1
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5e0f525b775b366eaa8ec2d2d2c0e088", "grade": false, "grade_id": "cell-aa712b4c2a825a98", "locked": true, "schema_version": 3, "solution": false}}

Utilisez maintenant la cellule ci-dessous pour calculer 1+2; puis
réutilisez la même cellule pour calculer 3*4:

```{code-cell} ipython3
1+2, 3*4
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "e487e1abff5bf0d0561ccedb03e27ba7", "grade": false, "grade_id": "cell-20435b0654662bc4", "locked": true, "schema_version": 3, "solution": false}}

Vous rencontrerez aussi des cellules à compléter comme la suivante
dans lesquelles vous remplacerez les deux lignes "Your code here" et
"raise ..." par le calcul à faire; calculez cinq fois sept:

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 823d803c0e85f5ed3431d0439a6cdd2b
  grade: true
  grade_id: cell-d8b61dce71965f3e
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
5*7
```

+++ {"deletable": false, "nbgrader": {"cell_type": "markdown", "checksum": "af3e97715d99c0e969d047d608542e16", "grade": true, "grade_id": "cell-b35d0d71e7e10dd3", "locked": false, "points": 1, "schema_version": 3, "solution": true}}

Vous pouvez aussi éditer les cellules contenant du texte comme
celle-ci. Allez-y: double-cliquez dans la cellule, présentez vous en
la complétant, puis appuyez sur Shift-Enter.

- Nom:

  Vincent

- Prénom:

  Maxime

Quelques mots sur votre expérience passée avec Python:
Python c'est bien pour écire une ligne. Mais au bout de deux lignes c'est déjà trop. 
Python c'est comme sauter dans le vide sans parachute.
Il vaut mieux préférer les langages compilés.

avec Jupyter:
Jupyter c'est pratique pour déboguer rapidement.

avec git:
Le meilleur logiciel de versionnage de code.

avec la théorie des graphes:
Un graphe est un objet relativement simple, mais ce qu'on peut en faire c'est compliqué.

Commentaire libre:
J'ai hâte de commencer !

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "bd4fd9136bacea0eb771d2c699dcb6c3", "grade": false, "grade_id": "cell-20435b0654662bc2", "locked": true, "schema_version": 3, "solution": false}}

On peut ausi mettre des formules mathématiques dans une cellule:
$$\frac 1 {1-\frac 1z} = \sum_{i=0}^\infty \frac 1 {z^i}$$

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "853009b73a6be736941c277d1e3badf0", "grade": false, "grade_id": "cell-20435b0654662bc5", "locked": true, "schema_version": 3, "solution": false}}

Notez que certaines cellules de ce document comme celle-ci sont en
lecture-seule. Vous ne pouvez pas les modifier. En revanche, vous
pouvez toujours insérer de nouvelles cellules.

Insérez une nouvelle cellule ci-dessous, et mettez y la formule $E=mc^2$:

Indications:
-  (menu `Insérer` / `Insert`)
- sélectionnez la cellule
- changez son type en `MarkDown` (menu `Cellule` / `Cell` -> `Type de cellule` / `Cell type`)
- double-cliquez sur cette cellule ou la précédente pour voir comment
  insérer des formules mathématiques en latex.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "5c93f877d9d2628f2d204b8635e90729", "grade": false, "grade_id": "cell-20435b0654662bc6", "locked": true, "schema_version": 3, "solution": false}}

- Lancez la visite guidée de l'interface Jupyter.<br>
  Indication: Menu `Aide` -> `Visite de l'interface utilisateur`.
- Consultez les raccourcis claviers.<br>
  Indication: Menu `Aide` -> `Raccourcis clavier`.

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "0a92b2818e65f8f19febdb180f47ad08", "grade": false, "grade_id": "cell-20435b0654662bc7", "locked": true, "schema_version": 3, "solution": false}}

## Correction semi-automatique avec nbgrader

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "c5f06e854c90bdfaa1c8566357cc7f86", "grade": false, "grade_id": "cell-20435b0654662bc8", "locked": true, "schema_version": 3, "solution": false}}

Certaines feuilles de travail seront notées. Les notes de certaines
séances ultérieures contribueront à votre moyenne. Cette première
séance est une séance d'entraînement; les notes seront indicative pour
que vous preniez en main le mécanisme.

Une partie de la correction est manuelle: vos enseignants regarderont
vos réponses et attribueront des points à chacune d'entre elles. Le
gros de la correction sera automatique, s'appuyant sur des tests
similaires à ceux du premier semestre.

Voici un exemple tout bête. Dans la cellule suivante, calculez la
somme de `3` et de `4`, et stockez le résultat dans la variable `s`:

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 36de014b646362e2bf7dbbb660cfe968
  grade: false
  grade_id: cell-d8b61dce71965f3g
  locked: false
  schema_version: 3
  solution: true
  task: false
---
s = 3 + 4
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4c3a3c88e1ef0310989fb3912787179e", "grade": false, "grade_id": "cell-074eb18a150a2c8e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

La commande suivante est un test qui vérifie votre réponse; vous
reconnaîtrez le `assert` (cette fois en minuscule) que nous utilisions
en C++ au premier semestre:

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 6ad2856d7da3b56ed5f56a3152f45af2
  grade: true
  grade_id: cell-d8b61dce71965f3h
  locked: true
  points: 1
  schema_version: 3
  solution: false
  task: false
---
assert s == 7
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "bff45e311b67b5d71efea3fc7382229c", "grade": false, "grade_id": "cell-4c9512739b1f0f29", "locked": true, "schema_version": 3, "solution": false, "task": false}}

<!--Validez votre feuille en cliquant sur le bouton `Validate`; cela en
exécute une copie dans l'ordre en vérifiant tous les tests
automatiques.!-->

Suivez les
[instructions](http://nicolas.thiery.name/Enseignement/M1-ISD-AlgorithmiqueAvancee/ComputerLab/README.html#telechargement-et-depot-des-tps)
pour déposer votre travail sur GitLab et obtenir les résultats de la
correction automatique.


<div class="alert alert-info">

- Il n'y aura pas de note pour le TP 1. Les résultats de la correction
  automatique sont indicatifs. Mais ce que vous allez développer
  servira dans tous les TPs suivants. Vous devez viser un zéro faute
  :-) En sus, la qualité du code de ce TP et de sa documentation sera
  l'un des éléments de la notation du TP 2 (jeudi).

- Pour les TPs suivants, le résultat de la correction automatique sera
  l'un des éléments de notation.

</div>

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "84f6551575e1411d2b119b6d33ccd62b", "grade": false, "grade_id": "cell-8226871d2f13ccb8", "locked": true, "schema_version": 3, "solution": false}}

## Au boulot!

Maintenant que vous avez appris les rudiments de Jupyter et de
l'environnement de travail; il est temps de passer au TP lui-même!
