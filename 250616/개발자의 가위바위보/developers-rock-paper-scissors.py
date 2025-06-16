N = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N):
    i, j = map(int, input().split())
    if i == j:
        continue

    arr[i][j] += 1


max_count = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        
        cnt = arr[i][j] + arr[j][6 - (i + j)]
        max_count = max(max_count, cnt)

print(max_count)

        