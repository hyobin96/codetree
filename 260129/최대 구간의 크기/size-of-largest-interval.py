import sys
input = sys.stdin.readline

n = int(input())

sections = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    sections.append((a, 1))
    sections.append((b, -1))

sections.sort(key=lambda s: (s[0], -s[1]))

s = sections[0][0]
합 = 0
answer = 0
for x, v in sections:
    합 += v
    if 합 == 0:
        answer = max(answer, x - s)
        s = x

print(answer)