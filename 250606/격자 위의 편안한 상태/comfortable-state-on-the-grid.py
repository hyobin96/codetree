n, m = map(int, input().split())
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
arr = [[0] * n for _ in range(n)]

def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < n

for _ in range(m):
    r, c = map(lambda x: x - 1, map(int, input().split()))
    arr[r][c] = 1
    cnt = 0
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and arr[nr][nc] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)
