import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
count_arr = [0] * (100_001)

count_arr[sequence[0]] = 1
l, r = 0, 0
max_size = 1
while l <= r:
    if count_arr[sequence[l]] == 1 and count_arr[sequence[r]] == 1:
        max_size = max(max_size, r - l + 1)
        r += 1
        if r >= n:
            break
        count_arr[sequence[r]] += 1
    else:
        count_arr[sequence[l]] -= 1
        l += 1

answer = max_size
print(answer)