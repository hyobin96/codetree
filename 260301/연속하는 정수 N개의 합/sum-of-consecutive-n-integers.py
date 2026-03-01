import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sequence = list(map(int, input().split()))

j = 0
count = 0
total = sequence[0]
for i in range(n):
    while total < m and j + 1 < n:
        j += 1
        total += sequence[j]
    
    if total == m:
        count += 1

    total -= sequence[i]

answer = count
print(answer)