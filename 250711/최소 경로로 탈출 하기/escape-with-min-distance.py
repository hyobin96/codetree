from collections import deque

in_range = lambda r, c: 0 <= r < N and 0 <= c < M
def can_go(nr, nc):
    return in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc]

def bfs():
    global step, visited
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)

    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                step[nr][nc] = step[r][c] + 1
                visited[nr][nc] = 1
                q.append((nr, nc))

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited, step = [[0] * M for _ in range(N)], [[0] * M for _ in range(N)]
bfs()
print(-1 if step[N - 1][M - 1] == -1 else step[N - 1][M - 1])