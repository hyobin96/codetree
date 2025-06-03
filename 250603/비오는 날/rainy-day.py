class Data:
    def __init__(self, date, yo, nal):
        self.d = date
        self.y = yo
        self.n = nal

def is_last(d1, d2):
    d1 = tuple(map(int, d1.split('-')))
    d2 = tuple(map(int, d2.split('-')))
    for x1, x2 in zip(d1, d2):
        if x1 > x2:
            return False
    return True

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
datas = [Data(d, y, n) for d, y, n in arr]

lat_idx = 0
for i, d in enumerate(datas):
    if d.n == 'Rain':
        lat_idx = i
        break

for i in range(lat_idx + 1, len(datas)):
    if datas[i].n == 'Rain' and is_last(datas[i].d, datas[lat_idx].d):
        lat_idx = i

last_d = datas[lat_idx]
print(last_d.d, last_d.y, last_d.n)