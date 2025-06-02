y = int(input())

def is_year(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 4 == 0:
        return True
    return False

print('true' if is_year(y) else 'false')