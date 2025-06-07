n = int(input())
arr = list(map(int, input().split()))
cnt = n
for i in range(n):
    for j in range(i+1, n):
        avg = sum(arr[i:j+1]) / (j-i+1)
        for k in range(i, j+1):
            if avg == arr[k]:
                cnt += 1
                break
print(cnt)