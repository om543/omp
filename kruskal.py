e = []

n = int(input("Edges: "))

for i in range(n):
    u = input("U: ")
    v = input("V: ")
    w = int(input("Weight: "))

    e.append((w, u, v))

p = {}

for w, u, v in e:
    p[u] = u
    p[v] = v


def f(x):
    if p[x] == x:
        return x
    return f(p[x])


for w, u, v in sorted(e):
    if f(u) != f(v):
        print(u, "-", v, "=", w)
        p[f(u)] = f(v)
