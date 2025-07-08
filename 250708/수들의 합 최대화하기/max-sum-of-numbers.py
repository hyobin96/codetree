def select_nums(cnt, result, start):
    global col_visited, answer, grid
    if cnt == N:
        answer = max(answer, result)
        return

    for i in range(start, N):
        for j in range(N):
            if col_visited[j]:
                continue

            col_visited[j] = True
            select_nums(cnt + 1, result + grid[i][j], i + 1)
            col_visited[j] = False

    
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
col_visited = [False] * N
answer = 0
select_nums(0, 0, 0)
print(answer)