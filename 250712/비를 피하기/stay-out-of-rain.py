from collections import deque

in_range = lambda r, c: 0 <= r < N and 0 <= c < N
can_go = lambda r, c: in_range(r, c) and grid[r][c] != 1 and visited[r][c] != cir

def bfs(curr):
    global visited
    q = deque()
    q.append(curr)

    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
    
    while q:
        r, c, dist = q.popleft()
        if grid[r][c] == 3:
            return dist
            break

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                visited[nr][nc] = cir
                q.append((nr, nc, dist + 1))

    return -1

N, H, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dist = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cir = 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            visited[i][j] = cir
            dist[i][j] = bfs((i, j, 0))
            cir += 1
        
for i in range(N):
    print(*dist[i])