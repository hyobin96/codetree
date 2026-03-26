edge_count = int(input())

max_node_count = 10_000

node_set = set()
to_child_edges = [[] for _ in range(max_node_count + 1)]
to_parent_edges = [[] for _ in range(max_node_count + 1)]
for _ in range(edge_count):
    begin_node, target_node = map(int, input().split(" "))
    node_set.add(begin_node)
    node_set.add(target_node)
    to_child_edges[begin_node].append(target_node)
    to_parent_edges[target_node].append(begin_node)

root_node = 0
root_count = 0
is_in_edge_count_one = True
for i in range(1, edge_count + 1):
    in_edge_count = len(to_parent_edges[i])
    if in_edge_count == 0:
        root_node = i
        root_count += 1
    elif in_edge_count > 1:
        is_in_edge_count_one = False
        break

def count_nodes(root, to_child_edges):
    stack = [root]
    node_count = 0
    while stack:
        parent_node = stack.pop()
        node_count += 1
        for child_node in to_child_edges[parent_node]:
            stack.append(child_node)

    return node_count

if root_count != 1 or not is_in_edge_count_one:
    print(0)
else:
    node_count = count_nodes(root_node, to_child_edges)
    print(int(node_count == len(node_set)))
    
    
