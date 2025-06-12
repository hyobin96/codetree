N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N+1):
    curr = i
    nxt = 1
    pointer = 0
    count_arr = [0] * (N+1)
    count_arr[curr] = 1
    ans_arr = [curr]

    while pointer < N-1:
        if arr[pointer] == curr + nxt:
            if curr == nxt or count_arr[nxt] == 1:
                break

            ans_arr.append(nxt)
            count_arr[nxt] = 1
            curr, nxt = nxt, 1
            pointer += 1
        
        nxt += 1


    if len(ans_arr) == N:
        print(*ans_arr)
        break