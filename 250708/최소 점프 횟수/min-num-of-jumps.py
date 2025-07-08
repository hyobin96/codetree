def go(pos, cnt):
    global dists, answer
    if pos >= N - 1:
        if pos == N - 1:
            answer = min(answer, cnt)
        return

    for dist in range(1, dists[pos] + 1):
        go(pos + dist, cnt + 1)


N = int(input())
dists = list(map(int, input().split()))
answer = 100
go(0, 0)
print(answer if answer != 100 else - 1)