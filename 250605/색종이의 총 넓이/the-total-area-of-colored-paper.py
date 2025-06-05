n = int(input())
arr = [[0] * 300 for _ in range(300)]
offset = 150

def draw(x, y):
    for i in range(x, x + 8):
        for j in range(y, y - 8, -1):
            arr[i][j] = 1

for _ in range(n):
    x, y = map(int, input().split())
    x, y = x + offset, y + offset
    draw(x, y)

total = 0
for e in arr:  
    total += sum(e)
print(total)