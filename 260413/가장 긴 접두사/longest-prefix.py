target = '#' + input().rstrip()
t_l = len(target)

f = [0] * (t_l)
f[0] = -1

for i in range(1, t_l):
    j = f[i - 1]

    while j >= 0 and target[i] != target[j + 1]:
        j = f[j]

    f[i] = j + 1

max_length = 1
for i in range(t_l - 1, 1, -1):
    if f[i] >= i // 2:
        max_length = max(max_length, i)
        continue
    max_length = max(max_length, f[i])

print(max_length)
