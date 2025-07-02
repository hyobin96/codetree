def simul():
    isCollision = False

    for i in range(1, N + 1):
        if pos_arr[i]:
            r, c, w, d = pos_arr[i]
            r, c = r + drs[d], c + dcs[d]
            pos_arr[i] = r, c, w, d

    # print(pos_arr)
    
    for i in range(1, N + 1):
        temp = []
        for j in range(i, N + 1):
            if not pos_arr[i] or not pos_arr[j]:
                continue

            r1, c1, w1, d1 = pos_arr[i]
            r2, c2, w2, d2 = pos_arr[j]

            if (r1, c1) == (r2, c2):
                temp.append([j, w2])

        
        temp.sort(key=lambda x: (-x[1], -x[0]))

        for i in range(1, len(temp)):
            isCollision = True
            pos_arr[temp[i][0]] = []

    return isCollision


T = int(input())

drs, dcs = [0, 0, -1, 1], [1, -1, 0, 0]

mapper = {'U':0, 'D':1, 'L':2, 'R':3}


size = 2000

N = 0
pos_arr = []

for _ in range(T):
    N = int(input())

    pos_arr = [[]]

    for _ in range(N):
        x, y, w, d = input().split()
        x, y, w, d = int(x) * 2, int(y) * 2, int(w), mapper[d]

        pos_arr.append([x, y, w, d])

    last = -1
    for t in range(1, 2000):
        if simul():
            last = t

    print(last)