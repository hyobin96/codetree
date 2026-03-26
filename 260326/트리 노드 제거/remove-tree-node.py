node_count = int(input())
tree = [[] for _ in range(node_count)]
parents = list(map(int, input().split(" ")))
for i, p in enumerate(parents):
    if p == -1:
        continue
    tree[p].append(i)

def count_leaf_node(parent, tree):
    stack = [parent]
    leaf_node_count = 0
    while stack:
        p = stack.pop()
        if len(tree[p]) == 0:
            leaf_node_count += 1
            continue

        for child in tree[p]:
            stack.append(child)
    
    return leaf_node_count

target_removed = int(input())
if target_removed == 0:
    print(0)
else:
    tree[parents[target_removed]].remove(target_removed)
    leaf_node_count = count_leaf_node(0, tree)
    print(leaf_node_count)
