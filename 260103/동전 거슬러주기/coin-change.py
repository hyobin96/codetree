n, m = map(int, input().split())

coins = list(map(int, input().split()))

coins.sort()

# print(coins)

dp = [0] * (m + 1)

for i in range(1, m + 1):
    dp[i] = 10001

for i in range(1, m + 1):
    for j in range(n):
        if coins[j] > i:
            break
        prev = i - coins[j]
        if dp[prev] == 10001:
            continue
        dp[i] = min(dp[prev] + 1, dp[i])

print(-1 if dp[i] == 10001 else dp[i])



