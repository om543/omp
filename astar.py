# A* Algorithm in Python
# Example: Finding shortest path in a graph

def a_star(graph, heuristic, start, goal):

    open_list = [start]
    closed_list = []

    g = {}
    g[start] = 0

    parent = {}
    parent[start] = start

    while open_list:

        # Find node with lowest f = g + h
        current = open_list[0]

        for node in open_list:
            if g[node] + heuristic[node] < g[current] + heuristic[current]:
                current = node

        # Goal reached
        if current == goal:
            path = []

            while parent[current] != current:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            print("Path found:", path)
            return

        open_list.remove(current)
        closed_list.append(current)

        # Check neighbors
        for neighbor, cost in graph[current]:

            if neighbor not in open_list and neighbor not in closed_list:
                open_list.append(neighbor)
                parent[neighbor] = current
                g[neighbor] = g[current] + cost

            else:
                if g[neighbor] > g[current] + cost:
                    g[neighbor] = g[current] + cost
                    parent[neighbor] = current

                    if neighbor in closed_list:
                        closed_list.remove(neighbor)
                        open_list.append(neighbor)

    print("Path does not exist!")


# Graph with cost
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 3,
    'G': 0
}

start = input("Enter start node: ")
goal = input("Enter goal node: ")

a_star(graph, heuristic, start, goal)

'''# ---------------- INPUT SECTION ----------------

graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

# Input graph
for i in range(n):

    node = input("\nEnter node name: ")

    h = int(input("Enter heuristic value of " + node + ": "))
    heuristic[node] = h

    neighbors = int(input("Enter number of neighbors of " + node + ": "))

    graph[node] = []

    for j in range(neighbors):

        neighbor = input("Enter neighbor node: ")
        cost = int(input("Enter cost: "))

        graph[node].append((neighbor, cost))


# Start and Goal
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Run A*
a_star(graph, heuristic, start, goal)'''
