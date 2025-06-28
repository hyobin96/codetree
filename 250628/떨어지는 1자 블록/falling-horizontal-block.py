N, M, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def is_exist(i):
    for j in range(K - 1, K + M - 1):
        if arr[i][j] == 1:
            return True

    return False

r = 0
for i in range(1, N):
    if is_exist(i):
        r = i - 1
        break

for j in range(K - 1, K + M):
    arr[r][j] = 1

for i in range(N):
    print(*arr[i])        
