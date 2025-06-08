arr = list(map(int, input().split()))
n = len(arr)
_sum = sum(arr)
_min = 200000000
for i in range(n):
    for j in range(i+1, n):
        for k in range(j + 1, n):
            tmp = arr[i] + arr[j] + arr[k]
            s = abs(_sum - tmp)
            _min = min(_min, abs(s-tmp))
print(_min)