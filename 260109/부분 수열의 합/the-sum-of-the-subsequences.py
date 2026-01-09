# dp[i] 는 i를 만들 수 있는 지 없는 지 1과 0으로 판단
# 수열 첫번째부터 마지막까지 순서대로 돌면서 dp[1] ~ dp[m] 까지
# dp[i]가 존재하면 dp[i + num] = 1로 설정
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

sequence = list(map(int, input().strip().split()))

dp = [True] + [False] * m
for num in sequence:
    for i in range(m, -1, -1):
        if dp[i] and i + num <= m:
            dp[i + num] = True

print('Yes' if dp[m] else 'No')

