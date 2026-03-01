import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sequence = [int(input()) for _ in range(n)]
sequence.sort()

count = 0
j = n - 1
for i in range(n - 1):

    while j - 1 > i and sequence[i] + sequence[j] > k:
        j -= 1
    
    if sequence[i] + sequence[j] <= k:
        count += j - i

answer = count
print(answer)
