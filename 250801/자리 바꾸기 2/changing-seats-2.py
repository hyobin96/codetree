n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
positions = [i for i in range(n + 1)]
d = {}
for i in range(1, n + 1):
    d[i] = {i}

for _ in range(3):
    for i in range(k):
        a, b = edges[i]
        i1, i2 = positions[a], positions[b]
        d[i1].add(b)
        d[i2].add(a)
        positions[a], positions[b] = positions[b], positions[a]

for i in range(1, n + 1):
    print(len(d[i]))