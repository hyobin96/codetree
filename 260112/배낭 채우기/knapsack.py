# 행은 n + 1, 열은 m + 1
# dp[n][m] 는 보석을 적절하게 골랐을 때 무게가 M이 넘지 않고 가치의 합이 최대인 것
# j는 무게, 무게가 j인 경우에서 최대 가치
# i는 보석의 순서
# i번째 보석을 고르거나 고르지 않거나 중 가치가 높은 걸 선택

import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

jewels = [0]

for _ in range(n):
    w, v = map(int, input().strip().split())
    jewels.append((w, v))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = jewels[i]
    for j in range(m + 1):
        if j >= w:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(max(dp[n]))

