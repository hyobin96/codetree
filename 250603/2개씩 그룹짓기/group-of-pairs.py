n = int(input())
arr = list(map(int, input().split()))
arr.sort()

_max = 0
for i in range(n):
    _sum = arr[i] + arr[-1-i]
    _max = max(_max, _sum)

print(_max)