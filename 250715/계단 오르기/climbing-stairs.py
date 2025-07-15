N = int(input())

step = [0] * (N + 2)
step[2] = step[3] = 1
for i in range(N - 1):
    step[i + 2] = (step[i + 2] + step[i]) % 10007
    step[i + 3] = (step[i + 3] + step[i]) % 10007

print(step[N])
