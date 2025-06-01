a = input()
b = input()
total = 0
for i in range(len(a) - len(b) + 1):
    is_same = True
    for j in range(len(b)):
        if a[i + j] != b[j]:
            is_same = False
            break
    if is_same:
        total += 1
print(total)