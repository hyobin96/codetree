import math
m1, d1, m2, d2 = map(int, input().split())
a = input()
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
pos = yoil.index(a)
def cal():
    return sum(days[:m2]) + d2 - (sum(days[:m1]) + d1 + pos) + 1

print(math.ceil(cal() / 7))