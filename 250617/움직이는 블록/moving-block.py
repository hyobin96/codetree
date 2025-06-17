N = int(input())
arr = [int(input()) for _ in range(N)]

avg = sum(arr) // N

cnt = 0
for n in arr:
    cnt += abs(n - avg)

print(cnt // 2)