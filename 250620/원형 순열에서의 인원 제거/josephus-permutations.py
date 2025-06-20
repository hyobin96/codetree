from collections import deque

N, K = map(int, input().split())

dq = deque()

for i in range(1, N+1):
    dq.append(i)

while dq:
    for _ in range(K - 1):
        dq.append(dq.popleft())

    print(dq.popleft(), end=' ')