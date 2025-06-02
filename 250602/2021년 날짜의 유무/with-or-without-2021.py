M, D = map(int, input().split())

def is_exist(M, D):
    if M == 2 and D > 28:
        return False
    if M > 12:
        return False
    return True
if D > 31:
    print('No')
elif is_exist(M, D):
    print('Yes')
else:
    print('No')
