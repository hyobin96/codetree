n, m = map(int, input().split())
arr1 = [0]
arr2 = [0]

def move(d, t, arr):
    if d == 'L':
        for _ in range(t):
            arr.append(arr[-1] - 1)
    else:
        for _ in range(t):
            arr.append(arr[-1] + 1)

for _ in range(n):
    d, t = input().split()
    move(d, int(t), arr1)
for _ in range(m):
    d, t = input().split()
    move(d, int(t), arr2)

idx = -1
for i in range(1, len(arr1)):
    if arr1[i] == arr2[i]:
        idx = i
        break
    
print(idx)
