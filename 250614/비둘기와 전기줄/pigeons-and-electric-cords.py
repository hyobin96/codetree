N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]

count_arr = [2] * 11

cnt = 0
for idx, pos in arr:
    value = count_arr[idx]
    
    if value == 2:
        count_arr[idx] = pos
    
    elif value != pos:
        count_arr[idx] = pos
        cnt += 1

print(cnt)

             