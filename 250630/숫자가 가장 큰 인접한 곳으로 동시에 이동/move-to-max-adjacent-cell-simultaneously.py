def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def search(i, j):
    _max = 0
    d = 0

    cnt = 0
    for dr, dc in zip(drs, dcs):
        nr, nc = i + dr, j + dc

        if not in_range(nr, nc):
            continue

        if _max < arr[nr][nc]:
            _max = arr[nr][nc]
            d = cnt

        cnt += 1

    return d
        

def simul():
    next_count = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if count[i][j] == 0:
                continue

            d = search(i, j)

            next_count[i + drs[d]][j + dcs[d]] += 1

    for i in range(N):
        for j in range(N):
            if next_count[i][j] == 1:
                count[i][j] = 1
            else:
                count[i][j] = 0

    





N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

count = [[0] * N for _ in range(N)]

drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(M):
    r, c = map(int, input().split())
    count[r - 1][c - 1] = 1

for _ in range(T):
    simul()

answer = 0

for i in range(N):
    answer += sum(count[i])

print(answer)