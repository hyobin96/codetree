# 지금까지 1계단을 오른 횟수
# 현재 층 수
# 지금까지 주운 동전의 개수

# dp[i][j], i는 층 수, j는 1계단을 오른 횟수

import sys
input = sys.stdin.readline

INT_MIN = -2e9

n = int(input())

coins = [0] + list(map(int, input().strip().split()))

dp = [[INT_MIN] * 4 for _ in range(n + 1)]

dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(4):
        # 두 칸
        if i - 2 >= 0: 
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coins[i])
        # 한 칸
        if i - 1 >= 0 and j - 1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coins[i])

print(max(dp[n]))
