X = int(input())

s = 0
v = 0
t = 0
for n in range(1, X + 1):
    s += n

    if s >= X // 2:
        v = n - 1
        t = n
        break
while s < X:
    s += v
    v = v - 1 if v - 1 > 0 else 1
    t += 1

print(t)