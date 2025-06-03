n, k, t = input().split()
n, k = int(n), int(k)
arr = []
for _ in range(n):
    s = input()
    if s.startswith(t):
        arr.append(s)

arr.sort()
print(arr[k-1])