# 연속합
# 양수면 그냥 더하고, 음수면 고를 경우, 고르지 않을 경우,
# dp[i][j]
# max(i + 1부터 시작하는 경우, i와 i + 1을 합치는 경우) 를 선택
# 음수라면 j + 1로 넘어가야 함
# j + 1 에서도 지금부터 시작하는 게 나은 지 이전과 합치는 걸 선택하는 게 나은지 선택 필요

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

numbers = [0] + list(map(int, input().strip().split()))

dp = [[-10_001] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    number = numbers[i]
    if number >= 0:
        dp[i][0] = number
    else:
        dp[i][1] = number

# for row in dp:
#     print(row)

for i in range(1, n):
    number = numbers[i + 1]
    for j in range(k + 1):
        if dp[i][j] == -10_001:
            continue
        if number >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + number)
        if number < 0:
            if j == k:
                continue
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + number) 

# for row in dp:
#     print(row)

answer = -10_001

for row in dp:
    answer = max(answer, max(row))

print(answer)
