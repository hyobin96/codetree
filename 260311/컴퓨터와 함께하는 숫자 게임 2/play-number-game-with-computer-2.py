m = int(input())
a, b = map(int, input().split())

# Please write your code here.

def binary_search(target):
    l, r = 1, m
    count = 0
    while l <= r:
        count += 1
        mid = (l + r) // 2
        if target == mid:
            break
        if target > mid:
            l = mid + 1
        else:
            r = mid - 1
    return count

min_cnt, max_cnt = 2e9, 0
for init in range(a, b + 1):
    count = binary_search(init)
    min_cnt = min(min_cnt, count)
    max_cnt = max(max_cnt, count)

print(min_cnt, max_cnt)