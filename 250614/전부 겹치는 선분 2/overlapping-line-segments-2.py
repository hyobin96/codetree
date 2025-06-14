N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

ans = 'No'

x1_max = 0
x2_min = 100
for i in range(N):
    for j, (x1, x2) in enumerate(arr):
        if i == j:
            continue
        
        x1_max = max(x1_max, x1)
        x2_min = min(x2_min, x2)

    if x1_max > x2_min:
        ans = 'Yes'

print(ans)
