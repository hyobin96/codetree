def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def shot(r, c, d):
    t = 1

    while in_range(r, c):
        if arr[r][c] == 1:
            d = 3 - d
        
        elif arr[r][c] == 2:
            d = (d + 2) % 4

        r, c = r + drs[d], c + dcs[d]
        t += 1

    global T
    T = max(T, t)
        


drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
T = 0

for j in range(N):
    shot(0, j, 1)

for i in range(N):
    shot(i, N - 1, 2)

for j in range(N - 1, -1, -1):
    shot(N - 1, j, 0)

for i in range(N - 1, -1, -1):
    shot(i, 0, 3)

print(T)