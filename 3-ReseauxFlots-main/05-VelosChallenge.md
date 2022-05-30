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

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "4966fbe4f4a3c5cd4f781b8ca57dd0ef", "grade": false, "grade_id": "cell-80e81a1d2028492e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

# Le défi des vélos

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ca09d7f0b846afb465624c79572c606e", "grade": false, "grade_id": "cell-177968e5ac0e7114", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Le problème à résoudre

Vous avez été embauché comme consultant chez *Schmurfvengo* qui vient d'obtenir de façon inespérée la gestion des vélibs à Paris. Le problème est le suivant : pour cause de soucis techniques, il faut régulièrement remplacer l'ensemble de la flotte (30 000 vélos) en **une nuit**. 

Pour cela, vous disposez de plusieurs gros camions qui peuvent déposer chacun 2000 vélos dans un ensemble de stations en périphérie de la ville. Il y a 1396 stations en fonctionnement dans la capitale. Il faut donc ensuite distribuer les vélos aux autres stations. On cherche une solution.

La société propose de mettre en place la stratégie suivante : des navettes électriques pouvant chacune transporter 300 vélos d'une station à l'autre. On peut mettre une navette en place entre deux stations $v_1$ et $v_2$ : si elles sont éloignées de 500m à vol d'oiseau ou moins, ou si $v_2$ est la station la plus proche de $v_1$ (cela permet de relier au réseau les stations "isolées" qui sont à plus de 500m de toutes les autres stations).

Cette solution est-elle viable :
 * Pourra-t-on livrer tous les vélos ? 
 * De combien de navettes aurons-nous besoin ? 
 * Toutes les stations recevront-elles des vélos ?

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "a1b624bd4845c3a0f6abd7d47a665635", "grade": false, "grade_id": "cell-2664bcf79eba1647", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Les données

Pour résoudre ce problème, vous pouvez utiliser les données de [Open Data Paris](https://opendata.paris.fr). La table dont vous avez besoin est [Stations Velibs : emplacement des stations](https://opendata.paris.fr/explore/dataset/velib-emplacement-des-stations/). Le fichier *json* est disponible dans ce dossier, les données sont directement interprétables en Python de cette façon.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: d064b677c5383ea5faf23200d07cee91
  grade: false
  grade_id: cell-f6b974e823b83bfc
  locked: true
  schema_version: 3
  solution: false
  task: false
---
import json
data = json.load(open("media/velib-emplacement-des-stations.json"))
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "50320d0b3e4571fdfb44fce6230dffaf", "grade": false, "grade_id": "cell-6144343959d07e8e", "locked": true, "schema_version": 3, "solution": false, "task": false}}

La variable `data` est une liste dont chaque élément est un dictionnaire python contenant les informations d'une station vélib.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 60a0d9825e978cb69456c44591f7b57c
  grade: false
  grade_id: cell-bdc02a3c16bd8a82
  locked: true
  schema_version: 3
  solution: false
  task: false
---
len(data)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "01d831d1c0c392779e00bd2113798228", "grade": false, "grade_id": "cell-e9df99b422da4171", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Voilà par exemple, le premier élément de la liste, la station *Bois de Vincennes - Gare*

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 8d4cfb8f7ca8bfa587e4da738a211d3f
  grade: false
  grade_id: cell-830b238cbbbbab32
  locked: true
  schema_version: 3
  solution: false
  task: false
---
data[0]
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ce94abba4bb9d8ee3f7399f183c32272", "grade": false, "grade_id": "cell-c3a8c70a4a080ced", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Voici l'ensemble des stations périphériques où les camions pourront livrer à chacune 2000 vélos.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 2146cb6bf50e03114d381bab47c77420
  grade: false
  grade_id: cell-a7b3e9526e6cb11e
  locked: true
  schema_version: 3
  solution: false
  task: false
