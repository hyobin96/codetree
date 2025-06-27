def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def is_same_row_col(r, c, i, j):
    return r == i or c == j

def bomb(r, c):
    global arr

    bombed_arr = [arr[i][0:] for i in range(N)]
    dist = arr[r][c] - 1

    for i in range(r - dist, r + dist + 1):
        for j in range(c - dist, c + dist + 1):
            if in_range(i, j) and is_same_row_col(r, c, i, j):
                bombed_arr[i][j] = 0

    return bombed_arr

def gravity(bombed_arr):
    temp_arr = [[0] * N for _ in range(N)]

    for j in range(N):
        end = N - 1
        for i in range(N - 1, -1, -1):
            if bombed_arr[i][j] != 0:
                temp_arr[end][j] = bombed_arr[i][j]
                end -= 1

    return temp_arr


drs, dcs = [1, 0], [0, 1]

def search(bombed_arr):
    cnt = 0

    for i in range(N):
        for j in range(N):
            if bombed_arr[i][j] != 0:

                for dr, dc in zip(drs, dcs):
                    nr, nc = i + dr, j + dc
                    if in_range(nr, nc) and bombed_arr[i][j] == bombed_arr[nr][nc]:
                        cnt += 1

    return cnt

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt_max = 0

for i in range(N):
    for j in range(N):
        cnt = search(gravity(bomb(i, j)))
        cnt_max = max(cnt_max, cnt)

print(cnt_max)

