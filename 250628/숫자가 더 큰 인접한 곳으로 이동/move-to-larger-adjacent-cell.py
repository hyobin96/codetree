N, r, c = map(int, input().split())
r, c = r - 1, c - 1

arr = [list(map(int, input().split())) for _ in range(N)]

drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(nr, nc):
    return 0 <= nr < N and 0 <= nc < N

def simul(r, c):
    
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and arr[r][c] < arr[nr][nc]:
            return nr, nc

    return r, c


while True:
    print(arr[r][c], end = ' ')
    nr, nc = simul(r, c)
    
    if (nr, nc) == (r, c):
        break

    r, c = nr, nc
         
    