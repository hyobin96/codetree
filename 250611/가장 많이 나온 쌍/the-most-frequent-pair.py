N, M = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(M)]

def get_count(i, j):
    cnt = 0
    for a, b in arr:
        if (a == i and b == j) or (a == j and b == i):
            cnt += 1
    return cnt

_max = 0
for i in range(1, N+1):
    for j in range(i + 1, N+1):
        count = get_count(i, j)
        _max = max(_max, count)

print(_max)