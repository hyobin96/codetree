s = input()
arr = []
for e in s:
    if e.isalpha():
        arr.append(e.lower())
    elif e.isdigit():
        arr.append(e)
print(''.join(arr))