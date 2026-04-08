import sys
sys.setrecursionlimit(100_000)

node_count = int(input())
edges = [tuple(map(int, input().split())) for _ in range(node_count - 2)]
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

for a, b in edges:
    union(a, b)

root = find(1)
for i in range(2, node_count + 1):
    if find(i) != root:
        print(1, i)
        break