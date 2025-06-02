a = input()
total = 0
for e in a:
    if e.isdigit():
        total += int(e)
print(total)