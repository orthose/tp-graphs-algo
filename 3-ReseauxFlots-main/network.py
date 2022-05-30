"""
Some utilities on top of Graph / networkx_graph to work on Networks and flows

- A convenient constructor
- Display explicitly showing weith 1 edges
"""

from typing import Any, Sequence, Tuple, Callable
import networkx                  # type: ignore
import graph_networkx
import matplotlib.pyplot as plt  # type: ignore


Node = Any
Capacity = Any
Edge = Tuple[Node, Node, Capacity]
NetworkType = Any


# Works by default with networkx
# Not yet completly compatible with homemade Graph yet

Graph = graph_networkx.Graph
graph = networkx


def Network(nodes: Sequence[Node], edges: Sequence[Edge]) -> NetworkType:
    """
    Renvoie un réseau, c'est-à-dire un graphe orienté donné par sa liste
    de noeuds et d'arêtes
    """
    return Graph(nodes, edges=[(a, b, c) for a, b, c in edges if c != 0], directed=True)


def set_edge_capacity(self: Any, v1: Node, v2: Node, c: Capacity) -> None:
    """
    Donne la capacité `c` à l'arête `(v1,v2)`

    INPUT:

        - v1, un sommet du graphe
        - v2, un sommet du graphe
        - c la capacité de l'arête (v1,v2)
    """
    if c == 0:
        if v2 in self[v1]:
            self.remove_edge(v1, v2)
    elif v2 not in self[v1]:
        self.add_edge(v1, v2, weight=c)
    else:
        self[v1][v2]["weight"] = c


def show(self: networkx.Graph) -> Any:
    edge_labels = {(u, v): self.get_edge_data(u, v)["weight"] for u, v in self.edges()}
    layout = graph_networkx.default_layout(self)

    plt.figure()
    networkx.draw(
        self,
        layout,
        width=3,
        linewidths=1,
        node_size=500,
        node_color="lightgray",
        alpha=0.9,
        labels={node: node for node in self.nodes()},
    )
    networkx.draw_networkx_edge_labels(
        self, layout, edge_labels=edge_labels, font_color="black", label_pos=0.5
    )
    plt.axis("off")
    plt.show()


def is_equal(self: NetworkType, other: NetworkType) -> bool:
    """
    Renvoie si deux réseaux ont les mêmes noeuds avec mêmes arrêtes et mêmes capacités
    """
    return self.nodes() == other.nodes() and all(
        self.capacity(i, j) == other.capacity(i, j)
        for i in self.nodes()
        for j in self.nodes()
    )


graph.Graph.show = show
graph.Graph.is_equal = is_equal
graph.Graph.set_edge_capacity = set_edge_capacity


class Examples:
    """
    Une collection de réseaux, pour tests, ...
    """

    def __init__(self, Network: Callable) -> None:
        self.Network = Network

    def example1(self) -> NetworkType:
        return self.Network(
            nodes=list(range(7)),
            edges=[
                (0, 1, 1),
                (0, 2, 2),
                (0, 3, 1),
                (1, 4, 3),
                (2, 1, 1),
                (2, 4, 1),
                (3, 5, 2),
                (4, 6, 5),
                (5, 2, 1),
                (5, 6, 4),
                (6, 3, 3),
            ],
        )

    def example2(self) -> NetworkType:
        return self.Network(
            nodes=list(range(7)),
            edges=[
                (0, 1, 1),
                (0, 2, 1),
                (0, 3, 0),
                (1, 4, 2),
                (2, 1, 1),
                (2, 4, 1),
                (3, 5, 2),
                (4, 6, 3),
                (5, 2, 1),
                (5, 6, 1),
                (6, 3, 2),
            ],
        )

    def example3(self) -> NetworkType:
        return self.Network(
            nodes=list(range(7)),
            edges=[
                (0, 1, 1),
                (0, 2, 1),
                (0, 3, 0),
                (1, 4, 3),
                (2, 1, 1),
                (2, 4, 1),
                (3, 5, 2),
                (4, 6, 3),
                (5, 2, 1),
                (5, 6, 1),
                (6, 3, 2),
            ],
        )

    def example4(self) -> NetworkType:
        return self.Network(
            nodes=list(range(7)),
            edges=[
                (0, 1, 1),
                (0, 2, 1),
                (0, 3, 0),
                (1, 4, 3),
                (2, 1, 1),
                (2, 4, 1),
                (3, 5, 2),
                (4, 6, 3),
                (5, 2, 2),
                (5, 6, 1),
                (6, 3, 2),
            ],
        )

    def small_example(self) -> NetworkType:
        return self.Network(
            nodes=list(range(4)),
            edges=[(0, 1, 3), (0, 2, 3), (1, 2, 2), (1, 3, 3), (2, 3, 3)],
        )

    def small_example2(self) -> NetworkType:
        return self.Network(
            nodes=list(range(4)),
            edges=[(0, 1, 8), (0, 2, 5), (1, 2, 2), (1, 3, 3), (2, 3, 6)],
        )

    def small_example2_flow(self) -> NetworkType:
        return self.Network(
            nodes=list(range(4)),
            edges=[(0, 1, 5), (0, 2, 4), (1, 2, 2), (1, 3, 3), (2, 3, 6)],
        )


examples = Examples(Network)
