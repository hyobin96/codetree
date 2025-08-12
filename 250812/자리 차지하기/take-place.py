from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet(range(1, m + 1))

for a in arr:
    idx = s.bisect_right(a)
    if idx == 0:
        break

    s.remove(s[idx - 1])    

print(m - len(s))

