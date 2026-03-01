import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sequence = [int(input()) for _ in range(n)]
sequence.sort()

total = 0
count = 0
for i in range(n - 1):
    j = i + 1
    total = sequence[i] + sequence[j]    
    while j < n and total <= k:
        count += 1
        j += 1
        total = sequence[i] + sequence[j]

answer = count
print(answer)
