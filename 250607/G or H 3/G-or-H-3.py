n, k = map(int, input().split())
k += 1
arr = [0] * 10001
R = 0
for _ in range(n):
    pos, s = input().split()
    arr[int(pos)] = 1 if s == 'G' else 2
    R = max(R, int(pos))

_max = 0
if k >= R:
    print(sum(arr))
else:
    for i in range(1, R-k+2):
        _max = max(_max, sum(arr[i:i+k]))
    print(_max)