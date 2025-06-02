Y, M, D = map(int, input().split())

def is_yun(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 4 == 0:
        return True
    return False

def last_day(Y, M, D):
    feb_last_day = 28
    if is_yun(Y):
        feb_last_day = 29
    if M == 2:
        return feb_last_day
    if M == 4 or M == 6 or M == 9 or M == 11:
        return 30
    return 31

def season(M):
    if 3 <= M <= 5:
        return 'Spring'
    if 6 <= M <= 8:
        return 'Summer'
    if 9 <= M <= 11:
        return 'Fall'
    return 'Winter'
if last_day(Y, M, D) < D:
    print(-1)
else:
    print(season(M))
