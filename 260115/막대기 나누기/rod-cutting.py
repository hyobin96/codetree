# dp[i], 길이가 i일 때 얻을 수 있는 최대 수익
# 10000 * 100 = 10 ** 6
# 2 9 10 11
# 2 9 11 12
# 2 9 11 18
n = int(input())

values = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            dp[i + j] = max(dp[i + j], dp[i] + values[j])

print(dp[n])
