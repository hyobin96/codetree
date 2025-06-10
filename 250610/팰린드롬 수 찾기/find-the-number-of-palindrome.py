X, Y = map(int, input().split())

cnt = 0
for num in range(X, Y+1):
    num = str(num)
    is_pal = True
    for i in range(len(num) // 2):
        if num[i] != num[len(num)-1-i]:
            is_pal = False
            break
    if is_pal:
        cnt += 1

print(cnt)