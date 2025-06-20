class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def empty(self):
        return not self.items

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")

        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            raise Exception("Stack is Empty")

        return self.items[-1]

N = int(input())
s = Stack()

for _ in range(N):
    q = input().split()

    if q[0] == 'push':
        s.push(int(q[1]))

    elif q[0] == 'size':
        print(s.size())

    elif q[0] == 'empty':
        print(int(s.empty()))

    elif q[0] == 'pop':
        print(s.pop())

    elif q[0] == 'top':
        print(s.top())
