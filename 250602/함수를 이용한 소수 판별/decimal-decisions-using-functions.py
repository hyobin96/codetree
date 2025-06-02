a, b = map(int, input().split())

def is_prime(n):
    for x in range(2, int(n ** 0.5 + 1)):
        if n % x == 0:
            return False
    return True

total = 0
for n in range(a, b+1):
    if is_prime(n):
        total += n
print(total)