a, b = map(int, input().split())
c, d = map(int, input().split())

if b < c or a > d:
    area = b - a + c - d
else:
    if a <= c and d <= b:
        area = b - a
    elif c <= a and b <= d:
        area = d - c
    elif a < c:
        area = d - a
    else:
        area = b - c
                    
print(area)
