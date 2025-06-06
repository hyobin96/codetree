n = int(input())
arr = list(map(int, input().split()))
dist = 0
for i in range(n):
    dist += i * arr[i]

_min = 100 * 100
for i in range(1, n):
    dist += sum(arr[:i]) - sum(arr[i:]) 
    _min = min(_min, dist)

print(_min)