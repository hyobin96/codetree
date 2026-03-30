# 1 // 3 4 5 // 8 9 // 15 // 30 31 32
# 1 - 3 4 5
# 3 - 8 9
# 4 - 15
# 5 - 30 31 32

# 집합으로 쪼개고 i, j 로?

node_count, target_node = map(int, input().split(" "))
nodes = list(map(int, input().split(" ")))

tree = [[] for _ in range(max(nodes) + 1)]
parents = [0] * (max(nodes) + 1)

j = 1
for i in nodes:
    tree[i].append(nodes[j])
    parents[nodes[j]] = i
    while j + 1 < node_count and nodes[j] + 1 == nodes[j + 1]:
        j += 1
        tree[i].append(nodes[j])
        parents[nodes[j]] = i
    j += 1
    # print(tree[i])

    if j >= node_count:
        break

# print(tree)
# print(parents)
if parents[target_node] == 1:
    print(0)

else:
# 부모의 부모
    p = parents[target_node]
    p_p = parents[p]

    count = 0
    for child in tree[p_p]:
        if child == p:
            continue
        count += len(tree[child])

    print(count)