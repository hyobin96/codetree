arr = list(input())
arr[1], arr[-2] = 'a', 'a'
print(''.join(arr))