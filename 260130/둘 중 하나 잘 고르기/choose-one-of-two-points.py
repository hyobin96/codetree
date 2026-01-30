# dp[i][j], i는 빨간색 카드를 고른 횟수, j는 파란색 카드를 고른 횟수
# dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + red_cards(i + j + 1 // 2))
# dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + blue_cards(i + j + 1 // 2))
# i == n이면 j로만 가야함, j == n이면 i로만 가야함
# 초기 세팅: 0

import sys
input = sys.stdin.readline

n = int(input())

red_cards, blue_cards = [0], [0]
for _ in range(2 * n):
    r, b = map(int, input().strip().split())
    red_cards.append(r)
    blue_cards.append(b)

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == n and j < n:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + blue_cards[i + j + 1])
        elif j == n and i < n:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + red_cards[i + j + 1])
        elif j < n and i < n:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + blue_cards[i + j + 1])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + red_cards[i + j + 1])

print(dp[n][n])