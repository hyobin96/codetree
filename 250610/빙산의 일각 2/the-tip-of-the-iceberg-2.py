N = int(input())
H_list = [int(input()) for _ in range(N)]

_max = 0
for x in range(1000):
    cnt = 0
    for i in range(N):
        if i == N-1:
            if H_list[i] > x and H_list[i-1] <= x:
                cnt += 1
        else:
            if H_list[i] > x and H_list[i+1] <= x:
                cnt += 1
    _max = max(_max, cnt)
print(_max)
