n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(nx, ny):
    return 0 <= nx < m and 0 <= ny < n
d = 0
x, y = 0, 0
num = 1
while True:
    arr[y][x] = num
    num += 1

    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx, ny) and arr[ny][nx] == 0:
        x, y = nx, ny
    else:
        d = (d + 1) % 4
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny) and arr[ny][nx] == 0:
            x, y = nx, ny
        else:
            break

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=' ')
    print()