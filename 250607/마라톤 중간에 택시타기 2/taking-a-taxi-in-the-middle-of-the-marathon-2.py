n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

def get_dist(i, j):
    return abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) 

_min = 100000000
for i in range(1, n - 1):
    _sum = 0
    pre = 0
    for j in range(1, n):
        if j == i:
            continue
        _sum += get_dist(pre, j)
        pre = j
    _min = min(_min, _sum)
print(_min)