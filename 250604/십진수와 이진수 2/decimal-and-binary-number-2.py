arr = list(map(int, list(input())))
num = 0
for e in arr:
    num = num * 2 + e
num *= 17

res = []
while True:
    res.append(str(num % 2))
    num //= 2
    if num == 0:
        break
print(''.join(res[::-1]))
