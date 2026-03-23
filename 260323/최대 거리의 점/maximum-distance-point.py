n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

# Please write your code here.
# 2e5 * log1e9
# target 값보다 거리가 작으면 다음 좌표로 건너가기
# 같거나 크면 꽂기
# 항상 맨 앞과 맨 뒤에는 꽂는 게 좋다
# 그 중 최솟값이 mid이상이면 만족

def is_possible(target_gap, arr):
    i, j = 0, 1
    cnt = m - 1
    while j < n and cnt > 0:
        gap = arr[j] - arr[i]
        if gap >= target_gap:
            cnt -= 1
            i, j = j, j + 1
            continue
        j += 1
    return False if cnt else True

max_gap = 0
left, right = 1, max(arr)
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid, arr):
        max_gap = max(max_gap, mid)
        left = mid + 1
    else:
        right = mid - 1

print(max_gap)
    