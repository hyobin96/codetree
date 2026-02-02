import sys
input = sys.stdin.readline

n = int(input())

sections = []
for _ in range(n):
    s, e = map(int, input().strip().split())
    sections.append((s, 1))
    sections.append((e, -1))

sections.sort(key=lambda s: (s[0], -s[1]))

room = 0
answer = 0
for section in sections:
    room += section[1]
    answer = max(answer, room)

print(answer)