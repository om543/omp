g = {}

n = int(input("Nodes: "))

for i in range(n):
    a = input("Node: ")
    g[a] = input("Neighbours: ").split()

v = []
q = [input("Start: ")]

while q:
    x = q.pop(0)

    if x not in v:
        print(x, end=" ")
        v.append(x)
        q += g[x]
