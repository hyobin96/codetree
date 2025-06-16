N = int(input())

arr = list(map(int, input().split()))

one, two = 101, 101
idx1, idx2 = 0, 0

for i, num in enumerate(arr, start = 1):
    if num < one:
        one, two = num, one
        idx1, idx2 = i, idx1
    elif one < num < two:
        two = num
        idx2 = i

if two == 101:
    print(-1)
else:
    if arr.count(two) > 1:
        print(-1)
    else:
        print(idx2)