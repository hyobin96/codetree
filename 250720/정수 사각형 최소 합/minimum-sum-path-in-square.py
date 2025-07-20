N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][N - 1] = grid[0][N - 1]
for i in range(N - 2, -1, -1):
    dp[0][i] = dp[0][i + 1] + grid[0][i]
    dp[N - i - 1][N - 1] = dp[N - i - 2][N - 1] + grid[N - i - 1][N - 1]

for i in range(1, N):
    for j in range(N - 2, -1, -1):
        dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j + 1] + grid[i][j])

print(dp[N - 1][0])