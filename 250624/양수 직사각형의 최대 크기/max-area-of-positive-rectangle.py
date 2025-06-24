import sys

input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def is_positive(r1, c1, r2, c2):
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if arr[i][j] <= 0:
                return False

    return True


max_area = -1

for i1 in range(N):
    for i2 in range(i1, N):
        for j1 in range(M):
            for j2 in range(j1, M):
                
                if is_positive(i1, j1, i2, j2):
                    area = (i2 - i1 + 1) * (j2 - j1 + 1)
                    max_area = max(max_area, area)

print(max_area)