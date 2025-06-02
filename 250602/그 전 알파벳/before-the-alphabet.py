char = ord(input()) - ord('a') - 1
if char < 0:
    char += ord('z') - ord('a') + 1
res = chr(char + ord('a'))
print(res)
