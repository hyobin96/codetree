def duplicate_perm(cnt):
    if cnt == N:
        print(*l)
        return

    for i in range(1, K + 1):
        l.append(i)
        duplicate_perm(cnt + 1)
        l.pop()

K, N = map(int, input().split())

l = []

duplicate_perm(0)

