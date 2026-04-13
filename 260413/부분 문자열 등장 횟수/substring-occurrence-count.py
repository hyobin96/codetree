target = '#' + input().rstrip()
pattern = '#' + input().rstrip()

t_l = len(target)
p_l = len(pattern)

f = [0] * (p_l)
f[0] = -1
for i in range(1, p_l):
    j = f[i - 1]

    while j >= 0 and pattern[i] != pattern[j + 1]:
        j = f[j]

    f[i] = j + 1

# print(f)
j = 0
count = 0
for i in range(1, t_l):
    
    while j >= 0 and target[i] != pattern[j + 1]:
        j = f[j]

    j += 1

    if j == p_l - 1:
        count += 1
        j = f[j]

print(count)