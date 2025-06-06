n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
_max = 0
for i in range(n):
    for j in range(n - 2):
        _max = max(_max, sum(arr[i][j:j+3]))
print(_max)