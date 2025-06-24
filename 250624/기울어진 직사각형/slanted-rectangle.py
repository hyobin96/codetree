N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def get_sum(i, j, d_13, d_24):
    r, c = i, j
    _sum = 0

    for d in range(4):
        if d == 0 or d == 2:
            for _ in range(d_13):
                nr, nc = r + dr[d], c + dc[d]
                if not in_range(nr, nc):
                    return 0

                _sum += arr[nr][nc]
                r, c = nr, nc
        else:
            for _ in range(d_24):
                nr, nc = r + dr[d], c + dc[d]
                if not in_range(nr, nc):
                    return 0

                _sum += arr[nr][nc]
                r, c = nr, nc
        
    return _sum

dr, dc = (-1, -1, 1, 1), (1, -1, -1, 1)

answer = 0
for i in range(N):
    for j in range(N):
        for d_13 in range(1, N):
            for d_24 in range(1, N):
                answer = max(answer, get_sum(i, j, d_13, d_24))

print(answer)
