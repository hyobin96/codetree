import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
sequence = list(map(int, input().split()))

element_map = defaultdict(int)
j = 0
max_length = 1
e = sequence[j]
element_map[e] += 1
for i in range(n):

    while j + 1 < n:
        e = sequence[j + 1]
        element_map[e] += 1
        if element_map[e] > k:
            element_map[e] -= 1
            break
        j += 1

    if element_map[sequence[j]] <= k:
        max_length = max(max_length, j - i + 1)
    
    e = sequence[i]
    element_map[e] -= 1

answer = max_length
print(answer)
    