N = int(input())
a = list(map(int, input().split()))
a.sort()
count_arr = [0] * 101
for num in a:
    count_arr[num] = 1

_max = 0
for k in range(a[-1]):
    cnt = 0
    for num in a:
        if num >= k:
            break
        diff = k - num
        if count_arr[num+diff] == 1:
            cnt += 1
    _max = max(_max, cnt)
print(_max)