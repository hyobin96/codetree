s = input()
arr = [e.upper() for e in s if e.isalpha()]
print(''.join(arr))