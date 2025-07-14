from collections import deque
from itertools import combinations

in_range = lambda r, c: 0 <= r < N and 0 <= c < N
can_go = lambda r, c: in_range(r, c) and visited[r][c] != cir and not grid[r][c]

def bfs(start, dest):
    global visited
    q = deque()
    q.append(start)

    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
    time = 0
    while q:
        q_size = len(q)
        for _ in range(q_size):
            r, c = q.popleft()
            if (r, c) == dest:
                return time
            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if can_go(nr, nc):
                    visited[nr][nc] = cir
                    q.append((nr, nc))
        time += 1

    return -1

def init_pos(pos):
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                pos.append((i, j))

def remove(selected):
    global grid
    for idx in selected:
        r, c = pos[idx]
        grid[r][c] = 0

def recover(selected):
    global grid
    for idx in selected:
        r, c = pos[idx]
        grid[r][c] = 1

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited, pos = [[0] * N for _ in range(N)], []
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
answer = 10000000
cir = 1

init_pos(pos)
for selected in combinations(range(len(pos)), K):
    remove(selected)
    time = bfs((r1 - 1, c1 - 1), (r2 - 1, c2 - 1))
    if time != -1:
        answer = min(answer, time)
    recover(selected)
    cir += 1

if answer == 10000000:
    print(-1)
else:
    print(answer)