from itertools import combinations
from collections import deque

in_range = lambda r, c: 0 <= r < N and 0 <= c < N
can_go = lambda r, c: in_range(r, c) and visited[r][c] != cir

def is_between(r, c, nr, nc):
    return U <= abs(grid[r][c] - grid[nr][nc]) <=D

def bfs(curr):
    global visited, visited_cities
    q = deque()
    q.append(curr)
    start_city = curr
    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
    
    while q:
        curr = q.popleft()
        r, c = curr // 3, curr % 3
        visited_cities[start_city].append(curr)
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc) and is_between(r, c, nr, nc):
                visited[nr][nc] = cir
                q.append(nr * 3 + nc)

N, K, U, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited_cities = [[] for _ in range(N * N)]
visited = [[0] * N for _ in range(N)]
cir = 1
for i in range(N * N):
    bfs(i)
    cir += 1
        

answer = 0
for cities in combinations(range(N * N), K):
    s = set()
    for city in cities:
        s.update(visited_cities[city])
    answer = max(answer, len(s))

print(answer)