class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0

    def begin(self):
        return self.head

    def end(self):
        return self.tail

    def delete(self, it):
        if it == self.head:
            it = it.next
            it.prev = None
            self.head = it
            self.num -= 1

            return

        if it.next == self.tail:
            it.next = None
            self.tail = it
            self.num -= 1
            return

        it.next.next.prev = it
        it.next = it.next.next
        self.num -= 1

    def push(self, it, data):
        new_node = Node(data)

        if it == self.tail:
            if self.num == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node

        elif it == self.head:
            if self.num == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

        else:
            new_node.next = it.next
            new_node.prev = it
            it.next.prev = new_node
            it.next = new_node

        self.num += 1

    
n, m = map(int, input().split())
s = input()
dll = DLL()
for alpha in s:
    it = dll.end()
    dll.push(it, alpha)


def pr():
    it = dll.begin()
    while it != None:
        print(it.data, end='')
        it = it.next
    
    print()

it = dll.end()
for _ in range(m):
    q = input().split()

    if q[0] == 'L':
        if it != dll.begin():
            it = it.prev
    elif q[0] == 'R':
        if it != dll.end():
            it = it.next

    elif q[0] == 'D':
        if it != dll.end():
            dll.delete(it)

    else:
        dll.push(it, q[1])
        it = it.next
    
pr()




        