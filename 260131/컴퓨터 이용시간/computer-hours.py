# number에 +1 -1
# +1이면 현재 number 기록
# 사용자 번호 순서대로 시작 순서가 같지 않을 수 있으므로 사용자 번호도 기록

import sys, heapq
input = sys.stdin.readline

n = int(input())

times = []
for i in range(n):
    s, e = map(int, input().strip().split())
    times.append((s, 1, i + 1))
    times.append((e, -1, i + 1))

times.sort()

# print(times)

사용번호 = [0] * (n + 1)
numbers = list(range(1, n + 1))
heapq.heapify(numbers)
# print(numbers)
for _, v, i in times:
    if v == 1:
        사용번호[i] = heapq.heappop(numbers)
    else:
        heapq.heappush(numbers, 사용번호[i])

print(*사용번호[1:])