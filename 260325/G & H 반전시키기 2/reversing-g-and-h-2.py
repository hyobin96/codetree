n = int(input())
a = list(input())
b = list(input())

# Please write your code here.
cnt = 0
for i in range(n - 1, -1, -1):
    if a[i] != b[i]:
        cnt += 1
        for j in range(i, -1, -1):
            a[j] = 'G' if a[j] == 'H' else 'H'

print(cnt)