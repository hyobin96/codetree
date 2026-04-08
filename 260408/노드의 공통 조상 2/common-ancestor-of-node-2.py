import sys, math
sys.setrecursionlimit(50_000)

node_count = int(input())
MAX_H = int(math.log(node_count, 2)) + 1
tree = [[] for _ in range(node_count + 1)]
parents = [[0] * (node_count + 1) for _ in range(MAX_H + 1)]

for _ in range(node_count - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

depths = [0] * (node_count + 1)

def dfs(curr, prev, tree, parents, depths):
    for nxt in tree[curr]:
        if nxt == prev:
            continue
        depths[nxt] = depths[curr] + 1
        parents[0][nxt] = curr
        dfs(nxt, curr, tree, parents, depths)

dfs(1, 0, tree, parents, depths)

for h in range(1, MAX_H + 1):
    for i in range(1, node_count + 1):
        parents[h][i] = parents[h - 1][parents[h - 1][i]]

# for row in parents: 
#     print(row)

# print(f"depths: {depths}")
query_count = int(input())
for _ in range(query_count):
    node1, node2 = map(int, input().split())

    if depths[node1] < depths[node2]:
        node1, node2 = node2, node1

    for h in range(MAX_H, -1, -1):
        if depths[node1] - depths[node2] >= (1 << h):
            node1 = parents[h][node1] 

    if node1 == node2:
        print(node1)
        continue

    for h in range(MAX_H, -1, -1):
        if parents[h][node1] != parents[h][node2]:
            node1 = parents[h][node1]
            node2 = parents[h][node2]

    print(parents[0][node1])
                    