from sortedcontainers import SortedSet

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet(arr)

for i in range(1, k + 1):
    print(s[-i], end = ' ')
