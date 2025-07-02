import sys

def simul():
    global cnt
    isCollision = False

    xy_map = {}

    for i in range(1, N + 1):
        if pos_arr[i]:
            cnt += 1
            r, c, w, d = pos_arr[i]
            r, c = r + drs[d], c + dcs[d]
            pos_arr[i] = r, c, w, d

            if r > max_x or c > max_y or r < min_x or c < min_y:
                pos_arr[i] = ()
                continue

            key = str(r) + " " + str(c)

            if key not in xy_map:
                xy_map[key] = (i, w)

            else:
                isCollision = True
                i2, w2 = xy_map[key]
                
                if w2 > w:
                    pos_arr[i] = ()
                
                elif w2 < w:
                    pos_arr[i2] = ()
                
                else:
                    if i2 > i:
                        pos_arr[i] = ()
                    
                    else:
                        pos_arr[i2] = ()
                
    return isCollision


T = int(input())

drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]

mapper = {'U':0, 'D':1, 'L':2, 'R':3}

offset = 1000
size = 4000

N = 0
pos_arr = []

input = sys.stdin.readline

for _ in range(T):
    N = int(input())

    pos_arr = [[]]

    min_x = 5000
    min_y = 5000

    max_x = 0
    max_y = 0
    for _ in range(N):
        x, y, w, d = input().split()
        x, y, w, d = (int(x) + offset) * 2, (int(y) + offset)* 2, int(w), mapper[d]

        min_x, min_y = min(min_x, x), min(min_y, y)

        max_x = max(max_x, x)
        max_y = max(max_y ,y)

        pos_arr.append([x, y, w, d])

    last = -1
    for t in range(1, 4001):
        cnt = 0
        if simul():
            last = t

        if cnt == 0:
            break

    print(last)