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
    while sequence[i] + sequence[j] <= k:
        count += 1
        j += 1
        if j == n:
            break

answer = count
print(answer)
