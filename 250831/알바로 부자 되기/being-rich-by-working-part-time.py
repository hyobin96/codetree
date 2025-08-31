n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.

last_day = max(e)

dp = [0] * (last_day + 1)

i = 1
j = 0
while i <= last_day and j < n:
    if e[j] <= i:
        dp[i] = max(dp[s[j] - 1] + p[j], dp[i])
        j += 1
    else:
        i += 1

print(max(dp))
