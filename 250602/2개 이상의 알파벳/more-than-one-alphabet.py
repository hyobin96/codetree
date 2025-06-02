s = input()
def is_same(s):
    for c in s:
        if s[0] != c:
            return False
    return True
print('No' if is_same(s) else 'Yes')