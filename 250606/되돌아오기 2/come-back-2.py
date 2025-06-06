query = input()
dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
x, y = 0, 0
d, t = 0, 0
idx = -1
for q in query:
    t += 1
    if q == 'L':
        d = (d - 1 + 4) % 4
    elif q == 'R':
        d = (d + 1) % 4
    else:
        x, y = x + dxs[d], y + dys[d]
        if x == 0 and y == 0:
            idx = t
            break

print(idx)