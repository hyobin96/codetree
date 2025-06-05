dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, d = 0, 0, 0
query = input()
for q in query:
    if q == 'L':
        d = (d - 1 + 4) % 4
    elif q == 'R':
        d = (d + 1) % 4
    else:
        x, y = x + dx[d], y + dy[d]
print(x, y)