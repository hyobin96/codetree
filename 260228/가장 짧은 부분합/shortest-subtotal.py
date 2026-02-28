import sys
input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))

l, r = 0, 0
length = 2e9
total = sequence[0]
while l <= r:
    if total < s:
        r += 1
        if r >= n:
            break
        total += sequence[r]
    else:
        length = min(length, r - l + 1)
        total -= sequence[l]
        l += 1

print(length if length != 2e9 else -1)