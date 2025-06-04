a, b, c = map(int, input().split())

def cal(d, h, m):
    return (d - 11) * 60 * 24 + h * 60 + c - (11 * 60 + 11)

res = cal(a, b, c)
if res < 0:
    print(-1)
else:
    print(res)