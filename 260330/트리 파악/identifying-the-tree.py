# leaf node의 모든 깊이? 홀수면 A 승리 짝수면 B 승리

node_count = int(input())
tree = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    u, v = map(int, input().split(" "))
    tree[u].append(v)
    tree[v].append(u)

def count_leaf_node(tree, root_node):
    stack = [root_node]
    visited = [0] * (len(tree) + 1)
    visited[root_node] = 1
    leaf_node_count = 0
    while stack:
        node = stack.pop()
        
        for nxt_node in list(tree[node]):
            tree[nxt_node].remove(node)
            if len(tree[nxt_node]) == 0:
                leaf_node_count += 1
            if visited[nxt_node]:
                continue
            visited[nxt_node] = 1
            stack.append(nxt_node)
        
    return leaf_node_count
    
leaf_node_count = count_leaf_node(tree, 1)
answer = int(leaf_node_count % 2 == 1)
print(answer)