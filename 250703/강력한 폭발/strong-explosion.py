def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def bomb(r, c):
    global area

    d = arr[r][c] - 1

    for dr, dc in zip(drs[d], dcs[d]):
        nr, nc = r + dr, c + dc

        if in_range(nr, nc):
            count[nr][nc] += 1
            if count[nr][nc] == 1:
                area += 1

def reset(r, c):
    global area

    d = arr[r][c] - 1

    for dr, dc in zip(drs[d], dcs[d]):
        nr, nc = r + dr, c + dc

        if in_range(nr, nc):
            count[nr][nc] -= 1
            if count[nr][nc] == 0:
                area -= 1

def select_bomb(cnt):
    global arr, pos, max_area

    if cnt == len(pos):
        max_area = max(max_area, area)
        return

    for i in range(1, 4):
        r, c = pos[cnt]
        arr[r][c] = i
        bomb(r, c) # arr[r][c] 에 놓여진 폭탄을 터뜨리기
        select_bomb(cnt + 1)
        reset(r, c) # count[r][c] 에 계산된 폭탄 개수 -1 하기 area 빼주기


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

pos = []

count = [[0 for _ in range(N)] for _ in range(N)]

max_area, area = 0, 0

drs = [[0, -1, -2, 1, 2], [0, -1, 1, 0, 0], [0, -1, -1, 1, 1]]
dcs = [[0, 0, 0, 0, 0], [0, 0, 0, -1, 1], [0, -1, 1, 1, -1]]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            pos.append([i, j])

select_bomb(0)

print(max_area)

