import sys
sys.setrecursionlimit(100_000)

node_count, start, dist = map(int, input().split())
tree = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [0] * (node_count + 1)

def dfs(curr, prev, tree, dp):
    for nxt in tree[curr]:
        if nxt == prev:
            continue
        dfs(nxt, curr, tree, dp)
        dp[curr] = max(dp[curr], dp[nxt] + 1)


dfs(start, 0, tree, dp)

total_dist = 0
for i in range(1, node_count + 1):
    if i == start:
        continue
    if dp[i] >= dist:
        total_dist += 2

print(total_dist)