def select_nums(cnt, result):
    global row_visited, col_visited, answer, grid
    if cnt == N:
        answer = max(answer, result)
        return

    for i in range(N):
        for j in range(N):
            if row_visited[i] or col_visited[j]:
                continue

            row_visited[i], col_visited[j] = True, True
            select_nums(cnt + 1, result + grid[i][j])
            row_visited[i], col_visited[j] = False, False

    
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
row_visited, col_visited = [False] * N, [False] * N
answer = 0
select_nums(0, 0)
print(answer)