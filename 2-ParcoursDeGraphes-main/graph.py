# -*- coding: utf-8 -*-
"""A home-made class for graphs

This class implements a (tiny) subset of `networkx` features, trying
to retain compatibility, up to some exceptions. For example, the nodes
and edges methods of networkx return views rather than
sequences. also, the `edges` method is richer in `networkx`, but does
not include the capacity, nor reverse edges for undirected graphs.

We test the compatibility of the basic methods on all the examples::

    >>> import graph, graph_networkx
    >>>
    >>> for G, GN in zip( graph.examples.all(), graph_networkx.examples.all() ):
    ...    assert G.is_directed() == GN.is_directed()
    ...    assert tuple(G.nodes()) == tuple(GN.nodes())
    ...    assert G.number_of_nodes() == GN.number_of_nodes()
    ...    #assert G.number_of_edges() == GN.number_of_edges()
    ...    for v in G.nodes():
    ...        assert set(G.successors(v)) == set(GN.neighbors(v))
    ...    for v1, v2, c in G.edges():
    ...        assert GN.has_edge(v1, v2)
    ...    for v1, v2 in GN.edges():
    ...        assert G.has_edge(v1, v2)
    ...    H = G.networkx()
    ...    assert H.nodes() == GN.nodes()
    ...    assert H.edges() == GN.edges()
    ...    assert H.is_directed() == GN.is_directed()

"""

from typing import Any, Dict, List, Set, Optional, Sequence, Tuple
import networkx  # type: ignore
import graph_examples
from graph_networkx import Node, Capacity, Edge


