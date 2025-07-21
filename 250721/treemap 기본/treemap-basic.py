from sortedcontainers import SortedDict

N = int(input())
d = SortedDict()

for _ in range(N):
    commands = input().split()
    com = commands[0]
    if com == 'add':
        k, v = int(commands[1]), int(commands[2])
        d[k] = v
    elif com == 'remove':
        k = int(commands[1])
        d.pop(k)
    elif com == 'find':
        k = int(commands[1])
        if k in d:
            print(d[k])
        else:
            print('None')
    else:
        if d:
            for k in d.values():
                print(k, end = ' ')
            print()
        else:
            print('None')