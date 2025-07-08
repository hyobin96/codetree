def select_orders(cnt, result, last):
    global answer, visited, costs
    if cnt == N - 1:
        answer = min(answer, result + costs[last][0])
        return
    
    for i in range(1, N):
        if visited[i]:
            continue
        
        visited[i] = True

        select_orders(cnt + 1, result + costs[last][i], i)

        visited[i] = False


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
answer, visited = 10000000, [False] * N
select_orders(0, 0, 0)
print(answer)