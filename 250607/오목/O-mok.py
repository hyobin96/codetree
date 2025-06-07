arr = [list(map(int, input().split())) for _ in range(19)]

drs, dcs = [1, 1, 1, 0], [-1, 0, 1, 1]

def is_range(nr, nc):
    return 0 <= nr < 19 and 0 <= nc < 19

def is_win(i, j, color):
    for dr, dc in zip(drs, dcs):
        r, c = i, j
        cnt = 1
        for _ in range(6):
            r, c = r + dr, c + dc
            if not is_range(r, c) or arr[r][c] != color:
                break
            cnt += 1
        if cnt == 5:
            return color, i + 2 * dr + 1, j + 2 * dc + 1
    return 0, 0, 0

def simul():
    for i in range(19):
        for j in range(19):
            color, r, c = is_win(i, j, arr[i][j])
            if color != 0:
                return color, r, c
    return 0

ans = simul()
if ans == 0:
    print(0)
else:
    print(ans[0])
    print(ans[1], ans[2])