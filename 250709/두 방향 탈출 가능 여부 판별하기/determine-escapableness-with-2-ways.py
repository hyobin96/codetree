def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

def can_go(nr, nc):
    global visited, grid
    return in_range(nr, nc) and grid[nr][nc] and not visited[nr][nc]


def dfs(curr):
    global is_exist, visited, drs, dcs
    if curr == (N-1, M-1):
        is_exist = True
        return

    r, c = curr

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if can_go(nr, nc):
            visited[nr][nc] = True
            dfs((nr, nc))


N, M = map(int, input().split())
is_exist, visited = False, [[False for _ in range(M)] for _ in range(N)]
drs, dcs = (1, 0), (0, 1)
grid = [list(map(int, input().split())) for _ in range(N)]
dfs((0, 0))
print(int(is_exist))
