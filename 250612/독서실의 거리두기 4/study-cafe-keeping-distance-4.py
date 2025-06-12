N = int(input())
arr = list(map(int, list(input())))

def get_min_dist():
    min_dist = 100

    for i in range(N):
        for j in range(i+1, N):
            if arr[i] == 1 and arr[j] == 1:
                dist = j - i
                min_dist = min(min_dist, dist)
                break

    return min_dist

max_dist = 0
#빈 좌석 두 개 선정
for i in range(N):
    for j in range(i+1, N):
        if arr[i] == 1 or arr[j] == 1:
            continue
        
        arr[i], arr[j] = 1, 1

        min_dist = get_min_dist()
        max_dist = max(max_dist, min_dist)
        
        arr[i], arr[j] = 0, 0

print(max_dist)

