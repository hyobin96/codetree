N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


def wise(r, c, m1, m2, m3, m4, dire):
    if dire == 0:
        drs, dcs = [-1, -1, 1, 1], [1, -1, -1, 1]
        dist = [m1, m2, m3, m4]

    else:
        drs, dcs = [-1, -1, 1, 1], [-1, 1, 1, -1]
        dist = [m2, m3, m4, m1]

    temp = [[] for _ in range(N)]

    for i in range(N):
        temp[i] = arr[i][::]

    for dr, dc, d in zip(drs, dcs, dist):
        for _ in range(d):
            nr = r + dr
            nc = c + dc

            arr[nr][nc] = temp[r][c]

            r, c = nr, nc

r, c, m1, m2, m3, m4, dire = map(int, input().split())
r, c = r - 1, c - 1

wise(r, c, m1, m2, m3, m4, dire)

for i in range(N):
    print(*arr[i])
