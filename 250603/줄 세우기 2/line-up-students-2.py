n = int(input())
arr = [tuple(map(int, input().split())) + (i+1,) for i in range(n)]
arr.sort(key=lambda x: (x[0], -x[1]))
for e in arr:
    print(e[0], e[1], e[2])