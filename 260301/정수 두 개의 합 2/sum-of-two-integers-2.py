import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sequence = [int(input()) for _ in range(n)]
sequence.sort()

count = 0
j = 1
for i in range(n - 1):

    while sequence[i] + sequence[j] <= k:
        j += 1
    
    count += j - i - 1

answer = count
print(answer)
