n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

prefix_grid = [[0] * (n + 1) for _ in range(n + 1)]

# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_grid[i][j] = prefix_grid[i - 1][j] + prefix_grid[i][j - 1] - prefix_grid[i - 1][j - 1] + grid[i - 1][j - 1]


answer = -1000000000

 # 0 0 0 0
# 세로 길이
for i in range(1, n + 1):
    # 가로 길이
    for j in range(1, n + 1):

        for k in range(i, n + 1):
            for l in range(j, n + 1):  # k - i, l - j
                _sum = prefix_grid[k][l] - prefix_grid[k - i][l] - prefix_grid[k][l - j] + prefix_grid[k - i][l - j]
                answer = max(answer, _sum)

print(answer)
        
        