N = int(input())

dp = [0] * (N + 1)
dp[0] = dp[1] = 1

for i in range(2, N + 1):
    res = 0
    for j in range(i):
        res += dp[j] * dp[i - j - 1]
    dp[i] = res

print(dp[N])
