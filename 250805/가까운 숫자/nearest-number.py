from sortedcontainers import SortedSet

n = int(input())
arr = list(map(int, input().split()))

s = SortedSet([0])
min_dist = 1000000000
for num in arr:
    idx = s.bisect_right(num)
    if idx == len(s):
        min_dist = min(min_dist, num - s[idx - 1])
    else:
        min_dist = min(min_dist, s[idx] - num, num - s[idx - 1])
    s.add(num)
    print(min_dist)
