from collections import deque

in_range = lambda r, c: 0 <= r < N and 0 <= c < N

def bfs(curr):
    global visited, step
    q = deque()
    q.append(curr)
    r, c = curr
    visited[r][c] = 1

    drs, dcs = (-1, -2, -2, -1, 1, 2, 2, 1), (-2, -1, 1, 2, 2, 1, -1, -2)

    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and not visited[nr][nc]:
                visited[nr][nc] = 1
                step[nr][nc] = step[r][c] + 1
                q.append((nr, nc))

N = int(input())
r1, c1, r2, c2 = map(lambda x : x - 1, map(int, input().split()))
visited, step = [[0] * N for _ in range(N)], [[0] * N for _ in range(N)]
bfs((r1, c1))
print(-1 if not visited[r2][c2] else step[r2][c2])