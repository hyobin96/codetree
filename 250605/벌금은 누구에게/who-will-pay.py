n, m, k = map(int, input().split())
q = [int(input()) for _ in range(m)]
arr = [0] * 101
idx = -1
for i in q:
    arr[i] += 1
    if arr[i] == k:
        idx = i
        break
print(idx)