n = int(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
direction = ['E', 'S', 'W', 'N']
def move(d, ds):
    global x, y
    idx = direction.index(d)
    x += dx[idx] * ds
    y += dy[idx] * ds

for _ in range(n):
    d, ds = input().split()
    move(d, int(ds))

print(x, y)