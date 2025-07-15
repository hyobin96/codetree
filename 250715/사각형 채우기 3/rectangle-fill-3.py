N = int(input())
dp = [0] * (N + 2)
dp[0], dp[1], dp[2] = 1, 2, 7
for i in range(3, N + 1):
    dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2]) % 1000000007
    dp[i] = (dp[i] + (sum(dp[:i - 2]) * 2)) % 1000000007

print(dp[N])