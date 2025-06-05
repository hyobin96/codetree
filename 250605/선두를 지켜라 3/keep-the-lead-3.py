n, m = map(int, input().split())
a, b = [0], [0]

def move(v, t, arr):
    for _ in range(t):
        arr.append(arr[-1] + v)

for _ in range(n):
    v, t = map(int, input().split())
    move(v, t, a)

for _ in range(m):
    v, t = map(int, input().split())
    move(v, t, b)

combi = [' ']
for i in range(1, len(a)):
    if a[i] > b[i]:
        combi.append('a')
    elif b[i] > a[i]:
        combi.append('b')
    else:
        combi.append('ab')

cnt = 0
for i in range(1, len(combi)):
    if combi[i] != combi[i-1]:
        cnt += 1
print(cnt)