---
entry_points = {"David Weill - Parc Montsouris", "Vanne - Saussaies", "Bruneseau - Quai d'Ivry", "Gare RER - Canadiens", "Porte de Vincennes", "Champeaux - Gallieni", "Romainville - Vaillant-Couturier", "Frères Flavien - Porte des Lilas", "Grands Moulins de Pantin", "Emile Reynaud - Porte de la Villette", "Wilson - Landy", "Fragonard - Porte de Clichy", "Gare d'Asnières sur Seine", "Reims - Porte d'Asnières", "Porte Maillot - Pereire", "Charles de Gaulle - Madrid", "Porte de la Muette", "Transvaal - Charles de Gaulle", "Rond-Point Rhin et Danube", "Murat - Porte de Saint-Cloud", "Porte de Vanves", "Porte d'Orléans", "Bois de Vincennes - Gare"}
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "430b0da2e0e04858403a32c4b1a1e3e5", "grade": false, "grade_id": "cell-8a442d7b2e280180", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Remarque : ici on a identifié les stations par leurs noms. MAIS ! Il existe des stations qui portent le même nom. De façon générale, on utilisera donc un identifiant comportant à la fois le nom et l'id de la station (pour que cela reste lisible et unique). La fonction suivante pourra être utile.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 11fabbeef74ffb9956d4f1fe220f4b29
  grade: false
  grade_id: cell-5015e89ca0904b10
  locked: true
  schema_version: 3
  solution: false
  task: false
---
def name(d):
    return d['fields']['name'] + "-" + str(d['fields']["stationcode"])
```

```{code-cell} ipython3
# Bah du coup sinon rien ne marche...
def find_index(name):
    for i in range(len(data)):
        if name == data[i]["fields"]["name"]:
            return i
        
entry_points = {name(data[find_index(x)]) for x in entry_points}
entry_points
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "3d2faaf4fa17e2e575a34126c40bd7df", "grade": false, "grade_id": "cell-d9e2532824cbd115", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Exemple :

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: e2576b8c5452e7fddc03950dcbc5c1b7
  grade: false
  grade_id: cell-ddde034ba11dd806
  locked: true
  schema_version: 3
  solution: false
  task: false
---
name(data[0])
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "ab95269a3d540fd469f7eabe29f76b86", "grade": false, "grade_id": "cell-901e35595c20a602", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On vous fournit aussi la fonction suivante qui permet de calculer la distance en mètres entre deux points données sous forme `(latitude, longitude)`.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 0f5c11feeb50b66fccfe7dd19a619ac5
  grade: false
  grade_id: cell-944c826f170be63c
  locked: true
  schema_version: 3
  solution: false
  task: false
---
import math
def toRad(angle):
    """
    Converti un angle donné en degré en un angle donné en radian.
    
    INPUT:
        
        - angle, un angle en degré
        
    OUTPUT : la valeur en radian
    """
    return angle*2*math.pi/360

def distance(p1, p2):
    """
    Renvoie la distance en mètres entre les points `p1` et `p2` données en coordonnées géographique
    
    INPUT:
    
        - p1, un tuple (latitude, longitude)
        - p2, un tuple (latitude, longitude)
        
    OUTPUT : la distance à vol d'oiseau en mètres entre p1 et p2
    """
    lat1, lon1 = p1
    lat2, lon2 = p2
    R = 6371e3
    phi1 = toRad(lat1)
    phi2 = toRad(lat2)
    dphi = toRad(lat2 - lat1)
    dlam = toRad(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlam/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R*c
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "764198d965fff55f7810c45590dbdd3b", "grade": false, "grade_id": "cell-b070b5d3a88acaba", "locked": true, "schema_version": 3, "solution": false, "task": false}}

Par exemple, la distance entre la première station de la liste *Bois de Vincennes - Gare* et la seconde, *Morillons - Dantzig* est environ de 12.5km.

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 2152d0d3fc11f293cbec98f43504cbeb
  grade: false
  grade_id: cell-87c1f0c7bfdd0485
  locked: true
  schema_version: 3
  solution: false
  task: false
