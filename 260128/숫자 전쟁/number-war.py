# 지금까지 얻은 점수
# 상대방이 버린 카드의 개수
# 남우가 버린 카드의 개수
# dp[i][j] -> i는 상대방이 버린 카드의 개수, j는 남우가 버린 카드의 개수
# dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
# 근데 규칙이 있기 때문에 카드 점수 비교해서 1 또는 2 선택 필요
# 상대방[i] 남우[j]

import sys
input = sys.stdin.readline

INT_MIN = -2e9

n = int(input())

상대방 = [0] + list(map(int, input().strip().split()))
남우 = [0] + list(map(int, input().strip().split()))


dp = [[0] * (n + 1) for _ in range(n + 1)]
# dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
        if 상대방[i] > 남우[j]:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + 남우[j])
        elif 상대방[i] < 남우[j]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

print(max(dp[n]))