class TrieNode():
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


def insert_word(root, s):
    global is_not_prefix
    node = root
    for char in s:
        if node.is_end:
            is_not_prefix = False

        index = int(char)
        
        if node.children[index] is None:
            node.children[index] = TrieNode()

        node = node.children[index]

    node.is_end = True
    

root = TrieNode()

s_count = int(input())
sequence = [input().rstrip() for _ in range(s_count)]
sequence.sort(key = lambda s: len(s))

is_not_prefix = True
for s in sequence:
    insert_word(root, s)

print(int(is_not_prefix))

        