import math

node_count = int(input())
tree = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    u, v = map(int, input().split(" "))
    tree[u].append(v)
    tree[v].append(u)


def farthest(begin, tree):
    stack = [(begin, 0, 0)] # curr, dist, parent
    max_node, max_dist = begin, 0
    while stack:
        curr, dist, parent = stack.pop()
        
        if dist > max_dist:
            max_dist = dist
            max_node = curr
        
        for nxt in tree[curr]:
            if nxt == parent:
                continue
            stack.append((nxt, dist + 1, curr))
    
    return max_node, max_dist

max_node, _ = farthest(1, tree)
_, max_dist = farthest(max_node, tree)
print(math.ceil(max_dist / 2))


