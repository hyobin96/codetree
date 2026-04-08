import sys
sys.setrecursionlimit(10_000)

node_count, edge_count = map(int, input().split())
node_types = [0] + input().split()
edges = [tuple(map(int, input().split())) for _ in range(edge_count)]
edges.sort(lambda x: x[2])
uf = [i for i in range(node_count + 1)]

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
    if node_types[a] == node_types[b]:
        continue

    a, b = find(a), find(b)
    if a != b:
        union(a, b)
        cost += w

root = find(1)
is_possible = True
for i in range(2, node_count + 1):
    if find(i) != root:
        is_possible = False
        break

if is_possible:
    print(cost)
else:
    print(-1)