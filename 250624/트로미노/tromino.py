N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def get_rect(i, j):
    area = 0
    for k in range(i, i + 2):
        area += sum(arr[k][j : j + 2])

    return max(area - arr[i][j], area - arr[i][j + 1], area - arr[i + 1][j], area - arr[i + 1][j + 1])


_max = 0

for i in range(N - 1):
    for j in range(M - 1):
        area = get_rect(i, j)

        _max = max(area, _max)

for i in range(N):
    area = sum(arr[i][:3])
    _max = max(area, _max)
    
    for j in range(1, M - 2):
        area += -arr[i][j - 1] + arr[i][j + 2]    
        _max = max(area, _max)

for j in range(M):
    area = arr[0][j] + arr[1][j] + arr[2][j]
    _max = max(area, _max)
    
    for i in range(1, N - 2):
        area += -arr[i - 1][j] + arr[i + 2][j]
        _max = max(area, _max)

print(_max)

        