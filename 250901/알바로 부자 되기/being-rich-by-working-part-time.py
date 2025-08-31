n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.


dp = [0] * (n)
dp[0] = p[0]

# i번째 알바를 선택한 경우
for i in range(1, n):
    dp[i] = p[i]
    for j in range(i - 1, -1, -1):
        if e[j] < s[i]:
            dp[i] = max(dp[j] + p[i], dp[i])
            break      

print(max(dp))
