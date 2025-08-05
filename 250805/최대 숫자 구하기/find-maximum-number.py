from sortedcontainers import SortedSet
n, m = map(int, input().split())
s = SortedSet([i for i in range(1, m + 1)])
nums = list(map(int, input().split()))
for n in nums:
    s.remove(n)
    print(s[-1])