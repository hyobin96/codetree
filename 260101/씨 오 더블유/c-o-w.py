import sys

input = sys.stdin.readline

n = int(input().strip())

strings = list(input().strip())

# print(strings)

L_C_sum_list = [0] * n
if strings[0] == 'C':
    L_C_sum_list[0] = 1

R_W_sum_list = [0] * n
if strings[-1] == 'W':
    R_W_sum_list[-1] = 1

for i in range(1, n):
    L_C_sum_list[i] = L_C_sum_list[i - 1] + int(strings[i] == 'C')
    R_W_sum_list[-i - 1] = R_W_sum_list[-i] + int(strings[-i - 1] == 'W')


answer = 0
for i in range(1, n - 1):
    if strings[i] == 'O':
        count = L_C_sum_list[i - 1] * R_W_sum_list[i + 1]
        answer += count

print(answer)