def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < M

def can_go(nr, nc):
    return in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] > K

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

drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_cnt, min_K, K = 0, 0, 0

for k in range(1, 101):
    K = k
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if can_go(i, j):
                cnt += 1
                visited[i][j] = 1
                dfs((i, j))
    if max_cnt < cnt:
        max_cnt, min_K = cnt, K

print(min_K, max_cnt)
    
