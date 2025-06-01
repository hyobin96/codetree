arr = ['ee', 'eb']
s = input()
for e in arr:
    cnt = 0    
    for i in range(len(s) - len(e) + 1):
        if s[i] == e[0] and s[i+1] == e[1]:
            cnt += 1
    print(cnt, end=' ')