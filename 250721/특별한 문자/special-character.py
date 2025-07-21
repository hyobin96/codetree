alphas = input()
d = dict()
for a in alphas:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

answer = 'None'
for a in alphas:
    if a in d and d[a] == 1:
        answer = a
        break
print(answer)