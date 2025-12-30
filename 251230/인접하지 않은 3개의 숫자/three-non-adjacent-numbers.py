import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

l_max_list, r_max_list = [0] * n, [0] * n

l_max_list[0], r_max_list[-1] = numbers[0], numbers[-1]

for i in range(1, n):
    l_max_list[i] = max(numbers[i], l_max_list[i - 1])
    r_max_list[-i - 1] = max(numbers[-i - 1], l_max_list[-i])

answer = 0

for i in range(2, n - 2):
    total = numbers[i] + l_max_list[i - 2] + r_max_list[i + 2]
    answer = max(answer, total)

print(answer)