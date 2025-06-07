n, k = map(int, input().split())
arr = [0] * 200
R = 0
for _ in range(n):
    c, pos = map(int, input().split())
    arr[pos] += c
    R = max(R, pos)

if k >= R:
    print(sum(arr))
else:
    _max = 0
    for i in range(k, R):
        _max = max(_max, sum(arr[i-k:i+k+1]))
    print(_max)