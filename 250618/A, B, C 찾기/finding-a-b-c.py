arr = list(map(int, input().split()))

arr.sort()
A = arr[0]
B = arr[1]
abc = arr[-1]
C = abc - A - B

print(A, B, C)