s = input()
query = input()
for q in query:
    if q == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[0:-1]
print(s)