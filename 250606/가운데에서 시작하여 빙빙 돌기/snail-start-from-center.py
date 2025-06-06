n = int(input())
arr = [[0] * n for _ in range(n)]
drs, dcs = [0, -1, 0, 1], [-1, 0, 1, 0]
r, c, d = [n-1, n-1, 0]

def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < n

for i in range(n * n, 0, -1):
    arr[r][c] = i
    nr, nc = r + drs[d], c + dcs[d]
    if not(in_range(nr, nc) and arr[nr][nc] == 0):
        d = (d + 1) % 4
        nr, nc = r + drs[d], c + dcs[d]
    r, c = nr, nc

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()