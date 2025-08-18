import heapq

n, m = map(int, input().split())
pq = list(map(lambda x: x * -1, map(int, input().split())))
heapq.heapify(pq)

for _ in range(m):
    max_num = -heapq.heappop(pq)
    heapq.heappush(pq, -(max_num - 1))

print(-heapq.heappop(pq))