

n, m = map(int, input().split())
sequence = list(map(int, input().split()))

def lower_bound(target):
    l, r = 0, n - 1
    min_idx = 2e9
    while l <= r:
        mid = (l + r) // 2
        if sequence[mid] >= target:
            if sequence[mid] == target:
                min_idx = min(min_idx, mid)
            r = mid - 1
        else:
            l = mid + 1

    return min_idx + 1 if min_idx != 2e9 else -1

targets = list(map(int, input().split()))
for target in targets:
    print(lower_bound(target))