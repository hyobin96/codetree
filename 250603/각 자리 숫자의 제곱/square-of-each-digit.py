n = int(input())

def square(n):
    if n < 10:
        return n * n
    return square(n // 10) + (n % 10) ** 2
print(square(n))