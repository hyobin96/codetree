n = int(input())
arr = list(map(int, input().split()))

for i in range(1, len(arr)):
    for j in range(len(arr) - i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)