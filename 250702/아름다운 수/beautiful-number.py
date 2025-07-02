def is_beautiful():
    prev = l[0]
    _sum = prev
    for i in range(1, N):
        if l[i] == prev:
            _sum += l[i]

        else:
            if prev != 1 and _sum // prev != prev:
                return False

            prev = l[i]
            _sum = l[i]

    if prev != 1 and _sum // prev != prev:
        return False

    return True

def dupli_perm(cnt):
    global answer
    if cnt == N:
        if is_beautiful():
            answer += 1
        return

    for i in range(1, N + 1):
        l.append(i)
        dupli_perm(cnt + 1)
        l.pop()
        


N = int(input())
count_arr = [0] * (N + 1)
l = []
answer = 0

dupli_perm(0)
print(answer)