---
distance(data[0]["fields"]["coordonnees_geo"],data[1]["fields"]["coordonnees_geo"]) 
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "0d967dd123f9c1e65f1fcef718691d1a", "grade": false, "grade_id": "cell-f2cc72bf190ab9d9", "locked": true, "schema_version": 3, "solution": false, "task": false}}

On vous montre aussi les scripts suivants qui permettent de faire un affichage graphique avec `matplotlib`. (Le premier affiche des points et le second des lignes)

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 01679edfc2f1bdb5f70d2949d0fcf0c6
  grade: false
  grade_id: cell-eca43aa78595e502
  locked: true
  schema_version: 3
  solution: false
  task: false
---
import matplotlib.pyplot as plt

x = [d["fields"]["coordonnees_geo"][1] for d in data]
y = [d["fields"]["coordonnees_geo"][0] for d in data]


plt.scatter(x,y,s=5)

plt.title('Les stations velibs dans Paris')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.savefig('StationsVelib.png')
plt.show()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 86c0f1a6fec097a44ec4026a451288b1
  grade: false
  grade_id: cell-291c2cb098ef8ba3
  locked: true
  schema_version: 3
  solution: false
  task: false
---
import matplotlib.pyplot as plt


station_names = set(name(d) for d in data)
station_dict = {name(d):d for d in data}
station = station_names.pop()

while len(station_names) > 0:
    next_station = min(station_names, key = lambda n: distance(station_dict[n]["fields"]["coordonnees_geo"], station_dict[station]["fields"]["coordonnees_geo"]))
    station_names.remove(next_station)
    plt.plot([station_dict[station]["fields"]["coordonnees_geo"][1], station_dict[next_station]["fields"]["coordonnees_geo"][1]], [station_dict[station]["fields"]["coordonnees_geo"][0], station_dict[next_station]["fields"]["coordonnees_geo"][0]], 'k-', lw=1)
    station = next_station

plt.title('Un chemin reliant toutes les stations')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.savefig('CheminsStations.png')
plt.show()
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "30ba59dea65b158ffc6a7e143852fade", "grade": false, "grade_id": "cell-a2554bd94f3aa09b", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## À vous de jouer !

Vous avez maintenant tous les éléments pour résoudre le problème. Petit résumé.

**Le but** : acheminer le maximum de vélos sur les 30000.

**Les contraintes** :

 * respecter la capacité de chaque station (pas plus de 80% de remplissage)
 * respecter les contraintes de l'énoncé sur les camions de départ et les navettes.
 
**Le résultat** : votre résultat doit être facilement utilisable. En particulier vous devez implanter les fonctions `navette` et `remplissage` définies en bas de la fiche et donner les lignes de codes affichant les réponses aux questions. 

**Un peu de dessin ?** Donnez une illustration de votre résultat en utilisant `matplotlib`.

**Comment faire ?** Aidez-vous des fiches précédentes, discutez avec votre groupe, posez des questions, lisez wikipedia.

**Remarque :** Le calcul final prend du temps ! (quelques minutes environ)

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 7977a57c98c64702167c281b24ecdced
  grade: true
  grade_id: cell-8cc35ad15c2fe347
  locked: false
  points: 5
  schema_version: 3
  solution: true
  task: false
---
edges = []

# Connexion de la source aux points d'entrée
# Valeur d'approvisionnement de 2000 vélos
for x in entry_points:
    edges.append(('S', x, 2000))
edges
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 0ddc3b398dcb558ccd671982c3339d9b
  grade: true
  grade_id: cell-ec3ece73f1715e02
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
import math
    
