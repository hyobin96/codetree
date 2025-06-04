n = int(input())
arr = []
while n != 0:
    arr.append(str(n % 2))
    n //= 2
print(''.join(arr[::-1]))