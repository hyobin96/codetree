# 정렬 필요
# i, j는 각각 불이 날 위치와 소방서의 위치
# 차이가 더 커지면 교체
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
fires = sorted(list(map(int, input().split())))
firestations = sorted(list(map(int, input().split())))

INF = 2e9

max_time = 0
j = 0
for i in range(n):
    dist = abs(fires[i] - firestations[j])
    while j + 1 < m and abs(fires[i] - firestations[j + 1]) < dist:
        dist = abs(fires[i] - firestations[j + 1])
        j += 1

    max_time = max(max_time, dist * 1)

answer = max_time
print(answer)

