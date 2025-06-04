m1, d1, m2, d2 = map(int, input().split())
yoil = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cal_days():
    return (sum(days[:m2]) + d2 - (sum(days[:m1]) + d1)) % 7

print(yoil[cal_days()])