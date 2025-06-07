n = int(input())
R = 0
arr = [' '] * 101
for _ in range(n):
    pos, pic = input().split()
    pos = int(pos)
    arr[pos] = pic
    R = max(R, pos)

def is_same(i, j):
    g, h = 0, 0
    for e in arr[i:j+1]:
        if e == 'G':
            g += 1
        elif e == 'H':
            h += 1
    if g == h or h == 0 or g == 0:
        return True
    return False

_max = 0
for i in range(R+1):
    if arr[i] != ' ':
        for j in range(i+1, R+1):
            if arr[j] != ' ' and is_same(i, j):
                _max = max(_max, j-i)
print(_max)
        