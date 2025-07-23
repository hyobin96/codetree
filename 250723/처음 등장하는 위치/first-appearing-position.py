from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

sd = SortedDict()
for i, num in enumerate(arr):
    if num not in sd:
        sd[num] = i + 1

for x, p in sd.items():
    print(x, p)