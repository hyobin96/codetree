def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def go(cnt, r, c):
    global answer

    d = d_arr[r][c]
    nr, nc = r + drs[d], c + dcs[d]
    while in_range(nr, nc):
        if in_range(nr, nc) and arr[nr][nc] > arr[r][c]:
            go(cnt + 1, nr, nc)

        nr, nc = nr + drs[d], nc + dcs[d]

    answer = max(answer, cnt)


drs, dcs = (0, -1, -1, 0, 1, 1, 1, 0, -1), (0, 0, 1, 1, 1, 0, -1, -1, -1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d_arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

r, c = map(int, input().split())
go(0, r - 1, c - 1)

print(answer)