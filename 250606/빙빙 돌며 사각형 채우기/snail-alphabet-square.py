n, m = map(int, input().split())
arr = [[' '] * m for _ in range(n)]
drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < m

r, c, d = 0, 0, 0
num = ord('A')
diff = ord('Z') - ord('A') + 1
for i in range(0, n*m):
    arr[r][c] = chr(num + (i % diff))
    nr, nc = r + drs[d], c + dcs[d]
    if not(in_range(nr, nc) and arr[nr][nc] == ' '):
        d = (d + 1) % 4
        nr, nc = r + drs[d], c + dcs[d]
    r, c = nr, nc

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()

