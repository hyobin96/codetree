import sys
sys.setrecursionlimit(5000)

def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def bbuyo(curr):
    global visited
    cnt = 1
    r, c = curr

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and not visited[nr][nc] and \
            grid[nr][nc] == grid[r][c]:
            visited[nr][nc] = 1
            cnt += bbuyo((nr, nc))
            
    return cnt


drs, dcs = (-1, 1, 0, 0), (0, 0, -1, 1)
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
bomb_cnt, max_cnt = 0, 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            cnt = bbuyo((i, j))
            if cnt >= 4:
                bomb_cnt += 1
            max_cnt = max(max_cnt, cnt)

print(bomb_cnt, max_cnt)