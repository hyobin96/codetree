n = int(input())
arr = []
while True:
    arr.append(str(n % 2))
    n //= 2
    if n == 0:
        break
print(''.join(arr[::-1]))