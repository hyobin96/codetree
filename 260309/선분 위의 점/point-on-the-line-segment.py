# lower, upper bound
# 1 2 3  , 0, 3  -> 0 2, 2 - 0 + 1
# lower가 끝이라면? 1 2 3 / 4 5 / 3 
import sys
input = sys.stdin.readline

def lower_bound(target):
    l, r = 0, n - 1
    min_idx = 2e9
    while l <= r:
        mid = (l + r) // 2
        if sequence[mid] >= target:
            min_idx = min(min_idx, mid)
            r = mid - 1
        else:
            l = mid + 1
    return min_idx if min_idx != 2e9 else -1

def upper_bound(target):
    l, r = 0, n - 1
    max_idx = -1
    while l <= r:
        mid = (l + r) // 2
        if sequence[mid] <= target:
            max_idx = max(max_idx, mid)
            l = mid + 1
        else:
            r = mid - 1

    return max_idx

n, m = map(int, input().split())
sequence = sorted(list(map(int, input().split())))

for _ in range(m):
    x1, x2 = map(int, input().split())
    
    l, r = lower_bound(x1), upper_bound(x2)
    # print(l, r)
    if l == -1 or r == -1:
        print(0)
        continue
    print(r - l + 1)