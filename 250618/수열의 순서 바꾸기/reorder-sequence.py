N = int(input())

arr = list(map(int, input().split()))

cnt = 0
for _ in range(N):
    if arr[-1] < arr[0]:
        arr.append(arr[0])
        arr.pop(0)
        cnt += 1
    else:
        idx = -1
        for i in range(N-1, 0, -1):
            if arr[i] > arr[0] and arr[i-1] < arr[0]:
                idx = i
                break

        for i in range(N-1, 0, -1):
            if arr[i] > arr[0] and arr[i-1] > arr[0] and arr[i] < arr[i-1]:
                idx = max(idx, i)
                break

        if idx != -1:
            arr.insert(idx, arr[0])
            arr.pop(0)
            cnt += 1
            
print(cnt)