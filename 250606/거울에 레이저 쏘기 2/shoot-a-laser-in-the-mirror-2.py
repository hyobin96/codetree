n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())
drs = [1, 0, -1, 0]
dcs = [0, -1, 0, 1]

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

mapper = [[0, 0, 0] for _ in range(n * 4 + 1)]
r, c, d = 0, 0, 0
for i in range(1, n * 4 + 1):
    mapper[i] = [r, c, d]
    if i % n == 0:
        d = (d + 1) % 4
    else:
        r, c = r + dr[d], c + dc[d]

def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < n

r, c, d = mapper[k]
cnt = 0
while True:
    cnt += 1
    if d == 0:
        if arr[r][c] == '/':
            d = 3
        else:
            d = 1
    elif d == 1:
        if arr[r][c] == '/':
            d = 0
        else:
            d = 2
    elif d == 2:
        if arr[r][c] == '/':
            d = 3
        else:
            d = 1
    else:
        if arr[r][c] == '/':
            d = 2
        else:
            d = 0
    nr, nc = r + drs[d], c + dcs[d]
    if in_range(nr, nc):
        r, c = nr, nc
    else:
        break
print(cnt)