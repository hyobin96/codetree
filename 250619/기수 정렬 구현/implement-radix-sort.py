n = int(input())
nums = list(map(int, input().split()))

mod = 1
for _ in range(len(str(max(nums)))):
    arr = [[] for _ in range(10)]
    for num in nums:
        remains = (num // mod) % 10
        arr[remains].append(num)

    mod *= 10

    store_arr = []
    for i in range(10):
        for j in range(len(arr[i])):
            store_arr.append(arr[i][j])

    nums = store_arr

print(*nums)
