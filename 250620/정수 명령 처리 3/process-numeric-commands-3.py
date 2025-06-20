from collections import deque

dq = deque()

N = int(input())

for _ in range(N):
    q = input().split()

    if q[0] == 'push_front':
        dq.appendleft(int(q[1]))

    elif q[0] == 'push_back':
        dq.append(int(q[1]))

    elif q[0] == 'pop_front':
        print(dq.popleft())

    elif q[0] == 'pop_back':
        print(dq.pop())

    elif q[0] == 'size':
        print(len(dq))

    elif q[0] == 'empty':
        print(int(not dq))

    elif q[0] == 'front':
        print(dq[0])

    elif q[0] == 'back':
        print(dq[-1])

    
