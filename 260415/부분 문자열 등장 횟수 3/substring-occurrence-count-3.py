target = '#' + input().rstrip()
pattern = '#' + input().rstrip()

t_l, p_l = len(target), len(pattern)

f = [0] * p_l
f[0] = -1

for i in range(1, p_l):
    j = f[i - 1]

    while j >= 0 and pattern[i] != pattern[j + 1]:
        j = f[j]

    f[i] = j + 1

idxs = []

j = 0
for i in range(1, t_l):

    while j >= 0 and target[i] != pattern[j + 1]:
        j = f[j]

    j += 1

    if j == p_l - 1:
        idxs.append((i - p_l + 2, i))
        j = f[j]

count = len(idxs)
if idxs:
    prev = idxs[0][1]
for i, (l, r) in enumerate(idxs):
    if i == 0:
        continue
    if l <= prev:
        count -= 1
    prev = r

print(count)
    