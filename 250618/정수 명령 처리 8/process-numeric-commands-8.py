class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num = 0

    def push_front(self, N):
        new_node = Node(N)
        new_node.next = self.head

        if new_node.next == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        else:
            self.head.prev = new_node
            self.head = new_node

        self.num += 1

    def push_back(self, N):
        new_node = Node(N)
        new_node.prev = self.tail

        if new_node.prev == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.num += 1

    def pop_front(self):
        return_data = self.head.data

        if self.num == 1:
            self.head = None
            self.tail = None

        else:
            self.head.next.prev = None
            self.head = self.head.next
        
        self.num -= 1
        return return_data


    def pop_back(self):
        return_data = self.tail.data

        if self.num == 1:
            self.head = None
            self.tail = None

        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        self.num -= 1
        return return_data

    def size(self):
        return self.num

    def empty(self):
        if self.num == 0:
            return True
    
        return False

    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data

    
N = int(input())
dl = DoublyLinkedList()

for _ in range(N):
    q = input().split()
    
    if q[0] == 'push_back':
        dl.push_back(q[1])

    elif q[0] == 'push_front':
        dl.push_front(q[1])

    elif q[0] == 'pop_front':
        print(dl.pop_front())

    elif q[0] == 'pop_back':
        print(dl.pop_back())

    elif q[0] == 'size':
        print(dl.size())

    elif q[0] == 'empty':
        print(int(dl.empty()))
    
    elif q[0] == 'front':
        print(dl.front())

    else:
        print(dl.back())


    
