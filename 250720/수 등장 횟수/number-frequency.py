N, M = map(int, input().split())
elements = list(map(int, input().split()))
querys = list(map(int, input().split()))

d = {}
for e in elements:
    if e in d:
        d[e] += 1
    else:
        d[e] = 1

answer = []
for q in querys:
    answer.append(d[q] if q in d else 0)

print(*answer)