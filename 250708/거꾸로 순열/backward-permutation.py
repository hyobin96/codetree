def perm(cnt):
    global selected_nums, visited
    if cnt == N:
        print(*selected_nums)
        return

    for i in range(N, 0, -1):
        if visited[i]:
            continue
        
        visited[i] = True
        selected_nums.append(i)

        perm(cnt + 1)

        selected_nums.pop()
        visited[i] = False


N = int(input())
selected_nums, visited = [], [False] * (N + 1)
perm(0)