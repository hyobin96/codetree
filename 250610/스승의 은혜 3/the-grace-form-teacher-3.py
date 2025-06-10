n, b = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0] + x[1])

_max = 0
for i in range(n):
    B = b
    cnt = 0
    for j, (p, s) in enumerate(arr):
        if i == j:
            p //= 2
        if B < (p+s):
            break
        cnt += 1
        B -= (p+s)
    _max = max(_max, cnt)
print(_max)