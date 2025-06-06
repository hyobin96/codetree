gualho = input()

total = 0
for i, v in enumerate(gualho):
    close_cnt = 0
    if v == '(':
        for j in range(i + 1, len(gualho)):
            if gualho[j] == ')':
                close_cnt += 1
        total += close_cnt
print(total)