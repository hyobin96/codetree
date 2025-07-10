from collections import deque

def update_dest(r, c):
    global num_max, max_r, max_c
    num = grid[r][c]
    if (num, -r, -c) > (num_max, -max_r, -max_c):
        num_max, max_r, max_c = num, r, c
    # if num_max < num:
    #     num_max, max_r, max_c = num, r, c
    #     return
    
    # if num_max == num:
    #     if max_r > r:
    #         num_max, max_r, max_c = num, r, c
    #         return

    #     if max_r == r and max_c > c:
    #         num_max, max_r, max_c = num, r, c
    #         return
    return

def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def can_go(nr, nc, curr_num):
    return in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] < curr_num

def bfs(curr):
    global visited
    q = deque()
    q.append(curr)
    curr_num = grid[curr[0]][curr[1]]
    drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)

    while q:
        r, c = q.popleft()
        if curr_num != grid[r][c]:
            update_dest(r, c)

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc, curr_num):
                visited[nr][nc] = 1
                q.append((nr, nc))


N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
r, c = map(lambda x: x - 1, map(int, input().split()))
num_max, max_r, max_c = -1, -1, -1

for _ in range(K):
    visited[r][c] = 1
    num_max, max_r, max_c = -1, -1, -1
    bfs((r, c))
    if num_max == -1:
        break
    visited = [[0] * N for _ in range(N)]
    r, c = max_r, max_c

print(r + 1, c + 1)