import sys
sys.setrecursionlimit(100_000)

node_count, oper_count = map(int, input().split())
parents = [0] + list(map(int, input().split()))
tree = [[] for _ in range(node_count + 1)]

for i in range(2, len(parents)):
    tree[parents[i]].append(i)

dp = [0] * (node_count + 1)
for _ in range(oper_count):
    curr, w = map(int, input().split())
    dp[curr] += w

def dfs(curr, prev, tree, dp):
    for nxt in tree[curr]:
        if nxt == prev:
            continue
        dp[nxt] += dp[curr]
        dfs(nxt, curr, tree, dp)

dfs(1, 0, tree, dp)
print(*dp[1 : ])