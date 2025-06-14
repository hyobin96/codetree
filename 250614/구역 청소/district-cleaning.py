a, b = map(int, input().split())
c, d = map(int, input().split())

area = 0
if b < c or a > d:
    area = b - a + d - c
else:
    if a <= c and d <= b:
        area = b - a
    elif c <= a and b <= d:
        area = d - c
    elif a < c and b < d:
        area = d - a
    elif c < a and d < b:
        area = b - c
                    
print(area)
