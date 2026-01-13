# dp[i][j] 무게가 j 이하일 때 i개의 보석을 골랐을 때 최대 가치
# j - jewels[i]를 매번 돌기?
# 100 * 10000 * 100 = 10 ** 8 , 1억번

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

jewels = [0]
for _ in range(n):
    w, v = map(int, input().strip().split())
    jewels.append((w, v))

# print(jewels)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(1, len(jewels)):
            w, v = jewels[k]
            if j >= w:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]

print(dp[n][m])