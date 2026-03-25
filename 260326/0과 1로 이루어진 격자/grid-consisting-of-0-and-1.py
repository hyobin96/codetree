n = int(input())
grid = [list(map(int, tuple(input()))) for _ in range(n)]

# Please write your code here.
def reverse_left_up(r, c, grid):
    for i in range(r, -1, -1):
        for j in range(c, -1, -1):
            grid[i][j] ^= 1

cnt = 0
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if grid[i][j]:
            reverse_left_up(i, j, grid)
            cnt += 1

print(cnt)
            