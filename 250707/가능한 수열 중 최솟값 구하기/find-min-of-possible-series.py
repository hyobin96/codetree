import sys

def is_same(cnt):
    for i in range(1, cnt // 2 + 1):
        idx = cnt - i - 1
        is_ok = True
        for j in range(i):
            if selected_nums[idx - j] != selected_nums[cnt - j - 1]:
                is_ok = False
                break
        if is_ok:
            return True
    return False


def select_nums(cnt):
    global N, selected_nums
    if is_same(cnt):
        return
    
    if cnt == N:
        for e in selected_nums:
            print(e, end='')
        sys.exit()

    for num in range(4, 7):
        selected_nums.append(num)
        select_nums(cnt + 1)
        selected_nums.pop()

N = int(input())
selected_nums = []
select_nums(0)