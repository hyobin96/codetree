n = int(input())
x, y = 0, 0
mapper = {'W':0, 'S':1, 'N':2, 'E':3}
dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]

idx = -1
t = 0
for i in range(n):
    d, ds = input().split()
    d = mapper[d]
    for _ in range(int(ds)):
        t += 1
        x, y = x + dxs[d], y + dys[d]
        if x == 0 and y == 0:
            idx = t
            break
print(idx)