n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]


cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            count_arr = [0] * (101)
            is_ok = True
            for l, (a, b) in enumerate(arr):
                if l in (i, j, k):
                    continue
                for m in range(a, b+1):
                    if count_arr[m] == 1:
                        is_ok = False
                        break
                    count_arr[m] = 1
                if not is_ok:
                    break
            if is_ok:
                cnt += 1
print(cnt)