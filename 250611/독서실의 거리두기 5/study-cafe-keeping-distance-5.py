N = int(input())
arr = list(map(int, list(input())))
_max = 0

def get_dist(j):
    l, r = j, j
    dist = 0
    while l != 0 or r != N-1:
        l = l-1 if l-1 >= 0 else 0
        r = r+1 if r+1 <= N-1 else N-1 
        dist += 1
        if l != j and arr[l] == 1:
            break
        if r != j and arr[r] == 1:
            break
    return dist

for i in range(N):
    if arr[i] == 1:
        continue
    arr[i] = 1
    _min = 2000000000
    for j in range(N):
        if arr[j] == 0:
            continue
        dist = get_dist(j)
        _min = min(_min, dist)
    _max = max(_max, _min)
    arr[i] = 0
print(_max)