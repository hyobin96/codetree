import sys, math
sys.setrecursionlimit(100_000)

root = 1
node_count = int(input())
edges = [tuple(map(int, input().split())) for _ in range(node_count - 1)]
colored_count = int(input())
colored_nodes = [int(input()) for _ in range(colored_count)]
query_count = int(input())
querys = [tuple(map(int, input().split())) for _ in range(query_count)]

H_MAX = int(math.log(node_count, 2)) + 1
tree = [[] for _ in range(node_count + 1)]
for u, v in edges:
    tree[u].append(v)
    tree[v].append(u)

colors = [0] * (node_count + 1)
for node in colored_nodes:
    colors[node] = 1

parents = [[0] * (node_count + 1) for _ in range(H_MAX + 1)]
depths = [0] * (node_count + 1)
color_dp = [0] * (node_count + 1)
def dfs(curr, prev, tree, depths, parents, colors, color_dp):
    color_dp[curr] += colors[curr]
    for nxt in tree[curr]:
        if nxt == prev:
            continue
        depths[nxt] = depths[curr] + 1
        parents[0][nxt] = curr
        color_dp[nxt] += color_dp[curr]
        dfs(nxt, curr, tree, depths, parents, colors, color_dp)

dfs(root, 0, tree, depths, parents, colors, color_dp)
# print(color_dp)
def fill_sparse_table(parents):
    for h in range(1, H_MAX + 1):
        for i in range(1, node_count + 1):
            parents[h][i] = parents[h - 1][parents[h - 1][i]]

fill_sparse_table(parents)

def get_lca(node1, node2, depths, parents):
    if depths[node1] < depths[node2]:
        node1, node2 = node2, node1

    for h in range(H_MAX, -1, -1):
        if depths[node1] - depths[node2] >= (1 << h):
            node1 = parents[h][node1]
    
    if node1 == node2:
        return node1

    for h in range(H_MAX, -1, -1):
        if parents[h][node1] != parents[h][node2]:
            node1, node2 = parents[h][node1], parents[h][node2]

    return parents[0][node1]

for node1, node2 in querys:
    lca = get_lca(node1, node2, depths, parents)
    count = color_dp[node1] + color_dp[node2] - 2 * color_dp[lca] + colors[lca]
    print(count)