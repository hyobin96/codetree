# dp[i] 는 i를 만드는 데 사용한 동전의 개수
# 1부터 M까지 1 - coin이 있는 지 확인
# i = 0 빼고 INF로 초기화
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
coins = list(map(int, input().strip().split()))
coins.sort()

dp = [0] * (m + 1)

for c in coins:
    if c <= m:
        dp[c] = 1

for i in range(1, m + 1):
    if not dp[i]:
        continue
    for c in coins:
        if i + c <= m:
            dp[i + c] = max(dp[i] + 1, dp[i + c])

print(dp[m] if dp[m] else -1)
        


