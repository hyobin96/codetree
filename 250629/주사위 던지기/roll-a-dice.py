drs, dcs = [-1, 0, 1, 0], [0, -1, 0, 1]

mapper = {'U': 0, 'L': 1, 'D':2, 'R':3}

dice = [5, 4, 2, 3]

N, M, r, c = map(int, input().split())
r, c = r - 1, c - 1

query = input().split()


def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


curr = 6
arr = [[0] * N for _ in range(N)]
arr[r][c] = curr

for q in query:
    d = mapper[q]

    nr, nc = r + drs[d], c + dcs[d]

    if not in_range(nr, nc):
        continue

    dice[d], dice[(d + 2) % 4], curr = 7 - curr, curr, dice[d]
    r, c = nr, nc
    arr[r][c] = curr

answer = 0

for i in range(N):
    answer += sum(arr[i])

print(answer)
    