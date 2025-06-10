X, Y = map(int, input().split())
_max = 0
for num in range(X, Y+1):
    _sum = sum(list(map(int, list(str(num)))))
    _max = max(_max, _sum)
print(_max)