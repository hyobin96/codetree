N = int(input())
arr = list(map(int, list(input())))

def get_max_dist_pos_x1_x2():
    x1, x2 = 0, 0
    max_dist = 0

    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] == 1 and arr[j] == 1:
                if j - i > max_dist:
                    x1, x2 = i, j
                break
                    

    return x1, x2

def get_min_dist():
    min_dist = 1000
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] == 1 and arr[j] == 1:
                min_dist = min(min_dist, j - i)
                break
    
    return min_dist

x1, x2 = get_max_dist_pos_x1_x2()
arr[(x1 + x2) // 2] = 1

dist = get_min_dist()
print(dist)
