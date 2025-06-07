n = int(input())
arr = [int(input()) for _ in range(n)]
inone = sum(arr)

_min = 1000000000
for i in range(n):
    tmp = inone
    dist = 0
    for j in range(i, i + n):
        tmp -= arr[j%n]
        dist += tmp
    _min = min(_min, dist)
print(_min)
