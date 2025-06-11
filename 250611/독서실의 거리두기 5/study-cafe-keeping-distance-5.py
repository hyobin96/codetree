N = int(input())
arr = list(map(int, list(input())))
_max = 0
for i in range(N):
    if arr[i] == 1:
        continue
    l, r = i, i
    _min = 2000000000
    dist = 0
    while l != 0 or r != N-1:
        l = l-1 if l-1 >= 0 else 0
        r = r+1 if r+1 <= N-1 else N-1 
        dist += 1
        if arr[l] == 1 or arr[r] == 1:
            _min = min(_min, dist)
            break
    _max = max(_max, _min)
print(_max)