n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
def is_possible(k, m, arr):
    cnt = 0
    for num in arr:
        cnt += num // k
    return cnt >= m

max_k = 0
left, right = 0, max(arr)
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid, m, arr):
        max_k = max(max_k, mid)
        left = mid + 1
    else:
        right = mid - 1

print(max_k)