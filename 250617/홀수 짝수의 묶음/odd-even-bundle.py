N = int(input())
arr = list(map(int, input().split()))

odd_cnt = 0
even_cnt = 0

for n in arr:
    if n % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

cnt = min(odd_cnt, even_cnt)    

if odd_cnt % 3 == 0:
    cnt += odd_cnt // 3 * 2
else:
    if odd_cnt % 3 == 1:
        cnt += odd_cnt // 3 * 2 - 1
    else:
        cnt += odd_cnt // 3 * 2 + 1

print(cnt)