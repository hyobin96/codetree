import sys
input = sys.stdin.readline

n = int(input())

points = []
for _ in range(n):
    x1, x2 = map(int, input().strip().split())
    points.append((x1, 1))
    points.append((x2, -1))

points.sort()

answer = 0

cnt = 0
for x, v in points:
    cnt += v
    answer = max(answer, cnt)

print(answer)