n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

_min = 2000000000
for i in range(n-t+1):
    cost = abs(arr[i] - h)
    for j in range(i+1, i+t):
        cost += abs(arr[j] - h)
    _min = min(_min, cost)
print(_min)