n, m = map(int, input().split())
a = [0]
b = [0]

def move(v, t, arr):
    for _ in range(t):
        arr.append(arr[-1] + v)

for _ in range(n):
    v, t = map(int, input().split())
    move(v, t, a)

for _ in range(m):
    v, t = map(int, input().split())
    move(v, t, b)

a_flag = False
b_flag = False
cnt = 0
for i in range(1, len(a)):
    if a[i] - b[i] > 0:
        a_flag = True
        if b_flag:
           cnt += 1
           b_flag = False
    elif b[i] - a[i] > 0:
        b_flag = True
        if a_flag:
            cnt += 1
            a_flag = False 
print(cnt)


    