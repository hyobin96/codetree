A, B, C = map(int, input().split())

_max = 0
for i in range(C // A + 1):
    a = A * i
    num_b = (C - a) // B
    _sum = a + B * num_b
    _max = max(_max, _sum)
print(_max)