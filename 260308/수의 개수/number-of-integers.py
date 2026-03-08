import sys

from collections import defaultdict

n, m = map(int, input().split())

sequence = list(map(int, input().split()))
count_map = defaultdict(int)
for num in sequence:
    count_map[num] += 1

for _ in range(m):
    target = int(input())
    print(count_map[target])

