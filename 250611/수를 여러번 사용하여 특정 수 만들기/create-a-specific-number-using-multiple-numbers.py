A, B, C = map(int, input().split())

_max = 0
for i in range(C // A + 1):
    for j in range(C // B + 1):
        _sum = A * i + B * j
        if _sum <= C:
            _max = max(_max, _sum)
print(_max)