length = int(input().rstrip())

mod = int(1e9) + 7

dp = [[0] * 10 for _ in range(length + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(1, length):
    for j in range(10):
        if dp[i][j] == 0:
            continue
        
        if j - 1 >= 0:
            dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % mod
        if j + 1 < 10:
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % mod

answer = sum(dp[length])
print(answer)

