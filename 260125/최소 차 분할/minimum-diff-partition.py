# dp[i] -> i의 합이 가능한 경우
# i는 최대 1000
# numbers의 합이랑 i 가 같은 경우는 안됨

import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().strip().split()))

total = sum(numbers)
m = total // 2 + 1

dp = [1] + [0] * m
for num in numbers:
    for j in range(m, num - 1, -1):
        if dp[j - num]:
            dp[j] = 1

answer = 0
for i in range(m, -1, -1):
    if dp[i] and total >= 2 * i:
        answer = total - 2 * i
        break

print(answer)