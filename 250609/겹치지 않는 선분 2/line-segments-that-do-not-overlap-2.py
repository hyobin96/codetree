n = int(input())
offset = 10000001
points = [tuple(map(lambda x: x + offset, map(int, input().split()))) for _ in range(n)]

total = 0
for i, (x11, x12) in enumerate(points):
    cnt = 0
    for j, (x21, x22) in enumerate(points):
        if i == j:
            continue
        if (x21-x11) * (x22-x12) > 0:
            cnt += 1
        else:
            break
    if cnt == n-1:
        total += 1
print(total)