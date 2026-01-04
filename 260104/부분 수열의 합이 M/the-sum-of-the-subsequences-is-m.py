n, m = map(int, input().split())

numbers = list(map(int, input().split()))

dp = [0] + [101 for _ in range(m)]

for i in range(n):
    for j in range(m, -1, -1):
        if j - numbers[i] >= 0 and dp[j - numbers[i]] != 101:
            dp[j] = min(dp[j], dp[j - numbers[i]] + 1)


print(dp[m] if dp[m] != 101 else -1)

                        
        









