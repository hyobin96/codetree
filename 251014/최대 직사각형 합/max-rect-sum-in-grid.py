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


# r1, c1 은 왼쪽 위 꼭짓점, r2, c2는 오른쪽 아래 꼭짓점
def get_area(r1, c1, r2, c2):
    return prefix_grid[r2][c2] - prefix_grid[r1 - 1][c2] - prefix_grid[r2][c1 - 1] + prefix_grid[r1 - 1][c1 - 1]

answer = -1000000000

# 시작 행
for i1 in range(1, n + 1):
    # 끝 행
    for i2 in range(i1, n + 1):
        _sums = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)

        for j in range(1, n + 1):
            _sums[j] = get_area(i1, j, i2, j)
            prefix_sum[j] = prefix_sum[j - 1] + _sums[j]

            if prefix_sum[j] < 0:
                answer = max(answer, prefix_sum[j])
                prefix_sum[j] = 0
            else:
                answer = max(answer, prefix_sum[j])
        

print(answer)
        
        