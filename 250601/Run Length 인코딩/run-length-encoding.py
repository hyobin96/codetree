A = input()
res = []
i = 0
while i < len(A):
    res.append(A[i])
    cnt = 1
    for j in range(i+1, len(A)):
        if A[i] != A[j]:
            break
        cnt += 1
    i += cnt
    res.append(str(cnt))

res = ''.join(res)
print(len(res))
print(res)