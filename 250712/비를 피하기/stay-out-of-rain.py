from collections import deque

q = deque()

in_range = lambda r, c: 0 <= r < N and 0 <= c < N
can_go = lambda r, c: in_range(r, c) and grid[r][c] != 1 and visited[r][c] != cir

def push(curr):
    global visited, q
    r, c, _ = curr
    visited[r][c] = cir
    q.append(curr)

def bfs():
    global visited, q

    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
    
    while q:
        r, c, cnt = q.popleft()
        if grid[r][c] == 2:
            dist[r][c] = cnt

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                push((nr, nc, cnt + 1))

N, H, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dist = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cir = 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 3:
            push((i, j, 0))
        elif grid[i][j] == 2:
            dist[i][j] = -1

bfs()        

for i in range(N):
    print(*dist[i])