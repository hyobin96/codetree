import heapq

n = int(input())
nums = list(map(lambda x: x * -1, map(int, input().split())))

heapq.heapify(nums)

while len(nums) >= 2:
    n1, n2 = heapq.heappop(nums), heapq.heappop(nums)
    if n1 != n2:
        heapq.heappush(nums, n1 - n2)

if nums:
    print(-nums[0])
else:
    print(-1)