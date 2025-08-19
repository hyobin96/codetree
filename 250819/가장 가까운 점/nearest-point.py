import heapq

n, m = map(int, input().split())

pq = []

for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(pq, (x + y, x, y))

for _ in range(m):
    dist, x, y = heapq.heappop(pq)
    heapq.heappush(pq, (dist + 4, x + 2, y + 2))

_, x, y = heapq.heappop(pq)
print(x, y)
