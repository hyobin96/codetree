T, a, b = map(int, input().split())
arr = [' '] * 1001
for _ in range(T):
    c, x = input().split()
    arr[int(x)] = c

cnt = 0
for x in range(a, b+1):
    x1 = x
    x2 = x
    while x1 != 0 or x2 != 1000:
        if arr[x1] == 'S' or arr[x2] == 'S':
            cnt += 1
            break
        elif arr[x1] == 'N' or arr[x2] == 'N':
            break
        x1 = x1 - 1 if x1 - 1 >= 0 else 0
        x2 = x2 + 1 if x2 + 1 <= 1000 else 1000
print(cnt)