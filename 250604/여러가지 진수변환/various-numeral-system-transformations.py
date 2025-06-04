n, b = map(int, input().split())
arr = []
while True:
    arr.append(str(n % b))
    n //= b
    if n == 0:
        break
print(''.join(arr[::-1]))