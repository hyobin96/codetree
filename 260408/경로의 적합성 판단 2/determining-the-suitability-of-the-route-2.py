import sys
input = sys.stdin.readline

node_count, edge_count, k = map(int, input().split())

uf = [i for i in range(node_count + 1)]
def find(a):
    while a != uf[a]:
        uf[a] = uf[uf[a]]
        a = uf[a]
    return a

def union(a, b):
    global uf
    a = find(a)
    b = find(b)
    if a != b:
        uf[a] = b

for _ in range(edge_count):
    u, v = map(int, input().split())
    union(u, v)

orders = list(map(int, input().split()))
parent = find(orders[0])
is_possible = True
for order in orders:
    if parent != find(order):
        is_possible = False
        break

print(int(is_possible))