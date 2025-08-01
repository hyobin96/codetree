input()
elements1 = set(map(int, input().split()))
input()
elements2 = list(map(int, input().split()))

for e in elements2:
    print(int(e in elements1))