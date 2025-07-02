def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def merge(r, c, i):
    idx = count_arr[r][c]

    if idx != 0:
        if idx > i:
            pos_arr[idx][3] += pos_arr[i][3]
            pos_arr[i] = 0
            
        else:
            pos_arr[i][3] += pos_arr[idx][3]
            pos_arr[idx] = 0
            count_arr[r][c] = i

    else:
        count_arr[r][c] = i


def move():

    for i in range(1, M + 1):
        if pos_arr[i] != 0:
            r, c, d, w = pos_arr[i]

            nr, nc = r + drs[d], c + dcs[d]

            if in_range(nr, nc):
                r, c = nr, nc

            else:
                d = (d + 2) % 4
            
            pos_arr[i] = [r, c, d, w]

            merge(r, c, i)


def init():
    for i in range(1, M + 1):
        if pos_arr[i] != 0:
            r, c, d, w = pos_arr[i]
            count_arr[r][c] = 0

def simul():
    move()
    init()
    

N, M, T = map(int, input().split())

pos_arr = [[]]

count_arr = [[0 for _ in range(N)] for _ in range(N)]

drs, dcs = [-1, 0, 1, 0], [0, -1, 0, 1]

mapper = {'U':0, 'L':1, 'D':2, 'R':3}

max_w, cnt = 0, 0

for _ in range(M):
    r, c, d, w = input().split()
    r, c, d, w = int(r) - 1, int(c) - 1, mapper[d], int(w)

    pos_arr.append([r, c, d, w])

for _ in range(T):
    simul()

for i in range(1, M+1):
    if pos_arr[i] != 0:
        _, _, _, w = pos_arr[i]
        max_w = max(max_w, w)
        cnt += 1

print(cnt, max_w)