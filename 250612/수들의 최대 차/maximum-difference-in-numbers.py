N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

max_cnt = 1
for start in range(N):
    min_value = arr[start]
    cnt = 1
    for search_idx in range(start + 1, N):
        max_value = arr[search_idx]
        if max_value - min_value <= K:
            cnt += 1
        else:
            break
    max_cnt = max(max_cnt, cnt)

print(max_cnt)