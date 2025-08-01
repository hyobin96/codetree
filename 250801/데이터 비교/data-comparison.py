N = int(input())
elements1 = set(map(int, input().split()))
N = int(input())
elements2 = list(map(int, input().split()))

for e in elements2:
    if e in elements1:
        print(1, end=' ')
    else:
        print(0, end=' ')