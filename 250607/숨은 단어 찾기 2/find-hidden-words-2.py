n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

drs, dcs = [-1, 0, 1, 0, -1, -1, 1, 1], [0, 1, 0, -1, -1, 1, 1, -1]

def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < m

cnt = 0
for i in range(n):
    for j in range(m):
        for dr, dc in zip(drs, dcs):
            r, c = i, j
            s = arr[r][c]
            for _ in range(2):
                r, c = r + dr, c + dc
                if not in_range(r, c):
                    break
                s += arr[r][c]
            if s == 'LEE':
                cnt += 1
print(cnt)