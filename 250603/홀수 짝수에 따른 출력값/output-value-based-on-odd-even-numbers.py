n = int(input())

def total(n):
    if n <= 2:
        return n
    return n + total(n-2)

print(total(n))