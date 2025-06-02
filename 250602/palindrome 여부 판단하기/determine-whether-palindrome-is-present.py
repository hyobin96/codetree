A = input()

def is_pal(s):
    if s == s[::-1]:
        return True
    return False

if is_pal(A):
    print('Yes')
else:
    print('No')
