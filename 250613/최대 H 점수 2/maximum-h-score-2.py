N, L = map(int, input().split())
num_list = list(map(int, input().split()))

MAX_NUM = 100

def is_possible(H):
    remain_L = L
    cnt = 0

    for num in num_list:
        if num >= H:
            cnt += 1
        elif num + 1 == H:
            if remain_L > 0:
                remain_L -= 1
                cnt += 1
    
    if cnt < H:
        return False
    
    return True

H_max = 1
for H in range(1, MAX_NUM + 1):
    if is_possible(H):
        H_max = H
    else:
        break

print(H_max)