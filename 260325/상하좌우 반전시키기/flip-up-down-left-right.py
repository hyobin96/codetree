n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def logging():
    for i in range(n):
        print(arr[i])
    print()

in_range = lambda r, c: 0 <= r < n and 0 <= c < n
drs, dcs = (0, -1, 1, 0), (-1, 0, 0, 1)
cnt = 0
for i in range(1, n):
    for j in range(n):
        is_zero_exist = False
        d = 1
        nr, nc = i + drs[d], j + dcs[d]
        if in_range(nr, nc) and arr[nr][nc] == 0:
            is_zero_exist = True
        if is_zero_exist:
            for dr, dc in zip(drs, dcs):
                nr, nc = i + dr, j + dc
                if in_range(nr, nc):
                    arr[nr][nc] ^= 1
            arr[i][j] ^= 1
            cnt += 1
        # logging()


for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            cnt = -1
            break

print(cnt)