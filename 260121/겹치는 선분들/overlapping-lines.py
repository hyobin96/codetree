# 같은 위치에 들어오는 점, 나가는 점이 있어도
# 오름차순 정렬이면 나가는 점이 먼저 나온다.
# 아 그러면 나갈 때 (시작, 끝) 을 해시에 넣어주면 된다.
# 그러면 중복이어도 상관이 없다.
# 근데 (시작, 끝) 이거 해시가 같은 걸 보장하나?

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

points = []
curr = 0
for i in range(n):
    m, dir = input().strip().split()
    m = int(m)
    if dir == 'R':
        x1, x2 = curr, curr + m
        curr += m
    else:
        x1, x2 = curr - m, curr
        curr -= m
    
    points.append((x1, 1, i))
    points.append((x2, -1, i))

points.sort()
d = dict()
sections = set()
x_max = points[0][0]
for x, v, i in points:
    if v == 1:
        d[i] = x
        if len(d) <= k:
            x_max = x
    else:
        if len(d) >= k:
            sections.add((x_max, x))
        del d[i]

answer = 0
# print(sections)
for section in sections:
    answer += section[1] - section[0]

print(answer)

