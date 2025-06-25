N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

r, c, m1, m2, m3, m4, dire = map(int, input().split())
r, c = r - 1, c - 1


dr, dc = [-1, -1, 1, 1], [1, -1, -1, 1]

dis = [m1, m2, m3, m4]

rcs = [[] for _ in range(4)]

for d in range(4):
    rcs[d].append((r, c))
    for _ in range(dis[d]):
        r += dr[d]
        c += dc[d]

        rcs[d].append((r, c))

# print(rcs)

def counterclockwise():
    temp1 = arr[rcs[0][-1][0]][rcs[0][-1][1]]

    for i in range(m1, 0, -1):
        r1, c1 = rcs[0][i]
        r2, c2 = rcs[0][i - 1]

        arr[r1][c1] = arr[r2][c2]

    # for i in range(N):
    #     print(*arr[i])

    temp2 = arr[rcs[3][0][0]][rcs[3][0][1]]

    for i in range(m3, 0, -1):
        r1, c1 = rcs[2][i]
        r2, c2 = rcs[2][i - 1]

        arr[r1][c1] = arr[r2][c2]


    for i in range(m2, 0, -1):
        r1, c1 = rcs[1][i]
        r2, c2 = rcs[1][i - 1]

        arr[r1][c1] = arr[r2][c2]

    for i in range(m4, 0, -1):
        r1, c1 = rcs[3][i]
        r2, c2 = rcs[3][i - 1]

        arr[r1][c1] = arr[r2][c2]

    r1, c1 = rcs[1][1]
    arr[r1][c1] = temp1
    
    r1, c1 = rcs[3][1]
    arr[r1][c1] = temp2


def clockwise():
    temp1 = arr[rcs[0][0][0]][rcs[0][0][1]]
    for i in range(m1):
        r1, c1 = rcs[0][i]
        r2, c2 = rcs[0][i + 1]

        arr[r1][c1] = arr[r2][c2]

    temp2 = arr[rcs[2][0][0]][rcs[2][0][1]]

    for i in range(m3):
        r1, c1 = rcs[2][i]
        r2, c2 = rcs[2][i + 1]

        arr[r1][c1] = arr[r2][c2]

    for i in range(m2):
        r1, c1 = rcs[1][i]
        r2, c2 = rcs[1][i + 1]

        arr[r1][c1] = arr[r2][c2]

    for i in range(m4):
        r1, c1 = rcs[3][i]
        r2, c2 = rcs[3][i + 1]

        arr[r1][c1] = arr[r2][c2]

    r1, c1 = rcs[2][-1]
    arr[r1][c1] = temp1
    
    r1, c1 = rcs[0][-1]
    arr[r1][c1] = temp2    


if dire == 0:
    counterclockwise()

else:
    clockwise()

for i in range(N):
    print(*arr[i])
