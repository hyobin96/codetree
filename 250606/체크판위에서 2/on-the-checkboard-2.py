R, C = map(int, input().split())
arr = [input().split() for _ in range(R)]

r, c = 0, 0

def search(r, c, curr, cnt):
    global total
    if cnt >= 3:
        if r == R-1 and c == C-1:
            total += 1
        return
    for i in range(r + 1, R):
        for j in range(c + 1, C):
            if arr[i][j] != curr:
                search(i, j, arr[i][j], cnt + 1)

total = 0
search(r, c, arr[r][c], 0)
print(total)