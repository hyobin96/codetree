arr = [[0] * 3000 for _ in range(3000)]

offset = 1500

def draw(x1, y1, x2, y2, k):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = k

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset
    draw(x1, y1, x2, y2, 1)

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset
draw(x1, y1, x2, y2, 0)

total = 0
for e in arr:
    total += sum(e)
print(total)