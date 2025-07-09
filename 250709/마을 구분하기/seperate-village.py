def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def can_go(nr, nc):
    return in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc]


def dfs(curr):
    global visited
    cnt = 1
    r, c = curr

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if can_go(nr, nc):
            visited[nr][nc] = 1
            cnt += dfs((nr, nc))

    return cnt


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
counts = []
drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)

for i in range(N):
    for j in range(N):
        if can_go(i, j):
            visited[i][j] = 1
            counts.append(dfs((i, j)))

counts.sort()
print(len(counts))
for c in counts:
    print(c)
