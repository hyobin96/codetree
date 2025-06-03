a, b, c = map(int, input().split())
res = a * b * c

def _sum(n):
    if n < 10:
        return n
    return n % 10 + _sum(n // 10)

print(_sum(res))