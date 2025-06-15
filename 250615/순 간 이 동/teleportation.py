A, B, x, y = map(int, input().split())

def get_dist(A, B, x, y):
    return abs(A - x) + abs(y - B)

dist1 = abs(A - B)

dist2 = get_dist(A, B, x, y)

dist3 = get_dist(A, B, y, x)

print(min(dist1, dist2, dist3))