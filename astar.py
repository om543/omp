g = {}
h = {}

n = int(input("Nodes: "))

for i in range(n):
    a = input("Node: ")
    h[a] = int(input("Heuristic: "))

    m = int(input("Neighbours: "))
    t = []

    for j in range(m):
        b = input("Neighbour: ")
        c = int(input("Cost: "))
        t.append((b, c))

    g[a] = t

s = input("Start: ")
goal = input("Goal: ")

o = [(s, 0)]

while o:
    o.sort(key=lambda x: x[1]+h[x[0]])

    x, c = o.pop(0)

    print(x, end=" ")

    if x == goal:
        break

    for i, j in g[x]:
        o.append((i, c+j))
