import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
    edges[v].append((u, w))

INF = 2e9
dists = [INF] * (n + 1)
dists[k] = 0

pq = []
heapq.heappush(pq, (0, k))

while pq:
    w, u = heapq.heappop(pq)
    if dists[u] != w:
        continue
    
    for v, w in edges[u]:
        new_dist = dists[u] + w
        if dists[v] > new_dist:
            dists[v] = new_dist
            heapq.heappush(pq, (w, v))

print(0)
for i in range(1, n + 1):
    if i == k:
        continue
    print(dists[i] if dists[i] != INF else -1)

