n, q = map(int, input().split())

rocks_arr = [[0] * 4 for _ in range(n + 1)]


for i in range(1, n + 1):
    group_num = int(input())
    rocks_arr[i][group_num] = 1


# print(rocks_arr)

for i in range(1, n + 1):
    for j in range(1, 4):
        rocks_arr[i][j] += rocks_arr[i - 1][j]

# print(rocks_arr)

for _ in range(q):
    a, b = map(int, input().split())

    answer = ''
    for i in range(1, 4):
        answer += str(rocks_arr[b][i] - rocks_arr[a - 1][i]) + ' '

    print(answer)