for i in range(len(data)):
    v = name(data[i])
    
    # Connexion des stations qui ne sont pas des points d'entrée à la cible
    # Chaque station doit être remplie à 80% de sa capacité au maximum
    if v not in entry_points:
        edges.append((v, 'T', int(0.80 * data[i]["fields"]["capacity"])))
    
    # Connexion de stations entre elles en fonction de leur distance
    nearest = None
    dmin = math.inf
    alone = True
    # On part de i + 1 pour éviter de répéter les calculs de distance
    for j in range(i + 1, len(data)):
        d = distance(
             data[i]["fields"]["coordonnees_geo"], 
             data[j]["fields"]["coordonnees_geo"])
        
        # Toutes les stations à moins de 500 m sont reliées entre elles
        if d <= 500:
            alone = False
            w = name(data[j])
            # Les arêtes sont bidirectionnelles
            edges.append((v, w, 300))
            edges.append((w, v, 300))
                
        if d < dmin:
            nearest = j
            dmin = d
                
    # Si v n'est rélié à personne on le relie à son plus proche voisin
    # Si il n'a aucun voisin on ne fait rien
    if alone and nearest is not None: 
        edges.append((v, name(data[nearest]), 300))
        
edges
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 0d9fcb8b9f2643e55a1fd91b1c999456
  grade: true
  grade_id: cell-dc499ea3f4ae79f3
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
from network import Network
from flow import Flow
from ford_fulkerson import maximal_flow

# Construction du réseau
N = Network(edges = edges, 
    # S et T sont la source et la cible
    nodes = ['S', 'T'] + [name(d) for d in data])

# Résolution du flot maximal avec Ford-Fulkerson
F = maximal_flow(N, 'S', 'T')
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: e430a0b7477e36609347aad373c980b6
  grade: true
  grade_id: cell-06ef8ce8ffaabe18
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
def navette(flot, station1, station2):
    """
    S'il existe une navette entre `station1` et `station2`, renvoie le nombre de vélos qui seront transportés par cette navette durant la nuit. Sinon, renvoie 0.
    
    INPUT:
    
        - flot, l'objet contenant le résultat de vos calculs
        - station1, le nom-id d'une station Velib
        - station2, le nom-id d'une seconde station Vélib
    """
    return F.flow(station1, station2)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ef96154492fb62e00ddf649c8d919802
  grade: false
  grade_id: cell-95e0aedcda921052
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# par exemple...
navette(F, "David Weill - Parc Montsouris-14124", "Jourdan - Cité Universitaire-14135") # pour mes calculs 300 vélos
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 7a4b81557feb10b6d73ef422b5f109bf
  grade: true
  grade_id: cell-5002575ee8904473
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
# vérifions qu'on ne dépasse pas la capacité des navettes
assert all( navette(F, name(d1), name(d2)) <= 300 for d1 in data for d2 in data)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 742d14e0f9c32c2ab3c741b0f6dedde2
  grade: true
  grade_id: cell-055018359c1cb961
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
# vérifions qu'on n'a pas de navettes entre une station et elle-même
assert all( navette(F, name(d), name(d)) == 0 for d in data)
```

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 79b0ef5a8e8b940f00d9021ef4540d21
  grade: true
  grade_id: cell-2d6a0c32f4038ca1
  locked: false
  points: 0
  schema_version: 3
  solution: true
  task: false
---
def remplissage(flot, station):
    """
    Renvoie le nombre de vélos qu'on aura installé à `station` à la fin de la nuit.
    
    INPUT :
    
        - flot, l'objet contenant le résultat de vos calculs
        - station, le nom d'une station velib
    """
    return F.flow(station, 'T')
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: ad9cc8060d93531cfcc20c4e93fb4335
  grade: false
  grade_id: cell-56f0aa5ed941e79e
  locked: true
  schema_version: 3
  solution: false
  task: false
---
# par exemple...
remplissage(F, "Jourdan - Stade Charléty-14014") # pour mes calculs 48
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 855aa6cd90476efc31cbb0ee4eebf327
  grade: true
  grade_id: cell-11c45b6b9551d3a8
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
# vérifions qu'on ne dépasse pas la capacité des stations
assert all( remplissage(F, name(d)) <= 0.8 * d["fields"]["capacity"] for d in data)
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: cafafb3c8fa874c247fdcbd87cbac3b9
  grade: true
  grade_id: cell-33a3285c830faa59
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
# vérifions qu'on ne distribue pas des "demi-vélos"
assert all( remplissage(F, name(d)) == int(remplissage(F, name(d))) for d in data)
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "b95074afe9020cd1e6086e2d0c1c6576", "grade": false, "grade_id": "cell-9e4b254223383e46", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Combien de vélos avez-vous livré ?**

Répondez par une ligne de code qui affecte la réponse à la variable `vélos_livrés` en se basant sur vos calculs.

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 4b2658ad1a415571dfb8c50f96e50da0
  grade: false
  grade_id: cell-a8fff63e26161157
  locked: false
  schema_version: 3
  solution: true
  task: false
---
vélos_livrés = F.global_value()
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 759a5c412452a59e888fb748089361ac
  grade: false
  grade_id: cell-dc588e05035a2229
  locked: true
  schema_version: 3
  solution: false
  task: false
---
vélos_livrés
```

