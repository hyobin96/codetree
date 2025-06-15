import math

X = int(input())

v = int(math.sqrt(X))
s = v * (v + 1) // 2
t = v

while s < X:
    if X - s < v * (v + 1) // 2:
        v -= 1

    s += v
    t += 1

print(t)