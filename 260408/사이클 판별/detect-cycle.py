from collections import deque

node_count, edge_count = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(edge_count)]
indegrees = [0] * (node_count + 1)
graph = [[] for _ in range(node_count + 1)]

for a, b in edges:
    graph[a].append(b)
    indegrees[b] += 1    

q = deque()
for i in range(1, node_count + 1):
    if indegrees[i] == 0:
        q.append(i)

paths = []
while q:
    curr = q.popleft()
    paths.append(curr)

    for nxt in graph[curr]:
        indegrees[nxt] -= 1
        if indegrees[nxt] == 0:
            q.append(nxt)


if len(paths) == node_count:
    print("Not Exists")
else:
    print("Exists")