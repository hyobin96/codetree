n, b = map(int, input().split())
prices = [int(input()) for _ in range(n)]
prices.sort()

_max = 0
for i in range(n):
    credit = b
    cnt = 0
    for j, p in enumerate(prices):
        if i == j:
            p //= 2
        if credit < p:
            break
        credit -= p
        cnt += 1
    _max = max(_max, cnt)
print(_max)