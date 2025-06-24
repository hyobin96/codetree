N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

def get_sum(i, j):
    _sum = 0
    for r in range(i, i+3):
        _sum += sum(arr[r][j : j + 3])

    return _sum

_max = 0
for i in range(N - 2):
    for j in range(N - 2): 
        _max = max(_max, get_sum(i, j))

print(_max)