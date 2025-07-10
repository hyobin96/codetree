import heapq

N = int(input())
pq = []
for _ in range(N):
    q = input().split()
    if q[0] == 'push':
        heapq.heappush(pq, -int(q[1]))
    elif q[0] == 'pop':
        print(-heapq.heappop(pq))
    elif q[0] == 'size':
        print(len(pq))
    elif q[0] == 'empty':
        print(int(not pq))
    elif q[0] == 'top':
        print(-pq[0])
    
