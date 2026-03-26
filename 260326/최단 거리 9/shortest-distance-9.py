vertex_count, edge_count = map(int, input().split())

edges = [[] for _ in range(vertex_count + 1)]

for _ in range(edge_count):
    u, v, d = map(int, input().split(" "))
    edges[u].append((v, d))
    edges[v].append((u, d))

begin, target = map(int, input().split(" "))

INF = 2e9

dists = [INF] * (vertex_count + 1)
paths = [0] * (vertex_count + 1)

dists[begin] = 0

import heapq

pq = []
heapq.heappush(pq, (0, begin))

while pq:
    min_dist, curr = heapq.heappop(pq)
    if min_dist != dists[curr]:
        continue
    
    for nxt, dist in edges[curr]:
        new_dist = dists[curr] + dist
        if dists[nxt] > new_dist:
            dists[nxt] = new_dist
            paths[nxt] = curr
            heapq.heappush(pq, (new_dist, nxt))

# print(paths)
x = target
answer = [str(x)]
while x != begin:
    x = paths[x]
    answer.append(str(x))

print(dists[target])
print(' '.join(answer[::-1]))