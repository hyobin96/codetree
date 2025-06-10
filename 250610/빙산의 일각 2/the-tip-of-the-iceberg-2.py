N = int(input())
H_list = [int(input()) for _ in range(N)]

_max = 0
for x in range(1000):
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        if cnt2 != 0:
            if H_list[i] <= x:
                cnt1 += 1
                cnt2 = 0
        elif H_list[i] > x:
            cnt2 += 1
    if cnt2 != 0:
        cnt1 += 1
    _max = max(_max, cnt1)
print(_max)
