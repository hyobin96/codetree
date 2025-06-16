N = int(input())
arr = input().split()

cnt = 0
for i in range(N):
    for j in range(1, N - i):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            cnt += 1

print(cnt)