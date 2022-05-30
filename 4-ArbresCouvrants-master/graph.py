# -*- coding: utf-8 -*-
# python -m doctest -v graph.py


class UnionFind:
    """
    Structure de UnionFind optimisée
    
        - Compression lors de l'appel à find
        - Heuristique de rang lors de l'appel à union
    """
    def __init__(self, V):
        self.father = dict()
        self.rank = dict()
        for v in V:
            self.father[v] = v
            self.rank[v] = 0
        
    def find(self, u):
        # Recherche du canonique par saut
        v = self.father[u]
        while v != self.father[v]:
            v = self.father[v]
        # Compression
        if v != self.father[u]:
            self.father[u] = v
        return v
        
    def union(self, u, v):
        # Heuristique de rang
        rank_u = self.rank[u]
        rank_v = self.rank[v]
        canon_u = self.find(u)
        canon_v = self.find(v)
        if rank_u == rank_v:
            self.father[canon_v] = canon_u
            self.rank[canon_u] += 1
        elif rank_u > rank_v:
            self.father[canon_v] = canon_u
        else:
            self.father[canon_u] = canon_v

class Graph:
    def __init__(self,
                 vertices=None,
                 matrix=None,
                 edges=None,
                 directed=False):
        """
        Initialisation d'un graphe

        INPUT :

            - vertices, un itérables sur les sommets du graphes
            - matrix, la matrice d'adjacence du graphe suivant les mêmes indices que `vertices`
            - edges, une liste de triplets (v1, v2, c) où v1 et v2 sont des sommets et c un nombre positif

        """
        if vertices is None:
            vertices = []

        #self._vertices = vertices
        self._nodes = list(vertices)
        # création d'un dictionnaire associant son indice à chaque sommet
        # (vous pouvez modifier si ça n'est pas utile à votre implantation)
        self._vertex_indices = {vertices[i]: i for i in range(len(vertices))}
        self._directed = directed

        # on ne peut pas donner à la fois matrix et edges
        if matrix is not None and edges is not None:
            raise ValueError("'matrix' et 'edges' ne peuvent pas être tous les deux initialisés")

        # initialisation différenciée: implantez les méthodes en question
        if matrix is not None:
            self._init_from_matrix(matrix)
        elif edges is not None:
            self._init_from_edges(edges)
        else:
            self._init_empty()
    
    def copy(self):
        return Graph(vertices=self.vertices(), edges=self.edges())

    def _init_empty(self):
        """
        Initialisation d'un graphe vide (sans arêtes)
        """
        self._edges = {}


    def _init_from_matrix(self, matrix):
        """
        Initialisation à partir d'une matrice

        EXAMPLES:

            >>> M = matrix = [[0, 12,  0, 12],
            ...               [0,  0, 23, 0],
            ...               [0,  0,  0, 0],
            ...               [0,  0,  0, 0]]
            >>> G = Graph(vertices = ["A", "B", "C", "D"],
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

    def _init_from_edges(self, edges):
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

    def is_directed(self):
        """
        Renvoie si le graph est orienté
        """
        return self._directed

    def set_edge_capacity(self, v1, v2, c):
        """
        Donne la capacité `c` à l'arête `(v1,v2)`

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
            - c la capacité de l'arête (v1,v2)
        """
        self._edges[(v1, v2)] = c
        if not self._directed:
            self._edges[(v2, v1)] = c

    def add_vertex(self, v):
        """
        Ajoute le sommet `v` au graphe

        INPUT:

            - v, un sommet du graphe

        """
        if v not in self._nodes:
            self._nodes.append(v)

    def vertices(self):
        """
        Renvoie la liste des sommets du graphe

        EXAMPLES::

            >>> from graph import examples
            >>> G = examples.cours_1_reseau()
            >>> G.vertices()
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        """
        return self._nodes

    def vertex_number(self):
        """
        Renvoie le nombre de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.vertex_number()
            8
        """
        return len(self._nodes)

    def has_vertex(self, v1):
        """
        Renvoie vrai si v1 est un sommet du graphe

        INPUT:

            - v1, un sommet
        """
        return v1 in self._nodes

    def edges(self):
        """
        Renvoie un tuple de triplets `(v1,v2,c)` correspondant aux arêtes du graphe avec leur capacité.

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
        """
        return tuple([(v1, v2, self._edges[(v1, v2)]) for (v1, v2) in self._edges])

    def edge_number(self):
        """
        Renvoie le nombre d'arêtes du graphe
        """
        return len(self._edges)


    def is_edge(self, v1, v2):
        """
        Renvoie si l'arête (v1,v2) existe

        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
        """
        return v2 in self.successors(v1)
    
    def remove_edge(self, v1, v2):
        """
        Supprime une arête du graphe si elle existe
        
        INPUT:

            - v1, un sommet du graphe
            - v2, un sommet du graphe
            
        RETURN: 
        
            Capacité de l'arête (v1, v2) ou None
        """
        if self._edges.__contains__((v1, v2)):
            res = self._edges.pop((v1, v2))
            if not self._directed:
                self._edges.pop((v2, v1))
            return res
        return None

    def capacity(self, v1, v2):
        """
        Renvoie la capacité de l'arête (v1,v2) (si l'arête n'existe pas, la capacité est 0)

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
        """
        res = self._edges.get((v1, v2))
        return 0 if res is None else res


    def matrix(self):
        """
        Retourne la matrice associée au graphe

        Soit `n` le nombre de sommets du graphe. Cette méthode renvoie
        une liste `M` de n listes de taille n, de sorte que `M[i][j]`
        est la capacité de l'arête reliant le i-ème sommet au j-ème
        sommet dans le graphe, s'il y en a une, et 0 sinon.

        EXAMPLES::

            >>> G = examples.directed()
            >>> G.matrix()              # doctest: +NORMALIZE_WHITESPACE
            [[0, 12, 0, 12],
             [0, 0, 23, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        """
        return [[ self.capacity(v1,v2)
                  for v2 in self.vertices() ]
                for v1 in self.vertices() ]

    def to_dict(self):
        """
        Retourne le dictionnaire associé au graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.to_dict()
            {'A': ('B', 'G', 'F'), 'B': ('A', 'C', 'G'), 'C': ('B', 'D', 'G', 'H'), 'D': ('C', 'E', 'H'), 'E': ('D', 'F', 'G', 'H'), 'F': ('A', 'E', 'G'), 'G': ('A', 'B', 'C', 'E', 'F', 'H'), 'H': ('C', 'D', 'E', 'G')}

        """
        return self._edges

    def predecessors(self, v):
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
        """
        return tuple([v1 for v1 in self._nodes if self._edges.get((v1, v)) is not None])

    def successors(self, v):
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
        """
        return tuple([v2 for v2 in self._nodes if self._edges.get((v, v2)) is not None])
    
    neighbors = successors

    def is_path(self, p):
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


    def networkx(self):
        import graph_networkx
        return graph_networkx.Graph(self.vertices(), self.edges(), directed=self.is_directed())

    def show(self):
        return self.networkx().show()

    ######################################################################
    # Partie sur les cycles dans un graphe à copier dans votre solution
    ######################################################################
    def is_cycle(self, c):
        """
        Renvoie si `c` est un chemin valide dans le graphe

        INPUT:

            - c, une liste de sommets du graphe

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.is_cycle([])
            False
            >>> G.is_cycle(["D"])
            False
            >>> G.is_cycle(["D", "G"])
            False
            >>> G.is_cycle(["D", "H"])
            False
            >>> G.is_cycle(["D", "H", "C"])
            True
            >>> G.is_cycle(["A", "G", "F"])
            True
            >>> G.is_cycle(["D", "H", "G", "B", "A", "F", "E"])
            True
            >>> G.is_cycle(["C", "G", "B", "A", "G", "H"])
            False
        """
        return len(c) > 2 and len(set(c)) == len(c) and self.is_path(c) and self.is_edge(c[0], c[-1])

    def connected_components(self):
        """
        Renvois les composantes connexe du graphe

        OUTPUT:

            - une liste d'ensemble de noeuds

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> CCG = G.connected_components()
            >>> len(CCG)
            1
            >>> sorted(list(CCG[0]))
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            >>> examples.undirected().connected_components()
            [{1, 2, 3}, {4}]
            >>> examples.disconnected().connected_components()
            [{1, 2, 5}, {3, 4}]
        """
        
        # Parcours en profondeur du graphe avec pile
        def depth_path(G, u):
            """
            INPUT:
            - 'G' - un graphe
            - 'u' - un sommet du graphe

            OUTPUT: la liste des sommets `v` de `G`
                    tels qu'il existe un chemin de `u` à `v`
            """
            marked = {u} # L'ensemble des sommets déjà rencontrés
            todo   = [u] # Pile des sommets rencontrés

            while todo:
                # Invariants:
                # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
                # - Si `v` est dans `marked` et pas dans `todo`
                #   alors tous les voisins de `v` sont dans dans `marked`

                # On prend le sommet `v` de la pile et on le dépile
                v = todo.pop()
                # On ajoute directement `v` aux sommets visités
                marked.add(v)
                # On empile les voisins `w` de `v`
                for w in G.neighbors(v):
                    if w not in marked:
                        todo.append(w)

            return marked
        
        # Recherche des composantes connexes
        res = []
        marked = set()
        for u in self.vertices():
            component = {}
            # On ne regarde pas les composantes connexes déjà trouvées
            if u not in marked:
                component = depth_path(self, u)
                marked.update(component)
                res.append(component)
        return res
    
    def connected_componentsUF(self):
        """
        Renvois les composantes connexe du graphe
        Algorithme optimisé avec la structure UnionFind

        OUTPUT:

            - une liste d'ensemble de noeuds
        """
        
        # Regroupement des sommets avec UnionFind
        UF = UnionFind(self.vertices())
        for (u, v, _) in self.edges():
            UF.union(u, v)
        # Récupération des composantes connexes
        components = dict()
        for v in self.vertices():
            canonical = UF.find(v)
            if not components.__contains__(canonical):
                components[canonical] = {v}
            else:
                components[canonical].add(v)
        return list(components.values())

    def is_connected(self):
        """
        Renvoie si le graphe est connexe

        EXAMPLES::

            >>> examples.cours_1_reseau().is_connected()
            True
            >>> examples.undirected().is_connected()
            False
            >>> examples.disconnected().is_connected()
            False
            >>> examples.tree1().is_connected()
            True
        """
        # Un graphe connexe possède une seule composante connexe
        return len(self.connected_components()) == 1

    def is_acyclic(self):
        """
        Renvoie si le graphe est acyclique

        EXAMPLES::

            >>> examples.cours_1_reseau().is_acyclic()
            False
            >>> examples.undirected().is_acyclic()
            True
            >>> examples.disconnected().is_acyclic()
            True
            >>> examples.lines().is_acyclic()
            True
        """
        # Un graphe est acyclique si et seulement si |V| = k + |E| avec k le nombre de composantes connexes
        # Dans mon implémentation len(G.edges()) est toujours multiple de 2 car dans un graphe non-orienté
        # les arêtes sont représentées dans les deux sens
        return len(self.vertices()) == (len(self.connected_components()) + (len(self.edges()) // 2))

    def is_tree(self):
        """
        Renvoie si le graphe est un arbre

        EXAMPLES::

            >>> examples.cours_1_reseau().is_tree()
            False
            >>> examples.undirected().is_tree()
            False
            >>> examples.disconnected().is_tree()
            False
            >>> examples.tree1().is_tree()
            True
            >>> examples.lines().is_tree()
            False
        """
        # Un arbre est un graphe connexe et acyclique
        return self.is_connected() and len(self.vertices()) == (len(self.edges()) // 2) + 1

    def find_cycle(self):
        """
        Renvoie un cycle du graphe

        OUTPUT:

            - une liste ou None si le graphe est acyclique

        EXAMPLES::

            >>> G = examples.cours_1_reseau()
            >>> G.is_cycle(G.find_cycle())
            True

            >>> G = examples.G2()
            >>> G.is_cycle(G.find_cycle())
            True

            >>> examples.undirected().find_cycle() is None
            True
            >>> examples.disconnected().find_cycle() is None
            True

            >>> for t in examples.trees():
            ...     assert(t.find_cycle() is None)

            >>> for G in examples.cyclic():
            ...     assert(G.is_cycle(G.find_cycle()))
        """
        
        # Parcours en profondeur du graphe avec pile
        def depth_path_cycle(G, u):
            """
            INPUT:
            - 'G' - un graphe
            - 'u' - un sommet du graphe

            OUTPUT: la liste des sommets `v` de `G`
                    tels qu'il existe un chemin de `u` à `v`
            """
            todo = [(None, u)] # Pile des sommets rencontrés
            path = [] # Chemin actuel depuis la racine 

            while todo:
                # Invariants:
                # - Si `v` est dans `marked`, alors il y a un chemin de `u` à `v`
                # - Si `v` est dans `marked` et pas dans `todo`
                #   alors tous les voisins de `v` sont dans dans `marked`

                # On prend le sommet `v` de la pile et on le dépile
                (_, v) = todo.pop()

                # Nombre d'éléments empilés
                size = len(todo)

                # On empile les voisins `w` de `v`
                for w in G.neighbors(v):
                    # Si on détecte un cyle alors on construit son chemin
                    if w in path[:-1]:
                        cycle = [w, v]
                        t = path.pop()
                        while t != w:
                            cycle.append(t)
                            t = path.pop()
                        # On stoppe la recherche
                        return cycle
                    # Sinon si le voisin n'est pas le dernier sommet du chemin alors on l'empile
                    elif w not in path[-1:]:
                        todo.append((v, w))

                # Si on a trouvé des voisins pour `v`
                # Alors on ajoute le sommet `v` au chemin actuel
                if size < len(todo):
                    path.append(v)

                # Sinon si la pile n'est pas vide
                # Alors on réduit le chemin actuel
                elif 0 < size:
                    (t, _) = todo[-1]
                    # On ne sait pas combien de sommets retirer
                    while t != path[-1]:
                        path.pop()

            return None
        
        cycle = None
        # Tant qu'on ne trouve pas de cycle on tente de faire
        # une recherche depuis chaque sommet
        for u in self.vertices():
            cycle = depth_path_cycle(self, u)
            if cycle is not None:
                break
        return cycle
    
    def kruskal(self):
        """
        Algorithme Kruskal de calcul de l'arbre recouvrant des poids minimum
        On utilise la structure UnionFind pour être efficace
        """
        # Création de l'arbre recouvrant des poids minimum
        T = Graph(vertices=self.vertices())
        # Structure UnionFind pour détecter les composantes connexes
        UF = UnionFind(self.vertices())
        # Tri dans l'ordre croissant des poids des arêtes
        edges = list(self.edges())
        edges.sort(key=lambda x: x[2])
        for (u, v, c) in edges:
            # On ne relie pas deux sommets dans le même composante connexe
            # Sinon cela créerait un cycle
            if UF.find(u) != UF.find(v):
                UF.union(u, v)
                T.set_edge_capacity(u, v, c)
        return T

    # Fin
    ######################################################################

import graph_examples
examples = graph_examples.Examples(Graph)
