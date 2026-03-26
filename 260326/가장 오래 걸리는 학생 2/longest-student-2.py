n, m = map(int, input().split())
segs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

INF = 2e9

edges = [[] for _ in range(n + 1)]
# print(edges)
for u, v, d in segs:
    edges[v].append((u, d))

# print(edges)

school = n
dists = [INF] * (n + 1)
dists[school] = 0
pq = []
heapq.heappush(pq, (0, school))

while pq:
    min_dist, u = heapq.heappop(pq)
    
    if min_dist != dists[u]:
        continue
    
    for v, dist in edges[u]:
        next_dist = min_dist + dist
        if dists[v] > next_dist:
            dists[v] = next_dist
            heapq.heappush(pq, (next_dist, v))

max_dist = 0
for dist in dists:
    if dist != INF:
        max_dist = max(max_dist, dist)

print(max_dist)
        

