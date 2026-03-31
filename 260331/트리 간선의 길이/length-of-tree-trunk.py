node_count = int(input())

tree = [[] for _ in range(node_count + 1)]

for _ in range(node_count - 1):
    u, v, w = map(int, input().split(" "))
    tree[u].append((v, w))
    tree[v].append((u, w))

def farthest(begin, tree):
    visited = [0] * (len(tree) + 1)
    visited[begin] = 1
    max_dist, max_node = 0, begin
    stack = [(begin, 0)]
    while stack:
        node, dist = stack.pop()
        if dist > max_dist:
            max_dist = dist
            max_node = node

        for nxt_node, w in tree[node]:
            if visited[nxt_node]:
                continue
            visited[nxt_node] = 1
            stack.append((nxt_node, dist + w))

    return max_dist, max_node
    
    
_, node_1 = farthest(1, tree)
max_dist, _ = farthest(node_1, tree)

print(max_dist)
