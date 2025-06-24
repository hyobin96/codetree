N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def is_manzok(i, j):
    for k in range(j, j + M):
        if arr[i][k] != arr[i][j]:
            return False

    return True

def is_manzok2(j, i):
    for k in range(i, i + M):
        if arr[i][j] != arr[k][j]:
            return False

    return True

cnt = 0
for i in range(N):
    for j in range(N - M + 1):
        if is_manzok(i, j):
            cnt += 1
            break

for j in range(N):
    for i in range(N - M + 1):
        if is_manzok2(j, i):
            cnt += 1
            break

print(cnt)

    