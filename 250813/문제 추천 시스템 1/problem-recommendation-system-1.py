from sortedcontainers import SortedSet

n = int(input())
s = SortedSet()
for _ in range(n):
    p, l = map(int, input().split())
    s.add((l, p))

m = int(input())
for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'rc':
        x = int(cmd[1])

        if x == 1:
            print(s[-1][1])
        else:
            print(s[0][1])

    elif cmd[0] == 'ad':
        p, l = int(cmd[1]), int(cmd[2])
        s.add((l, p))

    else:
        p, l = int(cmd[1]), int(cmd[2])
        s.remove((l, p))