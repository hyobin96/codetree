import sys
input = sys.stdin.readline

n, k = map(int, input().split())

baskets = [0] * (1_000_001)

for _ in range(n):
    cnt, pos = map(int, input().split())
    baskets[pos] += cnt

l, r = 0, 2 * k
count = sum(baskets[l : r + 1])
max_count = count

while r + 1 < 1_000_001 :
    r += 1
    count += baskets[r] - baskets[l]
    l += 1
    max_count = max(max_count, count)

answer = max_count
print(answer)

