import sys
sys.setrecursionlimit(100_000)

node_count, root = map(int, input().split())
tree = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def search_central(curr, prev, tree):
    child_count = 0
    for nxt in tree[curr]:
        if nxt == prev:
            continue
        child_count += 1

    if child_count >= 2:
        return curr
    
    for nxt in tree[curr]:
        if nxt == prev:
            continue
        return search_central(nxt, curr, tree)
    
    return curr

central = search_central(root, 0, tree)

dp = [0] * (node_count + 1)

def count_nodes(curr, prev, tree, dp):
    dp[curr] = 1
    for nxt in tree[curr]:
        if nxt == prev:
            continue
        count_nodes(nxt, curr, tree, dp)
        dp[curr] += dp[nxt]

count_nodes(central, 0, tree, dp)

max_size, min_size = 0, 100_000
for subtree in tree[central]:
    max_size = max(max_size, dp[subtree])
    min_size = min(min_size, dp[subtree])

print(max_size - min_size)