class Data:
    def __init__(self, date, yo, nal):
        self.d = date
        self.y = yo
        self.n = nal

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
datas = [Data(d, y, n) for d, y, n in arr]

ans = Data('9999-99-99', '', '')

for i in range(len(datas)):
    if datas[i].n == 'Rain' and datas[i].d < ans.d:
        ans = datas[i]

print(ans.d, ans.y, ans.n)