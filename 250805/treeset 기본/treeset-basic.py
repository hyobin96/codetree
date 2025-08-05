from sortedcontainers import SortedSet

n = int(input())

s = SortedSet()
for _ in range(n):
    line = input().split()
    com = line[0]
    if com == 'add':
        s.add(int(line[1]))
    elif com == 'remove':
        s.remove(int(line[1]))
    elif com == 'find':
        x = int(line[1])
        print('true' if x in s else false)
    elif com == 'lower_bound':
        x = int(line[1])
        idx = s.bisect_left(x)
        print('None' if idx == len(s) else s[idx])
    elif com == 'upper_bound':
        x = int(line[1])
        idx = s.bisect_right(x)
        print('None' if idx == len(s) else s[idx])
    elif com == 'largest':
        print(s[-1] if s else 'None')
    else:
        print(s[0] if s else 'None')
