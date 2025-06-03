class Info:
    def __init__(self, name, addr, city):
        self.n = name
        self.a = addr
        self.c = city

n = int(input())
arr = []
for _ in range(n):
    n, a, c = input().split()
    arr.append(Info(n, a, c))

arr.sort(key = lambda x : x.n)
p = arr[-1]
print(f'name {p.n}')
print(f'addr {p.a}')
print(f'city {p.c}')

