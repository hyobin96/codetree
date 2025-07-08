def calculate_dist(i, j):
    global poses
    r1, c1 = poses[i]
    r2, c2 = poses[j]
    return abs(r1 - r2) + abs(c1 - c2)


def get_dist():
    global selected_coins
    dist = 0
    dist += calculate_dist(0, selected_coins[0]) + calculate_dist(selected_coins[-1], 10)
    for i in range(2):
        dist += calculate_dist(selected_coins[i], selected_coins[i + 1])

    return dist
    

def select_coins(cnt, start):
    global answer, poses, selected_coins
    if cnt == 3:
        answer = min(answer, get_dist())
        return

    for coin in range(start, 10):
        if poses[coin] != 0:
            selected_coins.append(coin)
            select_coins(cnt + 1, coin + 1)
            selected_coins.pop()

    
N = int(input())
grid = [list(input()) for _ in range(N)]
poses, answer, selected_coins = [0] * 11, 400, []
for i in range(N):
    for j in range(N):
        if grid[i][j] == '.':
            continue
        if grid[i][j] == 'S':
            poses[0] = (i, j)
        elif grid[i][j] == 'E':
            poses[10] = (i, j)
        else:
            poses[int(grid[i][j])] = (i, j)

select_coins(0, 1)
print(answer if answer != 400 else -1)