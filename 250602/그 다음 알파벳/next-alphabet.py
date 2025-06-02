char = input()
char = ord(char) - ord('a')
res = (char + 1) % (ord('z') - ord('a') + 1)
print(chr(res + ord('a')))