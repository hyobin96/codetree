s = list(input())
while len(s) > 1:
    x = int(input())
    if len(s) - 1 < x:
        s.pop()
    else:
        s.pop(x)
    print(''.join(s))