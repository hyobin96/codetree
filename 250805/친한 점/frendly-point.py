from sortedcontainers import SortedSet

n, m = map(int, input().split())

xys = SortedSet()
for _ in range(n):
    xys.add(tuple(map(int, input().split())))

for _ in range(m):
    x, y = map(int, input().split())
    idx = xys.bisect_left((x, y))
    if idx == len(xys):
        print('-1 -1')
    else:
        x, y = xys[idx]
        print(x, y)

