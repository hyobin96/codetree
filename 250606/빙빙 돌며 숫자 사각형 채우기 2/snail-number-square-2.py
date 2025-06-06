n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
num = 1
drs, dcs = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < m

r, c, d = 0, 0, 0
for i in range(1, n * m + 1):
    arr[r][c] = i
    nr, nc = r + drs[d], c + dcs[d]
    if not(in_range(nr, nc) and arr[nr][nc] == 0):
        d = (d + 1) % 4
        nr, nc = r + drs[d], c + dcs[d]

    r, c = nr, nc

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=' ')
    print()    
    