from sortedcontainers import SortedSet
import sys

input = sys.stdin.readline

n, q = map(int, input().split())

# n 개의 점의 위치 입력받고 treeset에 오름차순으로 저장
inputs = list(map(int, input().split()))

nums = SortedSet(inputs)

# 점의 개수는 nums.bisect_right(b) - nums.bisect_left(a)개
# 
output = [0] * q
for i in range(q):
    a, b = map(int, input().split())
    output[i] = str(nums.bisect_right(b) - nums.bisect_left(a))
    # print(hash_set[b] - hash_set[a] + 1)

print('\n'.join(output))