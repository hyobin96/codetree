arr = []
idx = 0

while True:
    s = input()
    if s == '0':
        break
    if idx % 2 == 0:
        arr.append(s)
    idx += 1

print(idx)
for e in arr:
    print(e)