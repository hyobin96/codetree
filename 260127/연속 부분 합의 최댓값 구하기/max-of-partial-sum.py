import sys

input = sys.stdin.readline

INT_MIN = -2e9

n = int(input())
elements = list(map(int, input().strip().split()))

dp = [INT_MIN] * n
dp[0] = elements[0]

for i in range(1, n):
    dp[i] = max(dp[i - 1] + elements[i], elements[i])

print(max(dp))

