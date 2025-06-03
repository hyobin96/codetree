n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
arr.sort(key=lambda x: x[1])

for e in arr:
    print(e[0], e[1], e[2])