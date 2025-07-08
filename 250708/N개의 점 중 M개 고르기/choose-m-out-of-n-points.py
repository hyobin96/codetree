def get_max_dist():
    global selected_points
    max_dist = 0
    for i in range(M - 1):
        for j in range(i + 1, M):
            x1, y1 = selected_points[i]
            x2, y2 = selected_points[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            max_dist = max(max_dist, dist)
    return max_dist

def select_points(cnt, start):
    global answer, points, selected_points
    if cnt == M:
        answer = min(answer, get_max_dist())

    for i in range(start, N):
        selected_points.append(points[i])
        select_points(cnt + 1, i + 1)
        selected_points.pop()


N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]
answer, selected_points = 100000, []
select_points(0, 0)
print(answer)
