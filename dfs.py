# Depth First Search (DFS) using Recursion
# Undirected Graph without using class

def add_edge(graph, u, v):
    # Add nodes if not present
    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    # Undirected graph
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Main Program
graph = {}

edges = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for i in range(edges):
    u, v = input().split()
    add_edge(graph, u, v)

start = input("Enter starting vertex: ")

print("\nDFS Traversal:")
visited = set()
dfs(graph, start, visited)
