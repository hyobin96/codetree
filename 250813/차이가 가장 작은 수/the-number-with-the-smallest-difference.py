from sortedcontainers import SortedSet

n, m = map(int, input().split())
s = SortedSet()
for _ in range(n):
    s.add(int(input()))

answer = 10000000000
for i in range(len(s) // 2):
    num = s[i]
    idx = s.bisect_left(m + num)
    if idx != len(s):
        answer = min(answer, s[idx] - num)
    
if answer == 10000000000:
    print(-1)
else:
    print(answer)
