node_count = int(input())

tree = [[] for _ in range(node_count + 1)]

for _ in range(node_count - 1):
    u, v, w = map(int, input().split(" "))
    tree[u].append((v, w))
    tree[v].append((u, w))

def update_dist(begin, dists, tree, visited):
    stack = [(begin, 0)]
    while stack:
        node, dist = stack.pop()
        for nxt_node, w in tree[node]:
            if visited[begin][nxt_node]:
                continue
            visited[begin][nxt_node] = 1
            dists[node][nxt_node] = dist + w
            stack.append((nxt_node, dist + w))
    

dists = [[0] * (node_count + 1) for _ in range(node_count + 1)]
visited = [[0] * (node_count + 1) for _ in range(node_count + 1)]
for i in range(1, node_count + 1):
    visited[i][i] = 1
    update_dist(i, dists, tree, visited)

max_dist = 0
for row in dists:
    max_dist = max(max_dist, max(row))

print(max_dist)