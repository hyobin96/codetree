N, K = map(int, input().split())
nums = list(map(int, input().split()))
d = {}
for n in nums:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

l = list(d.items())
l.sort(key=lambda x: (-x[1], -x[0]))
for n, _ in l[:K]:
    print(n, end=' ')