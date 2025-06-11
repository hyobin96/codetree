import sys

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

def is_possible(xs=('',), ys=('',)):
    for i, (x, y) in enumerate(arr):
        if not(x in xs or y in ys):
            return False
    return True

for i in range(11):        
    for j in range(11):
        for k in range(11):
            if is_possible((i, j, k)) or is_possible((i, j), (k,)) or is_possible((i,), (k,j)) or is_possible(('',), (i,j,k)):
                print(1)
                sys.exit()
print(0)        

