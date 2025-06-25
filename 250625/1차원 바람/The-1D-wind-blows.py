N, M, Q = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

info = [input().split() for _ in range(Q)]

#왼쪽으로 밀기
def to_left(arr):
    temp = arr[0]
    for i in range(M - 1):
        arr[i] = arr[i + 1]

    arr[-1] = temp

def to_right(arr):
    temp = arr[-1]
    for i in range(M-1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = temp

def is_same(arr1, arr2):
    for e1, e2 in zip(arr1, arr2):
        if e1 == e2:
            return True

    return False

dire = ['L', 'R']

for r, d in info:
    idx = -1
    r = int(r) - 1

    if d == 'L':
        to_right(arr[r])
        idx = 0
    
    else:
        to_left(arr[r])
        idx = 1

    up_idx = idx
    up = r - 1
    down = r + 1

    
    while up >= 0 and is_same(arr[up], arr[up + 1]):
        up_idx = (up_idx + 1) % 2
        if dire[up_idx] == 'L':
            to_right(arr[up])
        
        else:
            to_left(arr[up])

        up -= 1


    down_idx = idx

    while down < N and is_same(arr[down], arr[down - 1]):
        down_idx = (down_idx + 1) % 2
        if dire[down_idx] == 'L':
            to_right(arr[down])
        
        else:
            to_left(arr[down])

        down += 1

for i in range(N):
    print(*arr[i])

        

    

    

