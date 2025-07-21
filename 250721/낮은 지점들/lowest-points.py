N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

d = {}
for x, y in points:
    if x in d:
        d[x] = min(d[x], y)
    else:
        d[x] = y

answer = 0
for y in d.values():
    answer += y

print(answer)