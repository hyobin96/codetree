from collections import deque

def can_go(nr, nc):
    return 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and grid[nr][nc]

def bfs(curr):
    global visited
    q = deque()
    q.append(curr)

    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)

    while q:
        r, c = q.popleft()
        if (r, c) == (N - 1, M - 1):
            return True

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                visited[nr][nc] = 1
                q.append((nr, nc))

    return False


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(int(bfs((0, 0))))
