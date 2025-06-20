from collections import deque


N = int(input())

dq = deque()

for _ in range(N):
    q = input().split()

    if q[0] == 'push':
        dq.append(int(q[1]))

    elif q[0] == 'pop':
        print(dq.popleft())

    elif q[0] == 'size':
        print(len(dq))

    elif q[0] == 'empty':
        print(int(not dq))

    elif q[0] == 'front':
        print(dq[0])

        
