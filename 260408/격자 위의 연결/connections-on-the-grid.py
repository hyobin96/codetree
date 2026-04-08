row, col = map(int, input().split())
edges = []
for i in range(1, row + 1):
    weights = [0] + list(map(int, input().split()))
    for j in range(1, col):
        edges.append((col * (i - 1) + j, col * (i - 1) + j + 1, weights[j]))

for i in range(1, row):
    weights = [0] + list(map(int, input().split()))
    for j in range(1, col + 1):
        edges.append((col * (i - 1) + j, col * i + j, weights[j]))

edges.sort(lambda x: x[2])    

uf = [i for i in range(row * col + 1)]

def find(a):
    if a == uf[a]:
        return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        uf[a] = b

cost = 0
for a, b, w in edges:
    a, b = find(a), find(b)
    if a != b:
        union(a, b)
        cost += w

print(cost)