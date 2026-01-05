# 0 0 0 0 0 0
# 0 1 1 0 0 1  
# 0 1 2 1 0 1   i = 1
# 0 1 2 3 2 1   i = 2
# 0 1 2 3 5 4   i = 3
# 0 1 2 3 5 9

n = int(input())

nums = (1, 2, 5)

dp = [0] * (n + 1)
for num in nums:
    dp[num] = 1

for i in range(1, n):
    for num in (1, 2, 5):
        if i + num <= n:
            dp[i + num] += dp[i]

print(dp[n] % 10007)