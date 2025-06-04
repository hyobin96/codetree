a, b = map(int, input().split())
n = list(input())

num = 0
for e in n:
    num = num * a + int(e)

arr = []
while True:
    arr.append(str(num % b))
    num //= b
    if num == 0:
        break

print(''.join(arr[::-1]))