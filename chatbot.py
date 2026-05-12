n = int(input("Vertices: "))

g = []

print("Enter matrix:")

for i in range(n):
    g.append(list(map(int, input().split())))

s = [1]+[0]*(n-1)

for k in range(n-1):
    m = 999

    for i in range(n):
        if s[i]:
            for j in range(n):
                if not s[j] and g[i][j]:
                    if m > g[i][j]:
                        m = g[i][j]
                        x, y = i, j

    print(x, "-", y, "=", g[x][y])
    s[y] = 1
