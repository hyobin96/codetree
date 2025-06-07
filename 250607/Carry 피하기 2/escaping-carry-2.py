n = int(input())
arr = [int(input()) for _ in range(n)]

def is_carry(a, b, c):
    # a, b, c = map(lambda x: str(x), (a, b, c))
    while not (a == 0 and b == 0 and c == 0):
        _sum = a % 10 + b % 10 + c % 10
        if _sum >= 10:
            return True
        a, b, c = a // 10, b // 10, c // 10
    return False

ans = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not is_carry(arr[i], arr[j], arr[k]):
                ans = max(ans, arr[i] + arr[j] + arr[k])
print(ans)