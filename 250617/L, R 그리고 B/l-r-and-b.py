arr = [list(input()) for _ in range(10)]

L, R, B = (), (), ()

for i in range(10):
    for j in range(10):
        if arr[i][j] == 'L':
            L = (i, j)
        elif arr[i][j] == 'R':
            R = (i, j)
        elif arr[i][j] == 'B':
            B = (i, j)

def get_dist():
    return abs(L[0] - B[0]) + abs(L[1] - B[1]) - 1

dist = 0
if L[0] == B[0] == R[0] or L[1] == B[1] == R[1]:
    dist = get_dist() + 2

else:
    dist = get_dist()

print(dist)