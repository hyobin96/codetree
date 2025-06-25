N, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]


for _ in range(T):
    temp1, temp2, temp3 = arr[0][-1], arr[1][-1], arr[2][-1]

    for i in range(3):
        for j in range(N - 1, 0, -1):
            arr[i][j] = arr[i][j - 1]

    
    arr[0][0] = temp3
    arr[1][0] = temp1
    arr[2][0] = temp2

for i in range(3):
    print(*arr[i])


