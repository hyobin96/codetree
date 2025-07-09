def dfs(curr):
    global visited
    visited[curr] = True
    cnt = 1

    for v in graph[curr]:
        if visited[v]:
            continue
        cnt += dfs(v)

    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = dfs(1) - 1
print(answer)