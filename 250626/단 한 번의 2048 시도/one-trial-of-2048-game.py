def gravity(direct):
    global arr

    temp_arr = [[0] * 4 for _ in range(4)]
    start, end, oper, end_of_len = 0, 0, 0, 0

    if direct in ('L', 'R'):
        if direct == 'L':
            start, end, oper, end_of_len = 0, N, 1, 0
        else:
            start, end, oper, end_of_len = N - 1, -1, -1, N - 1

        for i in range(N):
            e = end_of_len
            prev = 0
            for j in range(start, end, oper):
                if arr[i][j] != 0:
                    if prev != 0 and prev == arr[i][j]:
                        temp_arr[i][e - oper] = prev * 2
                        prev = 0
                    else:
                        temp_arr[i][e] = arr[i][j]
                        e += oper
                        prev = arr[i][j]

    else:
        if direct == 'U':
            start, end, oper, end_of_len = 0, N, 1, 0
        else:
            start, end, oper, end_of_len = N - 1, -1, -1, N - 1

        for j in range(N):
            e = end_of_len
            prev = 0
            for i in range(start, end, oper):
                if arr[i][j] != 0:
                    if prev != 0 and prev == arr[i][j]:
                        temp_arr[e - oper][j] = prev * 2
                        prev = 0
                    else:
                        temp_arr[e][j] = arr[i][j]
                        e += oper
                        prev = arr[i][j]
                    

    for i in range(N):
        arr[i] = temp_arr[i][0:]


N = 4

arr = [list(map(int, input().split())) for _ in range(4)]

direct = input()

gravity(direct)

for i in range(N):
    print(*arr[i])