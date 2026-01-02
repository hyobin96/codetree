import sys

input = sys.stdin.readline

n, q = map(int, input().rstrip().split())

numbers = [0] + list(map(int, input().rstrip().split()))

L_max = [0] * (n + 1)
L_max[1] = numbers[1]

R_max = [0] * (n + 1)
R_max[-1] = numbers[-1]

for i in range(2, n + 1):
    L_max[i] = max(L_max[i - 1], numbers[i])
    R_max[-i] = max(R_max[-i + 1], numbers[-i])


for _ in range(q):
    a, b = map(int, input().rstrip().split())
    print(max(L_max[a - 1], R_max[b + 1]))