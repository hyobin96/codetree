n = int(input())
arr = list(map(int, input().split()))
for i, v in enumerate(arr):
    arr[i] = (v, i+1)

arr.sort(key=lambda x:x[0])
for i, v in enumerate(arr):
    arr[i] += (i+1,)
arr.sort(key=lambda x:x[1])

for e in arr:
    print(e[2], end=' ')