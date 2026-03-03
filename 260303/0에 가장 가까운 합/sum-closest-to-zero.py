import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
sequence.sort()

abs_min = 2e10
i, j = 0, n - 1
while i < j:
    diff = sequence[i] + sequence[j]
    abs_min = min(abs_min, abs(diff))
    if abs_min == 0:
        break
    if abs_min > 0:
        j -= 1
    else:
        i += 1

answer = abs_min
print(answer)
