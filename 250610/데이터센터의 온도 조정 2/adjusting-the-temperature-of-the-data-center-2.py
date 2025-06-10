N, C, G, H = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]

def get_jakup(t, Ta, Tb):
    if t > Tb:
        return H 
    elif t >= Ta:
        return G
    else:
        return C

_max = 0
for t in range(1001):
    _sum = 0
    for i, (Ta, Tb) in enumerate(arr):
        _sum += get_jakup(t, Ta, Tb)
    _max = max(_max, _sum)

print(_max)