n, t = map(int, input().split())
query = input()
arr = [list(map(int, input().split())) for _ in range(n)]

drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]
r, c, d = n // 2, n // 2, 0

def in_range(nr, nc):
    return 0 <= nr < n and 0 <= nc < n

total = arr[r][c]
for q in query:
    if q == 'L':
        d = (d - 1 + 4) % 4
    elif q == 'R':
        d = (d + 1) % 4
    else:
        nr, nc = r + drs[d], c + dcs[d]
        if in_range(nr, nc):
            r, c = nr, nc
            total += arr[r][c]

print(total)