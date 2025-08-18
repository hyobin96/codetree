from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s1 = SortedSet([(n + 1, -1, n + 1)])
s2 = SortedSet([-1, n + 1])

for num in arr:
    idx = s2.bisect_right(num)
    start, end = s2[idx - 1], s2[idx]
    s2.add(num)
    s1.remove((end - start - 1, start, end))
    s1.add((num - start - 1, start, num))
    s1.add((end - num - 1, num, end))
    print(s1[-1][0])