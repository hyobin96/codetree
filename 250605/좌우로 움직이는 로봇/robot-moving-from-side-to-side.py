n, m = map(int, input().split())
a, b = [0], [0]
def move(t, d, arr):
    if d == 'L':
        for _ in range(t):
            arr.append(arr[-1] - 1)
    else:
        for _ in range(t):
            arr.append(arr[-1] + 1)

for _ in range(n):
    t, d = input().split()
    move(int(t), d, a)
for _ in range(m):
    t, d = input().split()
    move(int(t), d, b)

if len(a) > len(b):
    a, b = b, a

cnt = 0
for i in range(1, len(a)):
    if a[i-1] != b[i-1] and a[i] == b[i]:
        cnt += 1

for i in range(len(a), len(b)):
    if b[i-1] != a[-1] and b[i] == a[-1]:
        cnt += 1

print(cnt)