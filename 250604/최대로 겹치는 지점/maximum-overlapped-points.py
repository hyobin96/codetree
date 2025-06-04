n = int(input())
arr = [0] * 101
for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2+1):
        arr[i] += 1
_max = 0
for e in arr:
    _max = max(e, _max)

print(_max)