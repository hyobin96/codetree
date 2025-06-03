n = int(input())
arr = list(map(int, input().split()))

def recur(lcm, i):
    if i == len(arr):
        return lcm
    if lcm > arr[i]:
        return recur((lcm * arr[i]) // gcd(lcm, arr[i]), i + 1)
    return recur((lcm * arr[i]) // gcd(arr[i], lcm), i + 1)

def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n%m)

print(recur(1, 0))