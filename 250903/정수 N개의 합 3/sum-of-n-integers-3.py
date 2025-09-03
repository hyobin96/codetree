n, k = map(int, input().split())

arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    inputs = list(map(int, input().split()))

    for j in range(1, n + 1):
        arr[i][j] = inputs[j - 1]


s_arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        s_arr[i][j] = s_arr[i - 1][j] + s_arr[i][j - 1] - s_arr[i - 1][j - 1] + arr[i][j]


answer = 0

for i in range(k, n + 1):
    for j in range(k, n + 1):
        _sum = s_arr[i][j] - s_arr[i - k][j] - s_arr[i][j - k] + s_arr[i - k][j - k]
        answer = max(answer, _sum)

print(answer)

