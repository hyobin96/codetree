s = int(input())

# Please write your code here.

left, right = 1, s
max_n = 1
while left <= right:
    mid = (left + right) // 2
    if (mid * (mid + 1)) // 2 <= s:
        max_n = max(max_n, mid)
        left = mid + 1
    else:
        right = mid - 1

print(max_n)