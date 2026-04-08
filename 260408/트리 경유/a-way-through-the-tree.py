node_count, target_count = map(int, input().split(" "))
written_nodes = set()

for _ in range(target_count):
    target = int(input())
    curr = target
    reason_node = curr
    is_possible = True
    while curr != 1:
        if curr in written_nodes:
            is_possible = False
            reason_node = curr
        curr //= 2

    if is_possible:
        print(0)
        written_nodes.add(target)
    else:
        print(reason_node)