N, K = map(int, input().split())
numbers = list(map(int, input().split()))
z_d = {}
for z in numbers:
    if z in z_d:
        z_d[z] += 1
    else:
        z_d[z] = 1


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

answer1 = 0
answer2 = 0
for z in z_d.keys():
    target = K - z
    if target in z_d:
        if target == z and z_d[target] > 1:
            answer2 += fact(z_d[target] - 1)
        else:
            answer1 += z_d[target] * z_d[z]

print(answer1 // 2 + answer2)