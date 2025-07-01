def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def simul(n):
    r, c = pos[n]

    i, j = 0, 0
    _max = 0
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if not in_range(nr, nc) or not arr[nr][nc]:
            continue

        if _max < max(arr[nr][nc]):
            _max = max(arr[nr][nc])
            i, j = nr, nc

    if _max == 0:
        return
    
    idx = arr[r][c].index(n)

    arr[r][c], arr[i][j] = arr[r][c][idx + 1:], arr[r][c][:idx + 1] + arr[i][j]
    
    for num in arr[i][j]:
        pos[num] = [i, j]


N, M = map(int, input().split())

arr = [[[] for _ in range(N)] for _ in range(N)]
inputs = [list(map(int, input().split())) for _ in range(N)]    
pos = [0] * (N ** 2 + 1)

drs, dcs = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, 1, -1]

for i in range(N):
    for j in range(N):
        arr[i][j].append(inputs[i][j])
        pos[inputs[i][j]] = [i, j]

nums = list(map(int, input().split()))

for n in nums:
    simul(n)

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            print(*arr[i][j])
        
        else:
            print('None')
                