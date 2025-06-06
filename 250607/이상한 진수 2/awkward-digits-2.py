n = input()
num = int(n, 2)
_max = 0
for i in range(0, len(n)):
    if n[i] == '1':
        tmp = num - 2 ** (len(n) - 1 - i)
    else:
        tmp = num + 2 ** (len(n) - 1 - i)
    _max = max(_max, tmp)
print(_max)