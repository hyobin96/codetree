a, b = input(), input()
n = -1
for i in range(1, len(a)):
    a = a[-1] + a[:-1]
    if a == b:
        n = i
        break

print(n)