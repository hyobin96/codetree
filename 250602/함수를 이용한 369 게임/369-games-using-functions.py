a, b = map(int, input().split())

def is_magic_num(n):
    return n % 3 == 0 or contains_369(n)
def contains_369(n):
    n = str(n)
    return '3' in n or '6' in n or '9' in n

total = 0
for n in range(a, b+1):
    if is_magic_num(n):
        total += 1
print(total)