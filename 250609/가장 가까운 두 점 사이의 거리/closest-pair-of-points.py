n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
_min = 2000000000
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        square = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
        _min = min(_min, square)
print(_min)