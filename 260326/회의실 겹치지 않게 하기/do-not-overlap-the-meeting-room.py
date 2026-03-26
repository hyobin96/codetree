n = int(input())
meetings = [tuple(map(int, input().split(" "))) for _ in range(n)]

# Please write your code here.
meetings.sort(lambda m: m[1])
# print(meetings)
prev_end_time, cancle_count = 0, 0
for start_time, end_time in meetings:
    if prev_end_time > start_time:
        cancle_count += 1
        continue
    prev_end_time = end_time

print(cancle_count)