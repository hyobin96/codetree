import sys
input = sys.stdin.readline

n = int(input())

sections = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    sections.append((a, 1))
    sections.append((b, -1))

sections.sort()

s = 0
합 = 0
answer = 0
for x, v in sections:
    if v == 1 and 합 == 0:
        s = x
    elif v == -1 and 합 == 1:
        answer = max(answer, x - s)
    합 += v

print(answer)