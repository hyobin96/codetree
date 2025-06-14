N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
MIN_NUM, MAX_NUM = 1, 100


def is_overlap(x):
    cnt = 0
    
    for x1, x2 in arr:
        if x1 <= x <= x2:
            cnt += 1
    
    if cnt == N:
        return True

    return False

ans = 'No'

for x in range(MIN_NUM, MAX_NUM + 1):
    if is_overlap(x):
        ans = 'Yes'
        break

print(ans)        