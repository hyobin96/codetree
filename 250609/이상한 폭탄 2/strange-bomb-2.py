n, k = map(int, input().split())
bomb = [int(input()) for _ in range(n)]

_max = -1
for i in range(n):
    for j in range(i + 1, n if i+4 > n else i+4):
        if bomb[i] == bomb[j]:
            _max = max(_max, bomb[i])

print(_max)