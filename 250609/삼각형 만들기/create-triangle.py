n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def is_triangle(i, j, k):
    if arr[i][0] == arr[j][0] == arr[k][0] or arr[i][1] == arr[j][1] == arr[k][1]:
        return False
    return True


def is_parallel(i, j, k):
    if arr[i][1] - arr[j][1] == 0:
        if arr[i][0] - arr[k][0] == 0:
            return abs(arr[i][0] - arr[j][0]) * abs(arr[i][1] - arr[k][1])
        elif arr[j][0] - arr[k][0] == 0:
            return abs(arr[i][0] - arr[j][0]) * abs(arr[j][1] - arr[k][1])
    elif arr[i][1] - arr[k][1] == 0:
        if arr[i][0] - arr[j][0] == 0:
            return abs(arr[i][0] - arr[k][0]) * abs(arr[i][1] - arr[j][1])
        elif arr[j][0] - arr[k][0] == 0:
            return abs(arr[i][0] - arr[k][0]) * abs(arr[j][1] - arr[k][1])
    elif arr[j][1] - arr[k][1] == 0:
        if arr[j][0] - arr[i][0] == 0:
            return abs(arr[j][0] - arr[k][0]) * abs(arr[i][1] - arr[j][1])
        elif arr[k][0] - arr[i][0] == 0:
            return abs(arr[j][0] - arr[k][0]) * abs(arr[i][1] - arr[k][1])
    return 0

_max = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j + 1, n):
            if is_triangle(i, j, k):
                area = is_parallel(i, j, k)
                _max = max(_max, area)
print(_max)