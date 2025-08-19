import heapq

n = int(input())
operations = [int(input()) for _ in range(n)]
pq = []

for o in operations:
    if o:
        heapq.heappush(pq, o)
    else:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)