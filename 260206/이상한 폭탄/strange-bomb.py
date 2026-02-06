import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

# (number, idx)
numbers = []
for i in range(1, n + 1):
    number = int(input())
    numbers.append((number, i))

numbers.sort()

answer = -1
prev_n, prev_idx = numbers[0]
for i in range(1, n):
    curr_n, curr_idx = numbers[i]
    if prev_n == curr_n and curr_idx - prev_idx <= k:
        answer = max(answer, curr_n)
    prev_n, prev_idx = curr_n, curr_idx

print(answer)