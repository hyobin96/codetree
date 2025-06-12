N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N+1):
    curr = i
    pointer = 0
    count_arr = [0] * (N+1)
    count_arr[curr] = 1
    ans_arr = [curr]

    while pointer < N-1:
        nxt = abs(arr[pointer] - curr)
        if nxt > N or nxt == curr or count_arr[nxt] == 1:
            break

        ans_arr.append(nxt)
        count_arr[nxt] = 1
        curr = nxt
        pointer += 1
    

    if len(ans_arr) == N:
        print(*ans_arr)
        break