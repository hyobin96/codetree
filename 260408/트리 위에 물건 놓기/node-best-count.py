import sys
sys.setrecursionlimit(100_000)

node_count = int(input())
tree = [[] for _ in range(node_count + 1)]
for _ in range(node_count - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0] * 2 for _ in range(node_count + 1)]

def dfs(curr, prev, tree, dp):
    dp[curr][1] = 1

    for nxt in tree[curr]:
        if nxt == prev:
            continue
        dfs(nxt, curr, tree, dp)
        
        dp[curr][1] += min(dp[nxt][0], dp[nxt][1])
        dp[curr][0] += dp[nxt][1]


dfs(1, 0, tree, dp)
print(min(dp[1]))