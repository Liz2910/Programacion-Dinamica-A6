#   KRUSKAL + GRAFOS DEL PUNTO 1

import networkx as nx
import matplotlib.pyplot as plt

#   UNION-FIND
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            elif self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1


#   KRUSKAL MÁXIMO
def kruskal_maximum_spanning_tree(nodes, edges):
    idx = {node: i for i, node in enumerate(nodes)}
    edges_sorted = sorted(edges, key=lambda x: x[2], reverse=True)

    uf = UnionFind(len(nodes))
    mst = []

    for u, v, w in edges_sorted:
        if uf.find(idx[u]) != uf.find(idx[v]):
            uf.union(idx[u], idx[v])
            mst.append((u, v, w))

        if len(mst) == len(nodes) - 1:
            break

    return mst

#   DIBUJO EXACTO (POSICIONES MANUALES)
def draw_graph(title, nodes, edges, mst, pos):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    plt.figure(figsize=(14, 6))

    # Grafo original
    plt.subplot(1, 2, 1)
    nx.draw(G, pos, with_labels=True, node_size=850, node_color="#6aa9ff", font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): w for u, v, w in edges})
    plt.title(f"{title} - Grafo Original")

    # Maximum Spanning Tree
    T = nx.Graph()
    T.add_weighted_edges_from(mst)

    plt.subplot(1, 2, 2)
    nx.draw(T, pos, with_labels=True, node_size=850, node_color="#98ffb6",
            edge_color="black", width=3, font_size=12)
    nx.draw_networkx_edge_labels(T, pos, edge_labels={(u, v): w for u, v, w in mst})
    plt.title(f"{title} - Maximum Spanning Tree")

    plt.show()

#   GRAFO 1 (A–B–C–D–E)
pos_graph1 = {
    "A": (-3, 0),
    "B": (-1, 2),
    "C": (1, 2),
    "D": (1, 0),
    "E": (3, 0),
}

edges1 = [
    ("A", "B", 5),
    ("A", "D", 6),
    ("B", "C", 1),
    ("B", "D", 3),
    ("C", "D", 4),
    ("C", "E", 6),
    ("D", "E", 2),
]

nodes1 = list(pos_graph1.keys())
mst1 = kruskal_maximum_spanning_tree(nodes1, edges1)

print("GRAFO 1 - Árbol de Expansión Máximo")
for u, v, w in mst1:
    print(f"{u} -- {v}  (peso: {w})")

draw_graph("GRAFO 1", nodes1, edges1, mst1, pos_graph1)

#   GRAFO 2 (12 nodos) — Posiciones fijas
pos_graph2 = {
    "A": (-2, 3),
    "B": (2, 3),

    "C": (-4, 1),
    "D": (-2, 1),
    "E": (2, 1),
    "F": (4, 1),

    "G": (-4, -1),
    "H": (-2, -1),
    "I": (2, -1),
    "J": (4, -1),

    "K": (-2, -3),
    "L": (2, -3),
}

edges2 = [
    ("A", "B", 3),
    ("A", "C", 5),
    ("A", "D", 4),

    ("B", "E", 3),
    ("B", "F", 6),

    ("C", "D", 2),
    ("C", "G", 4),

    ("D", "E", 1),
    ("D", "H", 5),

    ("E", "I", 4),
    ("E", "F", 2),

    ("F", "J", 5),

    ("G", "H", 3),
    ("G", "K", 6),

    ("H", "I", 6),
    ("H", "K", 7),

    ("I", "J", 3),
    ("I", "L", 5),

    ("K", "L", 8)
]

nodes2 = list(pos_graph2.keys())
mst2 = kruskal_maximum_spanning_tree(nodes2, edges2)

print("\nGRAFO 2 - Árbol de Expansión Máximo")
for u, v, w in mst2:
    print(f"{u} -- {v}  (peso: {w})")

draw_graph("GRAFO 2", nodes2, edges2, mst2, pos_graph2)