node_count, root, query_count = map(int, input().split())
tree = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [0] * (node_count + 1)

def dfs(curr, prev, tree, dp):
    dp[curr] = 1
    for nxt in tree[curr]:
        if nxt == prev:
            continue
        dfs(nxt, curr, tree, dp)
        dp[curr] += dp[nxt]

dfs(root, 0, tree, dp)

for _ in range(query_count):
    target = int(input())
    print(dp[target])