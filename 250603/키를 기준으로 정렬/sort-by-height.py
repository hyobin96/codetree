class Person:
    def __init__(self, name, height, weight):
        self.n = name
        self.h = height
        self.w = weight

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
p = [Person(n, h, w) for n, h, w in arr]
p.sort(key=lambda x: x.h)

for e in p:
    print(e.n, e.h, e.w)