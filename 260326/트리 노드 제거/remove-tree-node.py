node_count = int(input())
tree = [[] for _ in range(node_count)]
parents = list(map(int, input().split(" ")))
root = 0
for i, p in enumerate(parents):
    if p == -1:
        root = i
        continue
    tree[p].append(i)

def count_leaf_node(root, tree, deleted_node):
    if root == deleted_node:
        return 0
    stack = [root]
    leaf_node_count = 0
    while stack:
        p = stack.pop()
        is_leaf_node = True
        for child in tree[p]:
            if child == deleted_node:
                continue
            stack.append(child)
            is_leaf_node = False
        
        leaf_node_count += int(is_leaf_node)
    
    return leaf_node_count

target_removed = int(input())
leaf_node_count = count_leaf_node(root, tree, target_removed)
print(leaf_node_count)
