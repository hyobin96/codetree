import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

numbers = [0] * n
for i in range(0, n):
    numbers[i] = int(input())

num_idx_dict = dict()

가장_가까운_인덱스 = [-1] * n

for i in range(n - 1, -1, -1):
    number = numbers[i]
    if number in num_idx_dict:
        가장_가까운_인덱스[i] = num_idx_dict[number]
    else:
        num_idx_dict[number] = i

max_num = -1
for i, idx in enumerate(가장_가까운_인덱스):
    if idx != -1 and idx - i <= k:
        max_num = max(max_num, numbers[i])

answer = max_num
print(answer)