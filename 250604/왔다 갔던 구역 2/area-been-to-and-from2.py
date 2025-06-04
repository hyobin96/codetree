n = int(input())
arr = [0] * (2001)
start = 1000

def move(x, c):
    global start
    if c == 'L':
        for i in range(start - 1, start-x-1, -1):
            arr[i] += 1
        start -= x
    else:
        for i in range(start, start + x):
            arr[i] += 1
        start += x

for _ in range(n):
    x, c = input().split()
    move(int(x), c)

total = 0
for e in arr:
    if e >= 2:
        total += 1
print(total)