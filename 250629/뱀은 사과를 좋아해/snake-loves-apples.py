import sys

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N


mapper = {'U':0, 'D':1, 'L':2, 'R':3}
drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]

tail = [0, 0]
head = [0, 0]

N, M, K = map(int, input().split())

arr = [[0] * N for _ in range(N)]

arr[0][0] = 1

for _ in range(M):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 2

query = [input().split() for _ in range(K)]

t = 0
for d, p in query:
    p = int(p)
    d = mapper[d]

    for _ in range(p):
        hr, hc = head
        nr, nc = hr + drs[d], hc + dcs[d]
        tr, tc = tail

        if not in_range(nr, nc):
            t += 1
            print(t)
            sys.exit()

        if arr[nr][nc] == 2:
            arr[hr][hc] = [1, d]
            arr[nr][nc] = 1

        elif arr[nr][nc] == 0:
            arr[hr][hc] = [1, d]

            prev_d = arr[tr][tc][1]
            tail = [tr + drs[prev_d], tc + dcs[prev_d]]
            
            arr[nr][nc] = 1
            
        else:
            t += 1
            print(t)
            sys.exit()
        
        t += 1
        head = [nr, nc]

print(t)



