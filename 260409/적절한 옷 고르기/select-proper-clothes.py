cloth_count, days = map(int, input().split())
cloth_info = [0] + [tuple(map(int, input().split())) for _ in range(cloth_count)]

dp = [[-1] * (cloth_count + 1) for _ in range(days + 1)]

for i in range(1, cloth_count + 1):
    s, e, v = cloth_info[i]
    dp[1][i] = 0 if s <= i <= e else dp[1][i]
    
for day in range(2, days + 1):
    for cloth1 in range(1, cloth_count + 1):
        s1, e1, v1 = cloth_info[cloth1]
        if not(s1 <= day <= e1):
            continue
        for cloth2 in range(1, cloth_count + 1):
            s2, e2, v2 = cloth_info[cloth2]
            if dp[day - 1][cloth2] == -1:
                continue
            dp[day][cloth1] = max(dp[day][cloth1], dp[day - 1][cloth2] + abs(v1 - v2))

answer = max(dp[days])
print(answer)