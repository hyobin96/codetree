depth = int(input())
tree = list(map(int, input().split(" ")))
node_count = len(tree)
root = node_count
for i in range(depth, 0, -1):
    root //= 2
    for j in range(root, node_count, 1 << i):
        print(tree[j], end = ' ')
    print()