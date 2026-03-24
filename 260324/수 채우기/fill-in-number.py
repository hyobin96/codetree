n = int(input())

# Please write your code here.
FIVE_MAX_NUM = 20000
min_cnt = -1

for i in range(FIVE_MAX_NUM + 1):
    remain = n - 5 * i
    if remain >= 0 and remain % 2 == 0:
        min_cnt = i + remain // 2

answer = min_cnt
print(answer)
        