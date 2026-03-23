n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
total = 0
max_total = -1000
for e in a:
    total += e
    max_total = max(max_total, total)
    if total < 0:
        total = 0

print(max_total)