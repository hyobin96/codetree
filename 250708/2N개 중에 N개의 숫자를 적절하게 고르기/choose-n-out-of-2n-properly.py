def select_nums(cnt, result, start):
    global N, nums, _sum, answer
    if cnt == N:
        answer = min(answer, abs(_sum - 2 * result))

    for i in range(start, 2 * N):
        select_nums(cnt + 1, result + nums[i], i + 1)


N, answer = int(input()), 100000000
nums = list(map(int, input().split()))
_sum = sum(nums)
select_nums(0, 0, 0)
print(answer)