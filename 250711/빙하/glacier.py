from collections import deque

in_range = lambda nr, nc: 0 <= nr < N and 0 <= nc < M

def is_around(i, j, q2):
    global visited2, cri, visited
    q = deque()
    q.append((i, j))
    pos = []
    is_ok = True
    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc):
                is_ok = False
                continue
            if visited2[nr][nc] == cri:
                continue
            visited2[nr][nc] = cri
            if grid[nr][nc] == 0:
                q.append((nr, nc))
                pos.append((nr, nc))
    
    if not is_ok:
        for r, c in pos:
            q2.append((r, c))
            visited[r][c] = 1

    return is_ok
        

def search_water(r, c, q):
    global visited
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and not grid[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = 1
            if next_to_glaicer(nr, nc):
                q.append((nr, nc))
            search_water(nr, nc, q)
    

def can_go(nr, nc):
    return in_range(nr, nc) and grid[nr][nc]

def next_to_glaicer(r, c):
    cnt = 0
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if can_go(nr, nc):
            cnt += 1

    return 0 < cnt < 4
        

def init_q(q):
    global visited, cri
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and not grid[i][j] and next_to_glaicer(i, j) and not is_around(i, j, q):
                cri += 1
                visited[i][j] = 1
                q.append((i, j))

def melting_glacier():
    global visited, grid
    q = deque()
    init_q(q)
    time = 0
    cnts = []
    while q:
        time += 1
        q_size = len(q)
        cnt = 0
        # for k in range(N):
        #     print(*grid[k])
        # print()
        for _ in range(q_size):
            r, c = q.popleft()
            for dr, dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                if can_go(nr, nc) and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    grid[nr][nc] = 0
                    cnt += 1
                    q.append((nr, nc))
                    search_water(nr, nc, q)
        cnts.append(cnt)
    return time - 1, cnts[-2]

drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited2 = [[0] * M for _ in range(N)]
cri = 1
time, size = melting_glacier()
print(time, size)