from collections import deque

def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def can_go(nr, nc):
    return in_range(nr, nc) and not grid[nr][nc] and not visited[nr][nc]

def bfs(curr):
    global visited
    q = deque()
    q.append(curr)

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


N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

answer = 0
for _ in range(K):
    r, c = map(int, input().split())
    r, c = r - 1, c - 1
    if visited[r][c]:
        continue
    visited[r][c] = 1
    answer += bfs((r, c))

print(answer)