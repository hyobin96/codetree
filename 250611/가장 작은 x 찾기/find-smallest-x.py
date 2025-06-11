N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(1, 10001):
    is_pos = True
    x = i
    for a, b in ab:
        x *= 2
        if not(a <= x <= b):
            is_pos = False
            break
    if is_pos:
        print(i)
        break