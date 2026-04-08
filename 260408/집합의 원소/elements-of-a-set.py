number_count, oper_count = map(int, input().split())
querys = [tuple(map(int, input().split())) for _ in range(oper_count)]

uf = [0] + [i for i in range(1, number_count + 1)]

def find(a, uf):
    if a == uf[a]:
        return a
    uf[a] = find(uf[a], uf)
    return uf[a]

def union(a, b, uf):
    a = find(a, uf)
    b = find(b, uf)
    uf[a] = b

for oper, a, b in querys:
    if oper == 0:
        union(a, b, uf)
    else:
        if find(a, uf) == find(b, uf):
            print(1)
        else:
            print(0)

    