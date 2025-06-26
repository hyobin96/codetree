N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]

def bomb(remove_idxs):
    global arr

    for i in remove_idxs:
        arr[i] = 0    


def gravity():
    global arr

    result_arr = []
    for e in arr:
        if e != 0:
            result_arr.append(e)

    return result_arr

def simul():
    global arr

    while True:
        remove_idxs = [0]
        cnt = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                remove_idxs.append(i)
                cnt += 1

            else:
                if cnt >= M:
                    bomb(remove_idxs)

                remove_idxs = [i]
                cnt = 1

        if cnt >= M:
            bomb(remove_idxs)

        prev = len(arr)
        arr = gravity()[0:]
        curr = len(arr)
        
        if prev == curr:
            print(curr)
            for e in arr:
                print(e)

            break


if M > 1:
    simul()
else:
    print(0)



