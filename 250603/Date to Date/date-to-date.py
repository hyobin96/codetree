days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

def cal(m, d):
    return sum(days[:m]) + d

print(cal(m2, d2) - cal(m1, d1) + 1)