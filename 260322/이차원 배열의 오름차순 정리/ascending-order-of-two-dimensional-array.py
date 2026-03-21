n = int(input())
k = int(input())

# Please write your code here.
# 내가 생각하는 숫자가 number 이라면,
# 행 단위로 생각, min(number // i, n) 개만큼 행에 존재
# 그 개수가 k 이상이면 만족
# 만족하는 최소 number 구하기

MAX_NUM = n ** 2

def is_possible(number, k):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(number // i, n)
    return cnt >= k

min_num = MAX_NUM
left, right = 1, MAX_NUM
while left <= right:
    mid = (left + right) // 2
    if is_possible(mid, k):
        min_num = min(min_num, mid)
        right = mid - 1
    else:
        left = mid + 1

print(min_num)

