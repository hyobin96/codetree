N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

d = {}
for i in range(N):
    for j in range(N):
        _sum = C[i] + D[j]
        if _sum in d:
            d[_sum] += 1
        else:
            d[_sum] = 1

answer = 0
for i in range(N):
    for j in range(N):
        target = -A[i] - B[j]
        if target in d:
            answer += d[target]

print(answer)