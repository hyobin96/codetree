N = int(input())
arr = list(map(int, list(input())))

def get_max_x1_x2():
    max_dist = 0
    x1, x2 = 0, 0

    for i in range(N):
        for j in range(i + 1, N):
            if not(arr[i] == 1 and arr[j] == 1):
                continue
            
            dist = j - i
            if dist > max_dist:
                x1, x2 = i, j
                max_dist = dist

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

x1, x2 = get_max_x1_x2()

min_dist = 0
if (x1, x2) != (0, 0):
    arr[(x1 + x2) // 2] = 1
    min_dist = get_min_dist()
    arr[(x1 + x2) // 2] = 0

arr[-1] = 1
min_dist = max(min_dist, get_min_dist())

print(min_dist)

