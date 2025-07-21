N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = grid[0][0]

for i in range(1, N):
    dp[0][i] = min(dp[0][i - 1], grid[0][i])
    dp[i][0] = min(dp[i - 1][0], grid[i][0])

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = min(grid[i][j], max(dp[i - 1][j], dp[i][j - 1]))

print(dp[N - 1][N - 1])