n = int(input())
arr = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]
res = []
for x, y, i in arr:
    x, y = abs(x), abs(y)
    res.append((x + y, i))
res.sort(key=lambda x:x[0])

for e in res:
    print(e[1])
