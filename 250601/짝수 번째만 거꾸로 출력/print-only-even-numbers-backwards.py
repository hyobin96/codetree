s = input()
even = []
for i in range(1, len(s), 2):
    even.append(s[i])
for e in even[::-1]:
    print(e, end='')