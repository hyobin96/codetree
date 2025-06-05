arr = [[0] * 3000 for _ in range(3000)]
offset = 1500

def draw(x1, y1, x2, y2, k):
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = k

x1, y1, x2, y2 = map(int, input().split())
draw(x1, y1, x2, y2, 1)
x1, y1, x2, y2 = map(int, input().split())
draw(x1, y1, x2, y2, 0)

x_min, x_max = 3001, -1
y_min, y_max = 3001, -1
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            x_min = min(i, x_min)
            x_max = max(i, x_max)
            y_min = min(j, y_min)
            y_max = max(j, y_max)

if x_max == -1:
    print(0)
else:
    print((x_max - x_min + 1) * (y_max - y_min + 1))


