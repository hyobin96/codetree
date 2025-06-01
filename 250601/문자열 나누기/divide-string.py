n = int(input())
arr = input().split()
s = ''.join(arr)
for i in range(len(s)):
    if i != 0 and i % 5 == 0:
        print()
    print(s[i], end='')
    