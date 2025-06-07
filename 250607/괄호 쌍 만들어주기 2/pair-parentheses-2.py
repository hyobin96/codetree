s = input()
cnt = 0
for i in range(len(s) - 1):
    if s[i:i+2] == '((':
        for j in range(i+2, len(s) - 1):
            if s[j:j+2] == '))':
                cnt += 1
print(cnt)