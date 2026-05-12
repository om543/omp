g = {}

n = int(input("Nodes: "))

for i in range(n):
    a = input("Node: ")
    g[a] = input("Neighbours: ").split()

v = []


def dfs(x):
    if x not in v:
        print(x, end=" ")
        v.append(x)

        for i in g[x]:
            dfs(i)


dfs(input("Start: "))
