from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = SortedSet([-1, n + 1])

for num in arr:
    max_dist = 0
    s.add(num)
    for i in range(1, len(s)):
        max_dist = max(max_dist, s[i] - s[i - 1] - 1)
    
    print(max_dist)