arr = [list(map(int, list(input()))) for _ in range(3)]

def is_manzok(i, j, count_arr):
    return count_arr[i] == 1 and count_arr[j] == 1 and sum(count_arr) == 2

def is_win(i, j):
    for k in range(0, 3):
        count_arr = [0] * 10
        for l in range(0, 3):
            count_arr[arr[k][l]] = 1
        if is_manzok(i, j, count_arr):
            return True
            
        count_arr = [0] * 10
        for l in range(0, 3):
            count_arr[arr[l][k]] = 1
        if is_manzok(i, j, count_arr):
            return True

    count_arr = [0] * 10
    for k in range(0, 3):            
        count_arr[arr[k][k]] = 1
    if is_manzok(i, j, count_arr):
        return True
    
    count_arr = [0] * 10
    for k in range(0, 3):
        count_arr[arr[k][2-k]] = 1
    if is_manzok(i, j, count_arr):
        return True

    return False

cnt = 0
for i in range(1, 10):
    for j in range(i+1, 10):
        if is_win(i, j):
            cnt += 1

print(cnt) 