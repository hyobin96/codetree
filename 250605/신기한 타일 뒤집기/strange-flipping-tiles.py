n = int(input())
arr = [0] * 200002  #흰색 1, 검은색 2, 회색 0
start = 100000

def move(x, c):
    global start
    if c == 'L':
        for i in range(start, start - x, -1):
            arr[i] = 1
        start -= x - 1
    else:
        for i in range(start, start + x):
            arr[i] = 2
        start += x - 1
    
for _ in range(n):
    x, c = input().split()
    move(int(x), c)

w, b = 0, 0
for e in arr:
    if e == 1:
        w += 1
    elif e == 2:
        b += 1
print(w, b)