```{code-cell} ipython3
---
deletable: false
editable: false
nbgrader:
  cell_type: code
  checksum: 850c65471f166270fa578640eb5d3e99
  grade: true
  grade_id: cell-d814656c75a81630
  locked: true
  points: 2
  schema_version: 3
  solution: false
  task: false
---
import hashlib
assert hashlib.md5(bytes(vélos_livrés)).hexdigest() == 'c60933c951b65c7e2c799843f585c54d'
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "7245ccc3808d80ccb05114f5c37c145e", "grade": false, "grade_id": "cell-dcdbb063bc1da834", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Combien de navettes avez-vous utilisées ?**

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: 548befc7bbc8bc2af9c6f3d016785f6f
  grade: true
  grade_id: cell-b5b84fd9c87b378c
  locked: false
  points: 1
  schema_version: 3
  solution: true
  task: false
---
sum([1 for x in F.network().nodes() for y in F.network().successors(x) if F.flow(x, y) > 0])
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "49b5c1000b4c7a29f0214423b9506fd3", "grade": false, "grade_id": "cell-c07bf4d6c866d383", "locked": true, "schema_version": 3, "solution": false, "task": false}}

**Combien de stations n'ont reçu aucun vélo ?**

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: d033384df5dc213df0fb4388eb7b60a5
  grade: true
  grade_id: cell-ee21984567ca34e4
  locked: false
  points: 1
  schema_version: 3
  solution: true
  task: false
---
sum([1 for x in F.network().nodes() if F.flow(x, 'T') == 0])
```

+++ {"deletable": false, "editable": false, "nbgrader": {"cell_type": "markdown", "checksum": "daeb02439a7c8defd2771ebde7ed718f", "grade": false, "grade_id": "cell-18902acd7afc3e78", "locked": true, "schema_version": 3, "solution": false, "task": false}}

## Un peu de dessin ?

On voudrait se faire une idée du réseau de navettes, pouvez-vous le représenter graphiquement ?

```{code-cell} ipython3
---
deletable: false
nbgrader:
  cell_type: code
  checksum: a8f82f0c52a052ca99258d9708e58cc4
  grade: true
  grade_id: cell-a5392fa01bc32f98
  locked: false
  points: 3
  schema_version: 3
  solution: true
  task: false
---
import matplotlib.pyplot as plt


station_names = set(name(d) for d in data)
station_dict = {name(d):d for d in data}
station = station_names.pop()

while len(station_names) > 0:
    next_station = min(station_names, key = lambda n: distance(station_dict[n]["fields"]["coordonnees_geo"], station_dict[station]["fields"]["coordonnees_geo"]))
    station_names.remove(next_station)
    if F.flow(station, next_station) > 0:
        plt.plot([station_dict[station]["fields"]["coordonnees_geo"][1], station_dict[next_station]["fields"]["coordonnees_geo"][1]], [station_dict[station]["fields"]["coordonnees_geo"][0], station_dict[next_station]["fields"]["coordonnees_geo"][0]], 'k-', lw=1)
    station = next_station

plt.title('Un chemin reliant toutes les stations')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.savefig('CheminsStations.png')
plt.show()
```

```{code-cell} ipython3

```
