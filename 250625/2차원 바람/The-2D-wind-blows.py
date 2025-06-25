import sys

input = sys.stdin.readline

N, M, Q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

info = [list(map(int, input().split())) for _ in range(Q)]


def rotate(r1, c1, r2, c2):
    temp1 = arr[r1][c2]
    temp2 = arr[r2][c1]

    for j in range(c2, c1, -1):
        arr[r1][j] = arr[r1][j - 1]

    for j in range(c1, c2):
        arr[r2][j] = arr[r2][j + 1]

    for i in range(r1, r2):
        arr[i][c1] = arr[i + 1][c1]

    for i in range(r2, r1, -1):
        arr[i][c2] = arr[i - 1][c2]

    
    arr[r1 + 1][c2] = temp1
    arr[r2 - 1][c1] = temp2

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def to_avg(r1, c1, r2, c2):
    temp_arr = [arr[i][0:] for i in range(N)]  

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            avg = temp_arr[i][j]
            cnt = 1
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]

                if in_range(nr, nc):
                    avg += temp_arr[nr][nc]
                    cnt += 1

            avg //= cnt

            arr[i][j] = avg


for r1, c1, r2, c2 in info:
    # print(r1, c1, r2, c2)
    r1, c1, r2, c2 = r1 -1, c1 - 1, r2 - 1, c2 - 1
    rotate(r1, c1, r2, c2)
    to_avg(r1, c1, r2, c2)


for i in range(N):
    print(*arr[i])