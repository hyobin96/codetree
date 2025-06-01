A = input()
B = input()

while B in A:
    idx = A.find(B)
    A = A[:idx] + A[idx + len(B):]
    
print(A)