from collections import deque

node_count, edge_count = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(edge_count)]
graph = [[] for _ in range(node_count + 1)]
indegree = [0] * (node_count + 1)

for a, b in edges:
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, node_count + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    print(node, end = ' ')

    for nxt in graph[node]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)


