a, b = map(int, input().split())

def is_onjun(n):
    if n % 2 == 0:
        return False
    if n % 10 == 5:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False
    return True

total = 0
for n in range(a, b+1):
    if is_onjun(n):
        total += 1
print(total)