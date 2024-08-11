from heapq import heapify, heappop, heappush
import networkx as nx
import matplotlib.pyplot as plt
from networkx import dijkstra_path
from networkx import Graph

# Create the graph
plt.figure(1, figsize=(80, 6), dpi=60)


def draw_graph(graph):
    # Draw the graph
    pos = nx.spring_layout(graph)
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=500,
        font_size=10,
    )
    plt.title("Graph Visualization")


def print_adjacency_matrix(G):
    # Adjacency Matrix representation
    adjacency_matrix = nx.adjacency_matrix(G)
    print("\nAdjacency Matrix Representation:")
    print(adjacency_matrix.todense())


# Dijkstra's Algorithm
def dijkstra(graph: Graph, start_vertex):

    D = {node: float("inf") for node in graph.nodes}
    visited = set()
    D[start_vertex] = 0
    pq = [(0, start_vertex)]
    heapify(pq)
    while pq:
        current_distance, current_node = heappop(pq)
        if current_node in visited:
            continue
        # for v in range(num_vertices):
        #     if v not in visited and D[v] < min_distance:
        #         min_distance = D[v]
        #         current_vertex = v

        visited.add(current_node)
        for neighbor in graph.neighbors(current_node):
            tentative_distance = current_distance + 1
            if tentative_distance < D[neighbor]:
                D[neighbor] = tentative_distance

                heappush(pq, (tentative_distance, neighbor))

    P = {node: None for node in graph.nodes}
    print(D)
    for node, distance in D.items():

        current_neighbors = graph.neighbors(node)
        for neighbor in current_neighbors:
            print(node, distance, neighbor, D[neighbor])
            if D[neighbor] == distance + 1:
                P[neighbor] = node

    return D, P


def create_graph(start_vertex):
    G = nx.Graph()
    return G


def show_graph():
    # Adjust the plot layout to accommodate the larger text box and change aspect ratio
    plt.subplots_adjust(right=0.7)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()


def main():
    edges = [
        (1, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (3, 4),
        (3, 5),
        (4, 5),
        (0, 2),
        (0, 4),
        (0, 3),
        (3, 4),
        (5, 9),
        (9, 13),
        (13, 13),
    ]
    G = create_graph(start_vertex=0)
    G.add_edges_from(edges)

    # P, D = create_graph(G, start_vertex=0)
    draw_graph(G)
    print_adjacency_matrix(G)
    D, P = dijkstra(G, 1)
    path = dijkstra_path(G, 0, 5)
    # Create a text box within the plot with adjusted size
    textstr = (
        f"Adjacency Matrix Representation:\n{nx.adjacency_matrix(G).todense()}\n\n"
    )
    textstr += f"Shortest path from {0} to {5}: {path}\n"
    textstr += f"P: {P}"
    props = dict(boxstyle="round", facecolor="white", alpha=0.5)
    plt.text(
        1.05,
        0.25,
        textstr,
        transform=plt.gca().transAxes,
        fontsize=8,
        verticalalignment="center",
        bbox=props,
    )
    print(textstr)
    show_graph()


if __name__ == "__main__":
    main()
