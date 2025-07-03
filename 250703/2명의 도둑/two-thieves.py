def get_price(i, j):
    l = arr[i][j:j+M]
    l.sort(reverse = True)
    
    _sum = 0
    total = 0
    for w in l:
        if _sum + w <= C:
            _sum += w
            total += w ** 2

    return total
    
N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N - M + 1):
        for k in range(i, N):
            for l in range(N - M + 1):
                if i == k and not (l >= j + M or j >= l + M):
                    continue

                v1 = get_price(i, j)
                v2 = get_price(k, l)

                ans = max(ans, v1 + v2)

print(ans)