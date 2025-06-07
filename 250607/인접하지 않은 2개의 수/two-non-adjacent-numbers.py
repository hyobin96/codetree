n = int(input())
arr = list(map(int, input().split()))

_max = 0
for i in range(n):
    for j in range(i + 2, n):
        _max = max(_max, arr[i] + arr[j])
print(_max)