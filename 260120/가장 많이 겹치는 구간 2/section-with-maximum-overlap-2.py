import sys
input = sys.stdin.readline

n = int(input())

points = []

for i in range(n):
    x1, x2 = map(int, input().strip().split())
    points.append((x1, 1, i))
    points.append((x2, -1, i))

points.sort()

s = set()
answer = 0
for x, v, i in points:
    if v == 1:
        s.add(i)
        answer = max(answer, len(s))

    else:
        s.remove(i)

print(answer)