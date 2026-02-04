# 닫는 괄호 쌍 부분합

a = input()

prefix_sum = [0] * len(a)

for i in range(len(a) - 2, -1, -1):
    if a[i] == ')' == a[i + 1]:
        prefix_sum[i] += 1
    prefix_sum[i] += prefix_sum[i + 1]


answer = 0
for i in range(1, len(a)):
    if a[i - 1] == '(' == a[i]:
        answer += prefix_sum[i]

print(answer)