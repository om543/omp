# Breadth First Search (BFS) using Recursion
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


# Recursive BFS function
def bfs(graph, queue, visited):
    if not queue:
        return

    node = queue.pop(0)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs(graph, queue, visited)


# Main Program
graph = {}

edges = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for i in range(edges):
    u, v = input().split()
    add_edge(graph, u, v)

start = input("Enter starting vertex: ")

print("\nBFS Traversal:")

visited = set()
visited.add(start)

queue = [start]

bfs(graph, queue, visited)
