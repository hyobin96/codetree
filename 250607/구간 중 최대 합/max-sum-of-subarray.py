n, k = map(int, input().split())
arr = list(map(int, input().split()))

_max = 0
for i in range(n-k+1):
    _max = max(_max, sum(arr[i:i+k]))
print(_max)