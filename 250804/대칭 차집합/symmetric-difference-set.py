n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

A, B = set(A), set(B)

print(len(A - B) + len(B - A))