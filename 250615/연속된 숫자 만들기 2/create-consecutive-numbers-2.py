arr = list(map(int, input().split()))
arr2 = sorted(arr)

if arr2[1] - arr2[0] == 1 and arr2[2] - arr2[1] == 1:
    print(0)
elif abs(arr[0] - arr[1]) == 2 or abs(arr[1] - arr[2]) == 2 or abs(arr[2] - arr[0]) == 2:
    print(1)
else:
    print(2)