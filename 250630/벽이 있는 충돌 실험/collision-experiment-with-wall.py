def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def simul():
    count_arr = [[0] * N for _ in range(N)]
    move_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                continue

            d = mapper[arr[i][j]]

            nr, nc = i + drs[d], j + dcs[d]

            if in_range(nr, nc):
                count_arr[nr][nc] += 1
                move_arr[nr][nc] = arr[i][j]
            else:
                count_arr[i][j] += 1
                move_arr[i][j] = num_to_alpha[(d + 2) % 4]

    
    for i in range(N):
        for j in range(N):
            if count_arr[i][j] > 1:
                arr[i][j] = 0
            
            else:
                arr[i][j] = move_arr[i][j]


def counting():
    answer = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                answer += 1

    return answer

drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]

mapper = {'U':0, 'R':1, 'D':2, 'L':3}
num_to_alpha = {0:'U', 1:'R', 2:'D', 3:'L'}




T = int(input())

N, M = 0, 0
arr = []

for _ in range(T):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]

    for _ in range(M):
        x, y, d = input().split()
        x, y = int(x) - 1, int(y) - 1

        arr[x][y] = d

    for _ in range(2 * N):
        simul()

    print(counting())