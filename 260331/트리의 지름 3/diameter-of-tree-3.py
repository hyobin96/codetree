node_count = int(input())
tree = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    u, v, w = map(int, input().split(" "))
    tree[u].append((v, w))
    tree[v].append((u, w))

def traverse(begin, tree):
    max_node, max_dist = begin, 0
    second_node, second_dist = begin, 0
    stack = [(begin, 0, 0)] # curr, dist, parent
    
    while stack:
        curr, dist, parent = stack.pop()
        
        if dist >= max_dist:
            max_dist, second_dist = dist, max_dist
            max_node, second_node = curr, max_node

        for nxt, w in tree[curr]:
            if nxt == parent:
                continue
            stack.append((nxt, dist + w, curr))

    return max_node, max_dist, second_node, second_dist

max_node, _, _, _ = traverse(1, tree)
max_node, _, _, second_dist1 = traverse(max_node, tree)
_, _, _, second_dist2 = traverse(max_node, tree)
print(max(second_dist1, second_dist2))