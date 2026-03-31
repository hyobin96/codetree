# 가장 많은 간선을 지나는 경로
# 각 간선의 가중치가 1이라고 가정하고 가장 먼 노드 구하기
# 가장 먼 노드에서 탐색하면서 간선 개수와 간선 길이 합 비교해서 
# 간선개수가 가장 많으면서 간선 길이가 가장 짧은 것 구해서 간선 길이 반환
# ceil(간선 길이 / D)
import math

node_count, day_dist = map(int, input().split(" "))
tree = [[] for _ in range(node_count + 1)]

for _ in range(node_count - 1):
    u, v, w = map(int, input().split(" "))
    tree[u].append((v, w))
    tree[v].append((u, w))

def farthest(begin, tree):
    max_node, max_dist = begin, 0
    stack = [(begin, 0, 0)] # curr, dist, parent
    while stack:
        curr, dist, parent = stack.pop()
        
        if dist > max_dist:
            max_dist = dist
            max_node = curr
        
        for nxt, _ in tree[curr]:
            if nxt == parent:
                continue
            stack.append((nxt, dist + 1, curr))
    
    return max_node, max_dist

def get_dist(begin, tree):
    min_dist, max_edge_count = 2e9, 0
    stack = [(begin, 0, 0, 0)] #  curr, edge_count, dist, parent
    while stack:
        curr, edge_count, dist, parent = stack.pop()

        if edge_count > max_edge_count:
            max_edge_count = edge_count
            min_dist = dist
        elif edge_count == max_edge_count and dist < min_dist:
            min_dist = dist
        
        for nxt, w in tree[curr]:
            if nxt == parent:
                continue
            stack.append((nxt, edge_count + 1, dist + w, curr))
    
    return min_dist


max_node, _ = farthest(1, tree)
min_dist = get_dist(max_node, tree)

answer = math.ceil(min_dist / day_dist)
print(answer)