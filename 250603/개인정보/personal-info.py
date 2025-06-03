arr = [tuple(input().split()) for _ in range(5)]
print('name')
for e in sorted(arr, key=lambda x:x[0]):
    print(e[0], e[1], e[2])
print()
print('height')
for e in sorted(arr, key=lambda x:-int(x[1])):
    print(e[0], e[1], e[2])