node_count = int(input())
tree = [0] * (node_count + 1)

def to_number(c):
    return ord(c) - ord('A') + 1

def to_char(number):
    return chr(number + ord('A') - 1)

for _ in range(node_count):
    parent, left, right = input().strip().split(" ")
    parent = to_number(parent)
    tree[parent] = [-1, -1]
    if left != '.':
        left = to_number(left)
        tree[parent][0] = left
    if right != '.':
        right = to_number(right)
        tree[parent][1] = right

def traverse(root, tree, command):
    if root > len(tree):
        return
    if command == 0:
        print(to_char(root), end = '')
    if tree[root][0] != -1:
        traverse(tree[root][0], tree, command)
    if command == 1:
        print(to_char(root), end = '')
    if tree[root][1] != -1:
        traverse(tree[root][1], tree, command)
    if command == 2:
        print(to_char(root), end = '')

traverse(1, tree, 0)
print()
traverse(1, tree, 1)
print()
traverse(1, tree, 2)
