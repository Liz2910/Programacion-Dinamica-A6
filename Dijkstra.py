#   DIJKSTRA (GRAFO DIRIGIDO)


import heapq
import networkx as nx
import matplotlib.pyplot as plt

#   ALGORITMO DE DIJKSTRA (DIRIGIDO)
def dijkstra_directed_path(nodes, edges, start):
    # Crear adyacencias
    graph = {n: [] for n in nodes}
    for u, v, w in edges:
        graph[u].append((v, w))

    # Distancias iniciales
    dist = {n: float("inf") for n in nodes}
    dist[start] = 0

    # Para reconstruir camino
    parent = {n: None for n in nodes}

    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent

#   POSICIONES DEL GRAFO
pos_graph = {
    "A": (-3, 0),
    "B": (-1, 2),
    "C": (1, 2),
    "D": (-1, 0),
    "E": (3, 0),
}

#   GRAFO DIRIGIDO
edges_dir = [
    ("A", "B", 3),
    ("A", "D", 7),
    ("B", "C", 4),
    ("B", "D", 2),
    ("C", "D", 5),
    ("C", "E", 6),
    ("D", "E", 4),
]

nodes = list(pos_graph.keys())

#   EJECUTAR DIJKSTRA DESDE A
distancias, padres = dijkstra_directed_path(nodes, edges_dir, start="A")

print("\nDISTANCIAS MÍNIMAS DESDE A")
for n, d in distancias.items():
    print(f"A → {n} = {d}")

#   RECONSTRUIR CAMINOS MÍNIMOS DESDE A
def build_paths(parents, start):
    paths = {}
    for node in parents:
        if parents[node] is None and node != start:
            paths[node] = None
            continue

        path = []
        current = node
        while current is not None:
            path.append(current)
            current = parents[current]
        paths[node] = list(reversed(path))
    return paths

paths = build_paths(padres, "A")

print("\nCAMINOS")
for node, path_nodes in paths.items():
    print(f"A → {node}: {path_nodes}")

#   DIBUJAR AMBAS GRÁFICAS
def draw_dijkstra(nodes, edges, pos, distances, parents):
    # Grafo original
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)

    # Construimos las aristas del camino mínimo
    mst_edges = []
    for node, parent in parents.items():
        if parent is not None:
            # peso de la arista
            for u, v, w in edges:
                if u == parent and v == node:
                    mst_edges.append((u, v, w))

    # Grafo del camino mínimo
    T = nx.DiGraph()
    T.add_weighted_edges_from(mst_edges)

    plt.figure(figsize=(16, 6))

    # GRAFO ORIGINAL
    plt.subplot(1, 2, 1)
    nx.draw(G, pos, with_labels=True, node_size=950,
            node_color="#6aa9ff", font_size=12, arrowsize=25)
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={(u, v): w for u, v, w in edges})
    plt.title("Grafo Dirigido Original")

    # CAMINO MÍNIMO
    plt.subplot(1, 2, 2)
    nx.draw(T, pos, with_labels=True, node_size=950,
            node_color="#98ffb6", edge_color="green",
            width=3, font_size=12, arrowsize=25)
    nx.draw_networkx_edge_labels(
        T, pos, edge_labels={(u, v): w for u, v, w in mst_edges})
    plt.title("Dijkstra — Caminos Mínimos desde A")

    plt.show()

draw_dijkstra(nodes, edges_dir, pos_graph, distancias, padres)