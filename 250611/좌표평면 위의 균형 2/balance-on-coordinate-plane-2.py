N = int(input())
xys = [tuple(map(int, input().split())) for _ in range(N)]

_min = 2000000000
for x_p in range(0, 101, 2):
    for y_p in range(0, 101, 2):
        cnts = [0] * 4
        for x, y in xys:
            if  x > x_p and y > y_p:
                cnts[0] += 1
            elif x < x_p and y > y_p:
                cnts[1] += 1
            elif x < x_p and y < y_p:
                cnts[2] += 1
            else:
                cnts[3] += 1

        _min = min(_min, max(cnts))
print(_min)    
        