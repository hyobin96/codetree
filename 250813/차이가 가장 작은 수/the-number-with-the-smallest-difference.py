from sortedcontainers import SortedSet

n, m = map(int, input().split())
s = SortedSet()
for _ in range(n):
    s.add(int(input()))

answer = 10000000000
i, j = 0, len(s) - 1
while i < j:
    l, r = s[i], s[j]
    if r - l < m:
        break
    answer = min(answer, r - l)
    
    next_l = s[i + 1]
    next_r = s[j - 1]
    if next_l - l > r - next_r:
        j = j - 1
    else:
        i = i + 1

if answer == 10000000000:
    print(-1)
else:
    print(answer)
