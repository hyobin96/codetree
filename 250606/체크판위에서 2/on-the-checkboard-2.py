R, C = map(int, input().split())
arr = [input().split() for _ in range(R)]

r, c = 0, 0

def search(r, c, curr, cnt):
    ans = 0
    if cnt >= 3:
        if r == R-1 and c == C-1:
            return 1
        return 0
    for i in range(r + 1, R):
        for j in range(c + 1, C):
            if arr[i][j] != curr:
                ans += search(i, j, arr[i][j], cnt + 1)
    return ans

ans = search(r, c, arr[r][c], 0)
print(ans)