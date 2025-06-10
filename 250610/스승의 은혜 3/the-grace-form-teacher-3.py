n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

_max = 0
for i in range(n):
    arr[i][0] //= 2
    arr.sort(key=lambda x: x[0]+x[1])
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
    arr[i][0] *= 2
print(_max)