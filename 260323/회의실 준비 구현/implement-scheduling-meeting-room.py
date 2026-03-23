n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(key = lambda x: x[1])
prev_e, cnt = 0, 0
for s, e in meetings:
    if prev_e <= s:
        cnt += 1
        prev_e = e

print(cnt)