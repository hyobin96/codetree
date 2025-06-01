a, b = input().split()
a = ord(a)
b = ord(b)
if a > b:
    print(a + b, a - b)
else:
    print(a + b, b - a)