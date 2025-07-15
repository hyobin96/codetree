N = int(input())
dp = [[0] * (N + 2) for _ in range(N + 2)]
dp[0][0], dp[0][1], dp[0][2] = 1, 2, 7
for i in range(3, N + 1):
    dp[1][i] = (dp[1][i - 1] + dp[0][i - 3]) % 1000000007
    dp[0][i] = (2 * dp[0][i - 1] + 3 * dp[0][i - 2] + 2 * dp[1][i]) % 1000000007

print(dp[0][N])