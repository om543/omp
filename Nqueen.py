n = int(input("N: "))

b = [-1]*n


def safe(r, c):
    for i in range(r):
        if b[i] == c or abs(b[i]-c) == abs(i-r):
            return 0
    return 1


def solve(r):
    if r == n:
        print(b)
        return

    for c in range(n):
        if safe(r, c):
            b[r] = c
            solve(r+1)


solve(0)
