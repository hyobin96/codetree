arr = []
for e in input():
    if e.islower():
        arr.append(e.upper())
    else:
        arr.append(e.lower())
print(''.join(arr))