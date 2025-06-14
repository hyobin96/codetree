N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

ans = 'No'

for i in range(N):
    x1_max = 1
    x2_min = 100
    for j, (x1, x2) in enumerate(arr):
        if i == j:
            continue
        
        x1_max = max(x1_max, x1)
        x2_min = min(x2_min, x2)

    if not (x2_min < x1_max):
        ans = 'Yes'

print(ans)
