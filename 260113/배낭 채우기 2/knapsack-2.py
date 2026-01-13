# dp[i] 무게가 i일 때 얻을 수 있는 최대 가치

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

jewels = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().strip().split())
    jewels.append((w, v))

jewels.sort()
# print(jewels)

dp = [0] * (m + 1)
for i in range(m + 1):
    for j in range(1, len(jewels)):
        w, v = jewels[j]
        if i + w <= m:
            dp[i + w] = max(dp[i + w], dp[i] + v)

print(max(dp))