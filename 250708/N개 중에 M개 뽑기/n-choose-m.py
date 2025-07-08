def select_nums(cnt, start):
    global selected_nums
    if cnt == M:
        print(*selected_nums)
        return

    for num in range(start, N + 1):
        selected_nums.append(num)
        select_nums(cnt + 1, num + 1)
        selected_nums.pop()


N, M = map(int, input().split())
selected_nums = []
select_nums(0, 1)
