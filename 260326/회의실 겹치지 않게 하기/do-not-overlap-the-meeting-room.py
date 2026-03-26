n = int(input())
meetings = [tuple(map(int, input().split(" "))) for _ in range(n)]

# Please write your code here.
meetings.sort(lambda m: m[1])
# print(meetings)
prev_e, cancle_cnt = 0, 0
for s, e in meetings:
    if prev_e > s:
        cancle_cnt += 1
        continue
    prev_e = e

print(cancle_cnt)