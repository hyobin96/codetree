def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


def move(r, c, d, v):
    for _ in range(v):
        nr, nc = r + drs[d], c + dcs[d]
        if in_range(nr, nc):
            r, c = nr, nc

        else:
            d = (d + 2) % 4
            r, c = r + drs[d], c + dcs[d]
    # print(r, c)
    return r, c, d, v

def simul():
    num_arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(M + 1):
        if pos[i]:
            r, c, d, v = pos[i]
            r, c, d, v = move(r, c, d, v)
            pos[i] = [r, c, d, v]

            num_arr[r][c].append([i, v])

    for i in range(N):
        for j in range(N):
            if len(num_arr[r][c]) > K:
                num_arr[r][c].sort(key=lambda x: (x[1], x[0]), reverse=True)
                
                for _ in range(len(num_arr[r][c]) - K):
                    p = num_arr[r][c].pop()[0]
                    pos[p] = [] 

    # print(num_arr)

drs, dcs = [-1, 0, 1, 0], [0, -1, 0, 1]

mapper = {'U':0, 'L':1, 'D':2, 'R':3}

N, M, T, K = map(int, input().split())
pos = [[]]
for _ in range(M):
    r, c, d, v = input().split()
    r, c, d, v = int(r) - 1, int(c) - 1, mapper[d], int(v)
    pos.append([r, c, d, v])

for _ in range(T):
    simul()


answer = 0
for i in range(M + 1):
    if pos[i]:
        answer += 1

print(answer)