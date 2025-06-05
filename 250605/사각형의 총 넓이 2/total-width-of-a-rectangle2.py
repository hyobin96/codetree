n = int(input())
arr = [[0] * 400 for _ in range(400)]
offset = 200

def draw(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + offset, y1 + offset, x2 + offset, y2 + offset
    draw(x1, y1, x2, y2)

total = 0
for i in arr:
    total += sum(i)
print(total)