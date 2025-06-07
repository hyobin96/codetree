n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

_max = 0
for i in range(n):
    for j in range(n):
        for k in range(n - 2):
            if i == j:
                for l in range(k + 3, n-2):
                    _max = max(_max, sum(arr[i][k:k+3]) + sum(arr[j][l:l+3]))
            else:
                for l in range(n-2):
                    _max = max(_max, sum(arr[i][k:k+3]) + sum(arr[j][l:l+3]))
print(_max)