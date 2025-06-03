n = int(input())

def cnt(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        n //= 2
    else:
        n //= 3
    return cnt(n) + 1

print(cnt(n))