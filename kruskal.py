# Kruskal's Minimum Spanning Tree Algorithm
# Greedy Algorithm in Python

parent = []

# Find function
def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

# Union function
def union(a, b):
    x = find(a)
    y = find(b)
    parent[x] = y


# Input
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = []

print("Enter edges and weights (u v w):")

for i in range(edges):
    u, v, w = map(int, input().split())
    graph.append([u, v, w])

# Sort edges by weight
graph.sort(key=lambda x: x[2])

# Initialize parent array
for i in range(vertices):
    parent.append(i)

mst_cost = 0

print("\nEdges in MST:")

# Kruskal Algorithm
for u, v, w in graph:

    if find(u) != find(v):
        union(u, v)
        print(u, "-", v, ":", w)
        mst_cost += w

print("\nMinimum Cost =", mst_cost)
