import sys, heapq

input = sys.stdin.readline

INF = 2e9
n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

dist = [INF] * (n + 1) 
dist[1] = 0

pq = []
heapq.heappush(pq, 1)

while pq:
    u = heapq.heappop(pq)
    for v, w in edges[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, v)

for i in range(2, n + 1):
    print(dist[i] if dist[i] != INF else -1)
