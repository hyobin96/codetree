s_list = [input() for _ in range(2)]
total = 0
for e in s_list:
    num = []
    for s in e:
        if s.isdigit():
            num.append(s)
    total += int(''.join(num))
print(total)