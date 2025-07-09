def select_col(cnt, result):
    global answer, visited, grid
    if cnt == N:
        answer = max(answer, result)
        return

    for col in range(N):
        if visited[col]:
            continue

        visited[col] = True
        select_col(cnt + 1, min(result, grid[cnt][col]))
        visited[col] = False
        

N = int(input())
answer, visited = 0, [False] * N
grid = [list(map(int, input().split())) for _ in range(N)]
select_col(0, 10001)
print(answer)
        
        