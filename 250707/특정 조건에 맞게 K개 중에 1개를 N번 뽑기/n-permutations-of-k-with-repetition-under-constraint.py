def select_num(cnt):
    global arr
    if cnt == N:
        print(*arr)
        return

    for num in range(1, K + 1):
        if cnt < 2 or arr[-1] != num or arr[-2] != num:
            arr.append(num)
            select_num(cnt + 1)
            arr.pop()

K, N = map(int, input().split())
arr = []
select_num(0)