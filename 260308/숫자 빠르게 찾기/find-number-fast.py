import sys
input = sys.stdin.readline
n, m = map(int, input().split())

numbers = list(map(int, input().split()))

positions = []
for _ in range(m):
    target = int(input())
    index = -2
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if numbers[mid] == target:
            index = mid
            break
        if numbers[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    positions.append(index + 1)

for pos in positions:
    print(pos)