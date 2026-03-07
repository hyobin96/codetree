# k보다 적으면 j++, 많으면 i--
import sys
input = sys.stdin.readline
INF = 2e9

n, k = map(int, input().split())
sequence = list(map(int, input().split()))

j = 0
cnt = int(sequence[j] == 1)
min_length = INF

for i in range(n):
    
    while j + 1 < n and cnt < k:
        cnt += int(sequence[j + 1] == 1)
        j += 1

    if cnt >= k:
        min_length = min(min_length, j - i + 1)

    cnt -= int(sequence[i] == 1)

answer = min_length if min_length != INF else -1 
print(answer)