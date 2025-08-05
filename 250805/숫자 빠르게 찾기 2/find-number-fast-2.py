from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.

s = SortedSet(arr)
for q in queries:
    idx = s.bisect_left(q)
    if idx == len(arr):
        print(-1)
    else:
        print(s[idx])