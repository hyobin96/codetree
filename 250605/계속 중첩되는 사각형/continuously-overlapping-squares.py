n = int(input())
arr = [[0] * 300 for _ in range(300)]
offset = 150

def draw(x1, y1, x2, y2, k):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = k

for i in range(n):
    x1, y1, x2, y2 = map(lambda x: x + offset , map(int, input().split()))
    draw(x1, y1, x2, y2, i % 2)

total = 0
for a in arr:
    total += sum(a)
print(total)