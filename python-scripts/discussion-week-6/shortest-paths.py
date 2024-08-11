import matplotlib.pyplot as plt
import networkx as nx

from heapq import heapify, heappop, heappush
import random
import string


class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(
        self,
        weight,
        node1,
        node2,
    ):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def shortest_distances(self, source: str):

        dist = {node: float("inf") for node in self.graph}
        dist[source] = 0
        pq = [(0, source)]
        heapify(pq)
        visited = set()
        while pq:
            current_distance, current_node = heappop(pq)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.graph.get(current_node).items():
                tent_dist = current_distance + weight
                if dist.get("neighbor") == None:
                    dist[neighbor] = tent_dist
                    heappush(pq, (tent_dist, neighbor))
                    continue
                if tent_dist < dist[neighbor]:
                    dist[neighbor] = tent_dist
                    heappush(pq, (tent_dist, neighbor))

        predecessors = {node: None for node in self.graph}

        for node, distance in dist.items():
            for neighbor, weight in self.graph[node].items():
                print(neighbor, weight)
                if dist[neighbor] == distance + weight:
                    print("ADDING PREDECESSOR")
                    predecessors[neighbor] = node

        return dist, predecessors

    def shortest_path(self, source: str, target: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()

        return path


def create_random_pairs(alphabet):
    """
    Creates a list of random pairs of alphabet letters as tuples, ensuring each letter is connected.
    Returns the pairs list and the original alphabet list.
    """

    pairs = []
    for letter in alphabet:
        # Ensure each letter has at least one connection
        while True:
            second_letter = random.choice(alphabet)
            if letter != second_letter and (letter, second_letter) not in pairs:
                pairs.append((letter, second_letter))
                break  # Exit the loop once a valid connection is made

    # Add more random pairs to increase connectivity (optional)
    for _ in range(len(alphabet)):  # You can adjust the number of additional pairs
        first_letter = random.choice(alphabet)
        second_letter = random.choice(alphabet)
        if (
            first_letter != second_letter
            and (first_letter, second_letter) not in pairs
            and (second_letter, first_letter) not in pairs
        ):
            pairs.append((first_letter, second_letter))

    return pairs


def main():
    start = "a"
    alphabet = list(string.ascii_lowercase)
    pairs = create_random_pairs(alphabet)
    edges = [{"weight": 1, "node1": tuple[0], "node2": tuple[1]} for tuple in pairs]
    graph = Graph()
    for edge in edges:
        graph.add_edge(edge.get("weight"), edge.get("node1"), edge.get("node2"))
    dist, predecessors = graph.shortest_distances(edges[0]["node1"])
    print(predecessors)

    print(graph.shortest_path("b", "f"))
    print(graph.shortest_path("a", "z"))
    edges = [(edge["node1"], edge["node2"]) for edge in edges]

    G = nx.Graph()
    G.add_edges_from(edges)

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(
        G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10
    )
    plt.title("Graph Visualization")
    plt.show()


if __name__ == "__main__":
    main()
