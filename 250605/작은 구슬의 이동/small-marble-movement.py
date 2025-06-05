n, t = map(int, input().split())
y, x, d = input().split()
y, x = int(y) - 1, int(x) - 1

mapper = {'U' : 0, 'R': 1, 'L': 2, 'D': 3}
dxs, dys = [0, 1, -1, 0], [-1, 0, 0, 1]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

d = mapper[d]
for _ in range(t):
    nx, ny = x + dxs[d], y + dys[d]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        d = 3 - d

print(y + 1, x + 1)