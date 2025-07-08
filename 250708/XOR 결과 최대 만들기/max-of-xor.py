def xor(cnt, result, start):
    global answer, M
    if cnt == M:
        answer = max(answer, result)
        return

    for i in range(start, N):
        xor(cnt + 1, result ^ nums[i], i + 1)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
xor(0, 0, 0)
print(answer)