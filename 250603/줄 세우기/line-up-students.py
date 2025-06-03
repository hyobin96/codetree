n = int(input())
arr = [tuple(map(int, input().split())) + (i,) for i in range(1, n+1)]
arr.sort(key=lambda x: (-x[0], -x[1], x[2]))
for e in arr:
    print(e[0], e[1], e[2])