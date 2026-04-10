floor_count = int(input().rstrip())
info = [0] + [tuple(map(int, input().split())) for _ in range(floor_count)]
dp = [[0] * 3 for _ in range(floor_count + 1)]

for i in range(3):
    dp[1][i] = info[1][i]

for i in range(2, floor_count + 1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + info[i][j])

answer = max(dp[floor_count])
print(answer)