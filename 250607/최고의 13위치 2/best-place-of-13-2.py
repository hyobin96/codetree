n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

_max = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(n - 2):
            for l in range(n-2):
                _max = max(_max, sum(arr[i][k:k+3]) + sum(arr[j][l:l+3]))
print(_max)