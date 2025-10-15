n, m, k = map(int, input().split())

answer = []

a_grid, b_grid, c_grid = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]

grids = [a_grid, b_grid, c_grid]

grid = [list(input()) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if grid[i][j] == 'a':
            a_grid[i][j] = 1
        elif grid[i][j] == 'b':
            b_grid[i][j] = 1
        else:
            c_grid[i][j] = 1


a_sums, b_sums, c_sums = [[0] * (m + 1) for _ in range(n + 1)], [[0] * (m + 1) for _ in range(n + 1)], [[0] * (m + 1) for _ in range(n + 1)]

sums = [a_sums, b_sums, c_sums]

for i in range(3):
    target_grid = grids[i]
    target_sums = sums[i]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            target_sums[i][j] = target_sums[i - 1][j] + target_sums[i][j - 1] - target_sums[i - 1][j - 1] + target_grid[i - 1][j - 1]


for _ in range(k):
    cnts = []
    r1, c1, r2, c2 = map(int, input().split())
    
    for target in sums:
        cnt = target[r2][c2] - target[r1 - 1][c2] - target[r2][c1 - 1] + target[r1 - 1][c1 - 1]
        cnts.append(cnt)

    answer.append(cnts)

for ans in answer:
    print(*ans)
