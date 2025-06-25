N, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(2)]

arr[1] = arr[1][::-1]

for _ in range(T):
    temp1, temp2 = arr[0][-1], arr[1][0]

    for i in range(N - 1, 0, -1):
        arr[0][i] = arr[0][i - 1]

    arr[0][0] = temp2

    for i in range(N - 1):
        arr[1][i] = arr[1][i + 1]

    arr[1][-1] = temp1

arr[1] = arr[1][::-1]

for i in range(2):
    print(*arr[i])