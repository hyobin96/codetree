n, t = map(int, input().split())
arr = list(map(int, input().split()))
_max = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] > t:
        cnt += 1
    else:
        cnt = 0
    _max = max(_max, cnt)
print(_max)