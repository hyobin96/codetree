M, D = map(int, input().split())

def is_exist(M, D):
    if M > 12 or D > 31:
        return False
    if M == 2 and D > 28:
        return False
    return True

if is_exist(M, D):
    print('Yes')
else:
    print('No')
