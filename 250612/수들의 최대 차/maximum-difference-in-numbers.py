N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

max_cnt = 0
for start in range(N):
    min_value = arr[start]
    for search_idx in range(start, N):
        max_value = arr[search_idx]
        if max_value - min_value > K:
            cnt = search_idx - start
            max_cnt = max(max_cnt, cnt)

print(max_cnt)