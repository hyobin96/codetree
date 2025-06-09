n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

_min = 2000000000
for i in range(n):
    x_min, y_min, x_max, y_max = 40001, 40001, 0, 0
    for j in range(n):
        if i == j:
            continue
        x_min = min(x_min, arr[j][0])
        x_max = max(x_max, arr[j][0])
        y_min = min(y_min, arr[j][1])
        y_max = max(y_max, arr[j][1])
    area = (x_max - x_min) * (y_max - y_min)
    _min = min(_min, area)

print(_min)
