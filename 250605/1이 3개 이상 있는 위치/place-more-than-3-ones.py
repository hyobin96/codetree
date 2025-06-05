n = int(input())
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(nx, ny):
    return nx >= 0 and nx < n and ny >= 0 and ny < n

total = 0
for y in range(n):
    for x in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and arr[ny][nx] == 1:
                cnt += 1
        if cnt >= 3:
            total += 1
print(total)