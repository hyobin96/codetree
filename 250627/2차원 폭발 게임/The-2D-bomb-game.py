def bomb():
    global arr
    is_bombed = False

    for j in range(N):
        for i in range(N):
            cnt = 1
            end = i - 1

            if arr[i][j] == 0:
                continue

            for k in range(i + 1, N):
                if arr[i][j] == arr[k][j]:
                    cnt += 1
                    end = k

                else:
                    break

            if cnt >= M:
                is_bombed = True
                for l in range(i, end + 1):
                    arr[l][j] = 0

    
    return is_bombed

                

def gravity():
    global arr

    temp_arr = [[0] * N for _ in range(N)]

    for j in range(N):
        end = N - 1
        for i in range(N - 1, -1, -1):
            if arr[i][j] != 0:
                temp_arr[end][j] = arr[i][j]
                end -= 1

    for i in range(N):
        arr[i] = temp_arr[i][0:]


def rotate():
    global arr

    temp_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            temp_arr[i][j] = arr[N - j - 1][i]

    for i in range(N):
        arr[i] = temp_arr[i][0:]


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

if M > 1:
    for _ in range(K):
        while bomb():
            gravity()
            # for i in range(N):
            #     print(*arr[i])
            # print()

        rotate()
        gravity()

    while bomb():
        gravity()

    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                cnt += 1

    print(cnt)

else:
    print(0)