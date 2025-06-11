N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

_max = 0
for start in range(1, N+1):
    _sum = 0
    for _ in range(M):
        start = arr[start]
        _sum += start
    _max = max(_max, _sum)
print(_max)
    