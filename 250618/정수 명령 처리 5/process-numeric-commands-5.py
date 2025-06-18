N = int(input())
arr = [input().split() for _ in range(N)]

l = []
for i in range(N):
    if arr[i][0] == 'push_back':
        l.append(arr[i][1])

    elif arr[i][0] == 'pop_back':
        l.pop()
    elif arr[i][0] == 'size':
        print(len(l))
    else:
        print(l[int(arr[i][1]) - 1])