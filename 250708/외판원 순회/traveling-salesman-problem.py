def select_orders(cnt, result, last):
    global answer, visited, costs
    if cnt == N - 1:
        if costs[last][0] != 0:
            answer = min(answer, result + costs[last][0])
        return
    
    for i in range(1, N):
        if visited[i] or costs[last][i] == 0:
            continue
        
        visited[i] = True

        select_orders(cnt + 1, result + costs[last][i], i)

        visited[i] = False


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
answer, visited = 1000000000, [False] * N
select_orders(0, 0, 0)
print(answer)