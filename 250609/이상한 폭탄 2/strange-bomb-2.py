n, k = map(int, input().split())
bomb = [int(input()) for _ in range(n)]

_max = -1
for i in range(n):
    for j in range(0 if i-k < 0 else i-k, n if i+4 > n else i+4):
        if i == j:
            continue
        if bomb[i] == bomb[j]:
            _max = max(_max, bomb[i])

print(_max)