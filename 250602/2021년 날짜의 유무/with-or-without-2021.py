M, D = map(int, input().split())

def is_exist(M, D):
    if M > 12 or D > 31:
        return False
    if M == 2 and D > 28:
        return False
    if not(M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12):
        if D > 30:
            return False
    return True

if is_exist(M, D):
    print('Yes')
else:
    print('No')
