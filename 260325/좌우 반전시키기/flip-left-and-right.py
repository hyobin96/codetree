n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(1, n):
    if arr[i - 1] == 0:
        arr[i - 1] ^= 1
        arr[i] ^= 1
        if i < n - 1:
            arr[i + 1] ^= 1
        cnt += 1

answer = cnt if arr[-1] != 0 else -1
print(answer)