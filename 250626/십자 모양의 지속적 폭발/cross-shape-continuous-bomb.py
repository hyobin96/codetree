def gravity():
    global arr

    temp_arr = [[0] * N for _ in range(N)]
    
    for j in range(N):
        end = N - 1
        for i in range(N-1, -1, -1):
            if arr[i][j] != 0:
                temp_arr[end][j] = arr[i][j]
                end -= 1

    for i in range(N):
        arr[i] = temp_arr[i][0:]
    

drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def bomb(i, j):
    global arr

    dist = arr[i][j] - 1
    arr[i][j] = 0

    for dr, dc in zip(drs, dcs):
        r, c = i, j

        for _ in range(dist):
            nr, nc = r + dr, c + dc

            if not in_range(nr, nc):
                break

            arr[nr][nc] = 0
            r, c = nr, nc


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    c = int(input()) - 1

    for i in range(N):
        if arr[i][c] != 0:
            bomb(i, c)
            gravity()
            break

for i in range(N):
    print(*arr[i])