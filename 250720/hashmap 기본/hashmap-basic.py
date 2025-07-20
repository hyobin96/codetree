N = int(input())

d = dict()
for _ in range(N):
    commands = input().split(" ")
    com = commands[0]
    if com == 'add':
        k, v = commands[1], commands[2]
        d[k] = v
    elif com == 'remove':
        k = commands[1]
        d.pop(k)
    else:
        k = commands[1]
        print(d[k] if k in d else 'None')