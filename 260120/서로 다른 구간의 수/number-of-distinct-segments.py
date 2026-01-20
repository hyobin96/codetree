import sys
input = sys.stdin.readline

n = int(input())

points = []

for i in range(n):
    a, b = map(int, input().strip().split())
    points.append((a, 1, i))
    points.append((b, -1, i))

points.sort()

s = set()
answer = 0
for x, v, i in points:
    if v == 1:
        s.add(i)

    else:
        s.remove(i)
        if not s:
            answer += 1

print(answer)

    