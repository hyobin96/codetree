from itertools import combinations
from collections import deque

in_range = lambda nr, nc: 0 <= nr < N and 0 <= nc < N

def can_go(nr, nc):
    return in_range(nr, nc) and not grid[nr][nc] and not visited[nr][nc]

def bfs(curr):
    global visited
    r, c = curr
    q = deque()
    q.append(curr)
    visited[r][c] = 1
    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)

    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                visited[nr][nc] = 1
                q.append((nr, nc))

    return cnt


def select_rocks(cnt, start, curr):
    global grid, answer, visited
    if cnt == M:
        visited = [[0] * N for _ in range(N)]
        answer = max(answer, bfs(curr))
        return

    for i in range(start, len(pos)):
        r, c = pos[i]
        grid[r][c] = 0
        select_rocks(cnt + 1, i + 1, curr)
        grid[r][c] = 1


def init_pos(pos):
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                pos.append((i, j))


N, K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
pos, answer = [], 0
visited = [[0] * N for _ in range(N)]
init_pos(pos)
for _ in range(K):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    select_rocks(0, 0, (r, c))

print(answer)

# for e in combinations(range(M), 3):
#     for