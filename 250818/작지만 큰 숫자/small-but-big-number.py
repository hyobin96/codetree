from sortedcontainers import SortedSet

n, m = map(int, input().split())
arr = list(map(lambda x: x * -1, map(int, input().split())))
querys = list(map(int, input().split()))

s = SortedSet(arr)
for num in querys:
    idx = s.bisect_left(-num)
    if idx == len(s):
        print(-1)
    else:
        print(-s[idx])
        s.remove(s[idx])