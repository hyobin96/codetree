import sys

class Node:
    def __init__(self):
        self.p = 0
        self.c = 0


input = sys.stdin.readline

N = int(input())

tree = [Node() for _ in range(N + 1)]

graph = [[] for _ in range(N + 1)]

while True:
    seg = input()
    if not seg:
        break
    u, v = map(int, seg.split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(u, visited):
    global tree
    visited[u] = 1


    for v in graph[u]:
        if visited[v]:
            continue

        tree[v].p = u
        dfs(v, visited)

dfs(1, [0] * (N + 1))

for i in range(2, N + 1):
    print(tree[i].p)