N = int(input())
x1_arr = []
x2_arr = []
for _ in range(N):
    x1, x2 = map(int, input().split())
    x1_arr.append(x1)
    x2_arr.append(x2)

min_length = 100
for i in range(N):
    arr1 = x1_arr[:i] + x1_arr[i+1:]
    arr2 = x2_arr[:i] + x2_arr[i+1:]

    x1 = min(arr1)
    x2 = max(arr2)

    min_length = min(min_length, x2 - x1)

print(min_length)