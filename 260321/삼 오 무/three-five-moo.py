n = int(input())

# Please write your code here.
# 3, 5, 15

def is_possible(number, n):
    cnt = number // 3 + number // 5 - number // 15
    return cnt + n <= number

min_num = 3 * n
left, right = 1, 3 * n
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid, n):
        right = mid - 1
        min_num = min(min_num, mid)
    else:
        left = mid + 1

print(min_num)
