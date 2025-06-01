arr = list(input())
s1 = arr[0]
s2 = arr[1]
for i in range(len(arr)):
    if arr[i] == s1:
        arr[i] = s2
    elif arr[i] == s2:
        arr[i] = s1

print(''.join(arr))