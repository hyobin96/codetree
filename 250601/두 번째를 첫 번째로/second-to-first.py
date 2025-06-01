s = list(input())
char1 = s[0]
char2 = s[1]
for i in range(len(s)):
    if s[i] == char2:
        s[i] = char1

print(''.join(s))