n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_same(i):
    for j in range(n2):
        if a[i+j] != b[j]:
            return False
    return True

is_contain = False
for i in range(n1 - n2 + 1):
    if is_same(i):
        is_contain = True
        break

if is_contain:
    print('Yes')
else:
    print('No')