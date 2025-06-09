n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

_max = 0
for i in range(n):
    count_arr = [0] * (1001)
    for j in range(n):
        if i == j:
            continue
        for k in range(arr[j][0], arr[j][1]):
            count_arr[k] = 1
        _max = max(_max, sum(count_arr))
print(_max)