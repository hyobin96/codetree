N, M = map(int, input().split())
num_arr = list(map(int, input().split()))

MAX_NUM = sum(num_arr)

def is_possible(max_num):
    remain_m_cnt = M - 1

    num_sum = 0
    for num in num_arr:
        if num > max_num:
            return False
            
        num_sum += num
        if num_sum > max_num:
            if remain_m_cnt == 0:
                return False

            remain_m_cnt -= 1
            num_sum = num
    
    return True

ans = MAX_NUM
for max_num in range(MAX_NUM, 0, -1):
    if is_possible(max_num):
        ans = max_num

print(ans)