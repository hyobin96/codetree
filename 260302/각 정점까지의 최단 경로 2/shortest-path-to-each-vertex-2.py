import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = 2e9

dists = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dists[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    dists[u][v] = min(dists[u][v], w)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dists[i][j] > dists[i][k] + dists[k][j]:
                dists[i][j] = dists[i][k] + dists[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dists[i][j] if dists[i][j] != INF else -1, end=" ")
    print()