N = int(input())
positive_nums = []
negative_nums = []
zero_nums = []

inputs = list(map(int, input().split()))

for num in inputs:
    if num > 0:
        positive_nums.append(num)
    elif num < 0:
        negative_nums.append(num)
    else:
        zero_nums.append(num)

positive_nums.sort()
negative_nums.sort()

res = []
if len(positive_nums) >= 3:
    multiple = 1
    for i in range(3):
        multiple *= positive_nums[i]

    res.append(multiple)

p_len = len(positive_nums)
n_len = len(negative_nums)
z_len = len(zero_nums)

if p_len >= 3:
    multiple = positive_nums[-1] * positive_nums[-2] * positive_nums[-3]
    res.append(multiple)

if p_len >= 1 and n_len >= 2:
    multiple = positive_nums[-1] * negative_nums[0] * negative_nums[1]
    res.append(multiple)

if p_len >= 2 and n_len >= 1:
    multiple = positive_nums[0] * positive_nums[1] * negative_nums[-1]
    res.append(multiple)

if n_len >= 3:
    multiple = negative_nums[-1] * negative_nums[-2] * negative_nums[-3]
    res.append(multiple)

if z_len > 0:
    res.append(0)

print(max(res))