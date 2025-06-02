n = int(input())
total = 0
for _ in range(n):
    total += int(input())
total = str(total)
print(total[1:] + total[0])