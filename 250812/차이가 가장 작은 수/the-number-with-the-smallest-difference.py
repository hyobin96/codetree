from sortedcontainers import SortedSet

n, m = map(int, input().split())
s = SortedSet()
for _ in range(n):
    s.add(int(input()))

answer = -1
i, j = 0, n - 1
while i < j:
    l, r = s[i], s[j]
    if r - l < m:
        break
    answer = r - l
    
    next_l = s[i + 1]
    next_r = s[j - 1]
    if next_l - l > r - next_r:
        i = i + 1
    else:
        j = j - 1

print(answer)
