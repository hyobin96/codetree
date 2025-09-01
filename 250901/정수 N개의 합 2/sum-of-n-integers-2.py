n, k = map(int, input().split())

arr = list(map(int, input().split()))

s = [0] * (n + 1)

for i in range(1, n + 1):
    s[i] = s[i - 1] + arr[i - 1]


answer = -100 * k

for i in range(1, n + 1):
    answer = max(s[i] - s[i - k], answer)

print(answer)