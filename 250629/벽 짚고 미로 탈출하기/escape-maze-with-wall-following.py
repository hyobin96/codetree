def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def is_right_exist(r, c, d):
    d = (d + 1) % 4
    return arr[r + drs[d]][c + dcs[d]] == '#'

def is_exist(r, c, d):
    return arr[r + drs[d]][c + dcs[d]] == '#'


drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]

N = int(input())
x, y = map(int, input().split())
r, c = x - 1, y - 1

arr = [list(input()) for _ in range(N)]
save_arr = [[0] * N for _ in range(N)]
is_impossible = False

d = 0
T = 0
while in_range(r, c):
    if is_right_exist(r, c, d):
        if not in_range(r + drs[d], c + dcs[d]):
            r, c = r + drs[d], c + dcs[d]
            T += 1
            break

        elif is_exist(r, c, d):
            d = (d + 3) % 4

        else:
            r, c = r + drs[d], c + dcs[d]
            if save_arr[r][c]:
                is_impossible = True
                break
            
            save_arr[r][c] = 1
            
            T += 1

    else:
        d = (d + 1) % 4
        r, c = r + drs[d], c + dcs[d]
        T += 1

    
if is_impossible:
    print(-1)
else:
    print(T)


