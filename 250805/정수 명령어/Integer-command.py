from sortedcontainers import SortedSet

T = int(input())
for _ in range(T):
    K = int(input())
    s = SortedSet()
    for _ in range(K):
        line = input().split()
        com, n = line[0], int(line[1])
        if com == 'I':
            s.add(n)
        else:
            if not s:
                continue
            if n == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0])
    
    if s:
        print(s[-1], s[0])
    else:
        print('EMPTY')