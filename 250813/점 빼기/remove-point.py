from sortedcontainers import SortedSet

n, m = map(int, input().split())
s = SortedSet()

for _ in range(n):
    x, y = map(int, input().split())
    s.add((x, y))

for _ in range(m):
    k = int(input())
    idx = s.bisect_left((k, 0))
    if idx == len(s):
        print(-1, -1)
    else:
        x, y = s[idx]
        print(x, y)
        s.remove(s[idx])

        