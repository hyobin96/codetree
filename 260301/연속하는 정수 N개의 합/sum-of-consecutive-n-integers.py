import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sequence = list(map(int, input().split()))

j = 0
count = 0
total = sequence[0]
for i in range(n):
    while total <= m and j < n:
        if total == m:
            count += 1
        j += 1
        if j == n:
            break
        total += sequence[j]
    total -= sequence[i]

answer = count
print(answer)