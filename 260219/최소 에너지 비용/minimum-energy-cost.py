import sys
input = sys.stdin.readline

n = int(input())
dists = list(map(int, input().strip().split()))
costs = list(map(int, input().strip().split()))

prefix_dist = [0] * n
for i in range(n - 1):
    prefix_dist[i + 1] = prefix_dist[i] + dists[i]

pos = 0
cost = 0
for i in range(pos + 1, n):
    if costs[i] < costs[pos]:
        dist = prefix_dist[i] - prefix_dist[pos]
        charging_cost = dist * costs[pos]
        cost += charging_cost
        pos = i

cost += (prefix_dist[n - 1] - prefix_dist[pos]) * costs[pos]

print(cost)

