def is_beautiful():
    i = 0
    while i < N:
        num = l[i]
        for j in range(i, i + num):
            if j == N or l[j] != num:
                return False

        i = i + num

    return True
            

def dupli_perm(cnt):
    global answer
    if cnt == N:
        if is_beautiful():
            answer += 1
        return

    for i in range(1, 5):
        l.append(i)
        dupli_perm(cnt + 1)
        l.pop()
        

N = int(input())
l = []
answer = 0

dupli_perm(0)
print(answer)