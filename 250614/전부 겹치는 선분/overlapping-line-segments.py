N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

x1_max = 0
x2_min = 100
for x1, x2 in arr:
    x1_max = max(x1_max, x1)
    x2_min = min(x2_min, x2)

ans = 'Yes'
if x1_max > x2_min:
    ans = 'No'

print(ans)        