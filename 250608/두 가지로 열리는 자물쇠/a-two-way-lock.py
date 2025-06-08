n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def is_manzok(d1, d2, d3):
    if (d1 <= 2 or d1 >= (n-2)) and (d2 <= 2 or d2 >= (n-2)) and (d3 <= 2 or d3 >= (n-2)):
        return True
    return False

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if is_manzok(abs(i-a1), abs(j-b1), abs(k-c1)) \
            or is_manzok(abs(i-a2), abs(j-b2), abs(k-c2)):
                cnt += 1
print(cnt)