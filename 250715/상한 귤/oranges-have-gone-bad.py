from collections import deque

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited, step = [[0] * N for _ in range(N)], [[0] * N for _ in range(N)]
q = deque()

def init():
    global q, step
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                step[i][j] = -1
            elif grid[i][j] == 2:
                q.append((i, j))

in_range = lambda r, c: 0 <= r < N and 0 <= c < N
can_go = lambda r, c: in_range(r, c) and grid[r][c] == 1 and not visited[r][c]

def bfs():
    global q, visited, step

    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                visited[nr][nc] = 1
                grid[nr][nc] = 2
                step[nr][nc] = step[r][c] + 1
                q.append((nr, nc))

def finish():
    global step
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                step[i][j] = -2

init()
bfs()

finish()

for i in range(N):
    print(*step[i])