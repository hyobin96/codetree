import sys
sys.setrecursionlimit(10_000)

node_count = int(input())
tree = [[] for _ in range(node_count + 1)]
parents = [0] * (node_count + 1)
nodes = set(range(1, node_count + 1))
for _ in range(node_count - 1):
    p, c = map(int, input().split())
    tree[p].append(c)
    parents[c] = p
    nodes.remove(c)

root = 0
for node in nodes:
    root = node

depth = [0] * (node_count + 1)
def dfs(curr, tree, depth):
    for nxt in tree[curr]:
        depth[nxt] = depth[curr] + 1
        dfs(nxt, tree, depth)

dfs(root, tree, depth)

node1, node2 = map(int, input().split())

while depth[node1] != depth[node2]:
    if depth[node1] > depth[node2]:
        node1 = parents[node1]
    else:
        node2 = parents[node2]

while node1 != node2:
    node1 = parents[node1]
    node2 = parents[node2]

print(node1)