# Prim's Minimum Spanning Tree Algorithm
# Greedy Algorithm in Python

INF = 9999999

# Number of vertices
n = int(input("Enter number of vertices: "))

# Adjacency Matrix
graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

selected = [False] * n

# Start from vertex 0
selected[0] = True

edge_count = 0
total_cost = 0

print("\nEdges in MST:")

while edge_count < n - 1:

    minimum = INF
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):

                # Select minimum edge
                if (not selected[j]) and graph[i][j]:

                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", graph[x][y])

    total_cost += graph[x][y]
    selected[y] = True
    edge_count += 1

print("\nMinimum Cost =", total_cost)
