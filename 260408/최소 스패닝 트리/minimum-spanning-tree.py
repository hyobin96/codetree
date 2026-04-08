import sys
sys.setrecursionlimit(10_000)

node_count, edge_count = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(edge_count)]
uf = [i for i in range(node_count + 1)]

edges.sort(lambda x: x[2])

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
for u, v, w in edges:
    u = find(u)
    v = find(v)

    if u != v:
        cost += w
        union(u, v)

print(cost)