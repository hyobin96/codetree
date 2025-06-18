x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

r_x = max(x2, a2) - min(x1, a1) 
r_y = max(y2, b2) - min(y1, b1)

print(r_x * r_y)