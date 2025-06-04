n = int(input())
arr = [[0, 0, 0] for _ in range(200002)] #흰색, 검은색, 마지막 색
start = 100000

def move(x, c):
    global start
    if c == 'L':
        for i in range(start, start - x, -1):
            arr[i][0] += 1
            arr[i][2] = 1
        start -= x - 1
    else:
        for i in range(start, start + x):
            arr[i][1] += 1
            arr[i][2] = 2
        start += x - 1
        
for _ in range(n):
    x, c = input().split()
    move(int(x), c)

b, w, g = 0, 0, 0
for e in arr:
    if e[0] >= 2 and e[1] >= 2:
        g += 1
    elif e[2] == 1:
        w += 1
    elif e[2] == 2:
        b += 1

print(w, b, g)