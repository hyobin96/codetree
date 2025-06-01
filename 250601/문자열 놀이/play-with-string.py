s, q = input().split()
s = list(s)
q = int(q)
for _ in range(q):
    a, b, c = input().split()
    if a == '1':
        b, c = int(b), int(c)
        s[b - 1], s[c - 1] = s[c - 1], s[b - 1]
        print(''.join(s))
    else:
        for i in range(len(s)):
            if s[i] == b:
                s[i] = c
        print(''.join(s))        
        