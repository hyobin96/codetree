N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
# 20씩 밀기, 0이 -20
# N * 41 배열? 각 행이 각 단계
dp = [[0] * 41 for _ in range(N)]

# 초기 세팅
dp[0][nums[0] + 20] = 1
dp[0][-nums[0] + 20] = 1

# 단계별로 수행
for i in range(1, N):
    num = nums[i]
    for j in range(41):
        if dp[i - 1][j]:
            nxt1, nxt2 = j + num, j - num
            if nxt1 <= 40:
                dp[i][nxt1] += dp[i - 1][j]
            if nxt2 >= 0:
                dp[i][nxt2] += dp[i - 1][j]

print(dp[N - 1][M + 20])
