n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
arr.sort(key=lambda x: (int(x[1]), -int(x[2])))
for e in arr:
    print(e[0], e[1], e[2])