# dp[i] 는 합이 i일 때 가능하면 1, 아니면 0
import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().strip().split()))

m = sum(numbers)
if m % 2 != 0:
    print('No')
    sys.exit()

m //= 2

dp = [1] + [0] * m
for num in numbers:
    for j in range(m, num - 1, -1):
        if dp[j - num]:
            dp[j] = 1

print('Yes' if dp[m] else 'No')

