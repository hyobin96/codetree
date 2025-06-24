N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def is_range(r, c):
    return 0 <= r < N and 0 <= c < N

def get_cnt(i, j, k):
    r1, r2, c1, c2 = i - 1, i + 1, j - k + 1, j + k - 1
    cnt = 0
    
    for _ in range(k - 1):
        if is_range(r1, c1) and arr[r1][c1] == 1:
            cnt += 1
        
        if is_range(r1, c2) and arr[r1][c2] == 1:
            cnt += 1

        if is_range(r2, c1) and arr[r2][c1] == 1:
            cnt += 1

        if is_range(r2, c2) and arr[r2][c2] == 1:
            cnt += 1

        r1, r2, c1, c2 = r1 - 1, r2 + 1, c1 + 1, c2 - 1

    if k > 0:
        if is_range(i, j - k) and arr[i][j - k] == 1:
            cnt += 1

        if is_range(i, j + k) and arr[i][j + k] == 1:
            cnt += 1

        if is_range(i - k, j) and arr[i - k][j] == 1:
            cnt += 1

        if is_range(i + k, j) and arr[i + k][j] == 1:
            cnt += 1

    return cnt


def is_possible(cnt, k):
    return cnt * M >= (k ** 2 + (k + 1) ** 2)

max_cnt = 0
for i in range(N):
    for j in range(N):
        cnt = arr[i][j]
        if is_possible(cnt, 0):
            max_cnt = max(max_cnt, cnt)

        for k in range(1, N + 1):
            cnt += get_cnt(i, j, k)
            # print(cnt, k, i, j, arr[i][j])

            if is_possible(cnt, k):
                max_cnt = max(max_cnt, cnt)

        # print(cnt, i, j)


print(max_cnt)

        


            