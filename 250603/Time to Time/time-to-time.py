a, b, c, d = map(int, input().split())

def cal(h, m):
    return h * 60 + m

print(cal(c, d) - cal(a, b))
