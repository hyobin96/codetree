n = int(input())
L, R = 101, -1
arr = [0] * 101
for _ in range(n):
    pos, pic = input().split()
    pos = int(pos)
    arr[pos] = pic
    L = min(L, pos)
    R = max(R, pos)

def is_same(i, j):
    g, h = 0, 0
    for e in arr[i:j+1]:
        if e == 'G':
            g += 1
        elif e == 'H':
            h += 1
    if g != 0 and g == h:
        return True
    return False

_max = 0
for i in range(R):
    if arr[i] != 0:
        for j in range(i+1, R):
            if arr[j] != 0:
                if is_same(i, j):
                    _max = max(_max, j-i)

print(_max)
        