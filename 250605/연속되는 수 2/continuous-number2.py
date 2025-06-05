n = int(input())
cnt = 0
pre = 0
curr = 0
_max = 0
for i in range(n):
    if i == 0:
        pre = int(input())
        cnt += 1
    else:
        curr = int(input())
        if pre != curr:
            _max = max(_max, cnt)
            cnt = 0
        cnt += 1
        pre = curr
    
print(_max)