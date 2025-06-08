arr = list(map(int, input().split()))
_sum = sum(arr)
_min = 20000000
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                if i == j or i == k or i == l or j == k or j == l or k == l:
                    continue
                team1 = arr[i] + arr[j]
                team2 = arr[k] + arr[l]
                team3 = _sum - team1 - team2
                _min = min(_min, max((team1, team2, team3)) - min((team1, team2, team3)))
print(_min)