n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n

answer = 0

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

    for k in range(i + 1, n):
        for m in range(i, k + 1):
            if arr[k] < arr[m]:
                dp[k] = max(dp[k], dp[m] + 1)

    answer = max(answer, max(dp))
    for l in range(i + 1, n):
        dp[l] = 1
    
print(answer)