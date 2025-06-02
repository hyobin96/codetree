n, m = map(int, input().split())
arr = list(map(int, input().split()))

def change_m(m):
    if m % 2 == 0:
        m //= 2
    else:
        m -= 1
    return m

total = arr[m - 1]
while m != 1:
    m = change_m(m)
    total += arr[m - 1]

print(total)  