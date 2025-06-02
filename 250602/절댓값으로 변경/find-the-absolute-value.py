n = int(input())
arr = list(map(int, input().split()))

def _abs(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = - arr[i]

_abs(arr)
print(*arr)