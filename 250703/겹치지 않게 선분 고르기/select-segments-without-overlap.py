def isOverlap():
    for i in range(len(idx_arr)):
        for j in range(i + 1, len(idx_arr)):
            l1, r1 = pos[idx_arr[i]];
            l2, r2 = pos[idx_arr[j]];
            
            if l2 > r1 or l1 > r2:
                continue

            else:
                return True

    return False


def select(idx):
    global pos, idx_arr, max_cnt
    
    if isOverlap():
        return

    max_cnt = max(max_cnt, len(idx_arr))
        
    for i in range(idx, N):
        idx_arr.append(i)
        select(i + 1)
        idx_arr.pop()


N = int(input())

pos = []

idx_arr = []

max_cnt = 0

for _ in range(N):
    l, r = map(int, input().split())
    pos.append([l, r])

select(0)

print(max_cnt)