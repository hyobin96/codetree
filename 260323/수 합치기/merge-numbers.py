n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq
heapq.heapify(arr)

min_cost = 0
while len(arr) > 1:
    a, b = heapq.heappop(arr), heapq.heappop(arr)
    cost = a + b
    min_cost += cost
    heapq.heappush(arr, cost)

print(min_cost)