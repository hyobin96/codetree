n = int(input())
arr = [0] * 300
offset = 100
for _ in range(n):
    x1, x2 = map(int, input().split())
    x1 += offset
    x2 += offset
    for i in range(x1, x2):
        arr[i] += 1

_max = 0
for e in arr:
    _max = max(_max, e)
print(_max)