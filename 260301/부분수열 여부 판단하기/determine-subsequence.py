import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sequence = list(map(int, input().split()))
subsequence = list(map(int, input().split()))

j = 0
for i in range(n):
    if sequence[i] == subsequence[j]:
        j += 1
    
    if j == m:
        break

answer = "Yes" if j == m else "No"

print(answer)