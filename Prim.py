#   ALGORITMO DE PRIM (Árbol de Expansión Mínimo)

import heapq
import networkx as nx
import matplotlib.pyplot as plt

#   ALGORITMO DE PRIM (MÍNIMO)
def prim_mst(nodes, edges, start):
    # Construimos lista de adyacencia
    graph = {n: [] for n in nodes}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = set()
    mst = []

    # Cola de prioridad (peso, u, v)
    min_heap = [(0, start, None)]

    while min_heap and len(visited) < len(nodes):
        weight, u, parent = heapq.heappop(min_heap)

        if u in visited:
            continue

        visited.add(u)

        if parent is not None:
            mst.append((parent, u, weight))

        # Agregar vecinos
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))

    return mst

#   POSICIONES FIJAS PARA VISUALIZACIÓN
pos_graph1 = {
    "A": (-3, 0),
    "B": (-1, 2),
    "C": (1, 2),
    "D": (1, 0),
    "E": (3, 0),
}

#   GRAFO 1
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


#   EJECUTAR PRIM DESDE EL NODO "A"
mst1 = prim_mst(nodes1, edges1, start="A")

print("ÁRBOL DE EXPANSIÓN MÍNIMO (PRIM)")
for u, v, w in mst1:
    print(f"{u} -- {v}  (peso: {w})")

#   VISUALIZAR EL GRAFO ORIGINAL Y EL MST
def draw_graph_and_mst(nodes, edges, mst, pos):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    plt.figure(figsize=(14, 6))

    # Grafo original
    plt.subplot(1, 2, 1)
    nx.draw(G, pos, with_labels=True, node_size=900,
            node_color="#6aa9ff", font_size=12)
    nx.draw_networkx_edge_labels(G, pos,
                                 edge_labels={(u, v): w for u, v, w in edges})
    plt.title("Grafo Original")

    # MST generado con Prim
    T = nx.Graph()
    T.add_weighted_edges_from(mst)

    plt.subplot(1, 2, 2)
    nx.draw(T, pos, with_labels=True, node_size=900,
            node_color="#98ffb6", edge_color="black", width=3, font_size=12)
    nx.draw_networkx_edge_labels(T, pos,
                                 edge_labels={(u, v): w for u, v, w in mst})
    plt.title("Árbol de Expansión Mínimo (Prim)")

    plt.show()

draw_graph_and_mst(nodes1, edges1, mst1, pos_graph1)