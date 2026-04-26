class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

def insert_word(root, s):
    node = root

    for char in s:
        index = ord(char) - ord('A')

        if not node.children[index]:
            node.children[index] = TrieNode()
        
        node = node.children[index]

    node.is_end = True

tree_count = int(input())
root = TrieNode()
for _ in range(tree_count):
    input_s = input().split(" ")
    insert_word(root, input_s[1:])

def dfs(node, cnt):
    for i, nxt_node in enumerate(node.children):
        if nxt_node is not None:
            out = '--' * cnt + chr(i + ord('A'))
            print(out)
            dfs(nxt_node, cnt + 1)
# print(root.children)
dfs(root, 0)
    