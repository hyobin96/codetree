a, b = map(int, input().split())

def is_prime(n):
    if n <= 2:
        return True
    for x in range(2, int(n ** 0.5 + 1)):
        if n % x == 0:
            return False
    return True

def is_even(n):
    if sum(map(int, list(str(n)))) % 2 == 0:
        return True
    return False

total = 0
for n in range(a, b+1):
    if is_prime(n) and is_even(n):
        total += 1
print(total)