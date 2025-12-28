import sys

input = sys.stdin.readline

class Point:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]

    def get_distance(self, p):
        distance = abs(self.x - p.x) + abs(self.y - p.y)
        return distance 

n = int(input())

checkpoints = [Point(tuple(map(int, input().split()))) for _ in range(n)]

L_dist, R_dist = [0] * n, [0] * n

for i in range(1, n):
    L_dist[i] = L_dist[i - 1] + checkpoints[i].get_distance(checkpoints[i - 1])
    R_dist[-i - 1] = R_dist[-i] + checkpoints[-i - 1].get_distance(checkpoints[-i])

answer = 5000000000
# print(L_dist)
# print(R_dist)


# 0 8 11 10
# 0 8 11 12
# 4 4  1  0

for i in range(1, n - 1):
    distance = L_dist[i - 1] + R_dist[i + 1] + checkpoints[i - 1].get_distance(checkpoints[i + 1])