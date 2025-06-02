arr = input().split()
total = 0
for e in arr:
    for i in range(len(e)):
        if not e[i].isdigit():
            total += int(e[:i])
print(total)