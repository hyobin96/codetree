s = input()
print(s)
L = len(s)
s *= 2

for i in range(L):
    print(s[L-i-1:2*L-i-1])