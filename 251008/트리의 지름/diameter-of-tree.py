import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))


target = 0
weight = 0

def dfs(u, w, visited):
    global target, weight

    visited[u] = 1
    if weight < w:
        target = u
        weight = w

    for v, wei in graph[u]:
        if visited[v]:
            continue

        dfs(v, w + wei, visited)


dfs(1, 0, [0] * (n + 1))

weight = 0

dfs(target, 0, [0] * (n + 1))

print(weight)

