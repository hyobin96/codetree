def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
def bomb(i, j, dist, t):
    for dr, dc in zip(drs, dcs):
        nr, nc = i + dist * dr, j + dist * dc
    
        if in_range(nr, nc) and arr[nr][nc] == 0:
            arr[nr][nc] = t

    
N, M, r, c = map(int, input().split())
r, c = r - 1, c - 1

arr = [[0] * N for _ in range(N)]

dist = 1
arr[r][c] = 1

for t in range(M):
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and arr[i][j] != t + 2:
                bomb(i, j, dist, t + 2)

    dist *= 2

answer = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            answer += 1

print(answer)