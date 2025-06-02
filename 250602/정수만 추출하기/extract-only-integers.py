arr = input().split()
total = 0
for e in arr:
    idx = len(e)
    for i in range(len(e)):
        if not e[i].isdigit():
            idx = i
            break
    total += int(e[:idx])
print(total)