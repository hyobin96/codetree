a, b = map(int, input().split())
c, d = map(int, input().split())

area = 0
if b < c or a > d:
    area = b - a + d - c
else:
    area = max(b, d) - min(a, c)
                    
print(area)
