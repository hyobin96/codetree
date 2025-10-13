n, q = map(int, input().split())

point_list = list(map(int, input().split()))

prefix_sums = [0] * 1000001

for p in point_list:
    prefix_sums[p] = 1


for i in range(1, 1000001):
    prefix_sums[i] += prefix_sums[i - 1]


for _ in range(q):
    a, b = map(int, input().split())

    cnt = prefix_sums[b] - prefix_sums[a - 1 if a > 0 else 0]
    print(cnt)