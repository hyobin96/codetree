n, s = map(int, input().split())
arr = list(map(int, input().split()))
total = sum(arr)

_min = 2000000000
for i in range(n):
    for j in range(i + 1, n):
        _sum = total - arr[i] - arr[j]
        _min = min(_min, abs(s - _sum))
print(_min)