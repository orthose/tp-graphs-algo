"""A class to implement flows on networks"""

from typing import Any, Iterable, List, Optional, Sequence, Tuple, Union, cast
import matplotlib.pyplot as plt  # type: ignore
import networkx  # type: ignore
from network import Network

Node = Any
Capacity = float
Edge = Tuple[Node, Node, Capacity]
NetworkType = Any


class Flow:
    def __init__(
        self,
        network: NetworkType,
        s: Node,
        t: Node,
        flow: NetworkType = None,
        check: bool = True,
    ):
        """
        Initialisation à partir d'un réseau et d'un second réseau représentant le flot.

        Si le paramètre `flow` n'est pas initilisé, on crée un flot nul.

        INPUT:

            - network, un reseau Network
            - s, le sommet source
            - t, le sommet cible
            - flow (optionnel), un reseau Network
            - check (default = True), si True, un test de cohérence entre le flot et le
              réseau est lancé.
        """
        self._network = network
        self._s = s
        self._t = t
        if flow is None:
            self._flow = Network(nodes=network.nodes(), edges=[])
        else:
            self._flow = flow
            if check:
                assert flow.nodes() == network.nodes()
                assert self.check_capacity()
                assert self.check_in_out()

    def network(self) -> NetworkType:
        """
        Renvoie le réseau sur lequel on construit le flot
        """
        return self._network

    def source(self) -> Node:
        """
        Renvoie la source du flot
        """
        return self._s

    def target(self) -> Node:
        """
        Renvoie la cible du flot
        """
        return self._t

    def flows(self) -> Sequence[Edge]:
        """
        Renvoie une liste de triplets `(v1,v2,c)` correspondant aux arêtes
        du flot avec leur valeur.

        """
        return tuple((a, b, self.flow(a, b)) for a, b in self.network().edges())

    def capacity(self, v1: Node, v2: Node) -> Capacity:
        """
        Renvoie la capicté de l'arête dans le réseau

        INPUT:

            - v1, un sommet du réseau
            - v2, un sommet du réseau
        """
        return cast(Capacity, self.network().capacity(v1, v2))

    def flow(self, v1: Node, v2: Node) -> Capacity:
        """
        Renvoie le flot entre v1 et v2

        INPUT:

            - v1, un sommet du réseau
            - v2, un sommet du réseau
        """
        return cast(Capacity, self._flow.capacity(v1, v2))

    def set_flow(self, v1: Node, v2: Node, f: Capacity) -> None:
        """
        Met la valeur du flot à `f` sur l'arête `(v1,v2)`

        INPUT :

            - v1, un sommet du réseau
            - v2, un sommet du réseau
            - f un nombre supérieur ou égal à 0
        """
        self._flow.set_edge_capacity(v1, v2, f)

    def add_flow(self, v1: Node, v2: Node, f: Capacity) -> None:
        """
        Modifie la valeur du flot sur `(v1,v2)` de `f`

        INPUT :

            - v1, un sommet du réseau
            - v2, un sommet du réseau
            - f un nombre
        """
        self._flow.set_edge_capacity(v1, v2, f + self.flow(v1, v2))

    def __eq__(self, n2: Any) -> bool:
        """
        Renvoie vrai si n2 repésente le même flot que n1

        INPUT :

            - n2, un objet
        """
        if not isinstance(n2, Flow):
            return False
        return cast(bool,
                    n2.network().is_equal(self.network()) and
                    n2._flow.is_equal(self._flow))

    def flow_in(self, v: Node) -> Capacity:
        """
        Renvoie la somme des flots entrant sur le sommet v
        """
        return sum([self.flow(x, v) for x in self.network().predecessors(v)])

    def flow_out(self, v: Node) -> Capacity:
        """
        Renvoie la somme des flots sortant du sommet v
        """
        return sum([self.flow(v, x) for x in self.network().successors(v)])

    def global_value(self) -> Capacity:
        """
        Renvoie la valeur globale du flot (flux net entrant sur la source,
        ou flux net sortant de la cible)
        """
        return self.flow_out(self.source()) - self.flow_in(self.source())

    def check_capacity(self) -> bool:
        """
        Renvoie vrai si la valeur du flot est bien inférieure ou égale à la capacité du
        réseau sur chacune des arêtes
        """
        res = True
        i = 0
        flows = self.flows()
        while res and i < len(flows):
            (v, w, f) = flows[i]
            res = (f <= self.capacity(v, w))
            i += 1
        return res

    def check_in_out(self) -> bool:
        """
        Renvoie vrai si la somme des flots entrant est égales à la somme des flots
        sortant sur chacun des sommets en dehors de la source et la cible
        """
        res = True
        i = 0
        nodes = list(self.network().nodes())
        nodes.remove(self.source())
        nodes.remove(self.target())
        while res and i < len(nodes):
            v = nodes[i]
            res = (self.flow_in(v) == self.flow_out(v))
            i += 1
        return res

    def show(self,
             marked_edges: Optional[Iterable] = None,
             marked_nodes: Optional[Iterable] = None) -> Any:
        """ """
        edge_labels = {
            (u, v): str(self.network().capacity(u, v)) + ", " + str(self.flow(u, v))
            for u, v in self.network().edges()
        }
        from graph_networkx import default_layout

        layout = default_layout(self.network())
        if marked_nodes is None:
            marked_nodes = set()
        color_map = [
            "green"
            if n == self.source() or n == self.target()
            else "red"
            if n in marked_nodes
            else "lightgray"
            for n in self.network().nodes()
        ]
        edge_color: Union[str, List[str]]
        if marked_edges is None:
            edge_color = "black"
        else:
            edge_color = [
                "black" if e not in marked_edges else "red"
                for e in self.network().edges()
            ]
        plt.figure()
        networkx.draw(
            self.network(),
            layout,
            width=3,
            linewidths=1,
            node_size=500,
            node_color=color_map,
            alpha=0.9,
            labels={node: node for node in self.network().nodes()},
            edge_color=edge_color,
        )
        networkx.draw_networkx_edge_labels(
            self, layout, edge_labels=edge_labels, font_color="black"
        )
        plt.axis("off")
        plt.show()

    ### Ford-Fulkerson ###

    def find_augmenting_path(self) -> Optional[List]:
        """
        Cherche une chaine augmentante sur le flot

        * si une chaine est trouvée, la méthode renvoie la chaine sous
          la forme d'une liste d'élément `(v1,v2,p)` où `(v1,v2)` est
          l'arête de la chaine et `p` son potentiel avec le bon signe
          (positif pour une arête dans le bon sens, négatif sinon)

        * si aucune chaîne n'est trouvée, la méthode renvoie `None`

        """
        N = self.network()
        marked = set() # L'ensemble des sommets déjà rencontrés
        
        # Parcours en profondeur et construction du chemin vers la cible
        # On utilise un tuple pour permettre un passage par copie
        def explorer(v: Node, path: Tuple) -> (bool, Tuple):
            # On atteint la cible
            if v == self.target():
                return (True, path)
            
            marked.add(v)
            # Arêtes dans le bon sens
            for w in N.successors(v):
                f = self.flow(v, w)
                c = N.capacity(v, w)
                if w not in marked and f < c:
                    (is_path, whole_path) = explorer(w, path + ((v, w, c-f),))
                    if is_path:
                        return (is_path, whole_path)
            
            # Arêtes dans le mauvais sens
            for w in N.predecessors(v):
                f = self.flow(w, v)
                if w not in marked and 0 < f:
                    (is_path, whole_path) = explorer(w, path + ((w, v, -f),))
                    if is_path:
                        return (is_path, whole_path)
            
            # Aucun chemin trouvé         
            return (False, path)
    
        (is_path, whole_path) = explorer(self.source(), ())
        if is_path:
            return list(whole_path)
        else:
            return None

    def increase_augmenting_path(self, path: List) -> None:
        """
        Modifie le flot en fonction de la chaine augmentante `path`

        INPUT:

            - path, une liste de triplet de la forme `(v1,v2,p)` où
              `(v1,v2)` est une arête du réseau et p est son potentiel
              d'augmentation (positif ou négatif)

        La méthode calcule la valeur minimale des valeurs absolues de
        p et modifie le flot en conséquence.

        """
        pmin = min([abs(p) for (_, _, p) in path])
        sign = lambda x: int(x / abs(x)) 
        for (v, w, p) in path:
            self.add_flow(v, w, sign(p) * pmin)
