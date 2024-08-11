import networkx as nx
import matplotlib.pyplot as plt

# Create a graph with 7 nodes and at least 10 edges

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 5), (5, 7), (6, 7), (1, 7)]
print(f"Nodes:\n\n{edges}")
plt.figure(1, figsize=(100, 8), dpi=60)
G = nx.Graph()

G.add_edges_from(edges)
# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=12)
plt.title("Graph Visualization")
# Adjacency List representation
adjacency_list = {}
for node in G.nodes():
    adjacency_list[node] = list(G.neighbors(node))

print("\nAdjacency List Representation:")
for node, neighbors in adjacency_list.items():
    print(f"Node {node}: {neighbors}")


# Graph Traversals - I will insert adjacent nodes in numeric order, smallest to largest
def breadth_first_search(graph, start_node):
    visited = set()
    queue = [start_node]
    visited.add(start_node)
    bfs_result = []  # Initialize the result list

    print("\nBreadth-First Traversal:")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        bfs_result.append(node)  # Add the node to the result list

        neighbors = sorted(graph[node])  # Sort neighbors in ascending order
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return bfs_result  # Return the traversal result


def depth_first_search(graph, start_node):
    visited = set()
    stack = [start_node]
    dfs_result = []  # Initialize the result list

    print("\nDepth-First Traversal:")
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            dfs_result.append(node)  # Add the node to the result list
            visited.add(node)

            neighbors = sorted(
                graph[node], reverse=True
            )  # Sort neighbors in descending order
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

    return dfs_result  # Return the traversal result


# Choose a starting node (let's say node 1)
start_node = 1

# Perform traversals
bfs_result = breadth_first_search(adjacency_list, start_node)
dfs_result = depth_first_search(adjacency_list, start_node)
# Create the text for the adjacency list and traversals
textstr = f"Adjacency List Representation:\n"
for node, neighbors in adjacency_list.items():
    textstr += f"Node {node}: {neighbors}\n"

textstr += f"\nBreadth-First Traversal: {' '.join(map(str, bfs_result))}\n"
textstr += f"Depth-First Traversal: {' '.join(map(str, dfs_result))}\n"

# Create a text box within the plot
props = dict(boxstyle="round", facecolor="white", alpha=1)
plt.text(
    1.05,
    0.25,
    textstr,
    fontsize=12,
    verticalalignment="center",
    bbox=props,
)
plt.gca().set_aspect(
    "equal", adjustable="box"
)  # Set aspect ratio to 'equal' and make the axes box adjustable

plt.show()


plt.show()
