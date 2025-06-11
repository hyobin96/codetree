n = int(input())
arr = list(map(int, input().split()))
_min = 2000000000

for i in range(n):
    arr[i] *= 2
    for j in range(n):
        diff_sum = 0
        remain_arr = [e for k, e in enumerate(arr) if j != k]
        for k in range(n-2):
            diff_sum += abs(remain_arr[k] - remain_arr[k+1])
        _min = min(_min, diff_sum)
    arr[i] //= 2
print(_min) 