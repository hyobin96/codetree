n, k, b = map(int, input().split())

nums = [0] * (n + 1)

for _ in range(b):
    num = int(input())
    nums[num] = 1


prefix_sums = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_sums[i] = prefix_sums[i - 1] + nums[i]


answer = k
for i in range(k, n + 1):
    cnt = prefix_sums[i] - prefix_sums[i - k]
    answer = min(answer, cnt)


print(answer)