class Graph:

    # Déclaration des attributs
    # La structure de donnée et l'initialisation vous est donnée
    # pour les sommets (nodes) et pour le choix orienté ou non (directed)
    _nodes: List[Node]
    _directed: bool
    # À vous de choisir la structure de donnée pour les arêtes (edges)
    # Remplacer la ligne suivante par le code adéquat
    _edges: Dict[Tuple[Node, Node], Node]

    def __init__(
        self,
        nodes: Optional[Sequence[Node]] = None,
        matrix: Optional[List[List[int]]] = None,
        edges: Optional[Sequence[Edge]] = None,
        directed: bool = False,
    ):
        """
        Initialisation d'un graphe

        INPUT :

            - nodes, un itérable sur les sommets du graphes
            - matrix, la matrice d'adjacence du graphe suivant les
              mêmes indices que `nodes`
            - edges, une liste de triplets (v1, v2, c) où v1 et v2
              sont des sommets et c un nombre positif

        """
        if nodes is None:
            nodes = []

        self._nodes = list(nodes)
        self._directed = directed

        # on ne peut pas donner à la fois matrix et edges
        if matrix is not None and edges is not None:
            raise ValueError(
                "'matrix' et 'edges' ne peuvent pas être tous les deux initialisés"
            )

        # Les méthodes _init_xxx sont responsables de
        # l'initialisation de la structure de donnée
        # pour les arêtes en fonction du type d'entrée
        if matrix is not None:
            self._init_from_matrix(matrix)
        elif edges is not None:
            self._init_from_edges(edges)
        else:
            self._init_empty()

    def _init_empty(self) -> None:
        """
        Initialisation pour un graphe vide (sans arêtes)
        """
        self._edges = {}

    def _init_from_matrix(self, matrix: Sequence[Sequence[Capacity]]) -> None:
        """
        Initialisation à partir d'une matrice

        EXAMPLES:

            >>> M = matrix = [[0, 12,  0, 12],
            ...               [0,  0, 23, 0],
            ...               [0,  0,  0, 0],
            ...               [0,  0,  0, 0]]
            >>> G = Graph(nodes = ["A", "B", "C", "D"],
            ...           matrix = M,
            ...           directed = True)
            >>> G.edges()
            (('A', 'B', 12), ('A', 'D', 12), ('B', 'C', 23))
            >>> G.matrix() == M
            True
        """
        # Matrice vide ou carrée
        assert len(matrix) == 0 or len(matrix) == len(matrix[0])
        # Si les sommets n'ont pas été entrés
        if len(self._nodes) == 0:
            self._nodes = [i for i in range(len(matrix))]

        self._edges = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 0:
                    (v1, v2) = (self._nodes[i], self._nodes[j])
                    c = matrix[i][j]
                    self._edges[(v1, v2)] = c
                    # Si pas graphe non-dirigé alors arêtes à double sens
                    if not self._directed:
                        self._edges[(v2, v1)] = c

    def _init_from_edges(self, edges: Sequence[Edge]) -> None:
        """
        Initialisation à partir d'une liste de triplets
        """
        # Si les sommets n'ont pas été entrés
        if len(self._nodes) == 0:
            nodes: Set[Node] = set()
            for (v1, v2, _) in edges:
                nodes.add(v1)
                nodes.add(v2)
            self._nodes = list(nodes)

        self._edges = dict()
        for (v1, v2, c) in edges:
            self._edges[(v1, v2)] = c
            # Si pas graphe non-dirigé alors arêtes à double sens
            if not self._directed:
                self._edges[(v2, v1)] = c

    def is_directed(self) -> bool:
        """
        Renvoie si le graph est orienté
        """
        return self._directed

    def set_edge_capacity(self, v1: Node, v2: Node, c: Capacity) -> None:
        """
        Donne la capacité `c` à l'arête `(v1,v2)`

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
            - c la capacité de l'arête (v1,v2)

        EXAMPLES:

            >>> G = GG = Graph(edges = [(1,2,1)], nodes = [1,2], directed = True)
            >>> G.set_edge_capacity(1,2,2)
            >>> G.edges()
            ((1, 2, 2),)
        """
        self._edges[(v1, v2)] = c

    def add_node(self, v: Node) -> None:
        """
        Ajoute le sommet `v` au graphe

        INPUT:

            - v, un sommet du graphe

        Complexity: Constante car ajout dans tableau redimensionnable
        """
        if v not in self._nodes:
            self._nodes.append(v)

    def nodes(self) -> Sequence[Node]:
        """
        Renvoie la liste des sommets du graphe

        EXAMPLES::

            >>> from graph import examples
            >>> G = examples.cours_1_reseau()
            >>> G.nodes()
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        Complexity: Constante car accès à un tableau
        """
        return self._nodes

    def number_of_nodes(self) -> int:
        """
        Renvoie le nombre de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.number_of_nodes()
            8

        Complexity: Constante car taille de tableau non-recalculée
        """
        return len(self._nodes)

    def has_node(self, v1: Node) -> bool:
        """
        Renvoie vrai si v1 est un sommet du graphe

        INPUT:

            - v1, un sommet

        Complexity: Linéaire sur le nombre de sommets
        """
        return v1 in self._nodes

    def edges(self) -> Sequence[Edge]:
        """
        Renvoie les arêtes de ce graphe avec leurs capacités

        Chaque arête est renvoyée comme un triplet `(v1, v2, c)`.

        EXAMPLES:

            >>> G = Graph((1,2,3,4))
            >>> G. edges()
            ()
            >>> G = examples.directed()
            >>> sorted(G.edges())
            [(1, 2, 12), (1, 4, 12), (2, 3, 23)]

            >>> G = examples.undirected()
            >>> sorted(G.edges())
            [(1, 2, 12), (2, 1, 12), (2, 3, 23), (3, 2, 23)]

        Complexity: Linéaire sur le nombre d'arêtes
        """
        return tuple([(v1, v2, self._edges[(v1, v2)]) for (v1, v2) in self._edges])

    def number_of_edges(self) -> int:
        """
        Renvoie le nombre d'arêtes du graphe

        Complexity: Constante car taille de dictionnaire non-recalculée
        """
        return len(self._edges)

    def has_edge(self, v1: Node, v2: Node) -> bool:
        """
        Renvoie si l'arête (v1,v2) existe

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe

        Complexity: Linéaire sur le nombre de sommets successeurs de v1
        """
        return v2 in self.successors(v1)

    def capacity(self, v1: Node, v2: Node) -> Capacity:
        """
        Renvoie la capacité de l'arête (v1,v2)

        Si l'arête n'existe pas, la capacité est 0.

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe

        EXAMPLES::

            >>> G = examples.directed()
            >>> G.capacity(1,2)
            12
            >>> G.capacity(2,1)
            0
            >>> G.capacity(2,3)
            23
            >>> G.capacity(3,2)
            0

        Complexity: Constante car accès à un élément de dictionnaire
        """
        res = self._edges.get((v1, v2))
        return 0 if res is None else res

    def matrix(self) -> List[List[Capacity]]:
        """
        Retourne la matrice associée au graphe

        Soit `n` le nombre de sommets du graphe. Cette méthode renvoie
        une liste `M` de n listes de taille n, de sorte que `M[i][j]`
        est la capacité de l'arête reliant le i-ème sommet au j-ème
        sommet dans le graphe, s'il y en a une, et 0 sinon.

        EXAMPLES::

            >>> G = examples.directed()
            >>> G.matrix()
            [[0, 12, 0, 12],
             [0, 0, 23, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

        Complexity: Quadratique sur le nombre de sommets
        """
        return [[self.capacity(v1, v2) for v2 in self.nodes()] for v1 in self.nodes()]

    def to_dict(self) -> Dict:
        """
        Retourne le dictionnaire associé au graphe
        """
        return self._edges

    def predecessors(self, v: Node) -> Sequence[Node]:
        """
        Renvoie la liste des voisins entrants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.predecessors("H"))
            ['C', 'D', 'E', 'G']
            >>> G = examples.directed()
            >>> G.predecessors(1)
            ()
            >>> G.predecessors(2)
            (1,)

        Complexity: Linéaire sur le nombre de sommets
        """
        return tuple([v1 for v1 in self._nodes if self._edges.get((v1, v)) is not None])

    def successors(self, v: Node) -> Sequence[Node]:
        """
        Renvoie la liste des voisins sortants de `v`

        INPUT:

            - v, un sommet du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> sorted(G.successors("A"))
            ['B', 'F', 'G']
            >>> G = examples.directed()
            >>> sorted(G.successors(1))
            [2, 4]
            >>> G.successors(2)
            (3,)
            >>> G.successors(4)
            ()

        Complexity: Linéaire sur le nombre de sommets
        """
        return tuple([v2 for v2 in self._nodes if self._edges.get((v, v2)) is not None])

    neighbors = successors

    def is_path(self, p: Sequence[Node]) -> bool:
        """
        Renvoie si `p` est un chemin valide dans le graphe

        INPUT:

            - p, une liste de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.is_path([])
            True
            >>> G.is_path(["D"])
            True
            >>> G.is_path(["D", "G"])
            False
            >>> G.is_path(["D", "H"])
            True
            >>> G.is_path(["D", "H", "F"])
            False
            >>> G.is_path(["D", "H", "G", "B", "A"])
            True

        Complexity: len(p) * len(self._nodes)
        """
        # Si un seul sommet il doit appartenir au graphe
        res = len(p) == 0 or (len(p) == 1 and p[0] in self._nodes) or len(p) > 1
        i = 1
        while res and i < len(p):
            # Sommet précédent
            v = p[i - 1]
            # Sommet courant
            w = p[i]
            # Le chemin d'un sommet vers lui-même existe toujours
            res = v == w or w in self.successors(v)
            i += 1
        return res

    def networkx(self) -> networkx.Graph:
        """
        Return a networkx graph with the same nodes and edges
        """
        import graph_networkx

        return graph_networkx.Graph(
            self.nodes(), self.edges(), directed=self.is_directed()
        )

    def show(self) -> Any:
        """
        Display the current graph
        """
        return self.networkx().show()


examples = graph_examples.Examples(Graph)
