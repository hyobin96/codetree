import sys
sys.setrecursionlimit(200000)

node_count = int(input())
tree = [[] for _ in range(node_count + 1)]
tree_values = [0] * (node_count + 1)
dp = [0] * (node_count + 1)

for i in range(2, node_count + 1):
    t, a, p = map(int, input().split(" "))
    if t:
        tree_values[i] = a
    else:
        tree_values[i] = -a
    tree[p].append(i)

# print(tree)
# print(tree_values)

def dfs(parent, tree, tree_values, dp):
    for child in tree[parent]:
        dp[parent] += dfs(child, tree, tree_values, dp)    
    
    dp[parent] += tree_values[parent]
    return dp[parent] if dp[parent] > 0 else 0
        
dfs(1, tree, tree_values, dp)
print(dp[1])