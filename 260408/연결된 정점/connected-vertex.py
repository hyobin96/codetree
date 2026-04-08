import sys
sys.setrecursionlimit(100_000)

node_count, oper_count = map(int, input().split())
opers = [input().split() for _ in range(oper_count)]
linked_counts = [1] * (node_count + 1)
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
        linked_counts[b] += linked_counts[a]

for oper in opers:
    if oper[0] == 'x':
        a, b = int(oper[1]), int(oper[2])
        union(a, b)
    else:
        a = int(oper[1])
        a = find(a)
        print(linked_counts[a])
    
