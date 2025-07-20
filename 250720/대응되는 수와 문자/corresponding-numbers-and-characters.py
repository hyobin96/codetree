N, M = map(int, input().split())
strings = [input() for _ in range(N)]
querys = [input() for _ in range(M)]

s_d, z_d = {}, {}

for i, s in enumerate(strings):
    s_d[s] = i + 1
    z_d[i + 1] = s

for q in querys:
    if q.isalpha():
        print(s_d[q])
    else:
        print(z_d[int(q)])
