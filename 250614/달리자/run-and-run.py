N = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

move_dist = 0
for i in range(N - 1):
    diff = A_arr[i] - B_arr[i]
    if diff > 0:
        A_arr[i + 1] += diff
        move_dist += diff
    
print(move_dist)
