arr = list(map(int, input().split()))
_sum = sum(arr)
_min = 2000000000
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(5):
            if i == k or j == k:
                continue
            team1 = arr[i] + arr[j]
            team2 = arr[k]
            team3 = _sum - team1 - team2
            if team1 == team2 or team1 == team3 or team2 == team3:
                continue
            _min = min(_min, max((team1, team2, team3)) - min(team1, team2, team3))
if _min == 2000000000:
    print(-1)
else:
    print(_min)