n, m = map(int, input().split())
arr = list(map(int, input().split()))

curr = 0
cnt = 0

while curr < n:
    if arr[curr] == 1:
        for i in range(curr + 1, curr + m + 1 if curr + m + 1 < n else n):
            if arr[i] == 1:
                curr = i

        cnt += 1
        curr += m + 1

    else:
        curr += 1

print(cnt)
