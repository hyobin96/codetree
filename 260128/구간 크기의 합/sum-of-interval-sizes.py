import sys
input = sys.stdin.readline

n = int(input())

sections = []
for i in range(n):
    a, b = map(int, input().strip().split())
    sections.append((a, 1))
    sections.append((b, -1))

sections.sort()

answer = 0
k = 0
for i in range(len(sections)):
    if k > 0:
        answer += sections[i][0] - sections[i - 1][0]
    k += sections[i][1]
print(answer)
