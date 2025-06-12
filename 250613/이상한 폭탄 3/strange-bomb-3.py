N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
max_n = 1000000

save_arr = [[] for _ in range(max_n + 1)]
for i, v in enumerate(arr):
    save_arr[v].append(i)

max_cnt = 0
max_num = 0
for i, array in enumerate(save_arr):
    if array == []:
        continue
    
    cnt = 0
    for j in range(len(array) - 1):
        if array[j+1] - array[j] <= K:
            cnt += 1
    
    if cnt != 0:
        cnt += 1
    
    if max_cnt <= cnt:
        max_cnt = cnt
        max_num = i

print(max_num)
