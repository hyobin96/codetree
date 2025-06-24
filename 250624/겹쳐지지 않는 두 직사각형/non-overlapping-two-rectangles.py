N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def get_sum(r1, c1, r2, c2):
    _sum = 0

    for i in range(r1, r2 + 1):
        _sum += sum(arr[i][c1 : c2 + 1])

    return _sum
        

_max = -2000000
for i1 in range(N):
    for i2 in range(i1, N):
        for j1 in range(M):
            for j2 in range(j1, M):
                # print(i1, i2, j1, j2)
                for i3 in range(N):
                    for i4 in range(i3, N):
                        for j3 in range(M):
                            for j4 in range(j3, M):
                                if j2 < j3 or i2 < i3 or j1 > j4 or i1 > i4:
                                    # print(i1, i2, j1, j2, i3, i4, j3, j4)
                                
                                    area = get_sum(i1, j1, i2, j2) + get_sum(i3, j3, i4, j4)
                                    _max = max(_max, area)

print(_max)