k, n = map(int, input().split())
ranks = []
for _ in range(k):
    arr = [0] * (n+1)
    _input = tuple(map(int, input().split()))
    for r, i in enumerate(_input):
        arr[i] = r + 1
    ranks.append(arr)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        is_always = True
        if i == j:
            continue
        for e in ranks:
            if e[i] > e[j]:
                is_always = False
                break
        if is_always:
            cnt += 1
print(cnt)