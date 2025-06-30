def init():
    global arr
    global pos_arr 

    for i in range(N):
        for j in range(N):
            pos_arr[arr[i][j]] = [i, j]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def simul():
    for idx in range(1, N ** 2 + 1):
        _max = 0
        r, c = pos_arr[idx]
        i, j = 0, 0
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            
            if not in_range(nr, nc):
                continue

            if _max < arr[nr][nc]:
                _max = arr[nr][nc]
                i, j = nr, nc

        pos_arr[idx], pos_arr[arr[i][j]] = pos_arr[arr[i][j]], pos_arr[idx]
        arr[r][c], arr[i][j] = arr[i][j], arr[r][c]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

pos_arr = [0] * (N ** 2 + 1)

drs, dcs = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, 1, -1]

init()

for _ in range(M):
    simul()

for i in range(N):
    print(*arr[i])