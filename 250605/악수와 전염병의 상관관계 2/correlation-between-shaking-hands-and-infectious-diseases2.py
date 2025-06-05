n, k, p, T = map(int, input().split())
arr = [[0, 0] for _ in range(101)] # 감염여부, 악수횟수
arr[p] = [1, k]
q = [tuple(map(int, input().split())) for _ in range(T)]
q.sort(key=lambda x: x[0])

def hand(x, y):
    if arr[x][0] == 1 and arr[y][0] == 1:
        arr[x][1] -= 1
        arr[y][1] -= 1
    elif arr[x][0] == 1:
        if arr[x][1] > 0:
            arr[y] = [1, k]
            arr[x][1] -= 1
    elif arr[y][0] == 1:
        if arr[y][1] > 0:
            arr[x] = [1, k]
            arr[y][1] -= 1

for _, x, y in q:
    hand(x, y)

for i in range(1, n+1):
    print(arr[i][0], end='')

