def move(r, c):
    while r < b_max:
        r += 1
        c += arr[r][c]

    return c

def simul():
    for i in range(1, N + 1):
        r, c = 0, i
        dest = move(r, c)

        if init_flag:
            answer_arr[i] = dest

        else:
            if answer_arr[i] != dest:
                return False

    return True


def write(idx):
    a, b = line_arr[idx]
    arr[b][a], arr[b][a + 1] = 1, -1

def erase(idx):
    a, b = line_arr[idx]
    arr[b][a], arr[b][a + 1] = 0, 0

def select_lines(idx):
    global min_garo, idx_arr, M
    if simul():
        min_garo = min(min_garo, len(idx_arr))

    if idx == M:
        return

    for i in range(idx, M):
        idx_arr.append(i)
        write(i)
        select_lines(i + 1)
        erase(i)
        idx_arr.pop()

N, M = map(int, input().split())

b_max = 0
line_arr = []
answer_arr = [0 for _ in range(N + 1)]
idx_arr = []

init_flag = True

min_garo = M

for _ in range(M):
    a, b = map(int, input().split())
    line_arr.append([a, b])
    b_max = max(b_max, b)


arr = [[0 for _ in range(N + 1)] for _ in range(b_max + 1)]

for a, b in line_arr:
    arr[b][a], arr[b][a + 1] = 1, -1

simul()
init_flag = False

arr = [[0 for _ in range(N + 1)] for _ in range(b_max + 1)]

select_lines(0)

print(min_garo)

