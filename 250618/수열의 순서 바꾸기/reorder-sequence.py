N = int(input())

arr = list(map(int, input().split()))

cnt = 0
for _ in range(N ** 2):
    if arr[0] == max(arr):
        arr.append(arr[0])
        arr.pop(0)
        cnt += 1
    else:
        is_ok = False
        for i in range(N-1, 0, -1):
            if arr[i] > arr[0] and arr[i-1] > arr[0] and arr[i] < arr[i-1]:
                arr.insert(i, arr[0])
                arr.pop(0)
                is_ok = True
                cnt += 1
                break
            
        if not is_ok:
            for i in range(N-1, 0, -1):
                if arr[i] > arr[0] and arr[i-1] < arr[0]:
                    arr.insert(i, arr[0])
                    arr.pop(0)
                    cnt += 1
                    break

print(cnt)